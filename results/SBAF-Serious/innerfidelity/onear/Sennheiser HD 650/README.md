# Sennheiser HD 650

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 5.9; 28 5.6; 30 5.3; 32 4.8; 35 4.3; 37 3.9; 40 3.5; 42 3.3; 45 3.0; 49 2.7; 52 2.6; 56 2.5; 59 2.1; 64 1.8; 68 1.9; 73 2.2; 78 1.7; 83 0.9; 89 0.3; 95 -0.2; 102 -0.7; 109 -1.1; 117 -1.5; 125 -1.9; 134 -2.2; 143 -2.5; 153 -2.6; 164 -2.5; 175 -2.5; 188 -2.6; 201 -2.7; 215 -2.5; 230 -2.4; 246 -2.3; 263 -2.2; 282 -2.0; 301 -1.9; 323 -1.8; 345 -1.5; 369 -1.5; 395 -1.4; 423 -1.2; 452 -1.0; 484 -1.0; 518 -1.0; 554 -0.8; 593 -0.5; 635 -0.4; 679 -0.5; 726 -0.3; 777 -0.2; 832 -0.4; 890 -0.6; 952 -0.4; 1019 -0.1; 1090 -0.5; 1167 -0.8; 1248 -1.0; 1336 -1.1; 1429 -1.3; 1529 -1.3; 1636 -1.6; 1751 -1.6; 1873 -1.4; 2004 -0.9; 2145 -0.7; 2295 -0.5; 2455 -0.2; 2627 0.1; 2811 -0.1; 3008 -0.6; 3219 -1.1; 3444 -1.0; 3685 -0.6; 3943 0.0; 4219 -0.0; 4514 -0.1; 4830 0.9; 5168 3.8; 5530 5.9; 5917 5.2; 6331 4.4; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 650 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters:

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 1.38 | 4.2 dB  |
| Peaking | 47 Hz   | 0.43 | 3.1 dB  |
| Peaking | 165 Hz  | 0.65 | -3.7 dB |
| Peaking | 1643 Hz | 2.32 | -1.6 dB |
| Peaking | 3401 Hz | 3    | -1.3 dB |
| Peaking | 5852 Hz | 3.28 | 6.2 dB  |
| Peaking | 8882 Hz | 2.77 | -0.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/SBAF-Serious/innerfidelity/onear/Sennheiser%20HD%20650/Sennheiser%20HD%20650.png)
# Run 2018-07-31T22:05:03.797121
There results were obtained with parameters:
* `--input_dir="innerfidelity\data\onear\Sennheiser HD 650"`
* `--output_dir="results\SBAF-Serious\innerfidelity\onear\Sennheiser HD 650"`
* `--compensation="innerfidelity\resources\innerfidelity_compensation_SBAF-Serious-brighter.csv"`
* `--bass_boost=4.0`
* `--tilt=0.0`
* `--max_gain=6.0`
* `--treble_f_lower=6000.0`
* `--treble_f_upper=8000.0`
* `--treble_max_gain=0.0`
* `--treble_gain_k=1.0`