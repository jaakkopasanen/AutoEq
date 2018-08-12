# 1MORE Quad Driver

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.5dB
GraphicEQ: 10 -84; 20 2.4; 22 1.4; 23 1.0; 25 0.4; 26 0.2; 28 -0.1; 30 -0.4; 32 -0.9; 35 -1.5; 37 -1.8; 40 -2.3; 42 -2.6; 45 -3.0; 49 -3.6; 52 -4.1; 56 -4.6; 59 -4.9; 64 -5.6; 68 -6.0; 73 -6.3; 78 -6.8; 83 -7.3; 89 -7.0; 95 -7.3; 102 -7.9; 109 -8.0; 117 -8.0; 125 -8.4; 134 -8.6; 143 -8.4; 153 -8.5; 164 -8.5; 175 -8.6; 188 -8.6; 201 -8.5; 215 -8.4; 230 -8.3; 246 -8.1; 263 -7.9; 282 -7.7; 301 -7.3; 323 -6.9; 345 -6.5; 369 -6.1; 395 -5.8; 423 -5.4; 452 -5.0; 484 -4.6; 518 -4.1; 554 -3.6; 593 -3.2; 635 -2.7; 679 -2.2; 726 -1.6; 777 -1.1; 832 -0.7; 890 -0.3; 952 -0.0; 1019 -0.0; 1090 -0.1; 1167 -0.3; 1248 -0.4; 1336 -0.3; 1429 -0.1; 1529 0.0; 1636 0.3; 1751 0.5; 1873 0.7; 2004 0.9; 2145 1.1; 2295 1.2; 2455 1.2; 2627 1.1; 2811 1.1; 3008 1.4; 3219 1.7; 3444 1.8; 3685 1.4; 3943 0.4; 4219 -0.7; 4514 -1.1; 4830 -0.3; 5168 1.1; 5530 1.8; 5917 3.9; 6331 4.8; 6775 2.6; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 -0.4; 11640 -3.0; 12455 -7.1; 13327 -13.8; 14260 -21.2; 15258 -26.6; 16326 -29.2; 17469 -29.3; 18692 -26.9; 20000 -21.3
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.5dB` and instead set Global volume in the UI for both channels to **-55**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1MORE Quad Driver ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 14 Hz    | 0.81 | 4.4 dB   |
| Peaking | 118 Hz   | 0.46 | -7.6 dB  |
| Peaking | 309 Hz   | 0.84 | -3.8 dB  |
| Peaking | 8605 Hz  | 0.29 | 25.9 dB  |
| Peaking | 16670 Hz | 0.33 | -46.7 dB |
| Peaking | 4676 Hz  | 2.44 | -7.0 dB  |
| Peaking | 5830 Hz  | 0.91 | 6.1 dB   |
| Peaking | 7885 Hz  | 2.17 | -6.4 dB  |
| Peaking | 11421 Hz | 2.63 | 4.6 dB   |
| Peaking | 14541 Hz | 3.61 | -6.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_in-ear_2017-1/1MORE%20Quad%20Driver/1MORE%20Quad%20Driver.png)