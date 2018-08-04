# Sennheiser HD 800 Balanced

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.8dB
GraphicEQ: 10 -84; 20 -1.3; 22 -1.7; 23 -1.9; 25 -2.2; 26 -2.3; 28 -2.6; 30 -2.8; 32 -3.0; 35 -3.2; 37 -3.3; 40 -3.3; 42 -3.3; 45 -3.2; 49 -2.9; 52 -2.8; 56 -3.0; 59 -3.5; 64 -4.1; 68 -4.0; 73 -3.9; 78 -4.3; 83 -4.5; 89 -4.7; 95 -4.9; 102 -4.8; 109 -4.8; 117 -4.8; 125 -5.0; 134 -5.0; 143 -5.0; 153 -5.0; 164 -4.8; 175 -4.9; 188 -4.9; 201 -4.9; 215 -4.7; 230 -4.6; 246 -4.5; 263 -4.4; 282 -4.4; 301 -4.3; 323 -4.0; 345 -3.8; 369 -3.6; 395 -3.3; 423 -3.0; 452 -2.8; 484 -2.5; 518 -2.0; 554 -1.7; 593 -1.4; 635 -1.1; 679 -0.9; 726 -0.7; 777 -0.5; 832 -0.5; 890 -0.4; 952 0.1; 1019 0.0; 1090 0.6; 1167 1.3; 1248 1.8; 1336 2.7; 1429 3.3; 1529 3.6; 1636 4.0; 1751 4.4; 1873 4.4; 2004 4.5; 2145 4.4; 2295 3.8; 2455 4.4; 2627 5.2; 2811 3.9; 3008 2.7; 3219 3.5; 3444 4.3; 3685 4.0; 3943 3.3; 4219 2.4; 4514 2.1; 4830 2.8; 5168 2.6; 5530 1.2; 5917 0.4; 6331 -2.1; 6775 -4.2; 7249 -4.3; 7756 -4.3; 8299 -1.9; 8880 -0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.8dB` and instead set Global volume in the UI for both channels to **-58**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 800 Balanced ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 46 Hz   |  0.31 | -2.1 dB |
| Peaking | 201 Hz  |  0.39 | -4.2 dB |
| Peaking | 1800 Hz |  1.29 | 3.4 dB  |
| Peaking | 3920 Hz |  0.61 | 3.3 dB  |
| Peaking | 7148 Hz |  2.93 | -7.0 dB |
| Peaking | 998 Hz  |  2.68 | -1.3 dB |
| Peaking | 977 Hz  |  1.3  | 0.8 dB  |
| Peaking | 4334 Hz | 13.48 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Sennheiser%20HD%20800%20Balanced/Sennheiser%20HD%20800%20Balanced.png)