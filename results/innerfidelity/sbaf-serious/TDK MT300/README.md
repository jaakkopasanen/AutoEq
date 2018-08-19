# TDK MT300

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.4dB
GraphicEQ: 10 -84; 20 -8.9; 22 -8.9; 23 -8.9; 25 -8.9; 26 -8.9; 28 -8.9; 30 -8.8; 32 -8.8; 35 -8.8; 37 -8.8; 40 -8.8; 42 -8.8; 45 -8.8; 49 -8.8; 52 -8.8; 56 -8.8; 59 -8.8; 64 -8.9; 68 -9.0; 73 -9.1; 78 -9.1; 83 -9.2; 89 -9.3; 95 -9.4; 102 -9.4; 109 -9.2; 117 -9.1; 125 -9.1; 134 -9.0; 143 -8.9; 153 -8.7; 164 -8.5; 175 -8.2; 188 -7.9; 201 -7.6; 215 -7.2; 230 -6.8; 246 -6.4; 263 -6.0; 282 -5.4; 301 -5.0; 323 -4.5; 345 -3.9; 369 -3.5; 395 -2.9; 423 -2.3; 452 -1.8; 484 -1.5; 518 -1.1; 554 -0.5; 593 0.0; 635 0.3; 679 0.2; 726 0.4; 777 0.7; 832 0.5; 890 0.3; 952 0.2; 1019 -0.1; 1090 -0.3; 1167 -0.4; 1248 -0.4; 1336 -0.6; 1429 -0.6; 1529 -0.5; 1636 -0.0; 1751 0.8; 1873 1.7; 2004 2.5; 2145 3.3; 2295 3.9; 2455 4.6; 2627 4.9; 2811 5.0; 3008 4.9; 3219 4.3; 3444 3.6; 3685 2.2; 3943 0.4; 4219 -2.4; 4514 -5.3; 4830 -7.3; 5168 -4.7; 5530 -0.7; 5917 3.0; 6331 5.3; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.41414977753346dB` and instead set Global volume in the UI for both channels to **-54**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `TDK MT300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.6dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 61 Hz   | 0.22 | -9.8 dB  |
| Peaking | 2907 Hz | 1.48 | 6.0 dB   |
| Peaking | 4803 Hz | 3.56 | -10.1 dB |
| Peaking | 6307 Hz | 3.89 | 7.2 dB   |
| Peaking | 7654 Hz | 2.14 | -1.0 dB  |
| Peaking | 18 Hz   | 1.12 | -2.4 dB  |
| Peaking | 55 Hz   | 0.85 | 1.4 dB   |
| Peaking | 191 Hz  | 0.69 | -1.3 dB  |
| Peaking | 636 Hz  | 1.05 | 2.1 dB   |
| Peaking | 1387 Hz | 2.6  | -1.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/TDK%20MT300/TDK%20MT300.png)