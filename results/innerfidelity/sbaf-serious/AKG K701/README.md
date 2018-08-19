# AKG K701

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 5.9; 30 5.6; 32 5.3; 35 4.8; 37 4.5; 40 4.1; 42 3.9; 45 3.6; 49 3.2; 52 2.9; 56 2.6; 59 2.5; 64 2.5; 68 2.8; 73 2.5; 78 1.9; 83 1.8; 89 1.4; 95 0.6; 102 0.0; 109 -0.3; 117 -0.6; 125 -1.0; 134 -1.3; 143 -1.5; 153 -1.6; 164 -1.6; 175 -1.8; 188 -2.0; 201 -2.1; 215 -2.1; 230 -2.0; 246 -2.1; 263 -2.1; 282 -2.0; 301 -2.0; 323 -1.8; 345 -1.6; 369 -1.6; 395 -1.4; 423 -1.1; 452 -0.8; 484 -0.6; 518 -0.5; 554 -0.2; 593 0.2; 635 0.6; 679 1.0; 726 1.5; 777 1.7; 832 1.3; 890 0.7; 952 0.4; 1019 -0.0; 1090 -0.1; 1167 -0.1; 1248 0.0; 1336 -0.1; 1429 -0.2; 1529 -0.4; 1636 -0.9; 1751 -1.6; 1873 -2.1; 2004 -2.7; 2145 -2.8; 2295 -2.6; 2455 -2.3; 2627 -1.7; 2811 -0.8; 3008 0.4; 3219 1.6; 3444 1.8; 3685 1.0; 3943 0.4; 4219 -0.8; 4514 -1.6; 4830 -1.4; 5168 -1.1; 5530 -1.9; 5917 -3.9; 6331 -4.5; 6775 -3.1; 7249 -2.6; 7756 -2.8; 8299 -3.2; 8880 -3.1; 9502 -2.2; 10167 -0.5; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -0.0; 18692 -1.2; 20000 -2.5
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K701 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.2dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 0.7  | 6.2 dB  |
| Peaking | 73 Hz    | 2.78 | 1.5 dB  |
| Peaking | 201 Hz   | 0.89 | -2.5 dB |
| Peaking | 2115 Hz  | 3.94 | -3.1 dB |
| Peaking | 6947 Hz  | 1.81 | -3.8 dB |
| Peaking | 762 Hz   | 3.76 | 2.1 dB  |
| Peaking | 2615 Hz  | 4.79 | -1.3 dB |
| Peaking | 3373 Hz  | 4.11 | 2.9 dB  |
| Peaking | 14882 Hz | 0.59 | 3.2 dB  |
| Peaking | 19246 Hz | 0.19 | -3.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K701/AKG%20K701.png)