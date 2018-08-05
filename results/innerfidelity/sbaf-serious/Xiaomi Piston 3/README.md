# Xiaomi Piston 3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.2dB
GraphicEQ: 10 -84; 20 -2.6; 22 -3.1; 23 -3.3; 25 -3.7; 26 -3.9; 28 -4.3; 30 -4.6; 32 -4.8; 35 -5.2; 37 -5.3; 40 -5.5; 42 -5.7; 45 -5.8; 49 -5.9; 52 -6.0; 56 -6.2; 59 -6.2; 64 -6.3; 68 -6.4; 73 -6.4; 78 -6.6; 83 -6.8; 89 -7.1; 95 -7.5; 102 -7.9; 109 -8.2; 117 -8.6; 125 -9.0; 134 -9.2; 143 -9.4; 153 -9.4; 164 -9.3; 175 -9.0; 188 -8.7; 201 -8.5; 215 -8.1; 230 -7.7; 246 -7.4; 263 -7.0; 282 -6.5; 301 -6.0; 323 -5.6; 345 -5.1; 369 -4.7; 395 -4.2; 423 -3.5; 452 -3.1; 484 -2.7; 518 -2.3; 554 -1.6; 593 -1.0; 635 -0.6; 679 -0.4; 726 -0.0; 777 0.4; 832 0.5; 890 0.5; 952 0.3; 1019 -0.1; 1090 -0.6; 1167 -1.2; 1248 -1.8; 1336 -2.6; 1429 -3.3; 1529 -3.9; 1636 -4.3; 1751 -4.6; 1873 -4.7; 2004 -4.8; 2145 -5.0; 2295 -5.0; 2455 -4.7; 2627 -4.3; 2811 -3.9; 3008 -2.7; 3219 -1.7; 3444 -0.8; 3685 -1.1; 3943 -2.5; 4219 -4.9; 4514 -6.7; 4830 -6.1; 5168 -3.2; 5530 -0.1; 5917 2.8; 6331 4.4; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.7; 10167 -1.3; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.2dB` and instead set Global volume in the UI for both channels to **-52**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Xiaomi Piston 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 58 Hz   | 0.33 | -5.0 dB |
| Peaking | 184 Hz  | 0.76 | -6.6 dB |
| Peaking | 2084 Hz | 1.64 | -5.3 dB |
| Peaking | 4656 Hz | 4.71 | -7.3 dB |
| Peaking | 6357 Hz | 4.63 | 5.8 dB  |
| Peaking | 381 Hz  | 2.13 | -1.0 dB |
| Peaking | 840 Hz  | 1.55 | 2.0 dB  |
| Peaking | 1446 Hz | 3.82 | -1.5 dB |
| Peaking | 5793 Hz | 0.32 | -0.2 dB |
| Peaking | 3563 Hz | 7.93 | 1.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Xiaomi%20Piston%203/Xiaomi%20Piston%203.png)