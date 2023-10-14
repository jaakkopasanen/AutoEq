import unittest
from autoeq.csv import parse_csv, create_csv, find_csv_separators, autoeq_pattern, rew_pattern

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


class TestCsv(unittest.TestCase):
    def test_regex(self):
        for s, pattern in [(csv1, autoeq_pattern), (csv2, None), (csv3, None), (csv4, None), (csv5, rew_pattern), (csv6, None), (csv7, None)]:
            if pattern:
                self.assertTrue(bool(pattern.match(s)))

    def test_find_csv_separators(self):
        for s, true_col, true_dec in [(csv1, ',', '.'), (csv2, '\t', '.'), (csv3, ';', ','), (csv4, '\t', '.'), (csv5, ',', '.'), (csv6, '\t', '.'), (csv7, ',', '.')]:
            col, dec = find_csv_separators(s)
            self.assertEqual(col, true_col)
            self.assertEqual(dec, true_dec)

    def test_parse_csv1(self):
        d = parse_csv(csv1)
        self.assertIn('frequency', d)
        self.assertEqual(d['frequency'], [20.0, 1000.0, 20000.0])
        self.assertIn('raw', d)
        self.assertEqual(d['raw'], [0.0, 3.0, 0.0])

    def test_parse_csv2(self):
        d = parse_csv(csv2)
        self.assertIn('frequency', d)
        self.assertEqual(d['frequency'], [20.0, 1000.0, 20000.0])
        self.assertIn('raw', d)
        self.assertEqual(d['raw'], [0.0, 3.0, 0.0])

    def test_parse_csv3(self):
        d = parse_csv(csv3)
        self.assertIn('frequency', d)
        self.assertEqual(d['frequency'], [20.0, 1000.0, 20000.0])
        self.assertIn('raw', d)
        self.assertEqual(d['raw'], [0.0, 3.0, 0.0])

    def test_parse_csv4(self):
        d = parse_csv(csv4)
        self.assertIn('frequency', d)
        self.assertEqual(d['frequency'], [20.0, 1000.0, 20000.0])
        self.assertIn('raw', d)
        self.assertEqual(d['raw'], [0.0, 3.0, 0.0])

    def test_parse_csv5(self):
        d = parse_csv(csv5)
        self.assertIn('frequency', d)
        self.assertEqual(d['frequency'], [20.0, 1000.0, 20000.0])
        self.assertIn('raw', d)
        self.assertEqual(d['raw'], [0.0, 3.0, 0.0])

    def test_parse_csv6(self):
        d = parse_csv(csv6)
        self.assertIn('frequency', d)
        self.assertEqual(d['frequency'], [20.0, 1000.0, 20000.0])
        self.assertIn('raw', d)
        self.assertEqual(d['raw'], [0.0, 3.0, 0.0])

    def test_parse_csv7(self):
        d = parse_csv(csv7)
        self.assertIn('frequency', d)
        self.assertEqual(d['frequency'], [20.0, 1000.0, 20000.0])
        self.assertIn('raw', d)
        self.assertEqual(d['raw'], [0.0, 3.0, 0.0])
