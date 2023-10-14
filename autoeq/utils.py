# -*- coding: utf-8 -*-
import numpy as np
from autoeq.constants import DEFAULT_F_MIN, DEFAULT_F_MAX, DEFAULT_STEP


def generate_frequencies(f_min=DEFAULT_F_MIN, f_max=DEFAULT_F_MAX, f_step=DEFAULT_STEP):
    frequencies = []
    f = f_min
    while f <= f_max:
        frequencies.append(f)
        f *= f_step
    return np.array(frequencies)
