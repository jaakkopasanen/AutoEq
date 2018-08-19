# AKG K271 MKII

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 5.9; 40 5.5; 42 5.1; 45 4.6; 49 4.0; 52 3.5; 56 3.1; 59 2.9; 64 2.9; 68 3.1; 73 3.8; 78 4.6; 83 5.3; 89 5.9; 95 5.9; 102 4.2; 109 2.8; 117 2.4; 125 2.2; 134 1.4; 143 0.9; 153 1.2; 164 2.0; 175 1.3; 188 1.2; 201 1.3; 215 1.0; 230 0.3; 246 -0.2; 263 -0.4; 282 -0.5; 301 -0.6; 323 -0.7; 345 -0.7; 369 -0.7; 395 -0.9; 423 -0.9; 452 -0.9; 484 -1.2; 518 -1.5; 554 -1.6; 593 -1.9; 635 -2.6; 679 -2.3; 726 0.1; 777 1.3; 832 0.9; 890 0.7; 952 0.5; 1019 -0.1; 1090 -0.4; 1167 -0.6; 1248 -0.9; 1336 -1.4; 1429 -2.0; 1529 -2.7; 1636 -3.2; 1751 -3.1; 1873 -2.2; 2004 0.0; 2145 1.2; 2295 0.7; 2455 2.1; 2627 2.2; 2811 2.2; 3008 3.0; 3219 3.5; 3444 4.3; 3685 5.0; 3943 4.7; 4219 3.2; 4514 2.8; 4830 4.4; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 -0.6; 8299 -4.5; 8880 -7.1; 9502 -7.5; 10167 -5.1; 10879 -0.6; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K271 MKII ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.73 | 6.4 dB  |
| Peaking | 92 Hz   | 2.78 | 4.9 dB  |
| Peaking | 3531 Hz | 3.14 | 4.1 dB  |
| Peaking | 5882 Hz | 2.15 | 6.9 dB  |
| Peaking | 9123 Hz | 3.59 | -9.6 dB |
| Peaking | 175 Hz  | 4.11 | 1.1 dB  |
| Peaking | 677 Hz  | 1.61 | -4.4 dB |
| Peaking | 791 Hz  | 2.74 | 4.8 dB  |
| Peaking | 1715 Hz | 2.59 | -4.7 dB |
| Peaking | 2160 Hz | 2.04 | 2.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K271%20MKII/AKG%20K271%20MKII.png)