# Monoprice 8320

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 5.9; 78 5.6; 83 5.3; 89 4.9; 95 4.5; 102 4.3; 109 4.1; 117 3.8; 125 3.6; 134 3.2; 143 2.9; 153 2.7; 164 2.3; 175 2.4; 188 2.1; 201 1.9; 215 1.7; 230 1.6; 246 1.4; 263 1.2; 282 1.2; 301 1.1; 323 1.0; 345 1.0; 369 0.9; 395 0.8; 423 0.9; 452 0.9; 484 0.8; 518 0.9; 554 1.0; 593 1.2; 635 1.2; 679 1.1; 726 0.9; 777 0.9; 832 0.4; 890 1.0; 952 0.5; 1019 -0.1; 1090 -0.7; 1167 -1.2; 1248 -1.8; 1336 -2.6; 1429 -3.4; 1529 -4.3; 1636 -5.2; 1751 -6.2; 1873 -7.2; 2004 -8.2; 2145 -9.3; 2295 -10.0; 2455 -8.6; 2627 -6.4; 2811 -4.2; 3008 -1.7; 3219 0.4; 3444 1.5; 3685 1.3; 3943 0.1; 4219 -2.3; 4514 -3.0; 4830 -0.9; 5168 -0.9; 5530 -1.9; 5917 4.3; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monoprice 8320 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 39 Hz   | 0.31 | 6.4 dB   |
| Peaking | 699 Hz  | 1.68 | 1.3 dB   |
| Peaking | 2125 Hz | 2.13 | -10.2 dB |
| Peaking | 5525 Hz | 5.46 | -4.9 dB  |
| Peaking | 6168 Hz | 4.47 | 8.2 dB   |
| Peaking | 932 Hz  | 6.59 | 0.7 dB   |
| Peaking | 1481 Hz | 4.47 | -1.3 dB  |
| Peaking | 2571 Hz | 5.38 | -2.6 dB  |
| Peaking | 3482 Hz | 2.65 | 3.9 dB   |
| Peaking | 4371 Hz | 6.81 | -3.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monoprice%208320/Monoprice%208320.png)