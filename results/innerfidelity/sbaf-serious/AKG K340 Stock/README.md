# AKG K340 Stock

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 5.2; 68 4.5; 73 3.9; 78 3.3; 83 2.6; 89 1.8; 95 1.2; 102 0.4; 109 -0.2; 117 -0.8; 125 -1.6; 134 -2.1; 143 -2.5; 153 -2.8; 164 -2.8; 175 -3.2; 188 -3.3; 201 -3.5; 215 -3.5; 230 -3.5; 246 -3.5; 263 -3.6; 282 -3.5; 301 -3.4; 323 -3.3; 345 -2.9; 369 -2.7; 395 -2.6; 423 -2.1; 452 -1.6; 484 -1.2; 518 -0.5; 554 0.7; 593 1.0; 635 1.2; 679 1.5; 726 1.5; 777 2.2; 832 1.9; 890 0.9; 952 0.3; 1019 -0.1; 1090 -0.2; 1167 4.5; 1248 5.7; 1336 2.5; 1429 0.3; 1529 -1.0; 1636 -1.4; 1751 -1.5; 1873 -0.9; 2004 -0.4; 2145 -3.2; 2295 -4.4; 2455 -4.8; 2627 -3.5; 2811 -1.9; 3008 0.2; 3219 1.2; 3444 2.7; 3685 1.8; 3943 1.5; 4219 3.4; 4514 2.1; 4830 2.3; 5168 2.7; 5530 2.3; 5917 0.5; 6331 -0.5; 6775 1.8; 7249 1.4; 7756 -1.2; 8299 -5.6; 8880 -8.2; 9502 -7.4; 10167 -4.1; 10879 -0.5; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -0.7; 18692 -3.7; 20000 -6.3
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K340 Stock ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 50 Hz   | 0.36 | 8.6 dB   |
| Peaking | 169 Hz  | 0.45 | -7.3 dB  |
| Peaking | 2335 Hz | 0.31 | 5.3 dB   |
| Peaking | 2316 Hz | 1.55 | -9.3 dB  |
| Peaking | 9061 Hz | 3.62 | -10.9 dB |
| Peaking | 712 Hz  | 2.71 | 1.2 dB   |
| Peaking | 1074 Hz | 3.89 | -4.3 dB  |
| Peaking | 1219 Hz | 6.9  | 6.6 dB   |
| Peaking | 1546 Hz | 6.58 | -2.6 dB  |
| Peaking | 3388 Hz | 8.7  | 1.4 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K340%20Stock/AKG%20K340%20Stock.png)