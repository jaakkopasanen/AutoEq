# Sennheiser HD 250 II

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.9dB
GraphicEQ: 10 -84; 20 0.5; 22 -0.2; 23 -0.6; 25 -1.1; 26 -1.4; 28 -1.8; 30 -2.1; 32 -2.4; 35 -2.8; 37 -3.0; 40 -3.2; 42 -3.3; 45 -3.4; 49 -3.5; 52 -3.6; 56 -3.5; 59 -3.3; 64 -2.9; 68 -2.7; 73 -2.4; 78 -1.8; 83 -1.4; 89 -1.6; 95 -2.6; 102 -4.2; 109 -5.1; 117 -5.4; 125 -4.7; 134 -4.0; 143 -4.3; 153 -3.9; 164 -2.1; 175 -2.8; 188 -1.7; 201 -0.9; 215 -0.5; 230 -0.7; 246 -0.5; 263 -0.1; 282 0.1; 301 0.3; 323 0.7; 345 1.1; 369 1.2; 395 1.2; 423 1.3; 452 1.1; 484 1.1; 518 0.9; 554 1.0; 593 1.2; 635 1.0; 679 0.9; 726 0.7; 777 0.8; 832 0.6; 890 0.4; 952 0.2; 1019 0.1; 1090 -0.1; 1167 0.0; 1248 0.6; 1336 0.1; 1429 -0.5; 1529 -1.0; 1636 -1.0; 1751 -0.5; 1873 -0.3; 2004 -0.5; 2145 -0.7; 2295 -0.9; 2455 -0.3; 2627 0.3; 2811 0.7; 3008 1.7; 3219 1.9; 3444 2.2; 3685 2.4; 3943 2.1; 4219 0.7; 4514 -0.1; 4830 -0.2; 5168 0.6; 5530 1.8; 5917 3.8; 6331 2.1; 6775 -0.4; 7249 -0.6; 7756 -0.8; 8299 -2.1; 8880 -3.4; 9502 -2.6; 10167 -0.3; 10879 0.0; 11640 -0.3; 12455 -0.8; 13327 -0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.934327137855155dB` and instead set Global volume in the UI for both channels to **-39**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 250 II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.2dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 46 Hz    | 1.26 | -3.6 dB |
| Peaking | 124 Hz   | 2.12 | -5.0 dB |
| Peaking | 3514 Hz  | 4.08 | 2.7 dB  |
| Peaking | 5982 Hz  | 8.5  | 4.2 dB  |
| Peaking | 8940 Hz  | 4.6  | -3.7 dB |
| Peaking | 86 Hz    | 8.3  | 0.8 dB  |
| Peaking | 176 Hz   | 3.22 | -0.9 dB |
| Peaking | 458 Hz   | 0.91 | 1.4 dB  |
| Peaking | 1765 Hz  | 1.85 | -0.9 dB |
| Peaking | 10507 Hz | 9.04 | 0.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20250%20II/Sennheiser%20HD%20250%20II.png)