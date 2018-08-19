# NHT Super Buds

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -10.1; 22 -10.3; 23 -10.3; 25 -10.4; 26 -10.4; 28 -10.3; 30 -10.3; 32 -10.2; 35 -10.1; 37 -10.1; 40 -10.0; 42 -9.9; 45 -9.8; 49 -9.7; 52 -9.6; 56 -9.5; 59 -9.4; 64 -9.3; 68 -9.2; 73 -9.2; 78 -9.1; 83 -9.0; 89 -8.9; 95 -8.9; 102 -8.7; 109 -8.4; 117 -8.2; 125 -8.0; 134 -7.9; 143 -7.6; 153 -7.4; 164 -7.0; 175 -6.7; 188 -6.4; 201 -6.0; 215 -5.6; 230 -5.2; 246 -4.8; 263 -4.4; 282 -3.9; 301 -3.5; 323 -3.1; 345 -2.6; 369 -2.3; 395 -1.9; 423 -1.4; 452 -1.0; 484 -0.7; 518 -0.4; 554 0.1; 593 0.5; 635 0.5; 679 0.6; 726 0.8; 777 0.9; 832 0.8; 890 0.5; 952 0.3; 1019 -0.1; 1090 -0.4; 1167 -0.8; 1248 -1.2; 1336 -1.8; 1429 -2.5; 1529 -3.2; 1636 -3.8; 1751 -4.2; 1873 -4.3; 2004 -4.3; 2145 -4.0; 2295 -3.5; 2455 -2.7; 2627 -1.9; 2811 -1.0; 3008 0.7; 3219 2.2; 3444 4.3; 3685 5.8; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999674948805dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NHT Super Buds ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of -7.1dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 27 Hz   | 0.1  | -10.0 dB |
| Peaking | 722 Hz  | 0.67 | 3.0 dB   |
| Peaking | 2014 Hz | 1.04 | -6.7 dB  |
| Peaking | 4362 Hz | 1.23 | 8.4 dB   |
| Peaking | 3644 Hz | 6.65 | 1.9 dB   |
| Peaking | 4470 Hz | 2.57 | -1.4 dB  |
| Peaking | 6379 Hz | 2.71 | 4.0 dB   |
| Peaking | 7435 Hz | 3.41 | -2.2 dB  |
| Peaking | 8231 Hz | 1.04 | -1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NHT%20Super%20Buds/NHT%20Super%20Buds.png)