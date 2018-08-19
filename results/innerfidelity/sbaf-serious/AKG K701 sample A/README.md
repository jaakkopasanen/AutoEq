# AKG K701 sample A

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 5.9; 30 5.6; 32 5.3; 35 4.8; 37 4.5; 40 4.1; 42 3.9; 45 3.6; 49 3.2; 52 2.9; 56 2.5; 59 2.3; 64 2.1; 68 2.1; 73 2.3; 78 2.3; 83 2.1; 89 1.5; 95 0.8; 102 0.1; 109 -0.3; 117 -0.7; 125 -1.1; 134 -1.4; 143 -1.6; 153 -1.7; 164 -1.8; 175 -2.0; 188 -2.2; 201 -2.4; 215 -2.4; 230 -2.3; 246 -2.4; 263 -2.4; 282 -2.4; 301 -2.4; 323 -2.3; 345 -2.2; 369 -2.2; 395 -2.1; 423 -1.8; 452 -1.5; 484 -1.2; 518 -1.2; 554 -0.9; 593 -0.3; 635 0.1; 679 0.4; 726 0.9; 777 1.1; 832 0.8; 890 0.5; 952 0.4; 1019 -0.0; 1090 0.2; 1167 0.4; 1248 0.6; 1336 0.6; 1429 0.4; 1529 0.1; 1636 -0.5; 1751 -1.0; 1873 -1.6; 2004 -2.3; 2145 -2.4; 2295 -2.1; 2455 -1.9; 2627 -1.1; 2811 0.0; 3008 1.6; 3219 2.7; 3444 2.7; 3685 2.0; 3943 1.0; 4219 -0.2; 4514 -0.9; 4830 -0.9; 5168 -1.0; 5530 -2.2; 5917 -4.1; 6331 -4.1; 6775 -2.1; 7249 -1.8; 7756 -1.8; 8299 -1.9; 8880 -2.0; 9502 -1.6; 10167 -0.2; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -0.3; 20000 -1.3
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K701 sample A ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.4dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.3  | 6.4 dB  |
| Peaking | 217 Hz  | 0.79 | -3.0 dB |
| Peaking | 2229 Hz | 3.26 | -2.9 dB |
| Peaking | 3369 Hz | 3.39 | 3.7 dB  |
| Peaking | 6255 Hz | 2.09 | -3.7 dB |
| Peaking | 127 Hz  | 5.71 | -0.6 dB |
| Peaking | 413 Hz  | 2.6  | -0.8 dB |
| Peaking | 771 Hz  | 3.21 | 1.6 dB  |
| Peaking | 1302 Hz | 5.04 | 0.9 dB  |
| Peaking | 8976 Hz | 8.07 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K701%20sample%20A/AKG%20K701%20sample%20A.png)