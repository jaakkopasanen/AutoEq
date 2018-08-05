# Monoprice Monolith M1060C

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -1.9; 22 -0.5; 23 0.1; 25 0.9; 26 1.1; 28 1.2; 30 1.1; 32 1.0; 35 1.1; 37 1.2; 40 1.2; 42 1.1; 45 0.8; 49 0.4; 52 0.4; 56 0.0; 59 -0.4; 64 -0.8; 68 -0.5; 73 -0.3; 78 -0.3; 83 -0.5; 89 -0.8; 95 -1.1; 102 -1.3; 109 -1.6; 117 -2.0; 125 -2.5; 134 -2.9; 143 -3.1; 153 -3.3; 164 -3.3; 175 -3.2; 188 -2.8; 201 -2.3; 215 -1.8; 230 -1.3; 246 -0.5; 263 0.5; 282 1.4; 301 1.8; 323 1.8; 345 1.2; 369 0.7; 395 1.1; 423 1.7; 452 2.3; 484 2.3; 518 2.0; 554 2.3; 593 2.6; 635 2.7; 679 3.2; 726 3.4; 777 3.0; 832 1.9; 890 1.0; 952 0.5; 1019 -0.3; 1090 -1.5; 1167 -2.1; 1248 -2.5; 1336 -3.5; 1429 -4.2; 1529 -4.8; 1636 -5.3; 1751 -4.8; 1873 -3.5; 2004 -2.2; 2145 -1.1; 2295 0.2; 2455 1.7; 2627 3.1; 2811 4.5; 3008 5.7; 3219 6.0; 3444 6.0; 3685 6.0; 3943 5.1; 4219 3.0; 4514 2.2; 4830 2.7; 5168 4.3; 5530 5.8; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monoprice Monolith M1060C ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 160 Hz  | 1.52 | -4.0 dB |
| Peaking | 746 Hz  | 0.62 | 4.4 dB  |
| Peaking | 1559 Hz | 1.11 | -8.2 dB |
| Peaking | 3164 Hz | 1.71 | 7.7 dB  |
| Peaking | 5945 Hz | 3.98 | 5.8 dB  |
| Peaking | 35 Hz   | 2.08 | 1.4 dB  |
| Peaking | 297 Hz  | 3.99 | 2.5 dB  |
| Peaking | 323 Hz  | 1.26 | -1.2 dB |
| Peaking | 742 Hz  | 7.49 | 1.1 dB  |
| Peaking | 8300 Hz | 4.48 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/custom/Monoprice%20Monolith%20M1060C/Monoprice%20Monolith%20M1060C.png)
# Run 2018-08-05T15:39:52.924046
There results were obtained with parameters:
* `--input_dir="data\Monoprice Monolith M1060C"`
* `--output_dir="results\custom\Monoprice Monolith M1060C"`
* `--compensation="calibration\zero.csv"`
* `--bass_boost=4.0`
* `--tilt=0.0`
* `--max_gain=6.0`
* `--treble_f_lower=6000.0`
* `--treble_f_upper=8000.0`
* `--treble_max_gain=0.0`
* `--treble_gain_k=1.0`