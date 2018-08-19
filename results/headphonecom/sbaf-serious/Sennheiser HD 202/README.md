# Sennheiser HD 202

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 5.9; 28 5.6; 30 5.1; 32 4.5; 35 3.5; 37 3.0; 40 2.3; 42 1.8; 45 1.2; 49 0.7; 52 0.4; 56 0.2; 59 -0.2; 64 -0.9; 68 -1.0; 73 -1.0; 78 -1.4; 83 -1.7; 89 -1.7; 95 -1.8; 102 -1.8; 109 -1.7; 117 -1.6; 125 -1.5; 134 -1.4; 143 -1.2; 153 -0.9; 164 -0.3; 175 0.3; 188 1.5; 201 3.4; 215 4.9; 230 5.0; 246 4.6; 263 4.4; 282 4.3; 301 4.2; 323 4.1; 345 3.2; 369 2.9; 395 2.9; 423 2.9; 452 2.6; 484 2.2; 518 1.9; 554 1.6; 593 1.3; 635 1.1; 679 0.8; 726 0.6; 777 0.5; 832 0.3; 890 0.2; 952 0.1; 1019 -0.0; 1090 -0.2; 1167 -0.3; 1248 -0.2; 1336 -0.0; 1429 -0.6; 1529 -0.7; 1636 -0.5; 1751 0.3; 1873 1.1; 2004 2.2; 2145 3.4; 2295 4.7; 2455 5.8; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 3.3; 4514 -0.3; 4830 2.9; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 202 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 1.08 | 6.6 dB  |
| Peaking | 156 Hz  | 0.6  | -5.7 dB |
| Peaking | 241 Hz  | 0.96 | 9.2 dB  |
| Peaking | 3018 Hz | 1.82 | 6.8 dB  |
| Peaking | 5843 Hz | 3.68 | 5.9 dB  |
| Peaking | 2387 Hz | 2.55 | 6.2 dB  |
| Peaking | 2553 Hz | 1.02 | -5.5 dB |
| Peaking | 4200 Hz | 2.13 | 6.4 dB  |
| Peaking | 4526 Hz | 7.75 | -8.2 dB |
| Peaking | 8224 Hz | 3.52 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20202/Sennheiser%20HD%20202.png)