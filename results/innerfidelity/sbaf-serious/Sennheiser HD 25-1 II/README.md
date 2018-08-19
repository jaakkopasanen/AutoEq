# Sennheiser HD 25-1 II

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 5.9; 59 5.6; 64 4.9; 68 4.4; 73 3.8; 78 3.4; 83 3.2; 89 3.2; 95 3.2; 102 2.2; 109 1.2; 117 0.6; 125 -0.1; 134 -1.1; 143 -1.6; 153 -1.7; 164 -1.6; 175 -2.0; 188 -2.1; 201 -2.0; 215 -1.8; 230 -1.7; 246 -1.5; 263 -1.3; 282 -1.0; 301 -1.1; 323 -1.1; 345 -0.9; 369 -0.7; 395 -0.4; 423 -0.2; 452 -0.2; 484 -0.2; 518 -0.1; 554 0.1; 593 0.2; 635 0.3; 679 0.2; 726 0.3; 777 0.4; 832 0.2; 890 0.1; 952 0.0; 1019 0.0; 1090 -0.1; 1167 -0.3; 1248 -0.5; 1336 -0.9; 1429 -1.4; 1529 -1.9; 1636 -2.5; 1751 -3.0; 1873 -2.9; 2004 -2.9; 2145 -2.8; 2295 -2.3; 2455 -1.2; 2627 0.3; 2811 1.7; 3008 2.6; 3219 2.4; 3444 2.4; 3685 2.3; 3943 2.7; 4219 2.6; 4514 2.5; 4830 4.1; 5168 5.2; 5530 4.9; 5917 5.8; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -1.4; 8880 -3.3; 9502 -1.6; 10167 -0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 25-1 II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.2dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.79 | 7.1 dB  |
| Peaking | 2055 Hz | 1.69 | -4.3 dB |
| Peaking | 3040 Hz | 2.08 | 3.3 dB  |
| Peaking | 5834 Hz | 1.99 | 6.0 dB  |
| Peaking | 8742 Hz | 4.42 | -4.6 dB |
| Peaking | 33 Hz   | 0.23 | 4.7 dB  |
| Peaking | 36 Hz   | 1.05 | -5.6 dB |
| Peaking | 167 Hz  | 0.87 | -4.5 dB |
| Peaking | 765 Hz  | 1.58 | 0.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%2025-1%20II/Sennheiser%20HD%2025-1%20II.png)