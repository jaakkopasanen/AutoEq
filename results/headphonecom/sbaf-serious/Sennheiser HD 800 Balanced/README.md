# Sennheiser HD 800 Balanced

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.3dB
GraphicEQ: 10 -84; 20 3.2; 22 2.8; 23 2.6; 25 2.3; 26 2.2; 28 1.9; 30 1.7; 32 1.5; 35 1.3; 37 1.2; 40 1.2; 42 1.2; 45 1.2; 49 1.4; 52 1.5; 56 1.2; 59 0.6; 64 -0.2; 68 -0.2; 73 -0.2; 78 -0.7; 83 -1.1; 89 -1.5; 95 -1.8; 102 -1.9; 109 -2.1; 117 -2.2; 125 -2.5; 134 -2.7; 143 -2.9; 153 -3.0; 164 -3.0; 175 -3.1; 188 -3.3; 201 -3.3; 215 -3.1; 230 -3.0; 246 -3.0; 263 -3.0; 282 -2.9; 301 -2.9; 323 -2.5; 345 -2.3; 369 -2.2; 395 -2.0; 423 -1.8; 452 -1.8; 484 -1.7; 518 -1.4; 554 -1.2; 593 -1.0; 635 -0.9; 679 -0.8; 726 -0.6; 777 -0.5; 832 -0.5; 890 -0.3; 952 0.1; 1019 0.0; 1090 0.5; 1167 1.1; 1248 1.1; 1336 1.4; 1429 1.2; 1529 0.9; 1636 1.0; 1751 1.4; 1873 1.5; 2004 1.6; 2145 1.4; 2295 0.8; 2455 1.4; 2627 2.3; 2811 1.0; 3008 0.1; 3219 1.2; 3444 2.3; 3685 2.0; 3943 0.7; 4219 -1.2; 4514 -2.6; 4830 -2.6; 5168 -2.9; 5530 -3.5; 5917 -3.1; 6331 -4.4; 6775 -5.7; 7249 -5.4; 7756 -5.3; 8299 -3.1; 8880 -0.3; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.3291242158054413dB` and instead set Global volume in the UI for both channels to **-33**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 800 Balanced ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -3.3dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 1.23 | 3.1 dB  |
| Peaking | 53 Hz   | 1.01 | 2.3 dB  |
| Peaking | 259 Hz  | 0.26 | -4.2 dB |
| Peaking | 2126 Hz | 0.14 | 2.8 dB  |
| Peaking | 6581 Hz | 1.36 | -7.6 dB |
| Peaking | 3629 Hz | 7.75 | 1.9 dB  |
| Peaking | 4490 Hz | 7.37 | -2.0 dB |
| Peaking | 7828 Hz | 7.26 | -2.0 dB |
| Peaking | 8909 Hz | 7.08 | 1.5 dB  |
| Peaking | 9482 Hz | 4.63 | 0.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20800%20Balanced/Sennheiser%20HD%20800%20Balanced.png)