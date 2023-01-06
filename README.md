# AutoEq
**TL;DR** If you are here just looking to make your headphones sound better, find your headphone model in
[results](./results) folder's recommended headphones list
and follow instructions in [Usage](#usage) section.

## About This Project
AutoEq is a project for equalizing headphone frequency responses automatically, and it achieves this by parsing
frequency response measurements and producing equalization settings which correct the headphone to a neutral sound.
This project currently has over 4000 headphones covered in the
[results](./results) folder.
See [Usage](#usage) for instructions how to use the results with
different equalizer softwares and
[Results](#results) section for details about parameters and how the results were
obtained.

AutoEq is not just a collection of automatically produced headphone equalization settings but also a tool for equalizing
headphones for yourself. AutoEq provides methods for reading data, equalizing it to a given target
response and saving the results for usage with equalizers. It's possible to use different compensation (target)
curves, apply tilt for making the headphones brighter/darker and adding a bass boost. It's even possible to make one
headphone sound (roughly) like another headphone. For more info about equalizing see [Equalizing](#equalizing).

Third major contribution of this project is the measurement data and compensation curves all in a numerical format
except for Crinacle's raw data. Everything is stored as CSV files so they are easy to process with any programming
language or even Excel.

![Sennheiser HD 800](./results/oratory1990/harman_over-ear_2018/Sennheiser%20HD%20800/Sennheiser%20HD%20800.png)

*Sennheiser HD 800 equalization results plotted*

### Updates
**2022-10-30** Restructured the project and published in PyPi. Source code moved under [autoeq](./autoeq) directory and 
command line usage changed from `python autoeq.py` to `python -m autoeq` with underscores `_` replaced with hyphens `-`
in the parameter names. 

**2022-09-18** Parametric eq optimizer reworked. The new optimizer supports shelf filters, has a powerful configuration
system, run 10x faster, has limits for Fc, Q and gain value ranges and treats +10 kHz range as average value instead of
trying to fix it precisely.

## Usage
AutoEq produces settings for basically all types of equalizer apps.

### Parametric Equalizers
Parametric equalizers have filters (bands) with user adjustable gain, center frequency and quality Q. Keep in mind that
parametric eq accuracy depends on the number of filters available. Usually 10 filters produce very good
results but as little as 5 can be good enough. Keep in mind that different parametric equalizers will produce different
outcomes with the same parameter values. Parameters produced by AutoEq are equal with EqualizerAPO using 44.1 kHz
sampling rate. When using other equalizers or sampling rates, it's always highly recommended to check that the frequency
response of the equalizer matches the parametric eq curve in the graphs.

All parametric equalizer except Peace require you to configure the filter parameters manually with the software user
interface. Some parametric equalizer use filter width (band width) instead of Q. Filter width can be calculated as:
`bw = Fc / Q` where `bw` is the band width in Herts, `Fc` is center frequency and `Q` is quality. Filter width in
octaves can be calculated as: `N = ln(1 + 1/(2*Q^2) + sqrt(((2*Q^2 + 1) / Q^2 )^2 / 4 - 1)) / ln(2)` where `ln` is the
natural logarithm. See http://www.sengpielaudio.com/calculator-bandwidth.htm for an online calculator.

It's very important to set preamp according to the value given in the result README.md document. Parametric eq filters
will produce positive gains and to avoid clipping a preamp with negative gain is required.

Parametric eq settings can be used with Peace or any other parametric eq which has at least 5 bands available. Even
fewer bands is possible but pre-computed results require you to use at least the five first of the filters.
Parametric equalizer filter parameters look like this:

| Type     | Fc      | Q    | Gain    |
| :------- | :------ | :--- | :------ |
| LowShelf | 105 Hz  | 0.70 | 6.3 dB  |
| Peaking  | 162 Hz  | 0.91 | -2.3 dB |
| Peaking  | 2237 Hz | 1.94 | -4.6 dB |
| Peaking  | 6093 Hz | 2.26 | -4.7 dB |
| Peaking  | 8251 Hz | 3.71 | -2.9 dB |

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

| Type    | Fc       | Q    | Gain    |
| :------ | :------- | :--- | :------ |
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

### Convolution Equalizers
Convolution equalizer is the most powerful type of equalizer software. These equalizers allow extremely precise control
over the frequency response and the results are the same on all devices and platforms when using the same FIR filter.

AutoEq supports convolution equalizers with FIR filters as WAV files and with EqualizerAPO's GraphicEQ filter type. The
default results contain FIR filters for both 44.1 kHz and 48 kHz sampling rates. Other sampling rates are supported but
not given in the default results. EqualizerAPO's GraphicEQ works with any sampling rate.

To use the FIR filters, download the appropriate WAV file and import it to the EQ software of your choice. Please keep
in mind that not all EQ softwares support convolution. Some equalizers can load multiple FIR filters at the same time.
Download both WAV files, create a Zip file containing both and load the Zip file to for example Roon.

Convolution equalizers might produce clipping with AutoEq generated files despite the fact that AutoEq normalizes the
impulse responses. You can add a few dB of negative preamp with `--preamp` parameter if you experience clipping.

See [EqualizerApo](#EqualizerAPO) for instructions on how to use the GraphicEQ.

### Windows
has [EqualizerAPO](#equalizerapo), [Peace](#peace) and many media players with parametric equalizers such as
[Neutron](https://www.microsoft.com/en-us/p/neutron-music-player/9nblggh4vp2h?activetab=pivot:overviewtab),
[Roon](https://roonlabs.com/) and [Foobar2000](https://www.foobar2000.org/).

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
[Wavelet](https://play.google.com/store/apps/details?id=com.pittvandewitt.wavelet) is an Android app which comes with
all the AutoEq eq profiles built in. The app works with all music apps so is closest to system-wide equalizer one can
have on Android without rooting. The equalizer built into this app is very powerful and can represent the AutoEq
profiles very accurately. There is also an option to tune the sound with graphic equalizer. Wavelet has the best
Bluetooth device compatibility of all the tested eq apps on Android.

The main functionalities of Wavelet are free (including AutoEq profiles and graphic eq) but some extra features can be
unlocked with an in-app purchase.

![Wavelet](https://i.imgur.com/UGiBwFX.png)

#### Neutron
[Neutron](https://play.google.com/store/apps/details?id=com.neutroncode.mp) is a music player with parametric equalizer 
and comes with all the AutoEq profiles built into a Frequency Response Correction DSP (FRC). It is also available on 
Apple iOS and Windows platforms and not free. On Android it has a [trial version](https://play.google.com/store/apps/details?id=com.neutroncode.mpeval)
where FRC with AutoEq is fully functional and can be freely evaluated. 

<p align="center">
  <img src="https://neutroncode.com/images/neutronmp/feature/feature_frc_autoeq_combined.png"/>
</p>

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

[RootlessJamesDSP](https://github.com/ThePBone/RootlessJamesDSP) works on non-rooted devices but does not work on some
apps like Spotify.

### Linux
#### PulseEffects / EasyEffects
[PulseEffects / EasyEffects](https://github.com/wwmm/easyeffects) is a Linux module with wide variety of signal
processing tools including convolution and parametric equalizers.

From version 4.7.2 onwards PulseEffects added support for convolution FIR filters. This is the recommended way to apply
AutoEq presets. Navigate to the plugins tab and add the convolver plugin, then click the waveform button above the stereo width controls (or just the 'Impulses' button as of 6.1.x), click "Import impulse" and select the AutoEq
generated WAV file. You may also need to manually click 'load' in the Impulses menu for the filter to be fully loaded. PulseEffects' convolver requires you to set the input gain to prevent clipping. The gain required
by parametric eq should be sufficient, maybe 0.5 dB of negative gain more. Depending on the version, you may need to
rename the `.wav` file as `.irs`.

To use parametric eq, from version 6.0.0 onwards, first select the `plugins` tab at
the bottom of the screen, add the equalizer plugin, and load APO settings by clicking "Load APO Preset" and
selecting the ParametricEQ.txt file. For EasyEffects <= 6.1.3, Pre-amp can be adjusted with the input slider.
Later versions support reading this from ParametricEQ.txt.

From version 5.0.0 onwards, PulseEffects was renamed to EasyEffects and uses PipeWire instead of PulseAudio as backend.
Load eq settings by clicking the top center cog & clicking *Import ACO Presets* button and select the ParametricEQ.txt
file.  Pre-amp can be adjusted with the input slider.

For versions prior to v4.8.0, adjust filter parameters by clicking the cog button on each filter
and set type to "Bell", mode to "APO" and adjust the gain with the slider. Number of filters can be changed by clicking
the screwdriver and wrench button.

![pulseeffects](https://user-images.githubusercontent.com/32952512/112381638-6cd3b280-8d08-11eb-844a-b83600c6c02a.png)

### OSX / MacOS
System wide parametric EQ solutions on OSX typically rely on separate plugin hosting software and the actual plugin
which does the actual equalization.

Pardon the lack of documentation for these. I have not tested any of the methods myself but they have been suggested by
helpful AutoEq users.

[SoundSource](https://rogueamoeba.com/soundsource/) is the easiest way to use AutoEq on Mac since it comes with all of the
profiles built in. The software is however not free.

Audio plugin hosts include:
- Apple's own [AU Lab](https://www.apple.com/apple-music/apple-digital-masters/) hosts AU plugins and can be used as a system-wide audio output via [BlackHole](https://github.com/ExistentialAudio/BlackHole) or [Soundflower](https://github.com/mattingalls/Soundflower).
- [MenuBus](https://www.menubus.audio/versions) has a free version but is no longer actively developed.
- [Hosting AU](http://ju-x.com/hostingau.html) with [BlackHole](https://github.com/ExistentialAudio/BlackHole) or
[Soundflower](https://github.com/mattingalls/Soundflower) can be used as a system wide AU plugin host.

EQ plugins include:
- [Voxengo PrimeEQ](https://www.voxengo.com/product/primeeq/) is a parametric EQ plugin but is not free.
- [Fabfilter Pro Q3](https://www.fabfilter.com/products/pro-q-3-equalizer-plug-in) is another parametric EQ plugin, more
expensive than Voxengo but might be easier to install and use. Note: Pro Q3 uses a different system and all Q values need to be multiplied by 1.41!
- [LAConvolver plugin](http://audio.lernvall.com/) is a free convolver EQ which works with impulse response WAV files.
- AUNBandEq comes built in with Mac OSX. Works at least with HostingAU + BlackHole

![hostingau+blackhole](https://user-images.githubusercontent.com/38220377/71527191-9706ac80-28da-11ea-8f70-88caf57c4821.png)

Tutorials:
- [Apple AU Lab + Soundflower + AUNBandEQ Tutorial](https://www.superbestaudiofriends.org/index.php?threads/systemwide-eq-on-mac.7435/) [AU Lab Permission Issue](https://discussions.apple.com/thread/8552731)

#### eqMac
[eqMac](https://eqmac.app) is a Free & [Open Source](https://github.com/bitgapp/eqmac) System Wide equalizer for macOS.
eqMac has a Free 10 Band EQ and an Unlimited Band EQ (paid) with built-in AutoEq Integration! (Expert EQ)
<p align="center">
  <img width="512" src="https://raw.githubusercontent.com/bitgapp/eqMac/master/assets/screenshots/autoeq-promo.png"/>
</p>

### iOS
iOS unfortunately doesn't allow system-wide equalizers, so the only options are either music players with built-in
equalizer or [hardware solutions](#Hardware).

#### Neutron
[Neutron](https://apps.apple.com/app/neutron-music-player/id766858884) is a music player with parametric equalizer and 
comes with all the AutoEq profiles built into a Frequency Response Correction DSP (FRC). It is also available
on Android and Windows platforms and not free.

#### EQE
[EQE](https://github.com/rweichler/EQE) is a system wide parametric equalizer on iOS but requires jailbreaking. Here
are instructions on how to set it up: https://www.reddit.com/r/headphones/comments/dqbt81/psa_if_you_have_a_jailbroken_iphone_you_can/

### Hardware
Some devices have built-in equalizers and since they do the processing in the device, they work with any source which
can connect to the device.

[Qudelix 5K](https://www.qudelix.com/products/qudelix-5k-dac-amp) is a portable DAC and amplifier
with wired and Bluetooth connectivity and 10 band parametric equalizer.

[MiniDSP IL-DSP](https://www.minidsp.com/products/plate-amplifiers/il-dsp-headphone-amp) is a smaller form factor mobile
headphone dac/amp with 10 band parametric equalizer. The equalizer in the device doesn't have adjustable preamp but
AutoEq can build that in with `--preamp` parameter.

## Equalizing
`autoeq.py` is the tool used to produce the equalization results from measurement data. There is no
fancy graphical user interface but instead it is used from command line.

### Installing
- Download and install Git: https://git-scm.com/downloads. When installing Git on Windows, use Windows SSL verification
instead of Open SSL or you might run into problems when installing project dependencies.
- Download and install 64-bit **[Python 3](https://www.python.org/getit/)**. Make sure to check *Add Python 3.X to PATH*.
- You may need to install [libsndfile](http://www.mega-nerd.com/libsndfile/) if you're having problems with `soundfile`
when installing and/or running AutoEq.
- On Linux you may need to install Python dev packages
```shell
sudo apt install python3-dev python3-pip python3-venv
```
- On Linux you may need to install [pip](https://pip.pypa.io/en/stable/installing/)
- On Windows you may need to install
[Microsoft Visual C++ Redistributable for Visual Studio 2015, 2017, and 2019](https://support.microsoft.com/en-us/help/2977003/the-latest-supported-visual-c-downloads)
- Open a terminal / command prompt. On Windows, search `cmd` in the start menu.
- Clone AutoEq
```shell
git clone https://github.com/jaakkopasanen/AutoEq.git
```
- Go to AutoEq location
```shell
cd AutoEq
```
- Create a python virtual environment
```shell
python -m venv venv
```
- Activate virtualenv
```shell
# On Windows
venv\Scripts\activate.bat
# On Linux and Mac
. venv/bin/activate
```
- Update pip
```shell
python -m pip install -U pip
```
- Install required packages
```shell
python -m pip install -U -e .
```
- Verify installation. If everything went well, you'll see the list of command line parameters AutoEq accepts.
```shell
python -m autoeq --help
```

When coming back at a later time you'll only need to activate virtual environment again
```shell
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
```shell
git pull
```

Dependencies may change from time to time, you can update to the latest with
```shell
python -m pip install -U -e .
```

### Command Line Usage
```
usage: __main__.py [-h] --input-dir INPUT_DIR --output-dir OUTPUT_DIR [--standardize-input] [--new-only] [--compensation COMPENSATION] [--equalize] [--parametric-eq]
                   [--fixed-band-eq] [--rockbox] [--ten-band-eq] [--parametric-eq-config PARAMETRIC_EQ_CONFIG] [--fixed-band-eq-config FIXED_BAND_EQ_CONFIG]
                   [--convolution-eq] [--fs FS] [--bit-depth BIT_DEPTH] [--phase PHASE] [--f-res F_RES] [--bass-boost BASS_BOOST] [--treble-boost TREBLE_BOOST]
                   [--tilt TILT] [--sound-signature SOUND_SIGNATURE] [--max-gain MAX_GAIN] [--window-size WINDOW_SIZE] [--treble-window-size TREBLE_WINDOW_SIZE]
                   [--treble-f-lower TREBLE_F_LOWER] [--treble-f-upper TREBLE_F_UPPER] [--treble-gain-k TREBLE_GAIN_K] [--thread-count THREAD_COUNT]

optional arguments:
  -h, --help            show this help message and exit
  --input-dir INPUT_DIR
                        Path to input data directory. Will look for CSV files in the data directory and recursively in sub-directories.
  --output-dir OUTPUT_DIR
                        Path to results directory. Will keep the same relative paths for files found in input-dir.
  --standardize-input   Overwrite input data in standardized sampling and bias?
  --new-only            Only process input files which don't have results in output directory.
  --compensation COMPENSATION
                        File path to CSV containing compensation (target) curve. Compensation is necessary when equalizing because all input data is raw microphone data.
                        See "compensation", "innerfidelity/resources" and "headphonecom/resources".
  --equalize            Will run equalization if this parameter exists, no value needed.
  --parametric-eq       Will produce parametric eq settings if this parameter exists, no value needed.
  --fixed-band-eq       Will produce fixed band eq settings if this parameter exists, no value needed.
  --rockbox             Will produce a Rockbox .cfg file with 10 band eq settings if this parameter exists,no value needed.
  --ten-band-eq         Shortcut parameter for activating standard ten band eq optimization.
  --parametric-eq-config PARAMETRIC_EQ_CONFIG
                        Name of parametric equalizer configuration or a path to a configuration file. Available named configurations are "10_PEAKING" for 10 peaking
                        filters, "8_PEAKING_WITH_SHELVES" for 8 peaking filters and a low shelf at 105 Hz for bass adjustment and a high shelf at 10 kHz for treble
                        adjustment, "4_PEAKING_WITH_LOW_SHELF" for 4 peaking filters and a low shelf at 105 Hz for bass adjustment, "4_PEAKING_WITH_HIGH_SHELF" for 4
                        peaking filters and a high shelf at 10 kHz for treble adjustments. You can give multiple named configurations by separating the names with commas
                        and filter sets will be built on top of each other. When the value is a file path, the file will be read and used as a configuration. The file
                        needs to be a YAML file with "filters" field as a list of filter configurations, each of which can define "fc", "min_fc", "max_fc", "q", "min_q",
                        "max_q", "gain", "min_gain", "max_gain" and "type" fields. When the fc, q or gain value is given, the parameter won't be optimized for the filter.
                        "type" needs to be either "LOW_SHELF", "PEAKING" or "HIGH_SHELF". Also "filter_defaults" field is supported on the top level and it can have the
                        same fields as the filters do. All fields missing from the filters will be read from "filter_defaults". Defaults to
                        "4_PEAKING_WITH_LOW_SHELF,4_PEAKING_WITH_HIGH_SHELF". Optimizer behavior can be adjusted by defining "optimizer" field which has fields "min_f"
                        and "max_f" for lower and upper bounds of the optimization range, "max_time" for maximum optimization duration in seconds, "target_loss" for RMSE
                        target level upon reaching which the optimization is ended, "min_change_rate" for minimum rate of improvement in db/s and "min_std" for minimum
                        standard deviation of the last few loss values. "min_change_rate" and "min_std" end the optimization when further time spent optimizing can't be
                        expected to improve the results dramatically. See peq.yaml for an example.
  --fixed-band-eq-config FIXED_BAND_EQ_CONFIG
                        Path to fixed band equalizer configuration. The file format is the same YAML as for parametric equalizer.
  --convolution-eq      Will produce impulse response for convolution equalizers if this parameter exists, no value needed.
  --fs FS               Sampling frequency in Hertz for impulse response and parametric eq filters. Single value or multiple values separated by commas eg 44100,48000.
                        When multiple values are given only the first one will be used for parametric eq. Defaults to 44100.
  --bit-depth BIT_DEPTH
                        Number of bits for every sample in impulse response. Defaults to 16.
  --phase PHASE         Impulse response phase characteristic. "minimum", "linear" or "both". Defaults to "minimum"
  --f-res F_RES         Frequency resolution for impulse responses. If this is 20 then impulse response frequency domain will be sampled every 20 Hz. Filter length for
                        impulse responses will be fs/f_res. Defaults to 10.0.
  --bass-boost BASS_BOOST
                        Bass boost shelf. Sub-bass frequencies will be boosted by this amount. Can be either a single value for a gain in dB or a comma separated list of
                        three values for parameters of a low shelf filter, where the first is gain in dB, second is center frequency (Fc) in Hz and the last is quality
                        (Q). When only a single value (gain) is given, default values for Fc and Q are used which are 105.0 Hz and 0.7, respectively. For example "--bass-
                        boost=6" or "--bass-boost=9.5,150,0.69".
  --treble-boost TREBLE_BOOST
                        Treble boost shelf. > 10 kHz frequencies will be boosted by this amount. Can be either a single value for a gain in dB or a comma separated list
                        of three values for parameters of a high shelf filter, where the first is gain in dB, second is center frequency (Fc) in Hz and the last is
                        quality (Q). When only a single value (gain) is given, default values for Fc and Q are used which are 10000.0 Hz and 0.7, respectively. For
                        example "--treble-boost=3" or "--treble-boost=-4,12000,0.69".
  --tilt TILT           Target tilt in dB/octave. Positive value (upwards slope) will result in brighter frequency response and negative value (downwards slope) will
                        result in darker frequency response. 1 dB/octave will produce nearly 10 dB difference in desired value between 20 Hz and 20 kHz. Tilt is applied
                        with bass boost and both will affect the bass gain.
  --sound-signature SOUND_SIGNATURE
                        File path to a sound signature CSV file. Sound signature is added to the compensation curve. Error data will be used as the sound signature target
                        if the CSV file contains an error column and otherwise the raw column will be used. This means there are two different options for using sound
                        signature: 1st is pointing it to a result CSV file of a previous run and the 2nd is to create a CSV file with just frequency and raw columns by
                        hand (or other means). The Sound signature graph will be interpolated so any number of point at any frequencies will do, making it easy to create
                        simple signatures with as little as two or three points.
  --max-gain MAX_GAIN   Maximum positive gain in equalization. Higher max gain allows to equalize deeper dips in frequency response but will limit output volume if no
                        analog gain is available because positive gain requires negative digital preamp equal to maximum positive gain. Defaults to 6.0.
  --window-size WINDOW_SIZE
                        Smoothing window size in octaves.
  --treble-window-size TREBLE_WINDOW_SIZE
                        Smoothing window size in octaves in the treble region.
  --treble-f-lower TREBLE_F_LOWER
                        Lower bound for transition region between normal and treble frequencies. Treble frequencies can have different max gain and gain K. Defaults to
                        6000.0.
  --treble-f-upper TREBLE_F_UPPER
                        Upper bound for transition region between normal and treble frequencies. Treble frequencies can have different max gain and gain K. Defaults to
                        8000.0.
  --treble-gain-k TREBLE_GAIN_K
                        Coefficient for treble gain, affects both positive and negative gain. Useful for disabling or reducing equalization power in treble region.
                        Defaults to 1.0.
  --thread-count THREAD_COUNT
                        Amount of threads to use for processing results. If set to "max" all the threads available will be used. Using more threads result in higher
                        memory usage. Defaults to 1.
```


### Examples

#### Reproducing Results
Reproducing pre-computed results for oratory1990 measured on-ear headphones:
```shell
python -m autoeq --input-dir="measurements/oratory1990/data/onear" --output-dir="my_results/oratory1990/harman_over-ear_2018" --compensation="compensation/harman_over-ear_2018_wo_bass.csv" --parametric-eq --parametric-eq-config=4_PEAKING_WITH_LOW_SHELF,4_PEAKING_WITH_HIGH_SHELF --ten-band-eq --bass-boost=4.0 --convolution-eq --fs=44100,48000
```

Reproducing pre-computed results for Rtings measured IEMs:
```shell
python -m autoeq --input-dir="measurements/rtings/data/inear" --output-dir="my_results/rtings/avg" --compensation="measurements/rtings/resources/rtings_compensation_avg.csv" --parametric-eq --parametric-eq-config=4_PEAKING_WITH_LOW_SHELF,4_PEAKING_WITH_HIGH_SHELF --ten-band-eq --bass-boost=6.0 --convolution-eq --fs=44100,48000
```

All parameters used for pre-computed results can be found in the `results/update.py` script.

#### Equalizing Individual Headphones
Equalizing Sennheiser HD 650 and saving results to `my_results/HD650`:
```shell
python -m autoeq --input-dir="measurements/innerfidelity/data/onear/Sennheiser HD 650" --output-dir="my_results/HD650" --compensation="measurements/innerfidelity/resources/innerfidelity_harman_over-ear_2018_wo_bass.csv" --bass-boost=4 --convolution-eq --parametric-eq --ten-band-eq --fs=44100,48000
```

#### Fixed Band Equalizers
Fixed band equalizer settings can be produced the same way as parametric eq. Create `fbeq.yaml` with contents
```yaml
filter_defaults:
  type: PEAKING
  q: 1.05
filters:
  - fc: 400
  - fc: 1000
  - fc: 2500
  - fc: 6300
  - fc: 16000
```
to optimize for Sony WH-1000XM3 app.
```shell
python -m autoeq --input-dir="measurements/oratory1990/data/onear/Sony WH-1000XM3" --output-dir="my_results/Sony WH-1000XM3 (app)" --compensation="compensation/harman_over-ear_2018_wo_bass.csv" --bass-boost=4.0 --fixed-band-eq --fixed-band-eq-config=fbeq.yaml
```

#### Using Sound Signatures
AutoEq provides a way to play around with different sound signatures easily. The use-cases include making headphones
deviate from the neutral target or making one headphone sound like another.

Equalizing Sennheiser HD 800 to sound like Sennheiser HD 650 using pre-computed results. Both have been measured by
oratory1990 so we'll use those measurements. Pre-computed results include 4dB of bass boost for over-ear headphones and
therefore we need to apply a bass boost of 4dB here as well.
```shell
python -m autoeq --input-dir="measurements/oratory1990/data/onear/Sennheiser HD 800" --output-dir="my_results/Sennheiser HD 800 (HD 650)" --compensation="compensation/harman_over-ear_2018_wo_bass.csv" --sound-signature="results/oratory1990/harman_over-ear_2018/Sennheiser HD 650/Sennheiser HD 650.csv" --parametric-eq --parametric-eq-config=8_PEAKING_WITH_SHELVES --ten-band-eq --bass-boost=4 --convolution-eq --fs=44100,48000
```

Equalizing Massdrop x Sennheiser HD 800 to sound like AKG K701. There is no K701 measurement made by oratory1990 so
we'll use Innerfidelity's measurement for the sound signature. The list of recommended results always points to best
measurement so you can check there which one to use (measurement system can be found in the URL).
```shell
python -m autoeq --input-dir="measurements/oratory1990/data/onear/Sennheiser HD 800" --output-dir="my_results/Sennheiser HD 800 (K701)" --compensation="compensation/harman_over-ear_2018_wo_bass.csv" --sound-signature="results/innerfidelity/innerfidelity_harman_over-ear_2018/AKG K701/AKG K701.csv" --parametric-eq --parametric-eq-config=8_PEAKING_WITH_SHELVES --ten-band-eq --bass-boost=4 --convolution-eq --fs=44100,48000
```

Equalizing HiFiMAN HE400S to sound like Massdrop x Meze 99 Noir. HE400S is measured only by Innerfidelity so we'll point
compensation file pointing to Innerfidelity's calibrated Harman target. Meze 99 Noir has massive natural bass boost and
to capture that we need to relax max gain to +12dB.
```shell
python -m autoeq --input-dir="measurements/innerfidelity/data/onear/HiFiMAN HE400S" --output-dir="my_results/HE400S (99 Noir)" --compensation="measurements/innerfidelity/resources/innerfidelity_harman_over-ear_2018_wo_bass.csv" --sound-signature="results/oratory1990/harman_over-ear_2018/Meze 99 Noir/Meze 99 Noir.csv" --parametric-eq --parametric-eq-config=8_PEAKING_WITH_SHELVES --ten-band-eq --bass-boost=4 --max_gain=8
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
Then use it by providing the path to `--sound-signature` parameter. We'll set bass boost to 0dB because the sound
signature already has a significant bass boost. Of course it's possible to add bass boost on top of the sound signature
file if you want even more bass.
```shell
python -m autoeq --input-dir="measurements/rtings/data/onear/Audeze Mobius" --output-dir="my_results/Audeze Mobius (V-signature)" --compensation="measurements/rtings/resources/rtings_compensation_avg.csv" --sound-signature="my_data/v.csv" --parametric-eq --parametric-eq-config=8_PEAKING_WITH_SHELVES --ten-band-eq --bass-boost=4.0
```

### Building
Build PyPi package
```shell
copy /y README.md README.md.bak && copy /y autoeq\README.md README.md && python -m build && copy /y README.md.bak README.md && del README.md.bak
```
publish
```shell
python -m twine upload dist/autoeq-<VERSION>*
```

## Results
The main principle used by AutoEq for producing the equalization function is to invert the error curve. Error is the
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

| Type    | Fc   | Q    | Gain |
| :------ | :--- | :--- | :--- |
| Peaking | 113  | 0.75 | 3.5  |
| Peaking | 3766 | 0.63 | -2.3 |

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
bass is taken as is in AutoEq and equalized as if there was nothing wrong with it. Your mileage may vary. Luckily bass
has smaller impact on music and having too much bass (especially sub-bass) doesn't create problems of the same magnitude
as having too much treble.

Moving resonances around 8 to 9kHz may cause big problems if not taken into account. Spikes and dips in this range are
of great amplitude and very narrow. If one equalizes these spikes and dips according to frequency response measurement
in worst case scenario a spike will move in a place of dip when headphone is moved, and therefore the spike is amplified
significantly, leading to a very sharp and piercing sound signature. To counter these problems by default AutoEq uses heavy
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
in it. Sharp changes in equalization may produce unwanted equalization artifacts. To counter this AutoEq rounds the
corners whenever max gain clips the curve.


## Parametric Equalizer Optimization
AutoEq has an optimizer to fit several filters to the desired equalization curve. Optimization is an iterative process
where the filter parameters which provide the best results are searched until optimization finishes or any of the early
stopping conditions are met.

The optimizer can be configured quite flexibly. The filter type (peaking, low shelf or high shelf) and minimum and
maximum values for center frequency (fc), quality (q) and gain can be set as well as disable optimization for any of
these in favor of fixed value. The optimizer itself can be configured to stop the process early when the changes being
made are too small, a target error level has been reached or maximum amount of time has been used.

[peq.yaml](./peq.yaml) has an example configuration. Feel free to adjust the file to your needs.

Here's an animation of what happens during the optimization.

![optimization-animation](https://i.imgur.com/3breF6l.gif)

*Optimization of parametric eq filters (click to play again)*

Technically speaking the optimization is an error minimization process. The error is the root mean squared difference
between the equalization target and the frequency response from the current set of filter parameters. The optimizer
adjusts the filter parameters multiple times on each iteration to figure out in which direction each should be adjusted
to decrease the error. In addition to the RMSE between target and current equalizer frequency response, the undesired
combination of filter parameters is penalized. Currently that means adding more error if the filter has positive
gain and too steep slope (as this can cause audible ringing). The additional error (regularization) ensures the
optimizer doesn't produce these kinds of filter parameter combinations.

The > 10 kHz frequency range is treated as a single average level because research indicates that the perceived sound
quality is not sensitive to accurately following a curve above 10 kHz but rather a total energy in the range.

## Contact
[Issues](https://github.com/jaakkopasanen/AutoEq/issues) are the way to go if you are experiencing problems or have
ideas or feature requests. Issues are not the correct channel for headphone requests because this project sources the
measurements from other databases and a headphone missing from AutoEq means it has not been measured by any of the
supported sources.

You can find me in [Reddit](https://www.reddit.com/user/jaakkopasanen),
[Audio Science Review](https://www.audiosciencereview.com/forum/index.php?members/jaakkopasanen.17838/) and
[Head-fi](https://www.head-fi.org/members/jaakkopasanen.491235/) if you just want to say hello.
