# Munitio Pro40

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 1.7; 22 0.8; 23 0.4; 25 -0.4; 26 -0.8; 28 -1.5; 30 -2.1; 32 -2.6; 35 -3.2; 37 -3.6; 40 -4.0; 42 -4.2; 45 -4.4; 49 -4.6; 52 -4.6; 56 -4.6; 59 -4.6; 64 -4.5; 68 -4.5; 73 -4.5; 78 -4.5; 83 -4.8; 89 -5.1; 95 -5.5; 102 -5.9; 109 -6.2; 117 -6.4; 125 -6.7; 134 -7.1; 143 -7.3; 153 -7.4; 164 -7.2; 175 -7.3; 188 -7.4; 201 -7.4; 215 -7.4; 230 -7.3; 246 -7.3; 263 -7.1; 282 -6.8; 301 -6.3; 323 -5.4; 345 -4.6; 369 -4.2; 395 -3.5; 423 -3.1; 452 -2.2; 484 -1.3; 518 0.1; 554 1.8; 593 3.7; 635 5.3; 679 5.9; 726 5.5; 777 4.5; 832 2.9; 890 1.5; 952 0.6; 1019 0.0; 1090 0.1; 1167 0.8; 1248 1.4; 1336 1.7; 1429 1.7; 1529 2.1; 1636 2.5; 1751 3.3; 1873 4.0; 2004 4.5; 2145 5.2; 2295 5.7; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 5.9; 3685 5.8; 3943 5.9; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 -0.8
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Munitio Pro40 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 1.4  | 3.7 dB  |
| Peaking | 41 Hz   | 1.17 | -3.1 dB |
| Peaking | 194 Hz  | 0.44 | -7.7 dB |
| Peaking | 662 Hz  | 2.54 | 8.5 dB  |
| Peaking | 3436 Hz | 0.72 | 6.9 dB  |
| Peaking | 11 Hz   | 0.73 | 1.3 dB  |
| Peaking | 1038 Hz | 6.32 | -1.4 dB |
| Peaking | 3609 Hz | 4.58 | -1.3 dB |
| Peaking | 6198 Hz | 2.06 | 5.4 dB  |
| Peaking | 7656 Hz | 1.59 | -4.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Munitio%20Pro40/Munitio%20Pro40.png)