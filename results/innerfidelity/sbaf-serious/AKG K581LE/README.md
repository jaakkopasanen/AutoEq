# AKG K581LE

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 5.7; 30 5.4; 32 5.1; 35 4.6; 37 4.3; 40 3.9; 42 3.7; 45 3.4; 49 3.3; 52 3.3; 56 2.9; 59 2.4; 64 1.9; 68 1.7; 73 1.7; 78 1.6; 83 0.9; 89 0.0; 95 -0.2; 102 0.7; 109 0.6; 117 -0.3; 125 -1.2; 134 -2.4; 143 -3.0; 153 -3.3; 164 -2.8; 175 -2.9; 188 -2.3; 201 -1.9; 215 -2.3; 230 -2.2; 246 -1.5; 263 -1.0; 282 -1.1; 301 -1.3; 323 -0.8; 345 -0.6; 369 -0.0; 395 0.5; 423 0.9; 452 1.0; 484 1.1; 518 1.1; 554 1.1; 593 1.2; 635 1.1; 679 0.8; 726 0.8; 777 0.7; 832 0.5; 890 0.3; 952 0.1; 1019 0.0; 1090 -0.1; 1167 -0.1; 1248 0.1; 1336 -0.3; 1429 -0.8; 1529 -1.0; 1636 -1.0; 1751 -0.8; 1873 -0.4; 2004 0.2; 2145 0.8; 2295 1.5; 2455 2.4; 2627 3.3; 2811 3.8; 3008 4.4; 3219 4.7; 3444 4.9; 3685 4.8; 3943 4.7; 4219 4.2; 4514 4.3; 4830 4.8; 5168 3.5; 5530 4.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K581LE ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 22 Hz   |  0.61 | 5.9 dB  |
| Peaking | 171 Hz  |  0.38 | 3.0 dB  |
| Peaking | 173 Hz  |  0.87 | -6.2 dB |
| Peaking | 3590 Hz |  1.76 | 5.2 dB  |
| Peaking | 6076 Hz |  4.2  | 5.2 dB  |
| Peaking | 88 Hz   |  6.74 | -0.6 dB |
| Peaking | 1643 Hz |  2.49 | -1.8 dB |
| Peaking | 2667 Hz |  5.26 | 1.3 dB  |
| Peaking | 4761 Hz | 11.13 | 1.7 dB  |
| Peaking | 8308 Hz |  3.31 | -0.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K581LE/AKG%20K581LE.png)