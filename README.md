# AutoEQ
**TL;DR** If you are here just looking to make your headphones sound better, find your headphone model in
[results](./results) folder's recommended headphones list
and follow instructions in [Usage](#usage) section. 

## About This Project
AutoEQ is a project for equalizing headphone frequency responses automatically and it achieves this by parsing
frequency response measurements and producing equalization settings which correct the headphone to a neutral sound.
This project currently has over 2500 headphones covered in the
[results](./results) folder.
See [Usage](#usage) for instructions how to use the results with
different equalizer softwares and
[Results](#results) section for details about parameters and how the results were
obtained.

AutoEQ is not just a collection of automatically produced headphone equalization settings but also a tool for equalizing
headphones for yourself. `autoeq.py` provides methods for reading data, equalizing it to a given target
response and saving the results for usage with equalizers. It's possible to use different compensation (target)
curves, apply tilt for making the headphones brighter/darker and adding a bass boost. It's even possible to make one
headphone sound (roughly) like another headphone. For more info about equalizing see [Equalizing](#equalizing). If
you're looking for something light weight to install as a dependency for your own project, you'll find
[autoeq-pkg](https://github.com/jaakkopasanen/autoeq-pkg) much more suited for your needs.

Third major contribution of this project is the measurement data and compensation curves all in a numerical format
except for Crinacle's raw data. Everything is stored as CSV files so they are easy to process with any programming
language or even Microsoft Excel.

![Sennheiser HD 800](./results/oratory1990/harman_over-ear_2018/Sennheiser%20HD%20800/Sennheiser%20HD%20800.png)

*Sennheiser HD 800 equalization results plotted*


## Usage
AutoEQ produces settings for basically all types of equalizer apps.

### Parametric Equalizers
Parametric equalizers have filters with user adjustable gain,  center frequency and quality Q. Keep in mind that
parametric eq accuracy depends on the number of filters available. Usually 10 filters produce very good
results but as little as 5 can be good enough. Keep in mind that different parametric equalizers will produce different
outcomes with the same parameter values. Parameters produced by AutoEq are equal with EqualizerAPO using 48 kHz sampling
rate. When using other equalizers or sampling rates, it's always highly recommended to check that the frequency response
of the equalizer matches the parametric eq curve in the graphs.

All parametric equalizer except Peace require you to configure the filter parameters manually with the software user
interface. Some parametric equalizer use filter width (band width) instead of Q. Filter width can be calculated as:
`bw = Fc / Q` where `bw` is the band width in Herts, `Fc` is center frequency and `Q` is quality. Filter width in
octaves can be calculated as: `N = ln(1 + 1/(2*Q^2) + sqrt(((2*Q^2 + 1) / Q^2 )^2 / 4 - 1)) / ln(2)` where `ln` is the
natural logarithm. See http://www.sengpielaudio.com/calculator-bandwidth.htm for an online calculator.

It's very important to set preamp according to the value given in the result README.md document. Parametric eq filters
will produce positive gains and to avoid clipping a preamp with negative gain is required.

Parametric eq settings can be used with Peace or any other parametric eq which has at least 5 bands available. Even
fewer bands is possible but pre-computed results require to use minimum five first of the filters. Parametric equalizer
filter parameters look like this:

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 28 Hz    | 0.46 | 6.3 dB  |
| Peaking | 162 Hz   | 0.91 | -2.3 dB |
| Peaking | 2237 Hz  | 1.94 | -4.6 dB |
| Peaking | 6093 Hz  | 2.26 | -4.7 dB |
| Peaking | 8251 Hz  | 3.71 | -2.9 dB |

### Convolution Equalizers
Convolution equalizer settings are finite impulse responses (FIR filters) and are the most advanced kind of (LTI)
filters. FIR filters make it possible to produce linear phase filters which some may prefer though generally minimum
phase filters are recommended. Convolution equalizer settings are provided as WAV files. Pre-computed results include
impulse responses with 44.1 kHz and 48 kHz but other sampling rates are supported as well. Import the WAV file with
correct sampling frequency into the software to use convolution equalizer.

### Fixed Band Equalizers
Fixed band eq is more commonly known as graphic equalizer but in order not to confuse with EqualizerAPO GraphicEQ it is
called like that in this project. Fixed band equalizer is like parametric equalizer with several peaking filters but
don't have adjustable frequency information, only gain. All other types are preferred over fixed band equalizers but on
some devices these are the only available ones.

Fixed band equalizers have trouble compensating for narrow notches and peaks that fall between two bands. Good example
is [Sennheiser HD 800](./results/oratory1990/harman_over-ear_2018/Sennheiser%20HD%20800)
with it's 6 kHz peak that is right in between 4 kHz and 8 kHz bands of standard 10-band equalizer.
When using 10-band equalizer check if the fixed band equalization curve is very different than the desired equalization
curve at some frequency and adjust the nearby filters by ear for best results.

Fixed band equalizer settings look like this:

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 1.41 | 6.1 dB  |
| Peaking | 62 Hz    | 1.41 | 3.0 dB  |
| Peaking | 125 Hz   | 1.41 | -1.1 dB |
| Peaking | 250 Hz   | 1.41 | -2.2 dB |
| Peaking | 500 Hz   | 1.41 | -0.9 dB |
| Peaking | 1000 Hz  | 1.41 | 0.1 dB  |
| Peaking | 2000 Hz  | 1.41 | 3.6 dB  |
| Peaking | 4000 Hz  | 1.41 | -1.0 dB |
| Peaking | 8000 Hz  | 1.41 | -4.1 dB |
| Peaking | 16000 Hz | 1.41 | -7.5 dB |

### Windows
has [EqualizerAPO](#plain-equalizerapo), [Peace](#peace) and many media players with
parametric equalizers such as [Roon](https://roonlabs.com/) and [Foobar2000](https://www.foobar2000.org/).

#### EqualizerAPO
It's possible to use plain [EqualizerAPO](https://sourceforge.net/projects/equalizerapo/) and edit configuration file in
`C:\Program Files\EqualizerAPO\config\config.txt`. Replace contents of the file with the GraphicEQ.txt file found in
results. Preamp is not needed because it is incorporated into the GraphicEQ line. Using
[Sennheiser HD 650](./results/oratory1990/harman_over-ear_2018/Sennheiser%20HD%20650)
would make config file look like this:
```
GraphicEQ: 20 -0.5; 21 -0.5; 22 -0.5; 23 -0.5; 24 -0.5; 26 -0.5; 27 -0.5; 29 -0.5; 30 -0.5; 32 -0.9; 34 -1.2; 36 -1.5; 38 -1.8; 40 -2.1; 43 -2.4; 45 -2.4; 48 -2.5; 50 -2.6; 53 -3.0; 56 -3.2; 59 -3.3; 63 -3.6; 66 -4.0; 70 -4.5; 74 -5.0; 78 -5.5; 83 -5.9; 87 -6.3; 92 -6.7; 97 -7.0; 103 -7.3; 109 -7.6; 115 -7.8; 121 -8.0; 128 -8.1; 136 -8.4; 143 -8.6; 151 -8.7; 160 -8.8; 169 -8.8; 178 -8.9; 188 -8.9; 199 -9.0; 210 -9.0; 222 -9.0; 235 -8.9; 248 -8.8; 262 -8.6; 277 -8.5; 292 -8.4; 309 -8.3; 326 -8.2; 345 -8.1; 364 -7.9; 385 -7.8; 406 -7.7; 429 -7.6; 453 -7.6; 479 -7.5; 506 -7.4; 534 -7.2; 565 -7.1; 596 -7.0; 630 -7.0; 665 -7.0; 703 -7.0; 743 -7.0; 784 -7.1; 829 -7.1; 875 -7.1; 924 -7.0; 977 -7.1; 1032 -7.2; 1090 -7.3; 1151 -7.2; 1216 -7.0; 1284 -6.9; 1357 -6.7; 1433 -6.4; 1514 -6.2; 1599 -6.1; 1689 -5.9; 1784 -5.6; 1885 -5.4; 1991 -5.2; 2103 -5.1; 2221 -5.2; 2347 -5.5; 2479 -5.8; 2618 -6.2; 2766 -6.6; 2921 -6.9; 3086 -7.0; 3260 -6.8; 3443 -6.2; 3637 -5.6; 3842 -5.1; 4058 -4.6; 4287 -4.2; 4528 -4.2; 4783 -4.8; 5052 -5.2; 5337 -4.8; 5637 -4.3; 5955 -4.7; 6290 -4.9; 6644 -4.7; 7018 -4.8; 7414 -5.7; 7831 -6.3; 8272 -6.5; 8738 -6.5; 9230 -6.5; 9749 -6.5; 10298 -6.5; 10878 -6.5; 11490 -6.5; 12137 -6.5; 12821 -7.8; 13543 -9.9; 14305 -9.7; 15110 -9.0; 15961 -11.0; 16860 -13.5; 17809 -14.5; 18812 -15.2; 19871 -15.7
```

EqualizerAPO has a graphical user interface for adjusting configurations. Launch the editor from
`C:\Program Files\EqualizerAPO\Editor.exe`.

![equalizerapo-editor](https://i.imgur.com/lHhRBuA.png)

*EqualizerAPO Editor GUI*

#### Peace
[Peace](https://sourceforge.net/projects/peace-equalizer-apo-extension/) is a GUI for manipulating parametric eq filters
with EqualizerAPO. Peace also has visualization for the end result equalization frequency response, profile manager for
multiple different eq settings and a switch for disabling everything among other features. Load eq settings into Peace
by clicking *Import* button and select the *<model> ParametricEQ.txt* file. Set the preamp to value mentioned in the
results.

![peace](https://i.imgur.com/e0POEbF.png)

*Peace with full GUI for EqualizerAPO*

### Android
Android has several different equalizer options but not too many powerful apps which work with all apps. Wavelet is the best
option for newer Androids (version 9 and up) but older devices have a built-in fixed band equalizer which works system wide
but the center frequencies and Q values vary so might need to [produce your own results](#equalizing).

#### Wavelet
[Wavelet](https://play.google.com/store/apps/details?id=com.pittvandewitt.wavelet) is an Android app which comes with all the
AutoEq eq profiles built in. The app works with all music apps so is closest to system-wide equalizer one can have on
Android without rooting. The equalizer built into this app is very powerful and can represent the AutoEq profiles very
accurately. There is also an option to tune the sound with graphic equalizer. Wavelet has the best Bluetooth device compatibility of all the tested eq apps on Android.

The main functionalities of Wavelet are free (including AutoEq profiles and graphic eq) but some extra features can be 
unlocked with an in-app purchase.

![Wavelet](https://i.imgur.com/UGiBwFX.png)

#### USB Audio Player PRO
[USB Audio Player PRO](https://play.google.com/store/apps/details?id=com.extreamsd.usbaudioplayerpro) is an Android app
with improved USB audio drivers for usage with USB DACs. USB Audio Player
PRO is not system-wide but works with local files and many streaming services though not with Spotify. USB Audio Player
has Toneboosters Morphit plugin which has parametric equalizer. This app and the plugin are not free.

#### Music EQ Equalizer
The best app for system wide equalization on older Android phones (without rooting) is
[Music Equalizer EQ](https://play.google.com/store/apps/details?id=mediam.music.equalizer) which is a 10-band standard
equalizer. Gains for each band can be adjusted with only 1 dB resolution but this isn't a problem because the average
error is then only 0.25 dB, hardly noticeable. Bigger problem is the potential narrow peaks and notches between the
bands' center frequencies since there isn't really anything that can be done for those. See notes about
[fixed band equalizers](#fixed-band-equalizers).

The app starts in the presets view so you need to click the left arrow in the top left corner to get to the manual view. Here you
can adjust the bands. Set each band level to the closest value to what the equalization settings ask. Pre-computed results
only support standard 10-band equalizers which have band center frequencies at 31, 63, 125, 250, 500, 1000, 2000, 4000,
8000 and 16000 Hz. Q values are not adjustable so you don't have to worry about those even though they are given in the
result settings.

#### Viper4Android
[Viper4Android](https://forum.xda-developers.com/showthread.php?t=2191223) is a system-wide
convolution based equalizer (and much more) on Android but it requires rooting of the device. Viper4Android is supported
with impulse response (WAV) files. For rooted users this is the best option.

#### JamesDSP
[JamesDSP](https://forum.xda-developers.com/android/apps-games/app-reformed-dsp-manager-t3607970) is an alternative to
Viper4Android. It provides a system wide solution, has a convolution engine but requires rooting.

### Linux
#### PulseEffects
[PulseEffects](https://github.com/wwmm/pulseeffects) is a PulseAudio (Linux) module with wide variety of signal
processing tools including parametric equalizer. Load eq settings by clicking the top center cog & clicking
*Import ACO Presets* button and select the ParametricEQ.txt file.
Pre-amp can be adjusted with the input slider.
For versions prior to v4.8.0, adjust filter parameters by clicking the cog button on each filter
and set type to "Bell" and adjust the gain with the slider. Number of filters can be changed by clicking the screwdriver
and wrench button.

![pulseeffects](https://i.imgur.com/F51y5Kl.png)

### OSX / MacOS
System wide parametric EQ solutions on OSX typically rely on separate plugin hosting software and the actual plugin
which does the actual equalization.

Pardon the lack of documentation for these. I have not tested any of the methods myself but they have been suggested by
helpful AutoEQ users.


Audio plugin hosts include:
- [MenuBus](https://www.menubus.audio/versions) has a free version but is no longer actively developed.
- [SoundSource](https://rogueamoeba.com/soundsource/) is in active development but not free.
- [Hosting AU](http://ju-x.com/hostingau.html) with [BlackHole](https://github.com/ExistentialAudio/BlackHole) or
[Soundflower](https://github.com/mattingalls/Soundflower) can be used as a system wide AU plugin host.

EQ plugins include:
- [Voxengo PrimeEQ](https://www.voxengo.com/product/primeeq/) is a parametric EQ plugin but is not free.
- [Fabfilter Pro Q3](https://www.fabfilter.com/products/pro-q-3-equalizer-plug-in) is another parametric EQ plugin, more
expensive than Voxengo but might be easier to install and use.
- [LAConvolver plugin](http://audio.lernvall.com/) is a free convolver EQ which works with impulse response WAV files.
- AUNBandEq comes built in with Mac OSX. Works at least with HostingAU + BlackHole

![hostingau+blackhole](https://user-images.githubusercontent.com/38220377/71527191-9706ac80-28da-11ea-8f70-88caf57c4821.png)

Tutorials:
- [Apple AU Lab + Soundflower + AUNBandEQ Tutorial](https://www.superbestaudiofriends.org/index.php?threads/systemwide-eq-on-mac.7435/) [AU Lab Permission Issue](https://discussions.apple.com/thread/8552731)

#### eqMac2
[eqMac2](https://bitgapp.com/eqmac/) is a free system wide 31-band equalizer on Mac. AutoEQ results don't have 31 band
presets but can be created by passing parameters

```
--fixed_band_eq --q=4.47 --fc=20,25,31.5,40,50,63,80,100,125,160,200,250,315,400,500,630,800,1000,1250,1600,2000,2500,3150,4000,5000,6300,8000,10000,12500,16000,20000
```

### iOS
[Contact me](#contact) if you know good solutions for iOS.

#### EQE
[EQE](https://github.com/rweichler/EQE) is a system wide parametric equalizer on iOS but requires jailbreaking. Here
are instructions on how to set it up: https://www.reddit.com/r/headphones/comments/dqbt81/psa_if_you_have_a_jailbroken_iphone_you_can/

### Hardware
Some devices have built-in equalizers one of these is [Radsone EasStudio ES100](https://www.radsone.com/earstudio).
ES100 is a Bluetooth DAC and amp with built-in 10 band equalizer. Since this is a hardware solution it will work with
practically any source.

## Equalizing
`autoeq.py` is the tool used to produce the equalization results from measurement data. There is no
fancy graphical user interface but instead it is used from command line.

### Installing
- Download and install Git: https://git-scm.com/downloads. When installing Git on Windows, use Windows SSL verification
instead of Open SSL or you might run into problems when installing project dependencies.
- Download and install 64-bit [Python 3.8](https://www.python.org/getit/). Make sure to check *Add Python 3.8 to PATH*.
- You may need to install [libsndfile](http://www.mega-nerd.com/libsndfile/) if you're having problems with `soundfile`
when installing `requirements.txt`
- On Linux you may need to install Python dev packages  
```bash
sudo apt install python3-dev python3-pip python3-venv
```
- On Linux you may need to install [pip](https://pip.pypa.io/en/stable/installing/)
- On Windows you may need to install
[Microsoft Visual C++ Redistributable for Visual Studio 2015, 2017, and 2019](https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads)
- Open a terminal / command prompt. On Windows, search `cmd` in the start menu.
- Clone AutoEq  
```bash
git clone https://github.com/jaakkopasanen/AutoEq.git
```
- Go to AutoEq location  
```bash
cd AutoEq
```
- Create a python virtual environment
```bash
python -m venv venv
```
- Activate virtualenv  
```bash
# On Windows
venv\Scripts\activate.bat
# On Linux and Mac
. venv/bin/activate
```
- Update pip
```bash
python -m pip install -U pip==20.3.3
```
- Install required packages  
```bash
python -m pip install -U -r requirements.txt
```
- Verify installation. If everything went well, you'll see the list of command line parameters AutoEq accepts.  
```bash
python autoeq.py --help
```

When coming back at a later time you'll only need to activate virtual environment again
```bash
# On Windows
cd AutoEq
venv\Scripts\activate.bat
# On Linux and Mac
cd AutoEq
. venv/bin/activate
```

To learn more about virtual environments, read [Python' venv documentation](https://docs.python.org/3.8/library/venv.html).

#### Updating
AutoEq is in active development and gets new measurements, results and features all the time. You can get the latest
version from git
```bash
git pull
```

Dependencies may change from time to time, you can update to the latest with
```bash
python -m pip install -U -r requirements.txt
```

### Command Line Arguments
```
usage: autoeq.py [-h] --input_dir INPUT_DIR [--output_dir OUTPUT_DIR]
                 [--standardize_input] [--new_only]
                 [--compensation COMPENSATION] [--equalize] [--parametric_eq]
                 [--fixed_band_eq] [--fc FC] [--q Q] [--ten_band_eq]
                 [--max_filters MAX_FILTERS] [--fs FS] [--bit_depth BIT_DEPTH]
                 [--phase PHASE] [--f_res F_RES] [--bass_boost BASS_BOOST]
                 [--iem_bass_boost IEM_BASS_BOOST] [--tilt TILT]
                 [--sound_signature SOUND_SIGNATURE] [--max_gain MAX_GAIN]
                 [--treble_f_lower TREBLE_F_LOWER]
                 [--treble_f_upper TREBLE_F_UPPER]
                 [--treble_max_gain TREBLE_MAX_GAIN]
                 [--treble_gain_k TREBLE_GAIN_K] [--show_plot]

optional arguments:
  -h, --help            show this help message and exit
  --input_dir INPUT_DIR
                        Path to input data directory. Will look for CSV files
                        in the data directory and recursively in sub-
                        directories.
  --output_dir OUTPUT_DIR
                        Path to results directory. Will keep the same relative
                        paths for files found in input_dir.
  --standardize_input   Overwrite input data in standardized sampling and
                        bias?
  --new_only            Only process input files which don't have results in
                        output directory.
  --compensation COMPENSATION
                        File path to CSV containing compensation (target)
                        curve. Compensation is necessary when equalizing
                        because all input data is raw microphone data. See
                        "compensation", "innerfidelity/resources" and
                        "headphonecom/resources".
  --equalize            Will run equalization if this parameter exists, no
                        value needed.
  --parametric_eq       Will produce parametric eq settings if this parameter
                        exists, no value needed.
  --fixed_band_eq       Will produce fixed band eq settings if this parameter
                        exists, no value needed.
  --fc FC               Comma separated list of center frequencies for fixed
                        band eq.
  --q Q                 Comma separated list of Q values for fixed band eq. If
                        only one value is passed, it is used for all bands. Q
                        value can be calculated from bandwidth in N octaves by
                        Q = 2^(N/2)/(2^N-1).
  --ten_band_eq         Shortcut parameter for activating standard ten band eq
                        optimization.
  --max_filters MAX_FILTERS
                        Maximum number of filters for parametric EQ. Multiple
                        cumulative optimization runs can be done by giving
                        multiple filter counts separated by "+". "5+5" would
                        create 10 filters where the first 5 are usable
                        independently from the rest 5 and the last 5 can only
                        be used with the first 5. This allows to have multiple
                        configurations for equalizers with different number of
                        bands available. Not limited by default.
  --fs FS               Sampling frequency for impulse response and parametric
                        eq filters. Defaults to 44100.
  --bit_depth BIT_DEPTH
                        Number of bits for every sample in impulse response.
                        Defaults to 16.
  --phase PHASE         Impulse response phase characteristic. "minimum",
                        "linear" or "both". Defaults to "minimum"
  --f_res F_RES         Frequency resolution for impulse responses. If this is
                        20 then impulse response frequency domain will be
                        sampled every 20 Hz. Filter length for impulse
                        responses will be fs/f_res. Defaults to 10.
  --bass_boost BASS_BOOST
                        Bass boost shelf. Sub-bass frequencies will be boosted
                        by this amount. Can be either a single value for a
                        gain in dB or a comma separated list of three values
                        for parameters of a low shelf filter, where the first
                        is gain in dB, second is center frequency (Fc) in Hz
                        and the last is quality (Q). When only a single value
                        (gain) is given, default values for Fc and Q are used
                        which are 100 Hz and 0.65, respectively. For example "
                        --bass_boost=6" or "--bass_boost=9.5,150,0.69".
  --iem_bass_boost IEM_BASS_BOOST
                        iem_bass_boost argument has been removed, use "--
                        bass_boost" instead!
  --tilt TILT           Target tilt in dB/octave. Positive value (upwards
                        slope) will result in brighter frequency response and
                        negative value (downwards slope) will result in darker
                        frequency response. 1 dB/octave will produce nearly 10
                        dB difference in desired value between 20 Hz and 20
                        kHz. Tilt is applied with bass boost and both will
                        affect the bass gain.
  --sound_signature SOUND_SIGNATURE
                        File path to a sound signature CSV file. Sound
                        signature is added to the compensation curve. Error
                        data will be used as the sound signature target if the
                        CSV file contains an error column and otherwise the
                        raw column will be used. This means there are two
                        different options for using sound signature: 1st is
                        pointing it to a result CSV file of a previous run and
                        the 2nd is to create a CSV file with just frequency
                        and raw columns by hand (or other means). The Sound
                        signature graph will be interpolated so any number of
                        point at any frequencies will do, making it easy to
                        create simple signatures with as little as two or
                        three points.
  --max_gain MAX_GAIN   Maximum positive gain in equalization. Higher max gain
                        allows to equalize deeper dips in frequency response
                        but will limit output volume if no analog gain is
                        available because positive gain requires negative
                        digital preamp equal to maximum positive gain.
                        Defaults to 6.0.
  --treble_f_lower TREBLE_F_LOWER
                        Lower bound for transition region between normal and
                        treble frequencies. Treble frequencies can have
                        different max gain and gain K. Defaults to 6000.0.
  --treble_f_upper TREBLE_F_UPPER
                        Upper bound for transition region between normal and
                        treble frequencies. Treble frequencies can have
                        different max gain and gain K. Defaults to 8000.0.
  --treble_max_gain TREBLE_MAX_GAIN
                        Maximum positive gain for equalization in the treble
                        region. Defaults to 0.0.
  --treble_gain_k TREBLE_GAIN_K
                        Coefficient for treble gain, affects both positive and
                        negative gain. Useful for disabling or reducing
                        equalization power in the treble region. Defaults to 1.0.
  --show_plot           Plot will be shown if this parameter exists, no value
                        needed.
```


### Examples

#### Reproducing Results
Reproducing pre-computed results for oratory1990 measured on-ear headphones:
```bash
python autoeq.py --input_dir="measurements/oratory1990/data/onear" --output_dir="my_results/oratory1990/harman_over-ear_2018" --compensation="compensation/harman_over-ear_2018_wo_bass.csv" --equalize --parametric_eq --max_filters=5+5 --ten_band_eq --bass_boost=4.0 --convolution_eq --fs=44100,48000
```

Reproducing pre-computed results for Rtings measured IEMs:
```bash
python autoeq.py --input_dir="measurements/rtings/data/inear" --output_dir="my_results/rtings/avg" --compensation="measurements/rtings/resources/rtings_compensation_avg.csv" --equalize --parametric_eq --max_filters=5+5 --ten_band_eq --bass_boost=6.0 --convolution_eq --fs=44100,48000
```

All parameters used for pre-computed results can be found in the `results/update.py` script.

#### Equalizing Individual Headphones
Equalizing Sennheiser HD 650 and saving results to `my_results/HD650`:
```bash
python autoeq.py --input_dir="measurements/innerfidelity/data/onear/Sennheiser HD 650" --output_dir="my_results/HD650" --compensation="measurements/innerfidelity/resources/innerfidelity_harman_over-ear_2018_wo_bass.csv" --equalize --bass_boost=4 --show_plot --convolution_eq --fs=44100,48000
```

#### Fixed Band Equalizers
Filter parameters for fixed band equalizers can be adjusted with `--q` and `--fc` parameters. Producing fixed band
equalizer settings for Sony WH-1000XM3 app:
```bash
python autoeq.py --input_dir="measurements/oratory1990/data/onear/Sony WH-1000XM3" --output_dir="my_results/Sony WH-1000XM3 (app)" --compensation="compensation/harman_over-ear_2018_wo_bass.csv" --equalize --bass_boost=4.0 --fixed_band_eq --fc=400,1000,2500,6300,16000 --q=1.05
```

#### Using Sound Signatures
AutoEQ provides a way to play around with different sound signatures easily. The use-cases include making headphones
deviate from the neutral target or making one headphone sound like another.

Equalizing Sennheiser HD 800 to sound like Sennheiser HD 650 using pre-computed results. Both have been measured by
oratory1990 so we'll use those measurements. Pre-computed results include 4dB of bass boost for over-ear headphones and
therefore we need to apply a bass boost of 4dB here as well.
```bash
python autoeq.py --input_dir="measurements/oratory1990/data/onear/Sennheiser HD 800" --output_dir="my_results/Sennheiser HD 800 (HD 650)" --compensation="compensation/harman_over-ear_2018_wo_bass.csv" --sound_signature="results/oratory1990/harman_over-ear_2018/Sennheiser HD 650/Sennheiser HD 650.csv" --equalize --parametric_eq --max_filters=5+5 --ten_band_eq --bass_boost=4 --convolution_eq --fs=44100,48000
```

Equalizing Massdrop x Sennheiser HD 800 to sound like AKG K701. There is no K701 measurement made by oratory1990 so
we'll use Innerfidelity's measurement for the sound signature. The list of recommended results always points to best
measurement so you can check there which one to use (measurement system can be found in the URL).
```bash
python autoeq.py --input_dir="measurements/oratory1990/data/onear/Sennheiser HD 800" --output_dir="my_results/Sennheiser HD 800 (K701)" --compensation="compensation/harman_over-ear_2018_wo_bass.csv" --sound_signature="results/innerfidelity/innerfidelity_harman_over-ear_2018/AKG K701/AKG K701.csv" --equalize --parametric_eq --max_filters=5+5 --ten_band_eq --bass_boost=4 --convolution_eq --fs=44100,48000
```

Equalizing HiFiMAN HE400S to sound like Massdrop x Meze 99 Noir. HE400S is measured only by Innerfidelity so we'll point
compensation file pointing to Innerfidelity's calibrated Harman target. Meze 99 Noir has massive natural bass boost and
to capture that we need to relax max gain to +12dB.
```bash
python autoeq.py --input_dir="measurements/innerfidelity/data/onear/HiFiMAN HE400S" --output_dir="my_results/HE400S (99 Noir)" --compensation="measurements/innerfidelity/resources/innerfidelity_harman_over-ear_2018_wo_bass.csv" --sound_signature="results/oratory1990/harman_over-ear_2018/Meze 99 Noir/Meze 99 Noir.csv" --equalize --parametric_eq --max_filters=5+5 --ten_band_eq --bass_boost=4 --max_gain=8
```

Applying V-shaped sound signature to Audeze Mobius. First step is to create the sound signature file. Save this to
`my_data/v.csv`:
```csv
frequency,raw
20,4.0
1000,-4.0
10000,4.0
20000,0.0
```
Then use it by providing the path to `--sound_signature` parameter. We'll set bass boost to 0dB because the sound
signature already has a significant bass boost. Of course it's possible to add bass boost on top of the sound signature
file if you want even more bass.
```bash
python autoeq.py --input_dir="measurements/rtings/data/onear/Audeze Mobius" --output_dir="my_results/Audeze Mobius (V-signature)" --compensation="measurements/rtings/resources/rtings_compensation_avg.csv" --sound_signature="my_data/v.csv" --equalize --parametric_eq --max_filters=5+5 --ten_band_eq --bass_boost=4.0
```

## Results
The main principle used by AutoEQ for producing the equalization function is to invert the error curve. Error is the
difference between raw microphone data and the compensation (target) curve. If headphone's frequency response is 4 dB
below the target at 20 Hz equalization function will have +4 dB boost at 20 Hz. In reality simply inverting the error is
not sufficient since measurements and equalization have several problems that need to be addressed, see
[Technical Challenges](#technical-challenges) for more details.

Results provided in this project currently have all the headphone measurements from
- [Crinacle](https://crinacle.com/)
- [Headphone.com](http://graphs.headphone.com/)
- [Innerfidelity](https://www.innerfidelity.com/headphone-measurements)
- [oratory1990](https://www.reddit.com/r/oratory1990)
- [Reference Audio Analyzer](https://reference-audio-analyzer.pro/en/catalog-reports.php?sp_1=1&tp=1)
- [Rtings](https://www.rtings.com/headphones)
with the exception of Reference Audio Analyzer measurements done on the SF1 system.

Results are organized by `source/target/headphone` so a Sennheiser HD 650 measured by Innerfidelity and tuned to a
calibrated Harman target would be found in
[innerfidelity/innerfidelity_harman_over-ear_2018/Sennheiser HD 650](./results/innerfidelity/innerfidelity_harman_over-ear_2018/Sennheiser%20HD%20650).
Multiple measurements of the same headphone by the same measurement entity are averaged. All different measurements for
averaging have been renamed with snXXX (serial number) or sample X in the end of the name to distinguish from the
averaged data which has no suffixes in the name.

oratory1990 measurements have been done on Gras 43AG and 43AC couplers, the same which were used to develop Harman
target responses by Olive et al. and therefore use Harman target responses for the equalization targets. These results
are recommended over all other measurements because of this reason. Harman target data is in the `compensation` folder.

Crinacle's in-ear measurements have been performed with IEC 60318-4 coupler and are therefore compatible with
Harman in-ear targets. This fact also earns Crinacle's measurements second highest ranking recommendation after
oratory1990. Crinacle's over-ear measurements use the same ear simulator attached to a MiniDSP ears pinna. The
measurements done on this system are not as accurate as oratory1990's but because of the high quality ear simulator,
these are a bit better than rest.

Innerfidelity, Rtings and Headphone.com measurements have been performed on Head Acoustics HMSII.3 measurement system.
This system is not an industry standard anymore because of the rigid pinnae. The Headphone.com measurements are the old
ones which are no longer available. These are not to be consfused with the new measurements Resolve is producing using
GRAS system.

Reference Audio Analyzer have [three different measurement systems](https://reference-audio-analyzer.pro/en/stands.php)
none of which seem to represent human hearing particularly well. The most recent HDM-X system is close to the Head
Acoustics HMSII.3 systems but seems to suffer a bit more in the bass range. HDM1 is clearly worse than other systems
and the measurements done on the SF1 system are not included at all because that is a flat plate coupler. IEM measurements
are done with what looks like a tubing coupler and these don't look very accurate. Reference Audio Analyzer
measurements and results are a last resort.

All of the results use frequency response targets that were specifically developed for this project except oratory1990
and Crinacle's IEM measurements which use standard Harman targets. The target curves were developed by calibrating
measurements against reference measurements by oratory1990 and Crinacle (IEMs) and modifying the Harman 2018 over-ear
and 2019 in-ear targets with the calibration data.

None of these targets have bass boost seen in Harman target responses and therefore a +4dB boost was applied for all
over-ear headphones, +6dB for in-ear headphones and no boost for earbuds. Harman targets actually ask for about +6dB for
over-ears and +9dB for in-ears but since some headphones cannot achieve this with positive gain limited to +6dB, a
smaller boost was selected. Above 6 to 12 kHz data is filtered more heavily to avoid equalizing the narrow dips and
notches that depend heavily on the listener's own ears.

### oratory1990 IEM Target
In-ear results with oratory1990 target (formerly "Usound" target) are not longer given because the new 2019 Harman
in-ear fixes the +10 kHz problems of the 2017 target. Also it is easy to transform results created for Harman 2019 to
oratory1990 target without running the processing yourself if you are using parametric equalizer and have two filters
(bands) available by adding these two to your eq software:

| Type    |   Fc |    Q |  Gain |
|:--------|:-----|:-----|:------|
| Peaking |  113 | 0.75 |   3.5 |
| Peaking | 3766 | 0.63 |  -2.3 |

The results will be remarkably similar to results produced with the actual oratory1990 target:

![oratory1990 vs Harman in-ear 2019](https://i.imgur.com/kGYBOev.png)

Of course it's still possible to produce native results with oratory1990 target by pointing compensation to the
oratory1990 target file: `--compensation="compensation/oratory1990.csv` or
`--compensation="compensation/oratory1990_wo_bass.csv`

### Innerfidelity Target by Super Best Audio Friends Forum User "Serious"
Innerfidelity and Headphone.com measured headphones previously used
[SBAF-Serious target](https://www.superbestaudiofriends.org/index.php?threads/innerfidelity-fr-target.5560/) only.
The SBAF-Serious curve is no longer used for these measurements since a new targets were developed by calibrating Harman
targets. This is a modified version of Innerfidelity target curve produced by a user called Serious on Super Best Audio
Friends forum. This curve doesn't have any glaring problems and is quite well balanced overall. Curve was turned into a
compensation for raw microphone data and tilted 0.2 dB / octave brighter. Innerfidelity measurements are recommended
over Headphone.com measurements because SBAF-Serious target was developed for Innerfidelity. SBAF-Serious curve was
modified to be suitable for Headphone.com measurements. CSV data files for Innerfidelity and
Headphone.com are at `innerfidelity/resources/innerfidelity_compensation_sbaf-serious.csv` and
`headphonecom/resources/headphonecom_compensation_sbaf-serious.csv`, respectively.

### Rtings Targets
Rtings measured headphones have a frequency response target made for this project. This treble average target is using an
average of frequency responses of all Rtings measured headphones in the treble range with small manual reduction of the
9kHz peak and the Rtings native response below 2500 Hz without bass boost. Three different targets were compared in
listening tests and the treble average target was found to sound the best. Other two were the Rtings native target curve
and calibrated and uncalibrated versions of SBAF Serious target curve. Rtings uses the same measurement system as
Innerfidelity uses so in theory the uncalibrated SBAF Serious target should work similarly with Rtings but listening
tests found the treble average target to be slightly better. Rtings have
[a very informative video](https://www.youtube.com/watch?v=HNEI3qLZEKo) about how they are doing the measurements and
how they came up with the target they use.

All of these Rtings targets retired when new calibrated Harman targets were developed for Rtings measurements.

## Technical Challenges
Simply inverting headphone frequency response deviation from target response does not usually produce sufficient
results. Some problems are caused by imperfections in measurements, some are reliability issues and some are practical
end-user problems. Rtings has a good [video on Youtube](https://www.youtube.com/watch?v=HNEI3qLZEKo) about measurement
system challenges and solutions which is definitely worth checking out. Innerfidelity also has a very
educational [video on Youtube](https://www.youtube.com/watch?v=SDRHFNfFCFU) about measurements and what constitutes as a
neutral sound. Main takeoffs are that bass and treble measurements are very inconsistent, neutral sound is not very well
defined yet and on-ear headphones have big reliability problems in 8 to 9kHz range due to resonances which move when
headphone placement is changed. Harman international has done some solid research into preferred headphone frequency
response but since that research was done on a different measurement system the target does not apply directly to
Innerfidelity (Summer 2018) and Headphone.com measurements.

There is very little that can be done for fighting bass inconsistencies because the same problems will be there whether
equalization is used or not. Headphones simply have different bass responses on different listeners (heads). Therefore
bass is taken as is in AutoEQ and equalized as if there was nothing wrong with it. Your mileage may vary. Luckily bass
has smaller impact on music and having too much bass (especially sub-bass) doesn't create problems of the same magnitude
as having too much treble.

Moving resonances around 8 to 9kHz may cause big problems if not taken into account. Spikes and dips in this range are
of great amplitude and very narrow. If one equalizes these spikes and dips according to frequency response measurement
in worst case scenario a spike will move in a place of dip when headphone is moved, and therefore the spike is amplified
significantly, leading to a very sharp and piercing sound signature. To counter these problems by default AutoEQ uses heavy
smoothing and limited positive gain above 6 to 8kHz. This way the equalization will follow a broader trend of the region
and will not care so much about narrow spikes and dips. Also positive gain is limited to 0dB as an extra safety measure
against amplifying spikes due to moving the headphone. Suppressing a narrow dip even further is not an optimal thing to do but in practice has
little negative effect on the sound. Both of these measures will also alleviate upper treble measurement inconsistencies
above 11 to 12 kHz.

A practical end-user problem is if too high positive gain is allowed which asks for equal amount of negative digital
pre-amp to prevent clipping. This negative preamp will limit maximum volume produced by the system if there is no analog
gain available. If a dedicated headphone amplifier is available or if the motherboard/soundcard can drive the headphones
loud enough even when using high negative preamp larger `--max_gain` values can be used. By default `--max_gain` is set
to +6dB so as not to cripple the user's volume too much. Max gain will clip the equalization curve which produces sharp kinks
in it. Sharp changes in equalization may produce unwanted equalization artifacts. To counter this AutoEQ rounds the
corners whenever max gain clips the curve.


## Parametric Equalizer Optimization
AutoEQ has an optimizer to fit several peaking filters to the desired equalization curve. Optimization is part heuristic
initialization and part mathematical optimization.

In the initialization phase peaks are detected from the target curve and a peaking filter is created to match the peak's
height (gain) and location (frequency). This way, the optimizer finds a suitable number of filters to optimize. If the bass
region has no peaks and therefore is missing filters entirely, a maximum of two filters will be added at 20 Hz and 60 Hz.

A way to limit the number of filters used is provided with `max_filters` parameter. If there are too many filters after
initialization, some filters are removed. First filters with small gain (< 0.2 dB and < 0.33 dB) are removed. If there are too
many filters after reduction of small gain filters, nearby filters are attempted to merge. Merged filter will be in the
mid point of the merged filters. If merging filters did not reduce the count enough, smallest filters are removed until
count matches maximum allowed number of filters. Image below shows initialization for 1More MK801 headphone. Red dots
are the peaks of filters before reduction and green dots are the peaks after reduction.

![filter-initialization](https://i.imgur.com/UlMb2jK.png)

*Equalization target and initial peak filters for optimization before and after filter number limitation*

After suitable number of filters have been achieved and filter center frequencies and gains have been set to appropriate
values a mathematical optimization is performed to fit sum frequency response of all filters to match as close as
possible the desired curve. Optimization is based on gradient descent and will attempt to minimize mean
squared error between the sum frequency response of the filters and the target. When improvements in the error are
getting too small to make a practical difference the optimization is stopped. Animation below shows progress from the
initialization to a close finished curve.

![optimization-animation](https://i.imgur.com/pM7JYAb.gif)

*Optimization of parametric eq filters (click to play)*


## Contact
[Issues](https://github.com/jaakkopasanen/AutoEq/issues) are the way to go if you are experiencing problems, have
ideas or if there is something unclear about how things are done or documented.

You can find me in [Reddit](https://www.reddit.com/user/jaakkopasanen) and
[Head-fi](https://www.head-fi.org/members/jaakkopasanen.491235/) if you just want to say hello.
