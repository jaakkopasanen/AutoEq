# Audeo PFE 121 Gray Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 5.6; 23 5.4; 25 5.1; 26 5.0; 28 4.7; 30 4.5; 32 4.3; 35 4.0; 37 3.8; 40 3.6; 42 3.4; 45 3.2; 49 2.9; 52 2.7; 56 2.4; 59 2.2; 64 1.9; 68 1.7; 73 1.4; 78 1.0; 83 0.7; 89 0.4; 95 0.1; 102 -0.2; 109 -0.2; 117 -0.4; 125 -0.7; 134 -0.9; 143 -1.1; 153 -1.1; 164 -1.2; 175 -1.3; 188 -1.3; 201 -1.4; 215 -1.3; 230 -1.3; 246 -1.2; 263 -1.2; 282 -1.0; 301 -0.9; 323 -0.8; 345 -0.6; 369 -0.5; 395 -0.4; 423 -0.0; 452 0.2; 484 0.3; 518 0.3; 554 0.7; 593 1.0; 635 1.2; 679 1.1; 726 1.1; 777 1.2; 832 1.0; 890 0.6; 952 0.3; 1019 -0.1; 1090 -0.4; 1167 -0.8; 1248 -1.2; 1336 -1.7; 1429 -2.3; 1529 -2.8; 1636 -3.1; 1751 -3.3; 1873 -3.2; 2004 -3.1; 2145 -2.8; 2295 -2.5; 2455 -1.6; 2627 -1.0; 2811 -0.1; 3008 1.6; 3219 3.0; 3444 4.2; 3685 4.3; 3943 3.6; 4219 1.9; 4514 0.7; 4830 0.8; 5168 2.0; 5530 2.9; 5917 4.0; 6331 4.7; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.1; 8880 -1.9; 9502 -3.3; 10167 -3.0; 10879 -0.7; 11640 0.0; 12455 0.0; 13327 -0.1; 14260 -3.0; 15258 -4.8; 16326 -1.5; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.071246826001084dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeo PFE 121 Gray Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.7dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 0.86 | 5.5 dB  |
| Peaking | 1889 Hz  | 1.88 | -3.6 dB |
| Peaking | 3565 Hz  | 3.1  | 5.8 dB  |
| Peaking | 6299 Hz  | 2.95 | 6.7 dB  |
| Peaking | 9410 Hz  | 0.39 | -2.3 dB |
| Peaking | 200 Hz   | 1.06 | -1.6 dB |
| Peaking | 694 Hz   | 2.04 | 1.7 dB  |
| Peaking | 9697 Hz  | 4.61 | -3.3 dB |
| Peaking | 14203 Hz | 1.03 | 4.4 dB  |
| Peaking | 15032 Hz | 3.07 | -7.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeo%20PFE%20121%20Gray%20Filter/Audeo%20PFE%20121%20Gray%20Filter.png)