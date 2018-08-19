# AKG K612

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 5.9; 30 5.8; 32 5.5; 35 5.2; 37 4.9; 40 4.6; 42 4.5; 45 4.3; 49 4.4; 52 4.6; 56 4.9; 59 4.9; 64 4.4; 68 3.8; 73 3.2; 78 2.9; 83 2.4; 89 1.9; 95 1.6; 102 1.2; 109 0.8; 117 0.5; 125 0.2; 134 -0.1; 143 -0.3; 153 -0.4; 164 -0.6; 175 -0.8; 188 -0.9; 201 -1.0; 215 -1.0; 230 -1.1; 246 -1.1; 263 -1.0; 282 -0.9; 301 -0.6; 323 -0.4; 345 -0.3; 369 -0.2; 395 -0.1; 423 -0.0; 452 0.1; 484 0.3; 518 0.4; 554 0.6; 593 0.7; 635 1.0; 679 1.2; 726 1.3; 777 0.8; 832 0.2; 890 0.1; 952 0.0; 1019 -0.0; 1090 0.0; 1167 0.2; 1248 0.1; 1336 -0.2; 1429 -0.9; 1529 -1.7; 1636 -2.5; 1751 -3.1; 1873 -3.4; 2004 -3.4; 2145 -3.4; 2295 -3.2; 2455 -3.8; 2627 -3.3; 2811 -3.1; 3008 -2.9; 3219 -1.6; 3444 -1.5; 3685 -1.3; 3943 -0.5; 4219 0.3; 4514 0.3; 4830 -0.7; 5168 -0.9; 5530 -1.9; 5917 -3.2; 6331 -2.9; 6775 -2.3; 7249 -3.0; 7756 -2.7; 8299 -0.6; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 -0.6; 12455 -2.5; 13327 -1.7; 14260 -0.1; 15258 0.0; 16326 -2.2; 17469 -5.9; 18692 -7.3; 20000 -5.3
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K612 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 0.98 | 6.2 dB  |
| Peaking | 60 Hz    | 2.04 | 3.6 dB  |
| Peaking | 2256 Hz  | 1.74 | -3.9 dB |
| Peaking | 6589 Hz  | 2.94 | -3.0 dB |
| Peaking | 18767 Hz | 1.7  | -8.0 dB |
| Peaking | 220 Hz   | 1.42 | -1.4 dB |
| Peaking | 683 Hz   | 1.99 | 1.4 dB  |
| Peaking | 4158 Hz  | 1.46 | -1.1 dB |
| Peaking | 4313 Hz  | 3.95 | 2.4 dB  |
| Peaking | 15236 Hz | 6.69 | 1.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/AKG%20K612/AKG%20K612.png)