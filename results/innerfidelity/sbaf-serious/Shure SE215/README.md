# Shure SE215

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.7dB
GraphicEQ: 10 -84; 20 -4.0; 22 -4.0; 23 -4.0; 25 -4.1; 26 -4.1; 28 -4.1; 30 -4.1; 32 -4.1; 35 -4.1; 37 -4.1; 40 -4.1; 42 -4.1; 45 -4.1; 49 -4.1; 52 -4.1; 56 -4.1; 59 -4.1; 64 -4.2; 68 -4.2; 73 -4.2; 78 -4.4; 83 -4.5; 89 -4.8; 95 -5.1; 102 -5.6; 109 -5.9; 117 -6.4; 125 -6.8; 134 -7.1; 143 -7.3; 153 -7.3; 164 -7.3; 175 -7.1; 188 -6.9; 201 -6.7; 215 -6.4; 230 -6.0; 246 -5.8; 263 -5.5; 282 -5.0; 301 -4.7; 323 -4.3; 345 -3.8; 369 -3.5; 395 -3.1; 423 -2.6; 452 -2.2; 484 -1.9; 518 -1.5; 554 -1.0; 593 -0.4; 635 -0.1; 679 0.0; 726 0.3; 777 0.6; 832 0.6; 890 0.4; 952 0.3; 1019 -0.0; 1090 -0.2; 1167 -0.3; 1248 -0.7; 1336 -1.5; 1429 -2.3; 1529 -2.9; 1636 -3.6; 1751 -4.1; 1873 -4.4; 2004 -4.7; 2145 -4.9; 2295 -4.6; 2455 -3.5; 2627 -2.0; 2811 -0.2; 3008 2.1; 3219 3.6; 3444 4.4; 3685 3.9; 3943 2.1; 4219 -1.4; 4514 -5.6; 4830 -7.9; 5168 -4.2; 5530 0.6; 5917 3.7; 6331 5.1; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.7dB` and instead set Global volume in the UI for both channels to **-57**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE215 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 134 Hz  | 0.45 | -7.0 dB  |
| Peaking | 2124 Hz | 2.07 | -6.0 dB  |
| Peaking | 3524 Hz | 2.49 | 6.9 dB   |
| Peaking | 4813 Hz | 4.34 | -10.7 dB |
| Peaking | 6237 Hz | 4.17 | 6.6 dB   |
| Peaking | 20 Hz   | 0.53 | -3.2 dB  |
| Peaking | 85 Hz   | 1.13 | 2.6 dB   |
| Peaking | 167 Hz  | 0.45 | -1.2 dB  |
| Peaking | 766 Hz  | 1.16 | 2.0 dB   |
| Peaking | 1551 Hz | 4.1  | -1.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SE215/Shure%20SE215.png)