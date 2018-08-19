# Sennheiser HD 202

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 5.9; 25 5.6; 26 5.4; 28 4.9; 30 4.2; 32 3.6; 35 2.8; 37 2.4; 40 1.8; 42 1.5; 45 1.0; 49 0.4; 52 -0.1; 56 -0.6; 59 -0.9; 64 -1.3; 68 -1.6; 73 -1.9; 78 -1.9; 83 -1.7; 89 -1.4; 95 -1.4; 102 -1.8; 109 -2.0; 117 -2.0; 125 -2.0; 134 -2.1; 143 -2.0; 153 -1.8; 164 -1.3; 175 -1.0; 188 -0.8; 201 -0.3; 215 0.6; 230 2.1; 246 3.0; 263 3.1; 282 2.8; 301 2.8; 323 3.0; 345 3.5; 369 3.9; 395 4.0; 423 3.4; 452 3.1; 484 2.7; 518 2.3; 554 2.1; 593 1.9; 635 1.5; 679 1.2; 726 0.9; 777 0.9; 832 0.7; 890 0.5; 952 0.2; 1019 -0.1; 1090 -0.4; 1167 -0.5; 1248 -0.6; 1336 -0.9; 1429 -1.3; 1529 -1.6; 1636 -1.8; 1751 -1.4; 1873 -0.5; 2004 0.6; 2145 1.6; 2295 2.7; 2455 4.4; 2627 5.8; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 5.6; 4514 2.1; 4830 2.3; 5168 5.2; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 202 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 2.12 | 6.4 dB  |
| Peaking | 262 Hz  | 5.28 | 2.5 dB  |
| Peaking | 399 Hz  | 2.21 | 4.0 dB  |
| Peaking | 3249 Hz | 2.04 | 6.8 dB  |
| Peaking | 5877 Hz | 3.64 | 5.8 dB  |
| Peaking | 35 Hz   | 2.64 | 1.9 dB  |
| Peaking | 103 Hz  | 0.97 | -2.4 dB |
| Peaking | 1619 Hz | 2.81 | -2.8 dB |
| Peaking | 2561 Hz | 6.46 | 2.4 dB  |
| Peaking | 8276 Hz | 4.57 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20202/Sennheiser%20HD%20202.png)