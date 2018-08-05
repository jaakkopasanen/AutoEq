# Ostry KC06

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 4.8; 22 4.4; 23 4.1; 25 3.7; 26 3.5; 28 3.2; 30 2.9; 32 2.6; 35 2.3; 37 2.1; 40 1.9; 42 1.7; 45 1.5; 49 1.3; 52 1.2; 56 1.0; 59 0.9; 64 0.7; 68 0.6; 73 0.3; 78 0.1; 83 -0.2; 89 -0.6; 95 -1.1; 102 -1.7; 109 -2.2; 117 -2.7; 125 -3.3; 134 -3.8; 143 -4.1; 153 -4.2; 164 -4.3; 175 -4.3; 188 -4.2; 201 -4.1; 215 -3.9; 230 -3.7; 246 -3.5; 263 -3.3; 282 -3.0; 301 -2.7; 323 -2.4; 345 -2.1; 369 -1.8; 395 -1.5; 423 -1.1; 452 -0.7; 484 -0.5; 518 -0.2; 554 0.2; 593 0.7; 635 0.9; 679 0.9; 726 1.1; 777 1.2; 832 1.0; 890 0.7; 952 0.3; 1019 -0.1; 1090 -0.6; 1167 -1.2; 1248 -1.8; 1336 -2.6; 1429 -3.4; 1529 -4.1; 1636 -4.7; 1751 -5.0; 1873 -5.0; 2004 -4.9; 2145 -4.6; 2295 -3.9; 2455 -2.4; 2627 -0.6; 2811 1.2; 3008 3.5; 3219 5.5; 3444 6.0; 3685 6.0; 3943 6.0; 4219 5.7; 4514 4.6; 4830 4.2; 5168 4.3; 5530 3.6; 5917 1.6; 6331 -1.7; 6775 -5.3; 7249 -5.9; 7756 -4.0; 8299 -1.6; 8880 -0.6; 9502 -1.8; 10167 -3.9; 10879 -3.8; 11640 -0.6; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ostry KC06 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 10 Hz    | 0.3  | 5.2 dB  |
| Peaking | 175 Hz   | 0.98 | -4.8 dB |
| Peaking | 2034 Hz  | 1.56 | -8.8 dB |
| Peaking | 3854 Hz  | 0.92 | 8.7 dB  |
| Peaking | 7128 Hz  | 2.28 | -8.3 dB |
| Peaking | 758 Hz   | 2.1  | 1.9 dB  |
| Peaking | 1453 Hz  | 4.33 | -1.4 dB |
| Peaking | 8658 Hz  | 7.28 | 2.1 dB  |
| Peaking | 5634 Hz  | 8.84 | 2.1 dB  |
| Peaking | 10468 Hz | 5.56 | -4.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Ostry%20KC06/Ostry%20KC06.png)