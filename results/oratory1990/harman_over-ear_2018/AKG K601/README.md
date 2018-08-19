# AKG K601

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 5.8; 68 5.1; 73 4.2; 78 3.6; 83 3.2; 89 2.7; 95 2.3; 102 1.8; 109 1.5; 117 1.1; 125 0.7; 134 0.5; 143 0.3; 153 0.1; 164 -0.1; 175 -0.1; 188 -0.3; 201 -0.4; 215 -0.5; 230 -0.5; 246 -0.5; 263 -0.4; 282 -0.2; 301 -0.1; 323 0.1; 345 0.2; 369 0.3; 395 0.4; 423 0.5; 452 0.6; 484 0.7; 518 0.9; 554 1.1; 593 1.2; 635 1.4; 679 1.6; 726 1.6; 777 1.4; 832 0.9; 890 0.5; 952 0.2; 1019 -0.1; 1090 -0.5; 1167 -0.9; 1248 -1.2; 1336 -1.5; 1429 -2.0; 1529 -2.6; 1636 -3.3; 1751 -3.8; 1873 -4.3; 2004 -4.9; 2145 -5.6; 2295 -5.7; 2455 -5.8; 2627 -5.6; 2811 -4.8; 3008 -3.7; 3219 -2.0; 3444 -1.2; 3685 -1.2; 3943 -1.9; 4219 -1.1; 4514 0.2; 4830 0.8; 5168 1.6; 5530 1.1; 5917 -0.1; 6331 -0.3; 6775 0.3; 7249 -0.2; 7756 -1.8; 8299 -1.9; 8880 -0.2; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 -0.2; 13327 -1.0; 14260 -0.2; 15258 0.0; 16326 -0.4; 17469 -2.8; 18692 -5.5; 20000 -8.2
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K601 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 36 Hz    | 0.66 | 6.9 dB  |
| Peaking | 705 Hz   | 2.13 | 2.1 dB  |
| Peaking | 2280 Hz  | 1.42 | -6.1 dB |
| Peaking | 5129 Hz  | 4.8  | 2.5 dB  |
| Peaking | 19753 Hz | 1.78 | -8.0 dB |
| Peaking | 41 Hz    | 2.89 | -1.2 dB |
| Peaking | 62 Hz    | 2.77 | 1.7 dB  |
| Peaking | 176 Hz   | 1.28 | -1.1 dB |
| Peaking | 8072 Hz  | 6.43 | -3.1 dB |
| Peaking | 8394 Hz  | 1.87 | 0.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/AKG%20K601/AKG%20K601.png)