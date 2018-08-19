# Ostry KC06

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 4.8; 22 4.3; 23 4.0; 25 3.6; 26 3.4; 28 3.0; 30 2.7; 32 2.4; 35 2.0; 37 1.8; 40 1.4; 42 1.2; 45 1.0; 49 0.6; 52 0.4; 56 0.0; 59 -0.2; 64 -0.6; 68 -0.8; 73 -1.3; 78 -1.6; 83 -1.8; 89 -2.2; 95 -2.5; 102 -2.8; 109 -2.9; 117 -3.1; 125 -3.3; 134 -3.5; 143 -3.6; 153 -3.7; 164 -3.7; 175 -3.7; 188 -3.7; 201 -3.7; 215 -3.5; 230 -3.3; 246 -3.2; 263 -3.1; 282 -2.8; 301 -2.6; 323 -2.3; 345 -2.0; 369 -1.7; 395 -1.4; 423 -1.0; 452 -0.7; 484 -0.5; 518 -0.2; 554 0.3; 593 0.8; 635 0.9; 679 0.9; 726 1.1; 777 1.2; 832 1.0; 890 0.7; 952 0.3; 1019 -0.1; 1090 -0.6; 1167 -1.2; 1248 -1.8; 1336 -2.6; 1429 -3.4; 1529 -4.1; 1636 -4.7; 1751 -5.0; 1873 -5.0; 2004 -4.9; 2145 -4.6; 2295 -3.9; 2455 -2.4; 2627 -0.6; 2811 1.2; 3008 3.5; 3219 5.5; 3444 6.0; 3685 6.0; 3943 6.0; 4219 5.7; 4514 4.6; 4830 4.2; 5168 4.3; 5530 3.6; 5917 1.6; 6331 -1.7; 6775 -5.3; 7249 -5.9; 7756 -4.0; 8299 -1.6; 8880 -0.6; 9502 -1.8; 10167 -3.9; 10879 -3.8; 11640 -0.6; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999984438796dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ostry KC06 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.4dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 0.82 | 4.7 dB  |
| Peaking | 160 Hz   | 0.77 | -4.1 dB |
| Peaking | 2033 Hz  | 1.56 | -9.0 dB |
| Peaking | 3873 Hz  | 0.88 | 8.8 dB  |
| Peaking | 7200 Hz  | 2.19 | -8.5 dB |
| Peaking | 753 Hz   | 2.07 | 1.9 dB  |
| Peaking | 1452 Hz  | 4.3  | -1.4 dB |
| Peaking | 5637 Hz  | 9.89 | 1.9 dB  |
| Peaking | 8624 Hz  | 6.92 | 2.4 dB  |
| Peaking | 10477 Hz | 5.64 | -4.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ostry%20KC06/Ostry%20KC06.png)