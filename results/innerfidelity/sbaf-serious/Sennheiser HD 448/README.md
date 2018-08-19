# Sennheiser HD 448

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 5.8; 56 5.2; 59 4.8; 64 4.5; 68 4.2; 73 3.7; 78 3.2; 83 2.4; 89 1.6; 95 1.7; 102 2.6; 109 3.0; 117 2.5; 125 1.3; 134 -0.1; 143 -1.1; 153 -1.5; 164 -1.5; 175 -1.9; 188 -2.1; 201 -1.9; 215 -1.6; 230 -1.4; 246 -1.0; 263 -0.7; 282 -0.1; 301 0.5; 323 0.9; 345 1.1; 369 1.0; 395 0.8; 423 0.8; 452 0.8; 484 0.5; 518 0.2; 554 0.2; 593 0.2; 635 -0.1; 679 -0.4; 726 -0.5; 777 -0.4; 832 -0.3; 890 -0.2; 952 -0.0; 1019 -0.1; 1090 -0.5; 1167 -0.7; 1248 -1.4; 1336 -2.1; 1429 -2.7; 1529 -3.4; 1636 -4.1; 1751 -4.2; 1873 -3.8; 2004 -3.0; 2145 -2.0; 2295 -0.2; 2455 2.0; 2627 1.4; 2811 1.8; 3008 2.2; 3219 2.3; 3444 2.8; 3685 3.6; 3943 5.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 3.9; 5530 3.3; 5917 5.7; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 448 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.92 | 5.6 dB  |
| Peaking | 53 Hz   | 1.36 | 4.2 dB  |
| Peaking | 1709 Hz | 2.67 | -5.0 dB |
| Peaking | 4306 Hz | 1.82 | 6.0 dB  |
| Peaking | 6248 Hz | 6.27 | 4.3 dB  |
| Peaking | 112 Hz  | 3.93 | 3.1 dB  |
| Peaking | 182 Hz  | 1.17 | -2.8 dB |
| Peaking | 347 Hz  | 1.87 | 1.8 dB  |
| Peaking | 2498 Hz | 9.9  | 2.0 dB  |
| Peaking | 8386 Hz | 3.4  | -0.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20448/Sennheiser%20HD%20448.png)