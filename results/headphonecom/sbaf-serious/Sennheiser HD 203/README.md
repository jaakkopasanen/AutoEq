# Sennheiser HD 203

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -7.4dB
GraphicEQ: 10 -84; 20 6.9; 22 5.8; 23 5.4; 25 4.6; 26 4.3; 28 3.7; 30 3.3; 32 3.0; 35 2.3; 37 1.7; 40 0.7; 42 0.1; 45 -0.5; 49 -0.9; 52 -1.1; 56 -1.6; 59 -2.0; 64 -2.4; 68 -2.5; 73 -2.4; 78 -1.9; 83 -1.6; 89 -2.3; 95 -2.9; 102 -3.2; 109 -3.2; 117 -3.1; 125 -3.0; 134 -2.7; 143 -2.3; 153 -1.7; 164 -0.7; 175 0.3; 188 2.4; 201 5.3; 215 6.0; 230 6.0; 246 5.9; 263 5.3; 282 4.7; 301 4.0; 323 2.8; 345 1.4; 369 0.7; 395 0.4; 423 0.3; 452 -0.0; 484 -0.4; 518 -0.4; 554 -0.1; 593 0.2; 635 0.3; 679 0.3; 726 0.4; 777 0.4; 832 0.2; 890 0.1; 952 0.2; 1019 -0.1; 1090 -0.5; 1167 -0.4; 1248 -0.6; 1336 -1.0; 1429 -1.1; 1529 -1.1; 1636 -1.0; 1751 -0.0; 1873 1.0; 2004 1.7; 2145 2.7; 2295 3.9; 2455 5.0; 2627 5.6; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 4.7; 4514 0.2; 4830 1.9; 5168 4.5; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-7.4dB` and instead set Global volume in the UI for both channels to **-74**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 203 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 20 Hz   |  1.12 | 6.7 dB  |
| Peaking | 174 Hz  |  0.51 | -8.0 dB |
| Peaking | 231 Hz  |  1.28 | 13.8 dB |
| Peaking | 3117 Hz |  1.82 | 6.8 dB  |
| Peaking | 5942 Hz |  4.14 | 5.8 dB  |
| Peaking | 1527 Hz |  3.31 | -2.0 dB |
| Peaking | 2368 Hz |  6.21 | 1.5 dB  |
| Peaking | 4094 Hz |  7.27 | 3.1 dB  |
| Peaking | 4505 Hz | 10.73 | -4.2 dB |
| Peaking | 8314 Hz |  4.76 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20203/Sennheiser%20HD%20203.png)