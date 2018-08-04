# Teac CT-H02

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 2.4; 22 2.2; 23 2.1; 25 1.9; 26 1.9; 28 1.8; 30 1.7; 32 1.7; 35 1.6; 37 1.6; 40 1.7; 42 1.7; 45 1.7; 49 1.8; 52 1.8; 56 1.8; 59 1.8; 64 1.9; 68 1.9; 73 1.8; 78 1.7; 83 1.7; 89 1.5; 95 1.4; 102 1.1; 109 0.6; 117 0.2; 125 0.1; 134 0.3; 143 0.5; 153 -0.2; 164 -0.4; 175 0.1; 188 -0.6; 201 -1.3; 215 -1.6; 230 -1.7; 246 -1.6; 263 -1.4; 282 -1.5; 301 -1.6; 323 -1.6; 345 -1.4; 369 -1.4; 395 -1.4; 423 -1.3; 452 -1.3; 484 -1.4; 518 -1.4; 554 -1.3; 593 -1.2; 635 -1.3; 679 -1.2; 726 -0.8; 777 -0.5; 832 -0.7; 890 -0.6; 952 -0.2; 1019 -0.1; 1090 -0.4; 1167 -0.3; 1248 -0.2; 1336 -0.2; 1429 -0.2; 1529 -0.3; 1636 -0.4; 1751 -0.2; 1873 0.4; 2004 1.3; 2145 1.8; 2295 2.9; 2455 4.4; 2627 5.1; 2811 5.8; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 5.0; 4514 5.9; 4830 6.0; 5168 5.9; 5530 5.7; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 -1.7; 8299 -4.9; 8880 -6.5; 9502 -5.9; 10167 -3.1; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Teac CT-H02 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 0.9  | 2.0 dB  |
| Peaking | 69 Hz    | 1.99 | 1.8 dB  |
| Peaking | 3064 Hz  | 2.27 | 5.0 dB  |
| Peaking | 5747 Hz  | 1.23 | 6.8 dB  |
| Peaking | 8810 Hz  | 2.96 | -9.8 dB |
| Peaking | 379 Hz   | 0.74 | -1.7 dB |
| Peaking | 1764 Hz  | 2.48 | -1.5 dB |
| Peaking | 2488 Hz  | 6.77 | 1.4 dB  |
| Peaking | 1976 Hz  | 3.92 | 0.7 dB  |
| Peaking | 25844 Hz | 1.59 | 0.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Teac%20CT-H02/Teac%20CT-H02.png)