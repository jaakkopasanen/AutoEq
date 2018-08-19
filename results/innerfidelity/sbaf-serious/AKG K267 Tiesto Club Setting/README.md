# AKG K267 Tiesto Club Setting

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 1.5; 22 1.4; 23 1.4; 25 1.4; 26 1.5; 28 1.5; 30 1.5; 32 1.6; 35 1.7; 37 1.8; 40 1.9; 42 2.0; 45 2.2; 49 2.4; 52 2.5; 56 2.6; 59 2.7; 64 2.8; 68 2.9; 73 3.1; 78 3.0; 83 2.7; 89 1.9; 95 1.2; 102 1.0; 109 0.8; 117 0.3; 125 -0.2; 134 -0.4; 143 -0.4; 153 -0.2; 164 0.4; 175 0.0; 188 -0.1; 201 -0.1; 215 -0.0; 230 0.2; 246 0.5; 263 0.9; 282 1.6; 301 2.5; 323 3.4; 345 3.4; 369 3.0; 395 2.2; 423 1.6; 452 1.1; 484 0.7; 518 0.5; 554 0.7; 593 0.8; 635 0.7; 679 0.7; 726 0.5; 777 0.7; 832 0.6; 890 0.4; 952 0.2; 1019 -0.2; 1090 -0.5; 1167 -0.9; 1248 -1.7; 1336 -3.0; 1429 -3.8; 1529 -3.4; 1636 -2.6; 1751 -1.6; 1873 -0.8; 2004 -0.2; 2145 0.3; 2295 1.0; 2455 2.1; 2627 2.3; 2811 2.2; 3008 2.9; 3219 3.0; 3444 3.5; 3685 4.4; 3943 5.8; 4219 6.0; 4514 6.0; 4830 6.0; 5168 4.2; 5530 5.1; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.0; 8880 -1.5; 9502 -1.3; 10167 -0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099997016566144dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K267 Tiesto Club Setting ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 58 Hz   | 1.21 | 3.1 dB  |
| Peaking | 344 Hz  | 3.07 | 3.6 dB  |
| Peaking | 1475 Hz | 3.61 | -4.4 dB |
| Peaking | 4195 Hz | 1.73 | 6.0 dB  |
| Peaking | 6114 Hz | 5.35 | 4.4 dB  |
| Peaking | 26 Hz   | 0.58 | 1.5 dB  |
| Peaking | 74 Hz   | 0.69 | -2.2 dB |
| Peaking | 80 Hz   | 2.1  | 2.7 dB  |
| Peaking | 707 Hz  | 1.83 | 0.7 dB  |
| Peaking | 9029 Hz | 5.24 | -2.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K267%20Tiesto%20Club%20Setting/AKG%20K267%20Tiesto%20Club%20Setting.png)