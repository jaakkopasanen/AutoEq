# AKG K581LE

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 5.7; 30 5.4; 32 5.1; 35 4.6; 37 4.2; 40 3.8; 42 3.6; 45 3.3; 49 3.1; 52 3.0; 56 2.5; 59 2.0; 64 1.4; 68 1.1; 73 1.0; 78 0.8; 83 0.1; 89 -0.8; 95 -0.9; 102 0.1; 109 0.2; 117 -0.5; 125 -1.2; 134 -2.2; 143 -2.8; 153 -3.1; 164 -2.5; 175 -2.6; 188 -2.1; 201 -1.7; 215 -2.1; 230 -2.0; 246 -1.4; 263 -0.9; 282 -1.0; 301 -1.3; 323 -0.8; 345 -0.6; 369 0.0; 395 0.5; 423 0.9; 452 1.0; 484 1.1; 518 1.1; 554 1.1; 593 1.2; 635 1.1; 679 0.8; 726 0.8; 777 0.7; 832 0.5; 890 0.3; 952 0.1; 1019 0.0; 1090 -0.1; 1167 -0.1; 1248 0.1; 1336 -0.3; 1429 -0.8; 1529 -1.0; 1636 -1.0; 1751 -0.8; 1873 -0.4; 2004 0.2; 2145 0.8; 2295 1.5; 2455 2.4; 2627 3.3; 2811 3.8; 3008 4.4; 3219 4.7; 3444 4.9; 3685 4.8; 3943 4.7; 4219 4.2; 4514 4.3; 4830 4.8; 5168 3.5; 5530 4.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K581LE ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.3dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 25 Hz   |  0.85 | 6.2 dB  |
| Peaking | 49 Hz   |  2.65 | 1.1 dB  |
| Peaking | 162 Hz  |  1.59 | -3.1 dB |
| Peaking | 3589 Hz |  1.68 | 5.2 dB  |
| Peaking | 6083 Hz |  4.27 | 5.1 dB  |
| Peaking | 559 Hz  |  2.02 | 1.4 dB  |
| Peaking | 1656 Hz |  2.32 | -1.7 dB |
| Peaking | 2649 Hz |  5.19 | 1.3 dB  |
| Peaking | 4791 Hz | 11.44 | 1.6 dB  |
| Peaking | 8321 Hz |  3.29 | -0.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K581LE/AKG%20K581LE.png)