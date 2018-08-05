# NHT Super Buds

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -10.1; 22 -10.2; 23 -10.2; 25 -10.3; 26 -10.3; 28 -10.2; 30 -10.1; 32 -10.0; 35 -9.8; 37 -9.7; 40 -9.6; 42 -9.4; 45 -9.2; 49 -8.9; 52 -8.8; 56 -8.5; 59 -8.3; 64 -8.0; 68 -7.8; 73 -7.6; 78 -7.4; 83 -7.4; 89 -7.4; 95 -7.5; 102 -7.6; 109 -7.7; 117 -7.9; 125 -8.0; 134 -8.1; 143 -8.1; 153 -7.9; 164 -7.6; 175 -7.2; 188 -6.8; 201 -6.5; 215 -6.0; 230 -5.5; 246 -5.1; 263 -4.7; 282 -4.1; 301 -3.7; 323 -3.2; 345 -2.8; 369 -2.4; 395 -2.0; 423 -1.4; 452 -1.0; 484 -0.8; 518 -0.5; 554 0.1; 593 0.5; 635 0.5; 679 0.6; 726 0.8; 777 0.9; 832 0.8; 890 0.5; 952 0.3; 1019 -0.1; 1090 -0.4; 1167 -0.8; 1248 -1.2; 1336 -1.8; 1429 -2.5; 1529 -3.2; 1636 -3.8; 1751 -4.2; 1873 -4.3; 2004 -4.3; 2145 -4.0; 2295 -3.6; 2455 -2.7; 2627 -1.9; 2811 -1.0; 3008 0.7; 3219 2.2; 3444 4.3; 3685 5.8; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NHT Super Buds ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 25 Hz   | 0.38 | -10.0 dB |
| Peaking | 161 Hz  | 0.66 | -6.1 dB  |
| Peaking | 764 Hz  | 0.96 | 2.3 dB   |
| Peaking | 2034 Hz | 1.1  | -6.3 dB  |
| Peaking | 4372 Hz | 1.23 | 8.3 dB   |
| Peaking | 8732 Hz | 1.17 | -1.1 dB  |
| Peaking | 3647 Hz | 5.46 | 2.3 dB   |
| Peaking | 4342 Hz | 1.84 | -1.7 dB  |
| Peaking | 6371 Hz | 2.59 | 4.0 dB   |
| Peaking | 7446 Hz | 3.51 | -2.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NHT%20Super%20Buds/NHT%20Super%20Buds.png)