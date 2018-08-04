# Sennheiser HD 700

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.2dB
GraphicEQ: 10 -84; 20 5.6; 22 5.0; 23 4.7; 25 4.1; 26 3.9; 28 3.4; 30 3.0; 32 2.6; 35 2.1; 37 1.8; 40 1.5; 42 1.3; 45 1.0; 49 0.7; 52 0.4; 56 0.2; 59 0.0; 64 -0.2; 68 -0.3; 73 -0.5; 78 -0.6; 83 -0.8; 89 -1.2; 95 -1.6; 102 -2.3; 109 -2.7; 117 -3.0; 125 -3.5; 134 -3.9; 143 -4.2; 153 -4.4; 164 -4.5; 175 -4.4; 188 -4.6; 201 -4.6; 215 -4.4; 230 -4.4; 246 -4.4; 263 -4.3; 282 -4.1; 301 -4.0; 323 -3.8; 345 -3.6; 369 -3.5; 395 -3.3; 423 -3.0; 452 -2.8; 484 -2.7; 518 -2.5; 554 -2.2; 593 -1.9; 635 -1.7; 679 -1.7; 726 -1.4; 777 -1.0; 832 -0.9; 890 -0.6; 952 -0.3; 1019 0.1; 1090 0.5; 1167 0.7; 1248 1.4; 1336 1.7; 1429 2.3; 1529 2.9; 1636 3.0; 1751 3.5; 1873 4.2; 2004 4.5; 2145 4.2; 2295 3.8; 2455 3.4; 2627 3.1; 2811 2.6; 3008 2.5; 3219 2.6; 3444 3.2; 3685 3.7; 3943 2.3; 4219 -0.6; 4514 -2.1; 4830 -4.1; 5168 -5.1; 5530 -5.4; 5917 -7.2; 6331 -9.6; 6775 -6.7; 7249 -3.2; 7756 -1.2; 8299 -1.3; 8880 -2.3; 9502 -2.5; 10167 -2.0; 10879 -0.8; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.4; 17469 -2.6; 18692 -5.5; 20000 -9.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.2dB` and instead set Global volume in the UI for both channels to **-62**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 11 Hz    | 0.41 | 7.0 dB  |
| Peaking | 222 Hz   | 0.48 | -4.7 dB |
| Peaking | 2023 Hz  | 1.25 | 4.8 dB  |
| Peaking | 3685 Hz  | 5.35 | 4.0 dB  |
| Peaking | 6070 Hz  | 2.28 | -8.8 dB |
| Peaking | 146 Hz   | 5.14 | -0.6 dB |
| Peaking | 8664 Hz  | 1.48 | -3.2 dB |
| Peaking | 7844 Hz  | 4.51 | 4.4 dB  |
| Peaking | 19943 Hz | 1.12 | -9.6 dB |
| Peaking | 14664 Hz | 0.59 | 2.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20700/Sennheiser%20HD%20700.png)