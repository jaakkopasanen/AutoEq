# AKG K167 Tiesto

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 5.9; 25 5.6; 26 5.5; 28 5.2; 30 4.9; 32 4.7; 35 4.5; 37 4.4; 40 4.3; 42 4.3; 45 4.3; 49 4.4; 52 4.5; 56 4.7; 59 5.0; 64 5.6; 68 5.9; 73 5.9; 78 5.5; 83 5.1; 89 4.8; 95 4.7; 102 4.7; 109 4.5; 117 4.4; 125 4.3; 134 4.2; 143 4.2; 153 4.3; 164 4.9; 175 4.5; 188 3.9; 201 3.8; 215 4.0; 230 4.1; 246 4.0; 263 4.0; 282 4.0; 301 3.6; 323 3.1; 345 2.8; 369 2.5; 395 2.3; 423 2.3; 452 2.2; 484 1.9; 518 1.6; 554 1.6; 593 1.6; 635 1.4; 679 1.1; 726 1.0; 777 0.9; 832 0.5; 890 0.3; 952 0.2; 1019 -0.1; 1090 -0.4; 1167 -0.9; 1248 -0.9; 1336 -0.7; 1429 -1.8; 1529 -2.3; 1636 -3.1; 1751 -3.2; 1873 -3.1; 2004 -2.0; 2145 -0.0; 2295 0.9; 2455 1.6; 2627 2.3; 2811 2.9; 3008 3.7; 3219 3.7; 3444 3.6; 3685 3.2; 3943 3.1; 4219 2.9; 4514 3.1; 4830 4.9; 5168 6.0; 5530 5.6; 5917 3.1; 6331 2.6; 6775 3.5; 7249 1.3; 7756 0.3; 8299 -0.4; 8880 -2.5; 9502 -2.6; 10167 -1.0; 10879 -0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K167 Tiesto ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of -5.7dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 1.12 | 4.4 dB  |
| Peaking | 72 Hz    | 0.71 | 4.6 dB  |
| Peaking | 241 Hz   | 0.82 | 3.3 dB  |
| Peaking | 4918 Hz  | 1.79 | 5.3 dB  |
| Peaking | 1799 Hz  | 1.54 | -7.3 dB |
| Peaking | 2505 Hz  | 0.68 | 4.8 dB  |
| Peaking | 4320 Hz  | 3.7  | -3.7 dB |
| Peaking | 9124 Hz  | 3.89 | -4.0 dB |
| Peaking | 20769 Hz | 2.5  | -0.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K167%20Tiesto/AKG%20K167%20Tiesto.png)