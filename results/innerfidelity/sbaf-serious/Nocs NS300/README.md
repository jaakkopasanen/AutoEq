# Nocs NS300

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 5.7; 42 5.4; 45 4.9; 49 4.4; 52 4.1; 56 3.8; 59 3.6; 64 3.3; 68 3.2; 73 3.0; 78 2.9; 83 3.0; 89 3.2; 95 3.1; 102 3.3; 109 3.9; 117 4.2; 125 3.9; 134 3.3; 143 3.1; 153 3.1; 164 3.9; 175 4.2; 188 4.6; 201 5.3; 215 6.0; 230 6.0; 246 6.0; 263 6.0; 282 6.0; 301 5.5; 323 3.7; 345 2.4; 369 2.1; 395 1.7; 423 1.4; 452 1.2; 484 0.9; 518 0.7; 554 0.7; 593 0.6; 635 0.3; 679 0.0; 726 -0.2; 777 -0.2; 832 -0.5; 890 -0.6; 952 -0.3; 1019 0.3; 1090 1.0; 1167 2.1; 1248 2.8; 1336 3.0; 1429 3.3; 1529 4.3; 1636 4.0; 1751 4.7; 1873 4.8; 2004 4.8; 2145 4.5; 2295 4.1; 2455 4.0; 2627 3.2; 2811 2.7; 3008 2.5; 3219 1.9; 3444 2.8; 3685 3.7; 3943 4.7; 4219 5.9; 4514 6.0; 4830 4.5; 5168 4.5; 5530 5.7; 5917 5.9; 6331 5.3; 6775 3.2; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Nocs NS300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.58 | 6.2 dB  |
| Peaking | 117 Hz  | 1.91 | 2.1 dB  |
| Peaking | 245 Hz  | 1.7  | 6.2 dB  |
| Peaking | 1862 Hz | 1.68 | 4.7 dB  |
| Peaking | 4979 Hz | 1.56 | 5.7 dB  |
| Peaking | 914 Hz  | 2.04 | -1.8 dB |
| Peaking | 1233 Hz | 3.2  | 1.6 dB  |
| Peaking | 6775 Hz | 5.42 | 1.6 dB  |
| Peaking | 6138 Hz | 6.31 | 3.0 dB  |
| Peaking | 7263 Hz | 1.72 | -2.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Nocs%20NS300/Nocs%20NS300.png)