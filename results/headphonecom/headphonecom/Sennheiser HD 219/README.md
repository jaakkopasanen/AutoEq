# Sennheiser HD 219

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -1.7; 22 -2.5; 23 -2.8; 25 -3.4; 26 -3.7; 28 -4.2; 30 -4.7; 32 -5.1; 35 -5.7; 37 -6.0; 40 -6.5; 42 -6.8; 45 -7.1; 49 -7.5; 52 -7.7; 56 -7.9; 59 -8.1; 64 -8.3; 68 -8.3; 73 -8.3; 78 -8.3; 83 -8.2; 89 -8.0; 95 -8.0; 102 -8.0; 109 -7.8; 117 -7.4; 125 -6.9; 134 -6.3; 143 -5.6; 153 -5.4; 164 -6.0; 175 -4.9; 188 -5.4; 201 -5.0; 215 -3.9; 230 -3.7; 246 -3.5; 263 -3.0; 282 -2.3; 301 -1.4; 323 -0.5; 345 0.0; 369 0.3; 395 0.6; 423 0.9; 452 0.9; 484 0.9; 518 0.9; 554 0.7; 593 0.6; 635 0.7; 679 1.5; 726 1.9; 777 1.4; 832 0.9; 890 0.5; 952 0.2; 1019 -0.0; 1090 -0.1; 1167 0.1; 1248 0.4; 1336 1.1; 1429 2.0; 1529 3.0; 1636 2.5; 1751 1.5; 1873 1.5; 2004 1.7; 2145 2.1; 2295 2.6; 2455 2.9; 2627 3.1; 2811 3.2; 3008 3.1; 3219 3.1; 3444 3.1; 3685 3.6; 3943 3.1; 4219 2.2; 4514 2.9; 4830 4.9; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 -0.6; 8299 -2.9; 8880 -3.4; 9502 -1.4; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 219 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 79 Hz   | 0.38 | -8.4 dB |
| Peaking | 442 Hz  | 1.07 | 2.6 dB  |
| Peaking | 2692 Hz | 0.88 | 2.6 dB  |
| Peaking | 5851 Hz | 2.12 | 6.1 dB  |
| Peaking | 8527 Hz | 3.77 | -5.3 dB |
| Peaking | 17 Hz   | 1.73 | 1.0 dB  |
| Peaking | 145 Hz  | 7.82 | 0.9 dB  |
| Peaking | 744 Hz  | 4.61 | 1.8 dB  |
| Peaking | 1075 Hz | 0.89 | -1.0 dB |
| Peaking | 1524 Hz | 6.41 | 2.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Sennheiser%20HD%20219/Sennheiser%20HD%20219.png)