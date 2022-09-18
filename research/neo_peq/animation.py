import sys
from pathlib import Path
from time import time
from copy import deepcopy
import yaml
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter
ROOT_PATH = Path().absolute().parent.parent
if str(ROOT_PATH) not in sys.path:
    sys.path.insert(1, str(ROOT_PATH))
from frequency_response import FrequencyResponse
from constants import DEFAULT_FS, PEQ_CONFIGS

with open(ROOT_PATH.joinpath('peq.yaml')) as fh:
    config = yaml.safe_load(fh)
fr = FrequencyResponse.read_from_csv(ROOT_PATH.joinpath('my_results/F3/Custom Art FIBAE 3 (CIEM).csv'))
config = PEQ_CONFIGS['4_PEAKING_WITH_LOW_SHELF']
config['optimizer']['min_std'] = 0.0
peqs = fr.optimize_parametric_eq(config, DEFAULT_FS)
peq = peqs[0]
#peq.plot()
#plt.show()


def interpolate(current, previous, ratio):
    return previous + ratio * (current - previous)


param_history = []
time_history = []
times = []
for i in range(1, len(peq.history.params)):
    for j in range(10):
        param_history.append(interpolate(np.array(peq.history.params[i]), np.array(peq.history.params[i - 1]), j / 10))
        time_history.append(interpolate(np.array(peq.history.time[i]), np.array(peq.history.time[i - 1]), j / 10))

fig, ax = FrequencyResponse.init_plot()
fills = [ax.fill_between([], [], []) for _ in peq.filters]
lines = [ax.plot([], [], linewidth=1, color=f'C{i}')[0] for i in range(len(peq.filters))]
lines.append(ax.plot([], [], color='black', linestyle='--')[0])
lines.append(ax.plot([], [], color='black')[0])
ax.set_ylim([-10, 15])


def animate(i):
    peq._parse_optimizer_params(param_history[i])
    ax.collections.clear()
    for j, filt in enumerate(peq.filters):
        ax.fill_between(filt.f, np.zeros(filt.fr.shape), filt.fr, alpha=0.3, color=f'C{j}')
        lines[j].set_data(filt.f, filt.fr)
    lines[-2].set_data(peq.f, peq.target)
    lines[-1].set_data(peq.f, peq.fr)
    ax.set_title(f't={time_history[i] * 1000:.0f} ms')
    return lines


ani = FuncAnimation(fig, animate, frames=len(param_history), interval=3, repeat=False)
ani.save('peq.mp4', writer=FFMpegWriter(fps=60))
plt.show()
