# AutoEq
AutoEq is a tool for equalizing headphone frequency responses automatically, and it achieves this by parsing
frequency response measurements and producing equalization settings which correct the headphone to a neutral sound.
AutoEq provides methods for reading data, equalizing it to a given target
response and saving the results for usage with equalizers. It's possible to use different compensation (target)
curves, apply tilt for making the headphones brighter/darker and adding a bass boost. It's even possible to make one
headphone sound (roughly) like another headphone. For more info about usage see [Usage](#usage).

AutoEq [Github page](https://github.com/jaakkopasanen/AutoEq) also serves as a database for headphone frequency response
measurements, pre-computed results and has documentation about different equalizers and how the implementation works.

### Updates
#### 2.2.0
Added `--preamp` parameter

#### 2.1.1
Fixed README in PyPi package

#### 2.1.0
Fixed dependencies for Apple Silicon and added `--treble-boost` parameter.

#### 2.0.0
Restructured the project and published in PyPi. Source code moved under [autoeq](./autoeq) directory and 
command line usage changed from `python autoeq.py` to `python -m autoeq` with underscores `_` replaced with hyphens `-`
in the parameter names. 

Parametric eq optimizer reworked. The new optimizer supports shelf filters, has a powerful configuration
system, run 10x faster, has limits for Fc, Q and gain value ranges and treats +10 kHz range as average value instead of
trying to fix it precisely.

## Installing
AutoEq requires Python 3 and should work with any decently recent version of Python 3.
```shell
pip install autoeq
```

You may need to install [libsndfile](http://www.mega-nerd.com/libsndfile/)

On Windows you may need to install
[Microsoft Visual C++ Redistributable for Visual Studio 2015, 2017, and 2019](https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads)

## Usage
AutoEq has command line interface in addition to Python methods. See `python -m autoeq --help` for arguments.

The full functionality with file input and output can be used with `batch_processing`:
```shell
from autoeq.batch_processing import batch_processing

batch_processing(
  input_dir='path/to/measurements', output_dir='path/to/results', new_only=False, standardize_input=False,
  compensation='path/to/compensation.csv', parametric_eq=True, fixed_band_eq=True, rockbox=False,
  ten_band_eq=True, parametric_eq_config='8_PEAKING_WITH_SHELVES', fixed_band_eq_config='10_BAND_GRAPHIC_EQ',
  convolution_eq=True, fs=44100, bit_depth=16, phase='minimum', f_res=10, bass_boost_gain=6,
  bass_boost_fc=105, bass_boost_q=0.7, treble_boost_gain=0, treble_boost_fc=10000, treble_boost_q=0.7, tilt=None,
  sound_signature=None, max_gain=12, thread_count=0)
```

The main functionalities of AutoEq are in `frequency_response` which implements `FrequencyResponse` class. Parametric
equalizer optimization and frequency response computations are implemented in `peq`.
```python
from autoeq.frequency_response import FrequencyResponse
from autoeq.constants import PEQ_CONFIGS

harman_target = FrequencyResponse.read_from_csv('path/to/harman_over-ear_2018.csv')

fr = FrequencyResponse.read_from_csv('path/to/measurement.csv')
fr.interpolate()  # Creates standard logarithmic sampling when no argument is passed
fr.center()  # Centers the frequency response around 0 dB
fr.compensate(harman_target)  # Creates target and error data for the FR
fr.smoothen_fractional_octave()  # Smoothens the FR data and error
fr.equalize(concha_interference=True)  # Creates equalization target
peqs = fr.optimize_parametric_eq(PEQ_CONFIGS['8_PEAKING_WITH_SHELVES'], 44100)
for filt in peqs[0].filters:
    print(f'{filt.gain:.2f} db, {filt.fc:.2f} Hz, {filt.q:.2f} Q')
```
