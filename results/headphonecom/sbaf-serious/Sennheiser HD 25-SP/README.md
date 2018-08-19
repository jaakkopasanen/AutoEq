# Sennheiser HD 25-SP

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 2.8; 22 2.1; 23 1.7; 25 1.1; 26 0.8; 28 0.2; 30 -0.2; 32 -0.6; 35 -0.8; 37 -0.9; 40 -1.3; 42 -1.8; 45 -2.6; 49 -3.3; 52 -3.6; 56 -3.8; 59 -4.0; 64 -4.1; 68 -4.4; 73 -4.6; 78 -4.3; 83 -4.0; 89 -4.1; 95 -5.4; 102 -6.7; 109 -7.1; 117 -7.0; 125 -6.9; 134 -6.4; 143 -5.9; 153 -5.2; 164 -5.0; 175 -5.9; 188 -6.5; 201 -6.6; 215 -6.3; 230 -5.8; 246 -5.0; 263 -4.3; 282 -3.7; 301 -2.9; 323 -1.6; 345 -0.6; 369 0.1; 395 0.8; 423 1.1; 452 1.2; 484 1.3; 518 1.4; 554 1.3; 593 1.4; 635 1.3; 679 1.2; 726 1.1; 777 0.9; 832 0.7; 890 0.5; 952 0.2; 1019 -0.1; 1090 -0.4; 1167 -0.8; 1248 -1.3; 1336 -2.0; 1429 -2.7; 1529 -3.4; 1636 -4.1; 1751 -4.6; 1873 -4.8; 2004 -4.7; 2145 -4.3; 2295 -3.8; 2455 -3.5; 2627 -3.0; 2811 -1.8; 3008 -0.1; 3219 0.6; 3444 1.2; 3685 1.5; 3943 0.4; 4219 0.7; 4514 0.9; 4830 0.7; 5168 2.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -4.0; 8880 -8.9; 9502 -8.5; 10167 -4.9; 10879 -1.3; 11640 -0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.090907327114606dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 25-SP ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.3dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 108 Hz  | 0.96 | -6.4 dB  |
| Peaking | 213 Hz  | 2.7  | -4.7 dB  |
| Peaking | 1944 Hz | 2.11 | -5.4 dB  |
| Peaking | 6112 Hz | 2.6  | 7.1 dB   |
| Peaking | 9148 Hz | 4.41 | -11.1 dB |
| Peaking | 15 Hz   | 0.86 | 4.1 dB   |
| Peaking | 59 Hz   | 0.63 | -2.1 dB  |
| Peaking | 86 Hz   | 3.68 | 3.0 dB   |
| Peaking | 542 Hz  | 1.51 | 2.3 dB   |
| Peaking | 3461 Hz | 7.54 | 1.7 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%2025-SP/Sennheiser%20HD%2025-SP.png)