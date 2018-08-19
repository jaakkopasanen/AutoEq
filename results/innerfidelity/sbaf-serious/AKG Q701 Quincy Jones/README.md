# AKG Q701 Quincy Jones

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 5.9; 32 5.7; 35 5.2; 37 4.9; 40 4.4; 42 4.1; 45 3.7; 49 3.3; 52 2.9; 56 2.5; 59 2.2; 64 1.8; 68 1.6; 73 1.6; 78 1.7; 83 1.5; 89 1.1; 95 0.5; 102 0.1; 109 -0.1; 117 -0.4; 125 -0.9; 134 -1.1; 143 -1.4; 153 -1.6; 164 -1.6; 175 -1.5; 188 -1.7; 201 -1.8; 215 -1.8; 230 -1.8; 246 -1.8; 263 -1.8; 282 -1.7; 301 -1.5; 323 -1.5; 345 -1.4; 369 -1.3; 395 -1.2; 423 -1.0; 452 -0.9; 484 -0.8; 518 -0.6; 554 -0.1; 593 1.0; 635 0.7; 679 0.6; 726 0.8; 777 1.0; 832 0.7; 890 0.3; 952 0.1; 1019 0.1; 1090 -0.1; 1167 -0.5; 1248 -0.9; 1336 -1.6; 1429 -2.4; 1529 -3.2; 1636 -4.0; 1751 -4.7; 1873 -5.4; 2004 -5.6; 2145 -5.3; 2295 -4.9; 2455 -3.9; 2627 -2.9; 2811 -1.7; 3008 -1.1; 3219 -0.3; 3444 0.6; 3685 0.3; 3943 -0.4; 4219 -2.0; 4514 -2.6; 4830 -1.7; 5168 -1.7; 5530 -2.9; 5917 -3.8; 6331 -4.7; 6775 -4.7; 7249 -4.4; 7756 -4.9; 8299 -5.5; 8880 -4.8; 9502 -2.3; 10167 -0.1; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -0.3; 18692 -2.1; 20000 -2.9
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG Q701 Quincy Jones ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.2dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 0.46 | 6.2 dB  |
| Peaking | 215 Hz   | 0.55 | -2.3 dB |
| Peaking | 728 Hz   | 1.53 | 1.8 dB  |
| Peaking | 1960 Hz  | 2.11 | -5.9 dB |
| Peaking | 7349 Hz  | 1.83 | -5.4 dB |
| Peaking | 2438 Hz  | 6.14 | -1.0 dB |
| Peaking | 3571 Hz  | 3.69 | 2.2 dB  |
| Peaking | 4398 Hz  | 5.61 | -1.7 dB |
| Peaking | 10905 Hz | 4.68 | 1.5 dB  |
| Peaking | 19513 Hz | 2.59 | -3.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20Q701%20Quincy%20Jones/AKG%20Q701%20Quincy%20Jones.png)