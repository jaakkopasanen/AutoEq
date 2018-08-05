# Sennheiser HD 560 Ovation II

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 5.9; 68 5.4; 73 4.8; 78 4.3; 83 3.8; 89 3.2; 95 2.7; 102 2.1; 109 1.6; 117 1.1; 125 0.5; 134 0.1; 143 -0.3; 153 -0.6; 164 -0.7; 175 -0.8; 188 -0.8; 201 -0.9; 215 -0.9; 230 -0.8; 246 -0.7; 263 -0.7; 282 -0.6; 301 -0.5; 323 -0.6; 345 -0.5; 369 -0.4; 395 -0.3; 423 -0.2; 452 -0.1; 484 -0.2; 518 -0.2; 554 -0.0; 593 0.3; 635 0.3; 679 0.1; 726 0.1; 777 0.3; 832 0.2; 890 -0.1; 952 -0.0; 1019 -0.2; 1090 -0.2; 1167 -0.2; 1248 -0.6; 1336 -1.1; 1429 -1.7; 1529 -2.1; 1636 -2.5; 1751 -2.7; 1873 -2.8; 2004 -3.0; 2145 -3.5; 2295 -3.9; 2455 -4.0; 2627 -4.4; 2811 -4.4; 3008 -3.9; 3219 -3.4; 3444 -2.4; 3685 -2.0; 3943 -2.0; 4219 -2.5; 4514 -3.0; 4830 -2.4; 5168 -1.4; 5530 2.4; 5917 5.8; 6331 5.4; 6775 2.3; 7249 -0.8; 7756 -3.5; 8299 -4.7; 8880 -3.9; 9502 -1.5; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 -0.3; 14260 -0.9; 15258 -0.1; 16326 0.0; 17469 0.0; 18692 -1.1; 20000 -6.9
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 560 Ovation II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 38 Hz    | 0.69 | 7.0 dB  |
| Peaking | 2523 Hz  | 1.24 | -4.3 dB |
| Peaking | 4952 Hz  | 3.24 | -4.0 dB |
| Peaking | 6003 Hz  | 3.54 | 8.9 dB  |
| Peaking | 8180 Hz  | 3.88 | -5.8 dB |
| Peaking | 36 Hz    | 1.31 | -4.7 dB |
| Peaking | 76 Hz    | 0.19 | 4.6 dB  |
| Peaking | 171 Hz   | 0.57 | -5.5 dB |
| Peaking | 10339 Hz | 6.9  | 0.9 dB  |
| Peaking | 19942 Hz | 3.87 | -6.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20560%20Ovation%20II/Sennheiser%20HD%20560%20Ovation%20II.png)