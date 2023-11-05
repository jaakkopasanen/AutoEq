import unittest
from autoeq.csv import parse_csv, find_csv_separators, autoeq_pattern, rew_pattern

csv1 = """frequency,raw
20,0
1000,3
20000,0
"""

csv2 = """freq\tspl
20.0\t0.0
1000.0\t3.0
20000.0\t0.0
"""

csv3 = """frequency; raw
20,0; 0,0
1000,0; 3,0
20000,0; 0,0
"""

csv4 = """
Frequency	dB	Unweighted
20.0	0
1000.0	3.0
20000.0	0
"""

csv5 = """* Measurement data measured by REW V5.19
* Source: ASIO MOTU M Series, In 1
* Format: 1M Log Swept Sine, 1 sweep at -3.0 dBFS  With no timing reference
* Dated: 21 Feb, 2023 6:43:46 PM
* REW Settings:
*  C-weighting compensation: Off
*  Target level: 75.0 dB
* Note: ; 
* Measurement: Feb 21 18:43:46
* Smoothing: 1/48 octave
* Frequency Step: 1/48 octave
* Start Frequency: 10.1 Hz
*
* Freq(Hz), SPL(dB), Phase(degrees)
20.000, 0.000, 64.208
1000.000, 3.000, 63.426
20000.000, 0.000, 62.377
"""

csv6 = """20.0\t0.0
1000.0\t3.0
20000.0\t0.0
"""

csv7 = """error,frequency,raw
0,20,0
-1,1000,3
1,20000,0
"""

csv8 = """frequency,raw,error,smoothed,error_smoothed,equalization,parametric_eq,fixed_band_eq,equalized_raw,equalized_smoothed,target
20.00,0.81,-8.06,0.82,-8.05,6.00,6.13,2.79,6.81,6.82,8.87
1000.00,0.89,-7.98,0.89,-7.98,6.00,6.13,2.87,6.89,6.89,8.87
20000.00,0.95,-7.91,0.95,-7.92,6.00,6.12,2.95,6.95,6.95,8.87
"""

csv9 = """
Frequency	dB	Unweighted
20.0	69.6
1000.0	69.7
20000	51
overall dB	93.3 dB
decay	Average
averaging	No Smoothing
source	Headset Mic 1 Low Range


saved	2/2/19, 4:17 PM
peak	20.5Hz
"""

csv10 = """* Measurement data saved by REW V5.18
* Source: Trace Arithmetic result A / B
* Format: Trace Arithmetic result A / B
* Dated: 17-Feb-2019 15:47:47
* REW Settings:
*  C-weighting compensation: Off
*  Target level: 75.0 dB
* Note: Trace Arithmetic A over B A = F111 Clone L.txt B = Phone to Desktop Only  
* Measurement: A over B
* Smoothing: None
* Frequency Step: 0.24999999 Hz
* Start Frequency: 19.5 Hz
*
* Freq(Hz) SPL(dB) Phase(degrees)
19.500 ? 0
19.750 ? 0
20.000 68.334 0
20.250 68.335 0
19998.498 27.402 0
19998.748 ? 0
19998.998 ? 0
19999.248 ? 0
19999.498 ? 0
"""

csv11 = """* Measurement data measured by REW V5.20.3
* Source: USB-C to 3.5mm Headphone Jack Adapter, USB-C to 3.5mm Headphone Jack Adapter, 0, volume: 0.138. Timing signal peak level -19.8 dBFS, measurement signal peak level -19.3 dBFS
* Format: 256k Log Swept Sine, 1 sweep at -12.0 dBFS using an acoustic timing reference
* Dated: Jul 10, 2023 9:36:37 PM
* REW Settings:
*  C-weighting compensation: Off
*  Target level: 75.0 dB
* Note: Delay -0.1027 ms (-35 mm, -1.39 in) using estimated IR delay relative to Acoustic reference on USB-C to 3.5mm Headphone Jack Adapter L with no timing offset
* Measurement: Duo L Jul 10
* Smoothing: 1/12 octave
* Frequency Step: 1/48 octave
* Start Frequency: 20.000 Hz
*
* Freq(Hz)	SPL(dB)	Phase(degrees)
20.000000	96.774	36.7401
20.299999	96.813	36.0714
20.600000	96.843	35.3904
"""


class TestCsv(unittest.TestCase):
    def test_regex(self):
        pattern_asserts = [
            (csv1, autoeq_pattern), (csv2, None), (csv3, None), (csv4, None), (csv5, rew_pattern), (csv6, None),
            (csv7, None), (csv8, autoeq_pattern), (csv9, None), (csv10, rew_pattern), (csv11, rew_pattern)
        ]
        for s, pattern in pattern_asserts:
            if pattern:
                self.assertTrue(bool(pattern.match(s)))

    def test_find_csv_separators(self):
        separator_asserts = [
            (csv1, ',', '.'), (csv2, '\t', '.'), (csv3, ';', ','), (csv4, '\t', '.'), (csv5, ',', '.'),
            (csv6, '\t', '.'), (csv7, ',', '.'), (csv8, ',', '.'), (csv9, '\t', '.')
        ]
        for s, true_col, true_dec in separator_asserts:
            col, dec = find_csv_separators(s)
            self.assertEqual(true_col, col)
            self.assertEqual(true_dec, dec)

    def test_parse_csv1(self):
        d = parse_csv(csv1)
        self.assertIn('frequency', d)
        self.assertEqual([20.0, 1000.0, 20000.0], d['frequency'])
        self.assertIn('raw', d)
        self.assertEqual([0.0, 3.0, 0.0], d['raw'])

    def test_parse_csv2(self):
        d = parse_csv(csv2)
        self.assertIn('frequency', d)
        self.assertEqual([20.0, 1000.0, 20000.0], d['frequency'])
        self.assertIn('raw', d)
        self.assertEqual([0.0, 3.0, 0.0], d['raw'])

    def test_parse_csv3(self):
        d = parse_csv(csv3)
        self.assertIn('frequency', d)
        self.assertEqual([20.0, 1000.0, 20000.0], d['frequency'])
        self.assertIn('raw', d)
        self.assertEqual([0.0, 3.0, 0.0], d['raw'])

    def test_parse_csv4(self):
        d = parse_csv(csv4)
        self.assertIn('frequency', d)
        self.assertEqual([20.0, 1000.0, 20000.0], d['frequency'])
        self.assertIn('raw', d)
        self.assertEqual([0.0, 3.0, 0.0], d['raw'])

    def test_parse_csv5(self):
        d = parse_csv(csv5)
        self.assertIn('frequency', d)
        self.assertEqual([20.0, 1000.0, 20000.0], d['frequency'])
        self.assertIn('raw', d)
        self.assertEqual([0.0, 3.0, 0.0], d['raw'])

    def test_parse_csv6(self):
        d = parse_csv(csv6)
        self.assertIn('frequency', d)
        self.assertEqual([20.0, 1000.0, 20000.0], d['frequency'])
        self.assertIn('raw', d)
        self.assertEqual([0.0, 3.0, 0.0], d['raw'])

    def test_parse_csv7(self):
        d = parse_csv(csv7)
        self.assertIn('frequency', d)
        self.assertEqual([20.0, 1000.0, 20000.0], d['frequency'])
        self.assertIn('raw', d)
        self.assertEqual([0.0, 3.0, 0.0], d['raw'])

    def test_parse_csv8(self):
        d = parse_csv(csv8)
        self.assertIn('raw', d)
        self.assertEqual([20.0, 1000.0, 20000.0], d['frequency'])
        self.assertIn('raw', d)
        self.assertEqual([0.81, 0.89, 0.95], d['raw'])

    def test_parse_csv9(self):
        d = parse_csv(csv9)
        self.assertIn('frequency', d)
        self.assertEqual([20.0, 1000.0, 20000.0], d['frequency'])
        self.assertIn('raw', d)
        self.assertEqual([69.6, 69.7, 51.0], d['raw'])

    def test_parse_csv10(self):
        d = parse_csv(csv10)
        self.assertIn('frequency', d)
        self.assertEqual([20.0, 20.25, 19998.498], d['frequency'], )
        self.assertIn('raw', d)
        self.assertEqual([68.334, 68.335, 27.402], d['raw'])

    def test_parse_csv11(self):
        d = parse_csv(csv11)
        self.assertIn('frequency', d)
        self.assertEqual([20.0, 20.299999, 20.600000], d['frequency'], )
        self.assertIn('raw', d)
        self.assertEqual([96.774, 96.813, 96.843], d['raw'])
