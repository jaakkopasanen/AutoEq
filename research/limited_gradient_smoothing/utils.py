# -*- coding: utf-8 -*-

import numpy as np


def log_log_gradient(f0, f1, g0, g1):
    octaves = np.log(f1 / f0) / np.log(2)
    gain = g1 - g0
    return gain / octaves
