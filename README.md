# AutoEQ
AutoEQ is a project for equalizing headphone frequency responses automatically and it achieves this by parsing
frequency response measurements and producing a equalization settings which correct the headphone to a neutral sound.
This project currently has 700+ onear headphones covered in the
[results](https://github.com/jaakkopasanen/AutoEq/tree/master/results) folder. Results are organized by
type/compensation/source/headphone so a Sennheiser HD 650 measured by Innerfidelity and tuned to
[Innerfidelity 2017 compensation curve](https://www.innerfidelity.com/content/compensation-curve-innerfidelity-measurements-dialog-part-1)
would be found in
[onear/innerfidelity2017/innerfidelity/Sennheiser HD 650](https://github.com/jaakkopasanen/AutoEq/tree/master/results/onear/innerfidelity2017/innerfidelity/Sennheiser%20HD%20650).
See [Usage](https://github.com/jaakkopasanen/AutoEq#usage) for instructions how to use the results with
[EqualizerAPO](https://sourceforge.net/projects/equalizerapo/) and
[Results](https://github.com/jaakkopasanen/AutoEq#results) for details about parameters and how the results were
obtained.

AutoEQ is not just a collection of automatically produced headphone equalization settings but also a tool for equalizing
headphones for yourself. `frequency_response.py` provides methods for reading data, equalizing it to a given target
response and saving the results for usage with EqualizerAPO. It's possible to use different compensation (target)
curves, apply tilt for making the headphones brighter/darker and adding a bass boost. For more info about equalizing see
[Equalizing](https://github.com/jaakkopasanen/AutoEq#equalizing)

Third major contribution of this project is the measurement data, compensation curves and calibration curves all in a
numerical format. Everything is stored as CSV files so they are easy to process with any programming language or even
Microsoft Excel. See [Compensation](), [Calibration]() and [Data Processing]() for more technical description about how
things were obtained and processed.


### Usage
Equalization settings produced by AutoEQ are EqualizerAPO GraphicEQ configuration lines, one for each headphone
processed. They look like this:
````
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 5.9; 45 5.7; 49 5.4; 52 5.2; 56 4.9; 59 4.7; 64 4.3; 68 4.1; 73 3.8; 78 3.5; 83 3.2; 89 2.8; 95 2.4; 102 2.1; 109 1.7; 117 1.2; 125 0.8; 134 0.5; 143 0.3; 153 0.2; 164 0.1; 175 0.1; 188 0.1; 201 0.1; 215 0.2; 230 0.3; 246 0.4; 263 0.3; 282 0.3; 301 0.2; 323 0.1; 345 0.0; 369 0.0; 395 -0.2; 423 0.3; 452 0.5; 484 0.9; 518 1.2; 554 1.1; 593 1.1; 635 1.0; 679 1.0; 726 0.8; 777 0.6; 832 0.3; 890 0.1; 952 -0.1; 1019 -0.1; 1090 -0.1; 1167 0.7; 1248 0.5; 1336 0.1; 1429 -0.1; 1529 0.1; 1636 0.3; 1751 0.7; 1873 1.3; 2004 1.7; 2145 1.7; 2295 2.4; 2455 2.7; 2627 3.0; 2811 2.4; 3008 2.3; 3219 2.5; 3444 2.6; 3685 2.6; 3943 2.4; 4219 0.7; 4514 -0.1; 4830 2.1; 5168 5.4; 5530 6.0; 5917 4.2; 6331 1.9; 6775 2.1; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
````
HeSuVi is highly recommended to be used with AutoEQ results. HeSuVi provides a convenient graphical user interface for
adjusting the equalizer, toggling eq on and off, adjusting preamp and saving and restoring multiple different
configurations making it very easy to compare different eq settings. To load a eq into HeSuVi, close HeSuVi and replace
contents of HeSuVi's eq file `C:\Program Files\EqualizerAPO\config\config.txt` with the produced GraphicEQ line. Then
start HeSuVi and adjust global volume for both channels to highest eq value. You can save the configuration with profile
manager in bottom right corner.

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/img/HeSuVi.png)

It is also possible to use EqualizerAPO without any graphical user interface by copying the result into the end of the
EqualizerAPO configuration file `C:\Program Files\EqualizerAPO\config\config.txt`. EqualizerAPO will update live as
soon as the file is saved. Adding a hash `#` to the beginning of the line and saving the file will disable EQ making it
possible to compare sound when using and not using EQ. When using EqualizerAPO like this it's **imperative** to apply a
preamp which brings everything down as much as the highest positive gain is, this can be done by adding this line also.
This example assumes that equalization has maximum positive gain of 6dB. Exact amounts are displayed in the results.
````
Copy: L=-6.0dB*L R=-6.0dB*R
````

If you are already using Peace GUI for EqualizerAPO you'll have to disable the configurations made by it because Peace
doesn't work with GraphicEQ and you don't want to have two EQs on at the same time. Producing parametric eq settings
for Peace users could be a consideration for the future if enough people want it.

### Results
- Links to sources
- Usage with HeSuVi
- Parameters used

### Equalizing
- Installing
    - python3
    - pip3
    - Virtualenv
    - requirements.txt
- frequency_response.py
    - CLI args
    - Examples
    - Use cases
- https://apps.automeris.io/wpd/

### Compensation
- Curve to turn raw microphone data into error data
- Targets have no bass boost
- Innerfidelity 2016
- Innerfidelity 2017 (link to post)
- Innerfidelity SBAF-Serious (how was made)
- Headphone.com (how was made)
- Equalizing to other headphones

### Calibration
- raw - calibration
- Same headphone models selected from both
- Difference in error calculated. Errors obtained by respective compensation curves.
- Calibration data is to be subtracted from error data (compensated data)
- Calibrating raw microphone data makes no sense because systems are different

### Data Processing
- Not meant as a user friendly tool. Obtaining data needs to be done only once.
- Innerfidelity
    - Innerfidelity PDFs crawled. PDFs turned into images. Images turned into data. All inspected manually.
    - Read data is the red and blue curves which are compensated with old compensation curve
    - Compensation curve 2016 obtained from Innerfidelity image
    - Compensation curve 2017 obtained from Innerfidelity image (see article...)
    - Transformation curve made from compensation curves
    - Data turned into raw data by adding compensation curve 2016
    - Original data still saved
- Headphone.com
    - Raw data images crawled. Compensated data images crawled. Images turned into data. All inspected manually.
    - Raw and compensated data used to produce compensation curve.
    - Only raw data kept.
  
### Technical Challenges
- Smoothing
- Interpolating
- Max gain with smoothed corners
