# -*- coding: utf-8 -*

import os
import math

DEFAULT_F_MIN = 20.0
DEFAULT_F_MAX = 20000.0
DEFAULT_STEP = 1.01

DEFAULT_MAX_GAIN = 6.0
DEFAULT_TREBLE_F_LOWER = 6000.0
DEFAULT_TREBLE_F_UPPER = 8000.0
DEFAULT_TREBLE_MAX_GAIN = 6.0
DEFAULT_TREBLE_GAIN_K = 1.0

DEFAULT_SMOOTHING_WINDOW_SIZE = 1 / 12
DEFAULT_SMOOTHING_ITERATIONS = 1
DEFAULT_TREBLE_SMOOTHING_F_LOWER = 6000.0
DEFAULT_TREBLE_SMOOTHING_F_UPPER = 8000.0
DEFAULT_TREBLE_SMOOTHING_WINDOW_SIZE = 2.0
DEFAULT_TREBLE_SMOOTHING_ITERATIONS = 1
DEFAULT_SOUND_SIGNATURE_SMOOTHING_WINDOW_SIZE = None

DEFAULT_FS = 44100
DEFAULT_BIT_DEPTH = 16
DEFAULT_PHASE = 'minimum'
DEFAULT_F_RES = 10.0

DEFAULT_TILT = 0.0
DEFAULT_BASS_BOOST_GAIN = 0.0
DEFAULT_BASS_BOOST_FC = 105.0
DEFAULT_BASS_BOOST_Q = 0.7
DEFAULT_TREBLE_BOOST_GAIN = 0.0
DEFAULT_TREBLE_BOOST_FC = 10000.0
DEFAULT_TREBLE_BOOST_Q = 0.7

DEFAULT_PEQ_OPTIMIZER_MIN_F = 20.0
DEFAULT_PEQ_OPTIMIZER_MAX_F = 20000.0
DEFAULT_PEQ_OPTIMIZER_MAX_TIME = None
DEFAULT_PEQ_OPTIMIZER_TARGET_LOSS = None
DEFAULT_PEQ_OPTIMIZER_MIN_CHANGE_RATE = None
DEFAULT_PEQ_OPTIMIZER_MIN_STD = 0.002

DEFAULT_FIXED_BAND_FILTER_MIN_GAIN = -12.0
DEFAULT_FIXED_BAND_FILTER_MAX_GAIN = 12.0

DEFAULT_PEAKING_FILTER_MIN_FC = 20.0
DEFAULT_PEAKING_FILTER_MAX_FC = 10000.0
DEFAULT_PEAKING_FILTER_MIN_Q = 0.18248  # AUNBandEq has maximum bandwidth of 5 octaves which is Q of 0.182479
DEFAULT_PEAKING_FILTER_MAX_Q = 6.0
DEFAULT_PEAKING_FILTER_MIN_GAIN = -20.0
DEFAULT_PEAKING_FILTER_MAX_GAIN = 20.0

DEFAULT_SHELF_FILTER_MIN_FC = 20.0
DEFAULT_SHELF_FILTER_MAX_FC = 10000.0
DEFAULT_SHELF_FILTER_MIN_Q = 0.4  # Shelf filters start to overshoot below 0.4
DEFAULT_SHELF_FILTER_MAX_Q = 0.7  # Shelf filters start to overshoot above 0.7
DEFAULT_SHELF_FILTER_MIN_GAIN = -20.0
DEFAULT_SHELF_FILTER_MAX_GAIN = 20.0

DEFAULT_BIQUAD_OPTIMIZATION_F_STEP = 1.02

DEFAULT_MAX_SLOPE = 18.0
DEFAULT_PREAMP = 0.0

DEFAULT_GRAPHIC_EQ_BANDS = 127

ROOT_DIR = os.path.abspath(os.path.dirname(os.path.abspath(__file__)))
MOD_REGEX = r' \((sample|serial number) [a-zA-Z0-9\-]+\)$'
DBS = ['crinacle', 'headphonecom', 'innerfidelity', 'oratory1990', 'rtings']
HARMAN_OVEREAR_PREFERENCE_FREQUENCIES = [20.0, 21.0, 22.0, 24.0, 25.0, 27.0, 28.0, 30.0, 32.0, 34.0, 36.0, 38.0, 40.0, 43.0, 45.0, 48.0, 50.0, 53.0, 56.0, 60.0, 63.0, 67.0, 71.0, 75.0, 80.0, 85.0, 90.0, 95.0, 100.0, 106.0, 112.0, 118.0, 125.0, 132.0, 140.0, 150.0, 160.0, 170.0, 180.0, 190.0, 200.0, 212.0, 224.0, 236.0, 250.0, 265.0, 280.0, 300.0, 315.0, 335.0, 355.0, 375.0, 400.0, 425.0, 450.0, 475.0, 500.0, 530.0, 560.0, 600.0, 630.0, 670.0, 710.0, 750.0, 800.0, 850.0, 900.0, 950.0, 1000.0, 1060.0, 1120.0, 1180.0, 1250.0, 1320.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2120.0, 2240.0, 2360.0, 2500.0, 2650.0, 2800.0, 3000.0, 3150.0, 3350.0, 3550.0, 3750.0, 4000.0, 4250.0, 4500.0, 4750.0, 5000.0, 5300.0, 5600.0, 6000.0, 6300.0, 6700.0, 7100.0, 7500.0, 8000.0, 8500.0, 9000.0, 9500.0, 10000.0, 10600.0, 11200.0, 11800.0, 12500.0, 13200.0, 14000.0, 15000.0, 16000.0, 17000.0, 18000.0, 19000.0, 20000.0]
HARMAN_INEAR_PREFENCE_FREQUENCIES = [20.0, 21.2, 22.4, 23.6, 25.0, 26.5, 28.0, 30.0, 31.5, 33.5, 35.5, 37.5, 40.0, 42.5, 45.0, 47.5, 50.0, 53.0, 56.0, 60.0, 63.0, 67.0, 71.0, 75.0, 80.0, 85.0, 90.0, 95.0, 100.0, 106.0, 112.0, 118.0, 125.0, 132.0, 140.0, 150.0, 160.0, 170.0, 180.0, 190.0, 200.0, 212.0, 224.0, 236.0, 250.0, 265.0, 280.0, 300.0, 315.0, 335.0, 355.0, 375.0, 400.0, 425.0, 450.0, 475.0, 500.0, 530.0, 560.0, 600.0, 630.0, 670.0, 710.0, 750.0, 800.0, 850.0, 900.0, 950.0, 1000.0, 1060.0, 1120.0, 1180.0, 1250.0, 1320.0, 1400.0, 1500.0, 1600.0, 1700.0, 1800.0, 1900.0, 2000.0, 2120.0, 2240.0, 2360.0, 2500.0, 2650.0, 2800.0, 3000.0, 3150.0, 3350.0, 3550.0, 3750.0, 4000.0, 4250.0, 4500.0, 4750.0, 5000.0, 5300.0, 5600.0, 6000.0, 6300.0, 6700.0, 7100.0, 7500.0, 8000.0, 8500.0, 9000.0, 9500.0, 10000.0, 10600.0, 11200.0, 11800.0, 12500.0, 13200.0, 14000.0, 15000.0, 16000.0, 17000.0, 18000.0, 19000.0, 20000.0]

PREAMP_HEADROOM = 0.2

PEQ_CONFIGS = {
    '10_BAND_GRAPHIC_EQ': {
        'optimizer': {'min_std': 0.01},
        'filter_defaults': {'q': math.sqrt(2), 'min_gain': -12.0, 'max_gain': 12.0, 'type': 'PEAKING'},
        'filters': [{'fc': 31.25 * 2 ** i} for i in range(10)]
    },
    '31_BAND_GRAPHIC_EQ': {
        'optimizer': {'min_std': 0.01},
        'filter_defaults': {'q': 4.318473, 'min_gain': -12.0, 'max_gain': 12.0, 'type': 'PEAKING'},
        'filters': [{'fc': 20 * 2 ** (i / 3), 'type': 'PEAKING'} for i in range(31)]
    },
    '10_PEAKING': {
        'filters': [{'type': 'PEAKING'}] * 10
    },
    '8_PEAKING_WITH_SHELVES': {
        'optimizer': {
            'min_std': 0.008
        },
        'filters': [{
            'type': 'LOW_SHELF',
            'fc': 105.0,
            'q': 0.7
        }, {
            'type': 'HIGH_SHELF',
            'fc': 10000.0,
            'q': 0.7
        }] + [{'type': 'PEAKING'}] * 8
    },
    '4_PEAKING_WITH_LOW_SHELF': {
        'optimizer': {
            'max_f': 10000.0,
        },
        'filters': [{
            'type': 'LOW_SHELF',
            'fc': 105.0,
            'q': 0.7
        }] + [{'type': 'PEAKING'}] * 4
    },
    '4_PEAKING_WITH_HIGH_SHELF': {
        'filters': [{
            'type': 'HIGH_SHELF',
            'fc': 10000.0,
            'q': 0.7
        }] + [{'type': 'PEAKING'}] * 4
    },
    'AUNBANDEQ': {
        'optimizer': {
            'min_std': 0.008
        },
        'filters': [{
            'type': 'LOW_SHELF',
            'fc': 105.0,
            'q': 0.7
        }, {
            'type': 'HIGH_SHELF',
            'fc': 10000.0,
            'q': 0.7
        }] + [{
            'type': 'PEAKING',
            'min_fc': 20.0,  # Can go to 16 Hz
            'max_fc': 10000.0,  # Can go to 20 kHz
            'min_q': 0.182479,  # Max bw of 5.0
            'max_q': 10.0  # Min bw of 0.01 = 144.27 Q
        }] * 8
    },
    'MINIDSP_2X4HD': {
        'optimizer': {
            'min_std': 0.008
        },
        'filter_defaults': {
            'min_gain': -16.0,
            'max_gain': 16.0,
        },
        'filters': [{
            'type': 'LOW_SHELF',
            'fc': 105.0,
            'q': 0.7
        }, {
            'type': 'HIGH_SHELF',
            'fc': 10000.0,
            'q': 0.7
        }] + [{
            'type': 'PEAKING',
            'min_q': 0.5,
            'max_q': 6.0,
            'min_fc': 20.0,
            'max_fc': 10000.0,
        }] * 8
    },
    'MINIDSP_IL_DSP': {
        'optimizer': {
            'min_std': 0.008
        },
        'filter_defaults': {
            'min_gain': -16.0,
            'max_gain': 16.0,
        },
        'filters': [{
            'type': 'LOW_SHELF',
            'fc': 105.0,
            'q': 0.7
        }, {
            'type': 'HIGH_SHELF',
            'fc': 10000.0,
            'q': 0.7
        }] + [{
            'type': 'PEAKING',
            'min_q': 0.5,
            'max_q': 6.0,
            'min_fc': 20.0,
            'max_fc': 10000.0,
        }] * 8
    },
    'NEUTRON_MUSIC_PLAYER': {
        'optimizer': {
            'min_std': 0.008
        },
        'filter_defaults': {
            'min_gain': -12.0,
            'max_gain': 12.0,
        },
        'filters': [{
            'type': 'LOW_SHELF',
            'fc': 105.0,
            'q': 0.7
        }, {
            'type': 'HIGH_SHELF',
            'fc': 10000.0,
            'q': 0.7
        }] + [{
            'type': 'PEAKING',
            'min_q': 0.1,
            'max_q': 5.0,
            'min_fc': 20.0,
            'max_fc': 10000.0,
        }] * 8
    },
    'POWERAMP_EQUALIZER': {
        'optimizer': {
            'min_std': 0.008
        },
        'filter_defaults': {
            'min_gain': -15.0,
            'max_gain': 15.0,
        },
        'filters': [{
            'type': 'LOW_SHELF',
            'fc': 105.0,
            'q': 0.7
        }, {
            'type': 'HIGH_SHELF',
            'fc': 10e3,
            'q': 0.7
        }] + [{
            'type': 'PEAKING',
            'min_q': 0.1,
            'max_q': 12.0,
            'min_fc': 20.0,
            'max_fc': 10000.0,
        }] * 8
    },
    'QUDELIX_5K': {
        'optimizer': {
            'min_std': 0.008
        },
        'filter_defaults': {
            'min_gain': -12.0,
            'max_gain': 12.0,
        },
        'filters': [{
            'type': 'LOW_SHELF',
            'fc': 105.0,
            'q': 0.7
        }, {
            'type': 'HIGH_SHELF',
            'fc': 10e3,
            'q': 0.7
        }] + [{
            'type': 'PEAKING',
            'min_q': 0.1,
            'max_q': 7.0,
            'min_fc': 20.0,
            'max_fc': 10000.0,
        }] * 8
    },
    'SPOTIFY': {
        'optimizer': {'min_std': 0.01},
        'filters': [
            {'fc': 60.0, 'q': 1.0, 'type': 'PEAKING'},
            {'fc': 150.0, 'q': 1.0, 'type': 'PEAKING'},
            {'fc': 400.0, 'q': 1.0, 'type': 'PEAKING'},
            {'fc': 2400.0, 'q': 1.0, 'type': 'PEAKING'},
            {'fc': 15000.0, 'q': 1.0, 'type': 'PEAKING'},
        ]
    },
    'USB_AUDIO_PLAYER_PRO': {
        'optimizer': {
            'min_std': 0.008
        },
        'filter_defaults': {
            'min_gain': -20.0,
            'max_gain': 20.0,
        },
        'filters': [{
            'type': 'LOW_SHELF',
            'fc': 105.0,
            'q': 0.7
        }, {
            'type': 'HIGH_SHELF',
            'fc': 10000.0,
            'q': 0.7
        }] + [{
            'type': 'PEAKING',
            'min_q': 0.1,
            'max_q': 10.0,
            'min_fc': 20.0,
            'max_fc': 10000.0,
        }] * 8
    },
}
