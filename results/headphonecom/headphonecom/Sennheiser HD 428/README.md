# Sennheiser HD 428

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 5.9; 56 5.2; 59 4.2; 64 3.0; 68 3.5; 73 5.1; 78 4.8; 83 3.3; 89 1.8; 95 0.8; 102 -0.2; 109 -0.7; 117 -1.2; 125 -1.4; 134 -1.4; 143 -1.4; 153 -1.3; 164 -1.0; 175 -0.7; 188 -0.3; 201 -0.1; 215 0.0; 230 0.7; 246 0.8; 263 0.2; 282 0.3; 301 0.5; 323 0.3; 345 0.1; 369 0.2; 395 0.4; 423 0.6; 452 0.7; 484 1.0; 518 1.4; 554 1.7; 593 2.0; 635 1.8; 679 1.3; 726 0.9; 777 0.4; 832 0.0; 890 -0.1; 952 -0.1; 1019 0.1; 1090 1.8; 1167 1.9; 1248 0.8; 1336 0.8; 1429 1.3; 1529 1.5; 1636 1.2; 1751 1.0; 1873 1.1; 2004 1.7; 2145 3.0; 2295 4.8; 2455 5.6; 2627 5.5; 2811 5.8; 3008 5.7; 3219 5.5; 3444 5.0; 3685 4.5; 3943 5.6; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 428 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.28 | 6.4 dB  |
| Peaking | 126 Hz  | 1.31 | -5.1 dB |
| Peaking | 587 Hz  | 3.69 | 1.8 dB  |
| Peaking | 2817 Hz | 1.69 | 5.3 dB  |
| Peaking | 5205 Hz | 1.9  | 5.9 dB  |
| Peaking | 980 Hz  | 4.18 | -1.1 dB |
| Peaking | 1127 Hz | 8.24 | 2.2 dB  |
| Peaking | 1878 Hz | 8.08 | -1.0 dB |
| Peaking | 6469 Hz | 5.62 | 2.9 dB  |
| Peaking | 7702 Hz | 2    | -1.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Sennheiser%20HD%20428/Sennheiser%20HD%20428.png)