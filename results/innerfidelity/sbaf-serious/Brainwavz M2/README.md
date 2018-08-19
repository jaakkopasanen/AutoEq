# Brainwavz M2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 5.8; 37 5.5; 40 5.0; 42 4.8; 45 4.4; 49 3.9; 52 3.6; 56 3.1; 59 2.8; 64 2.3; 68 2.0; 73 1.6; 78 1.1; 83 0.8; 89 0.3; 95 -0.0; 102 -0.4; 109 -0.5; 117 -0.7; 125 -1.0; 134 -1.2; 143 -1.4; 153 -1.6; 164 -1.6; 175 -1.8; 188 -1.7; 201 -1.8; 215 -1.7; 230 -1.6; 246 -1.5; 263 -1.5; 282 -1.3; 301 -1.1; 323 -0.9; 345 -0.7; 369 -0.5; 395 -0.3; 423 0.0; 452 0.3; 484 0.4; 518 0.6; 554 0.9; 593 1.2; 635 1.4; 679 1.3; 726 1.3; 777 1.4; 832 1.1; 890 0.8; 952 0.4; 1019 -0.1; 1090 -0.6; 1167 -1.0; 1248 -1.4; 1336 -2.2; 1429 -2.8; 1529 -3.3; 1636 -3.6; 1751 -3.2; 1873 -2.0; 2004 0.1; 2145 2.0; 2295 2.5; 2455 2.5; 2627 3.8; 2811 5.4; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 5.3; 4830 4.4; 5168 4.2; 5530 4.2; 5917 4.8; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Brainwavz M2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.63 | 6.4 dB  |
| Peaking | 162 Hz  | 1    | -2.4 dB |
| Peaking | 1633 Hz | 2.71 | -5.6 dB |
| Peaking | 3447 Hz | 1.1  | 6.7 dB  |
| Peaking | 6241 Hz | 6.09 | 3.7 dB  |
| Peaking | 297 Hz  | 2.17 | -0.7 dB |
| Peaking | 708 Hz  | 1.34 | 1.7 dB  |
| Peaking | 1189 Hz | 2.58 | -1.1 dB |
| Peaking | 6733 Hz | 1.76 | 1.8 dB  |
| Peaking | 7797 Hz | 1.73 | -2.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Brainwavz%20M2/Brainwavz%20M2.png)