# Sennheiser HD 228

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.9dB
GraphicEQ: 10 -84; 20 -2.2; 22 -2.7; 23 -2.9; 25 -3.3; 26 -3.5; 28 -3.8; 30 -4.1; 32 -4.3; 35 -4.7; 37 -4.9; 40 -5.2; 42 -5.3; 45 -5.6; 49 -5.8; 52 -6.0; 56 -6.2; 59 -6.4; 64 -6.8; 68 -7.0; 73 -7.3; 78 -7.5; 83 -7.6; 89 -7.3; 95 -6.9; 102 -6.9; 109 -6.8; 117 -7.8; 125 -8.7; 134 -9.2; 143 -9.3; 153 -9.3; 164 -8.7; 175 -8.3; 188 -7.6; 201 -6.4; 215 -4.9; 230 -4.3; 246 -5.5; 263 -5.9; 282 -4.9; 301 -4.6; 323 -4.1; 345 -3.5; 369 -3.1; 395 -2.6; 423 -1.9; 452 -1.1; 484 -0.6; 518 -0.1; 554 0.3; 593 0.7; 635 0.9; 679 1.1; 726 1.0; 777 0.8; 832 0.6; 890 0.4; 952 0.2; 1019 0.0; 1090 0.1; 1167 0.4; 1248 0.7; 1336 0.9; 1429 1.2; 1529 0.9; 1636 -0.2; 1751 0.3; 1873 0.7; 2004 0.9; 2145 1.4; 2295 1.8; 2455 2.4; 2627 2.9; 2811 2.8; 3008 3.4; 3219 3.9; 3444 4.2; 3685 5.6; 3943 4.3; 4219 -0.2; 4514 -2.5; 4830 -3.6; 5168 -1.2; 5530 1.3; 5917 2.3; 6331 1.4; 6775 1.7; 7249 0.1; 7756 -0.7; 8299 -1.7; 8880 -1.7; 9502 -0.1; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -1.2; 17469 -3.8; 18692 -5.5; 20000 -6.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.907684453584801dB` and instead set Global volume in the UI for both channels to **-59**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 228 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.9dB.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 62 Hz    |  0.54 | -6.3 dB |
| Peaking | 153 Hz   |  1.62 | -6.4 dB |
| Peaking | 290 Hz   |  2.57 | -3.1 dB |
| Peaking | 3790 Hz  |  1.48 | 6.3 dB  |
| Peaking | 4634 Hz  |  4.7  | -8.5 dB |
| Peaking | 304 Hz   |  6.81 | 0.8 dB  |
| Peaking | 376 Hz   |  2.25 | -1.0 dB |
| Peaking | 636 Hz   |  1.92 | 1.6 dB  |
| Peaking | 5840 Hz  | 10.2  | 1.9 dB  |
| Peaking | 19493 Hz |  1.35 | -6.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20228/Sennheiser%20HD%20228.png)