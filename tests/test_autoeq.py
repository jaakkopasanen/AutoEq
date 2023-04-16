import os
import re
import shutil
import tempfile
from pathlib import Path
import unittest
import pandas as pd
from autoeq.frequency_response import FrequencyResponse
from autoeq.batch_processing import batch_processing
from autoeq.constants import DEFAULT_MAX_GAIN, DEFAULT_TREBLE_F_LOWER, DEFAULT_TREBLE_F_UPPER, DEFAULT_TREBLE_GAIN_K, \
    DEFAULT_BIT_DEPTH, DEFAULT_F_RES, DEFAULT_BASS_BOOST_GAIN, DEFAULT_BASS_BOOST_FC, DEFAULT_BASS_BOOST_Q, \
    DEFAULT_SMOOTHING_WINDOW_SIZE, DEFAULT_TREBLE_SMOOTHING_WINDOW_SIZE, PEQ_CONFIGS, DEFAULT_TREBLE_BOOST_GAIN, \
    DEFAULT_TREBLE_BOOST_FC, DEFAULT_TREBLE_BOOST_Q


class TestAutoEq(unittest.TestCase):
    def setUp(self):
        self._root = Path(tempfile.gettempdir()).joinpath(os.urandom(24).hex())
        self._input = self._root.joinpath('input')
        self._output = self._root.joinpath('output')
        for i in range(1, 3):
            path = self._input.joinpath(f'Headphone {i}', f'Headphone {i}.csv')
            path.parent.mkdir(parents=True, exist_ok=True)
            with open(path, 'w') as fh:
                fh.write('frequency,raw\n20,2\n50,2\n200,0\n1000,1\n3000,10\n10000,0\n20000,-15')
        self._compensation = self._root.joinpath('compensation.csv')
        with open(self._compensation, 'w') as fh:
            fr = FrequencyResponse(
                name='compensation',
                frequency=[20, 50, 200, 1000, 3000, 10000, 20000],
                raw=[6, 6, -1, 0, 8, 1, -10])
            fr.interpolate(pol_order=2)
            fr.smoothen_fractional_octave(window_size=2, treble_window_size=2)
            fr.center()
            fr.write_to_csv(self._compensation)
        self._sound_signature = self._root.joinpath('sound_signature.csv')
        with open(self._sound_signature, 'w') as fh:
            fh.write('frequency,raw\n20.0,0\n10000,0.0\n20000,3')

    def tearDown(self):
        shutil.rmtree(self._root)

    def test_batch_processing(self):
        self.assertTrue(self._input.joinpath('Headphone 1', 'Headphone 1.csv').exists())
        self.assertTrue(self._input.joinpath('Headphone 2', 'Headphone 2.csv').exists())
        frs = batch_processing(
            input_dir=self._input, output_dir=self._output, standardize_input=True, compensation=self._compensation,
            parametric_eq=True, fixed_band_eq=True, rockbox=True,
            ten_band_eq=True,
            parametric_eq_config=['4_PEAKING_WITH_LOW_SHELF', PEQ_CONFIGS['4_PEAKING_WITH_HIGH_SHELF']],
            fixed_band_eq_config=None, convolution_eq=True,
            fs=[44100, 48000], bit_depth=DEFAULT_BIT_DEPTH, phase='both', f_res=DEFAULT_F_RES,
            bass_boost_gain=DEFAULT_BASS_BOOST_GAIN, bass_boost_fc=DEFAULT_BASS_BOOST_FC,
            bass_boost_q=DEFAULT_BASS_BOOST_Q, treble_boost_gain=DEFAULT_TREBLE_BOOST_GAIN,
            treble_boost_fc=DEFAULT_TREBLE_BOOST_FC, treble_boost_q=DEFAULT_TREBLE_BOOST_Q,
            tilt=-0.2, sound_signature=self._sound_signature,
            max_gain=DEFAULT_MAX_GAIN,
            window_size=DEFAULT_SMOOTHING_WINDOW_SIZE, treble_window_size=DEFAULT_TREBLE_SMOOTHING_WINDOW_SIZE,
            treble_f_lower=DEFAULT_TREBLE_F_LOWER, treble_f_upper=DEFAULT_TREBLE_F_UPPER,
            treble_gain_k=DEFAULT_TREBLE_GAIN_K, preamp=-1.0, thread_count=1
        )
        self.assertEqual(len(frs), 2)

        self.assertTrue(self._output.joinpath('Headphone 1', 'Headphone 1.png').exists())

        # CSV file
        self.assertTrue(self._output.joinpath('Headphone 1', 'Headphone 1.csv').exists())
        df = pd.read_csv(self._output.joinpath('Headphone 1', 'Headphone 1.csv'))
        columns = 'frequency,raw,error,smoothed,error_smoothed,equalization,parametric_eq,fixed_band_eq,' \
                  'equalized_raw,equalized_smoothed,target'.split(',')
        self.assertEqual(list(df.columns), columns)
        self.assertEqual(df.size, 695 * len(columns))

        # Graphic equalizer
        self.assertTrue(self._output.joinpath('Headphone 1', 'Headphone 1 GraphicEQ.txt').exists())
        with open(self._output.joinpath('Headphone 1', 'Headphone 1 GraphicEQ.txt')) as fh:
            self.assertRegexpMatches(fh.read().strip() + '; ', r'GraphicEQ: \d{2,5} (-?\d(\.\d+)?; )+')

        # Fixed band equalizer
        self.assertTrue(self._output.joinpath('Headphone 1', 'Headphone 1 FixedBandEq.txt').exists())
        with open(self._output.joinpath('Headphone 1', 'Headphone 1 FixedBandEq.txt')) as fh:
            lines = fh.read().strip().split('\n')
        self.assertTrue(re.match(r'Preamp: -?\d+(\.\d+)? dB', lines[0]))
        for line in lines[1:]:
            self.assertRegexpMatches(line, r'Filter \d{1,2}: ON PK Fc \d{2,5} Hz Gain -?\d(\.\d+)? dB Q 1.41')

        # Parametric equalizer
        self.assertTrue(self._output.joinpath('Headphone 1', 'Headphone 1 ParametricEq.txt').exists())
        with open(self._output.joinpath('Headphone 1', 'Headphone 1 ParametricEq.txt')) as fh:
            lines = fh.read().strip().split('\n')
        self.assertTrue(re.match(r'Preamp: -?\d+(\.\d+)? dB', lines[0]))
        for line in lines[1:]:
            self.assertRegexpMatches(
                line, r'Filter \d{1,2}: ON (PK|LS|HS) Fc \d{2,5} Hz Gain -?\d(\.\d+)? dB Q \d(\.\d+)?')

        # Convolution (FIR) filters
        for phase in ['minimum', 'linear']:
            for fs in [44100, 48000]:
                fp = self._output.joinpath('Headphone 1', f'Headphone 1 {phase} phase {fs}Hz.wav')
                self.assertTrue(fp.exists())
                # Frequency resolution is 10, 2 channels, 16 bits per sample, 8 bits per byte
                # Real file size has headers
                min_size = fs / 10 * 2 * 16 / 8
                self.assertGreater(os.stat(fp).st_size, min_size)

        # README
        self.assertTrue(self._output.joinpath('Headphone 1', 'README.md').exists())
        with open(self._output.joinpath('Headphone 1', 'README.md')) as fh:
            s = fh.read().strip()
        self.assertTrue('# Headphone 1' in s)
        self.assertTrue('### Parametric EQs' in s)
        self.assertTrue('### Fixed Band EQs' in s)
        self.assertTrue('### Graphs' in s)
