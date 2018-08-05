# AKG K812

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.9dB
GraphicEQ: 10 -84; 20 1.0; 22 0.6; 23 0.5; 25 0.2; 26 0.1; 28 -0.1; 30 -0.2; 32 -0.4; 35 -0.5; 37 -0.6; 40 -0.8; 42 -0.8; 45 -0.9; 49 -1.0; 52 -1.0; 56 -1.1; 59 -1.1; 64 -1.2; 68 -1.3; 73 -1.3; 78 -1.4; 83 -1.7; 89 -2.0; 95 -2.4; 102 -2.8; 109 -3.1; 117 -3.4; 125 -4.0; 134 -4.2; 143 -4.4; 153 -4.6; 164 -4.6; 175 -4.5; 188 -4.7; 201 -4.7; 215 -4.6; 230 -4.5; 246 -4.4; 263 -4.4; 282 -4.2; 301 -4.1; 323 -4.1; 345 -3.9; 369 -3.8; 395 -3.7; 423 -3.4; 452 -3.2; 484 -3.1; 518 -2.9; 554 -2.6; 593 -2.2; 635 -2.0; 679 -1.8; 726 -1.5; 777 -1.0; 832 -0.6; 890 -0.5; 952 -0.2; 1019 0.1; 1090 0.4; 1167 0.5; 1248 0.7; 1336 0.6; 1429 0.0; 1529 -0.3; 1636 -0.4; 1751 0.3; 1873 0.9; 2004 0.9; 2145 0.7; 2295 0.6; 2455 2.4; 2627 3.2; 2811 0.4; 3008 -1.6; 3219 -2.5; 3444 -2.7; 3685 -2.2; 3943 -0.4; 4219 1.7; 4514 1.9; 4830 -0.5; 5168 -3.7; 5530 -6.4; 5917 -8.8; 6331 -6.3; 6775 -1.0; 7249 -1.2; 7756 -2.1; 8299 -3.3; 8880 -3.8; 9502 -2.9; 10167 -0.9; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.2; 17469 -1.1; 18692 -3.2; 20000 -7.7
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.9dB` and instead set Global volume in the UI for both channels to **-39**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K812 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 228 Hz   | 0.46 | -4.8 dB |
| Peaking | 1576 Hz  | 1.36 | 3.1 dB  |
| Peaking | 1581 Hz  | 3.64 | -3.1 dB |
| Peaking | 5912 Hz  | 4.91 | -9.2 dB |
| Peaking | 28014 Hz | 2.14 | -7.3 dB |
| Peaking | 15 Hz    | 1.59 | 1.5 dB  |
| Peaking | 2602 Hz  | 7.63 | 4.2 dB  |
| Peaking | 3350 Hz  | 2.53 | -3.4 dB |
| Peaking | 4364 Hz  | 5.79 | 4.3 dB  |
| Peaking | 8859 Hz  | 5.8  | -3.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K812/AKG%20K812.png)