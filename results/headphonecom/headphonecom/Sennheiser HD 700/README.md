# Sennheiser HD 700

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 0.5; 22 -0.1; 23 -0.4; 25 -1.0; 26 -1.2; 28 -1.7; 30 -2.0; 32 -2.4; 35 -2.8; 37 -3.1; 40 -3.4; 42 -3.6; 45 -3.8; 49 -4.1; 52 -4.3; 56 -4.5; 59 -4.7; 64 -4.8; 68 -4.9; 73 -5.1; 78 -5.1; 83 -5.1; 89 -5.3; 95 -5.3; 102 -5.3; 109 -5.3; 117 -5.3; 125 -5.5; 134 -5.3; 143 -5.4; 153 -5.5; 164 -5.4; 175 -5.2; 188 -5.3; 201 -5.2; 215 -5.1; 230 -5.0; 246 -5.0; 263 -4.9; 282 -4.8; 301 -4.5; 323 -4.4; 345 -4.0; 369 -3.9; 395 -3.6; 423 -3.2; 452 -3.0; 484 -2.5; 518 -2.2; 554 -1.9; 593 -1.6; 635 -1.1; 679 -0.9; 726 -0.7; 777 -0.5; 832 -0.6; 890 -0.4; 952 0.0; 1019 0.0; 1090 0.4; 1167 1.1; 1248 1.6; 1336 2.5; 1429 3.6; 1529 4.3; 1636 5.2; 1751 5.6; 1873 6.0; 2004 6.0; 2145 6.0; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 5.7; 4219 3.2; 4514 1.9; 4830 2.7; 5168 3.1; 5530 4.3; 5917 3.5; 6331 -2.6; 6775 -3.9; 7249 -1.0; 7756 0.1; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 61 Hz   |  0.71 | -3.2 dB |
| Peaking | 207 Hz  |  0.45 | -4.8 dB |
| Peaking | 1783 Hz |  1.88 | 3.8 dB  |
| Peaking | 3147 Hz |  0.95 | 5.7 dB  |
| Peaking | 6626 Hz |  9.79 | -6.9 dB |
| Peaking | 3919 Hz |  6.24 | 1.8 dB  |
| Peaking | 6385 Hz | 14.07 | -1.9 dB |
| Peaking | 4399 Hz |  5.89 | -2.5 dB |
| Peaking | 5801 Hz |  4.92 | 3.9 dB  |
| Peaking | 7330 Hz |  0.97 | -0.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Sennheiser%20HD%20700/Sennheiser%20HD%20700.png)