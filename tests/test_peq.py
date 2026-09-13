import unittest
from unittest.mock import patch
import numpy as np
from autoeq.peq import PEQ, Peaking, OptimizationHistory


class TestPeqCallback(unittest.TestCase):
    """Regression test for the optimizer callback's change_rate division.

    `PEQ._callback` divides a loss delta by a time delta (`d_time`) measured between two
    successive optimizer iterations. `d_time` can legitimately be 0.0 when two callbacks land
    within the same clock tick, e.g. when loss evaluations are cheap relative to the clock's
    resolution. That must not raise ZeroDivisionError or leak inf/nan into the optimization
    history, since a nan change rate silently disables the "change too small" stopping
    criterion for the rest of the run.
    """

    def setUp(self):
        self.f = np.geomspace(20, 20000, 50)
        self.fs = 44100
        self.target = np.zeros(len(self.f))
        self.filt = Peaking(
            self.f, self.fs, fc=1000, q=1.0, gain=3.0,
            min_fc=20, max_fc=10000, min_q=0.1, max_q=6, min_gain=-12, max_gain=12,
            optimize_fc=True, optimize_q=True, optimize_gain=True)
        # Disable every other stopping criterion so only the callback's time handling is exercised.
        # (min_std=None would fall back to PEQ's non-zero default, so it must be 0 here instead.)
        self.peq = PEQ(self.f, self.fs, filters=[self.filt], target=self.target, min_std=0.0)

    def test_repeated_timestamp_does_not_divide_by_zero(self):
        # Absolute perf_counter() readings: the first is consumed as OptimizationHistory's
        # start_time, the rest as one reading per _callback() call. Indices 8-10 (elapsed
        # 0.0075s) simulate a clock whose resolution is coarser than the gap between two
        # callbacks -- exactly the point where change_rate first becomes active, since it
        # requires more than n=8 samples of history.
        absolute_timestamps = [
            0.000, 0.001, 0.002, 0.003, 0.004, 0.005, 0.006, 0.0075, 0.0075, 0.0075, 0.008, 0.009,
        ]
        dummy_params = np.zeros(3)

        with patch('autoeq.peq.perf_counter', side_effect=absolute_timestamps):
            self.peq.history = OptimizationHistory()
            with self.assertRaises(StopIteration):
                # Exhaust the fake clock rather than guessing exactly how many callbacks fire;
                # a ZeroDivisionError or RuntimeWarning-as-error would surface before this.
                with np.errstate(divide='raise', invalid='raise'):
                    for _ in range(len(absolute_timestamps) + 5):
                        self.peq._callback(dummy_params)

        self.assertTrue(all(np.isfinite(cr) for cr in self.peq.history.change_rate))
        self.assertEqual(self.peq.history.time.count(0.0075), 3)


if __name__ == '__main__':
    unittest.main()
