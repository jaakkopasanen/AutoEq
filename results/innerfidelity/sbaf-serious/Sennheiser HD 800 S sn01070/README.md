# Sennheiser HD 800 S sn01070

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.3dB
GraphicEQ: 10 -84; 20 5.2; 22 4.6; 23 4.4; 25 4.0; 26 3.8; 28 3.4; 30 3.1; 32 2.8; 35 2.5; 37 2.3; 40 2.0; 42 1.9; 45 1.7; 49 1.5; 52 1.4; 56 1.3; 59 1.2; 64 1.2; 68 1.1; 73 1.1; 78 0.5; 83 -0.2; 89 -0.7; 95 -0.9; 102 -1.3; 109 -1.5; 117 -1.8; 125 -2.2; 134 -2.3; 143 -2.5; 153 -2.6; 164 -2.6; 175 -2.7; 188 -2.9; 201 -3.0; 215 -3.0; 230 -2.9; 246 -2.9; 263 -2.9; 282 -2.7; 301 -2.7; 323 -2.6; 345 -2.5; 369 -2.4; 395 -2.3; 423 -2.1; 452 -1.9; 484 -1.9; 518 -1.8; 554 -1.5; 593 -1.2; 635 -1.1; 679 -1.1; 726 -0.9; 777 -0.6; 832 -0.4; 890 -0.4; 952 -0.1; 1019 0.1; 1090 0.5; 1167 0.6; 1248 0.9; 1336 1.4; 1429 1.5; 1529 1.7; 1636 1.5; 1751 1.4; 1873 1.4; 2004 1.6; 2145 1.6; 2295 1.3; 2455 2.0; 2627 2.5; 2811 2.2; 3008 2.0; 3219 2.4; 3444 2.9; 3685 1.6; 3943 0.5; 4219 -0.3; 4514 -0.2; 4830 -0.0; 5168 -0.5; 5530 -1.2; 5917 -0.6; 6331 -3.1; 6775 -4.3; 7249 -3.3; 7756 -2.2; 8299 -1.1; 8880 -0.1; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 -2.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.257130528899575dB` and instead set Global volume in the UI for both channels to **-52**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 800 S sn01070 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.1dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of -2.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 210 Hz  | 0.44 | -3.3 dB |
| Peaking | 1549 Hz | 1.38 | 1.7 dB  |
| Peaking | 3044 Hz | 2.24 | 2.4 dB  |
| Peaking | 6841 Hz | 3.91 | -4.5 dB |
| Peaking | 14 Hz   | 0.5  | 5.7 dB  |
| Peaking | 69 Hz   | 2.12 | 1.5 dB  |
| Peaking | 215 Hz  | 1.21 | 0.2 dB  |
| Peaking | 4257 Hz | 9.73 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20800%20S%20sn01070/Sennheiser%20HD%20800%20S%20sn01070.png)