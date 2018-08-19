# AKG K81DJ

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 5.9; 25 5.6; 26 5.4; 28 5.0; 30 4.6; 32 4.3; 35 3.8; 37 3.5; 40 3.1; 42 2.9; 45 2.7; 49 2.4; 52 2.1; 56 1.7; 59 1.3; 64 0.9; 68 0.7; 73 0.6; 78 0.3; 83 -0.1; 89 -0.2; 95 0.2; 102 0.4; 109 -0.4; 117 -1.2; 125 -1.9; 134 -2.5; 143 -2.8; 153 -2.9; 164 -2.5; 175 -2.7; 188 -2.7; 201 -1.9; 215 -1.2; 230 -0.9; 246 -0.5; 263 -0.6; 282 -0.7; 301 -0.5; 323 -0.3; 345 0.6; 369 1.6; 395 2.1; 423 2.3; 452 2.2; 484 2.1; 518 1.9; 554 1.8; 593 1.8; 635 1.5; 679 1.3; 726 0.9; 777 1.0; 832 0.7; 890 0.4; 952 0.2; 1019 -0.0; 1090 -0.2; 1167 -0.3; 1248 -0.4; 1336 -0.8; 1429 -1.3; 1529 -1.8; 1636 -2.2; 1751 -2.4; 1873 -2.5; 2004 -2.0; 2145 -1.8; 2295 -1.1; 2455 0.5; 2627 1.5; 2811 2.4; 3008 3.4; 3219 3.7; 3444 3.5; 3685 3.1; 3943 2.8; 4219 2.2; 4514 2.0; 4830 3.0; 5168 3.8; 5530 1.6; 5917 2.5; 6331 4.6; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 -0.9; 16326 -2.0; 17469 -2.4; 18692 -0.9; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K81DJ ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.0dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 21 Hz    | 0.69 | 6.0 dB   |
| Peaking | 159 Hz   | 1.67 | -3.5 dB  |
| Peaking | 1713 Hz  | 0.98 | -10.8 dB |
| Peaking | 1879 Hz  | 0.44 | 8.1 dB   |
| Peaking | 6474 Hz  | 9.01 | 3.2 dB   |
| Peaking | 432 Hz   | 4.05 | 1.7 dB   |
| Peaking | 918 Hz   | 3.16 | -1.1 dB  |
| Peaking | 3180 Hz  | 5.63 | 1.6 dB   |
| Peaking | 8650 Hz  | 2.95 | -1.3 dB  |
| Peaking | 17098 Hz | 2.23 | -2.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K81DJ/AKG%20K81DJ.png)