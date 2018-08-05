# Sync by 50

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.9dB
GraphicEQ: 10 -84; 20 -1.2; 22 -2.0; 23 -2.4; 25 -3.2; 26 -3.5; 28 -4.1; 30 -4.6; 32 -5.1; 35 -5.7; 37 -6.1; 40 -6.5; 42 -6.7; 45 -7.0; 49 -7.4; 52 -7.6; 56 -7.8; 59 -7.9; 64 -8.0; 68 -8.1; 73 -8.2; 78 -8.3; 83 -8.5; 89 -8.7; 95 -9.1; 102 -9.3; 109 -9.5; 117 -9.8; 125 -10.1; 134 -10.2; 143 -10.3; 153 -10.3; 164 -10.2; 175 -10.0; 188 -9.9; 201 -9.6; 215 -9.2; 230 -8.8; 246 -8.7; 263 -8.7; 282 -9.1; 301 -9.0; 323 -8.8; 345 -8.6; 369 -8.3; 395 -8.1; 423 -8.1; 452 -7.9; 484 -7.7; 518 -6.8; 554 -5.3; 593 -2.9; 635 -0.7; 679 0.7; 726 1.8; 777 2.3; 832 1.8; 890 1.1; 952 0.4; 1019 -0.2; 1090 -0.7; 1167 -0.8; 1248 -0.5; 1336 0.2; 1429 0.2; 1529 -0.9; 1636 -2.2; 1751 -2.8; 1873 -3.2; 2004 -3.2; 2145 -2.6; 2295 -2.1; 2455 -1.2; 2627 -0.1; 2811 0.7; 3008 1.3; 3219 1.5; 3444 1.1; 3685 0.7; 3943 -0.3; 4219 -0.6; 4514 1.2; 4830 3.2; 5168 4.5; 5530 3.1; 5917 3.3; 6331 5.1; 6775 0.7; 7249 -0.6; 7756 0.2; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.9dB` and instead set Global volume in the UI for both channels to **-59**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sync by 50 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 68 Hz   | 0.45 | -7.1 dB |
| Peaking | 188 Hz  | 0.88 | -6.5 dB |
| Peaking | 403 Hz  | 2.1  | -6.0 dB |
| Peaking | 1950 Hz | 4.23 | -3.6 dB |
| Peaking | 5540 Hz | 2.8  | 4.3 dB  |
| Peaking | 493 Hz  | 7.72 | -1.9 dB |
| Peaking | 552 Hz  | 6.71 | -2.1 dB |
| Peaking | 754 Hz  | 2.83 | 4.2 dB  |
| Peaking | 3105 Hz | 3.2  | 3.9 dB  |
| Peaking | 3138 Hz | 1.49 | -2.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sync%20by%2050/Sync%20by%2050.png)