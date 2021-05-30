# -*- coding: utf-8 -*-

from pathlib import Path
import sys
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers
import tensorflow_addons as tfa
import numpy as np

ROOT_PATH = Path().resolve().parent.parent
if str(ROOT_PATH) not in sys.path:
    sys.path.insert(1, str(ROOT_PATH))
DIR_PATH = Path().resolve()

from constants import DEFAULT_F_MIN, DEFAULT_F_MAX, DEFAULT_STEP


class NeuralPEQ:
    def __init__(self, fs=46010.0, n_filters=10, frequency=None, hidden_size=16,
                 learning_rate=1e-4, learning_rate_decay=0.0, warmup_epochs=3,
                 log_f=False, q_normalization=3.0, gain_normalization=10.0):
        self.fs = fs
        self.n_filters = n_filters
        self.frequency = frequency
        if self.frequency is None:
            self.frequency = self.generate_frequencies()
        self.hidden_size = hidden_size
        self.learning_rate = learning_rate
        self.learning_rate_decay = learning_rate_decay
        self.warmup_epochs = warmup_epochs
        self.log_f = log_f
        self.q_normalization = q_normalization
        self.gain_normalization = gain_normalization

        # Construct model architecture
        inputs = keras.Input(shape=self.frequency.size)  # Input layer, take size data
        x = layers.Dense(hidden_size, activation='sigmoid')(inputs)  # First hidden layer
        outputs = layers.Dense(self.n_filters * 3)(x)  # Output layer: 10 filters with 3 parameters each
        self.model = keras.Model(inputs=inputs, outputs=outputs, name='peq')
        self.model.compile(loss=self.loss, optimizer=tfa.optimizers.AdamW(
            weight_decay=0.01,
            learning_rate=self.learning_rate,
            beta_1=0.9,
            beta_2=0.999,
            epsilon=1e-7,
            amsgrad=False))

    @staticmethod
    def generate_frequencies(f_min=DEFAULT_F_MIN, f_max=DEFAULT_F_MAX, f_step=DEFAULT_STEP):
        freq = []
        f = f_min
        while f <= f_max:
            freq.append(f)
            f *= f_step
        return np.array(freq)

    def loss(self, eq_fr_target, eq_param_vector):
        """Loss function. Calculates frequency response of a parametric equalizer which has N filters with Fc, Q and gain given as eq_parameters

            Args:
                eq_fr_target: Target vector for the equalizer frequency response
                eq_param_vector: Predicted parametric eq parameters as 3*N dimensional vector with N 3 parameter groups

            Returns:
                Loss value
            """
        # Reshape rank 1 Tensor of eq parameters to rank 2 Tensor with shape Nx3
        # First 3 items in the input eq parameters are Fc, Q and gain of the first filter,
        # next 3 are Fc, Q and gain of the second filters and so on
        filters = tf.reshape(eq_param_vector, (
            tf.size(eq_param_vector) / (self.n_filters * 3), self.n_filters, 3))  # Each row contains Fc, Q and gain
        if self.log_f:
            filters = tf.stack([
                tf.pow(10.0, filters[:, :, 0]),  # Letting optimizer operate center frequencies in linear scale ~1..4
                filters[:, :, 1] * self.q_normalization,
                filters[:, :, 2] * self.gain_normalization
            ], axis=2)
        else:
            filters = tf.stack([
                filters[:, :, 0],
                filters[:, :, 1] * self.q_normalization,
                filters[:, :, 2] * self.gain_normalization
            ], axis=2)

        # MSE as loss
        # Equalizer frequency response should be zero
        loss = tf.reduce_mean(tf.square(self.fr(filters) - eq_fr_target))
        return loss

    def fr(self, filters):
        """Calculate frequency response from the predicted parameters

        Parametric equalizers use biquad filters for which frequency response can be calculated from zero-pole
        # presentation

        Args:
            filters: n by 3 tack of filters, one filter per row. Columns are Fc, Q and gain
        """
        #
        # Calculate a and b coefficients first
        # https://en.wikipedia.org/wiki/Digital_biquad_filter
        # Index ranges are necessary to prevent Tensors from being squeezed
        A = 10 ** (filters[:, :, 2:3] / 40)  # Gain is column 2
        # Power 10 for center frequency forcing optimizer to produce linear values between ~1~5
        # Optimizer cannot handle logarithmic variables
        w0 = 2 * np.pi * filters[:, :, 0:1] / self.fs  # Fc is column 0
        alpha = tf.sin(w0) / (2 * filters[:, :, 1:2])  # Q is column 1

        a0 = 1 + alpha / A
        a1 = -(-2 * tf.cos(w0)) / a0
        a2 = -(1 - alpha / A) / a0

        b0 = (1 + alpha * A) / a0
        b1 = (-2 * tf.cos(w0)) / a0
        b2 = (1 - alpha * A) / a0

        a0 = 1.0  # Normalized form
        a1 *= -1
        a2 *= -1

        frequency = tf.constant(
            np.repeat(np.expand_dims(self.frequency, axis=0), filters.shape[1], axis=0),
            name='f', dtype='float32')
        w = 2 * np.pi * frequency / self.fs
        phi = 4 * tf.sin(w / 2) ** 2

        # Equalizer frequency response from a and b coefficients
        eq_fr = 10 * tf.math.log(
            (b0 + b1 + b2) ** 2 + (b0 * b2 * phi - (b1 * (b0 + b2) + 4 * b0 * b2)) * phi
        ) / tf.math.log(10.0) - 10 * tf.math.log(
            (a0 + a1 + a2) ** 2 + (a0 * a2 * phi - (a1 * (a0 + a2) + 4 * a0 * a2)) * phi
        ) / tf.math.log(10.0)  # TF doesn't have log10 hence log(x)/log(10)
        # Total equalizer frequency response is the sum of all filters' frequency responses
        return tf.reduce_sum(eq_fr, axis=1)

    def train(self, data):
        return self.model.fit(
            data, data,
            # train[:10], train[:10],
            batch_size=32,
            epochs=100,
            validation_split=0.2,
            callbacks=[
                tf.keras.callbacks.LearningRateScheduler(self.scheduler_factory()),
                tf.keras.callbacks.EarlyStopping(monitor='loss', patience=10, restore_best_weights=True)
            ]
        )

    def scheduler_factory(self):
        def scheduler(epoch, current_lr):
            if epoch < self.warmup_epochs:
                return self.learning_rate / (self.warmup_epochs - epoch)
            else:
                return current_lr * (1.0 - self.learning_rate_decay)
        return scheduler

    def infer(self, eq_fr_target):
        filters = self.model.predict(eq_fr_target)
        filters = np.reshape(filters, (filters.size // (self.n_filters * 3), self.n_filters, 3))
        if self.log_f:
            filters[:, :, 0] = 10 ** filters[:, :, 0]
        filters[:, :, 1] = np.abs(filters[:, :, 1]) * self.q_normalization
        filters[:, :, 2] *= self.gain_normalization
        return filters
