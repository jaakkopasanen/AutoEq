import sys
from pathlib import Path
ROOT_PATH = Path().absolute().parent.parent
if str(ROOT_PATH) not in sys.path:
    sys.path.insert(1, str(ROOT_PATH))
from peq import PEQ, Peaking
from frequency_response import FrequencyResponse
from constants import DEFAULT_FS, PEQ_CONFIGS
import matplotlib.pyplot as plt
import numpy as np
from time import time

fs = DEFAULT_FS
#fs = 192000
fr = FrequencyResponse.read_from_csv(ROOT_PATH.joinpath('results/oratory1990/harman_in-ear_2019v2/1MORE Quad Driver/1MORE Quad Driver.csv'))
t = time()
#fr.interpolate(f_step=1.05)
fr.optimize_parametric_eq(PEQ_CONFIGS['4_PEAKING_WITH_LOW_SHELF'], fs)
print(f'{(time() - t)*1000:.1f} ms')
