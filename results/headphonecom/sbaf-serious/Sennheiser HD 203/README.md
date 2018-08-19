# Sennheiser HD 203

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -7.0dB
GraphicEQ: 10 -84; 20 6.9; 22 5.8; 23 5.4; 25 4.6; 26 4.3; 28 3.7; 30 3.3; 32 2.9; 35 2.3; 37 1.6; 40 0.5; 42 -0.1; 45 -0.7; 49 -1.1; 52 -1.4; 56 -1.9; 59 -2.4; 64 -3.0; 68 -3.1; 73 -3.1; 78 -2.6; 83 -2.4; 89 -3.1; 95 -3.6; 102 -3.7; 109 -3.6; 117 -3.3; 125 -3.0; 134 -2.6; 143 -2.1; 153 -1.4; 164 -0.5; 175 0.5; 188 2.6; 201 5.4; 215 6.0; 230 6.0; 246 5.9; 263 5.4; 282 4.7; 301 4.0; 323 2.9; 345 1.4; 369 0.7; 395 0.4; 423 0.3; 452 -0.1; 484 -0.3; 518 -0.2; 554 -0.1; 593 0.1; 635 0.2; 679 0.4; 726 0.5; 777 0.3; 832 0.2; 890 0.1; 952 0.2; 1019 -0.1; 1090 -0.5; 1167 -0.4; 1248 -0.6; 1336 -1.0; 1429 -1.1; 1529 -1.1; 1636 -1.0; 1751 0.0; 1873 1.0; 2004 1.7; 2145 2.7; 2295 3.9; 2455 4.9; 2627 5.6; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 4.8; 4514 0.3; 4830 2.0; 5168 4.4; 5530 5.9; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.97888363989245dB` and instead set Global volume in the UI for both channels to **-69**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 203 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 20 Hz   |  0.91 | 7.0 dB  |
| Peaking | 155 Hz  |  0.42 | -7.3 dB |
| Peaking | 232 Hz  |  1.27 | 12.9 dB |
| Peaking | 3119 Hz |  1.81 | 6.8 dB  |
| Peaking | 5945 Hz |  4.14 | 5.8 dB  |
| Peaking | 1531 Hz |  3.4  | -2.0 dB |
| Peaking | 2370 Hz |  6.02 | 1.4 dB  |
| Peaking | 4105 Hz |  7.34 | 3.0 dB  |
| Peaking | 4514 Hz | 10.75 | -4.0 dB |
| Peaking | 8313 Hz |  4.72 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20203/Sennheiser%20HD%20203.png)