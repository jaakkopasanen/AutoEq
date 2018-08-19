# AKG K550

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.0dB
GraphicEQ: 10 -84; 20 -0.7; 22 -1.0; 23 -1.1; 25 -1.2; 26 -1.3; 28 -1.4; 30 -1.5; 32 -1.5; 35 -1.6; 37 -1.5; 40 -1.5; 42 -1.4; 45 -1.2; 49 -1.0; 52 -0.9; 56 -0.9; 59 -0.8; 64 -0.3; 68 0.2; 73 0.6; 78 0.8; 83 0.8; 89 0.3; 95 -0.6; 102 -1.6; 109 -2.2; 117 -2.6; 125 -2.8; 134 -2.7; 143 -2.5; 153 -2.0; 164 -0.3; 175 -1.2; 188 -1.8; 201 -1.5; 215 -1.3; 230 -1.2; 246 -1.1; 263 -1.1; 282 -0.9; 301 -0.8; 323 -0.9; 345 -0.8; 369 -0.6; 395 -0.4; 423 -0.2; 452 0.2; 484 0.1; 518 0.3; 554 0.7; 593 1.1; 635 1.2; 679 1.3; 726 1.5; 777 1.7; 832 1.2; 890 0.6; 952 0.3; 1019 -0.1; 1090 -0.6; 1167 -1.0; 1248 -1.4; 1336 -1.7; 1429 -1.8; 1529 -1.9; 1636 -1.8; 1751 -1.3; 1873 -0.7; 2004 -0.3; 2145 -0.1; 2295 -0.0; 2455 0.3; 2627 0.6; 2811 1.0; 3008 1.8; 3219 2.6; 3444 3.3; 3685 3.8; 3943 3.8; 4219 3.6; 4514 3.5; 4830 3.3; 5168 1.1; 5530 -0.5; 5917 -0.7; 6331 -0.2; 6775 1.4; 7249 1.5; 7756 -1.3; 8299 -4.9; 8880 -7.1; 9502 -5.8; 10167 -1.8; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -0.4; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.025585278340339dB` and instead set Global volume in the UI for both channels to **-40**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K550 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.3dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 1.75 | -1.8 dB |
| Peaking | 133 Hz  | 2.06 | -2.7 dB |
| Peaking | 1526 Hz | 2.9  | -2.3 dB |
| Peaking | 3940 Hz | 2.08 | 4.3 dB  |
| Peaking | 8968 Hz | 5.27 | -8.2 dB |
| Peaking | 80 Hz   | 5.03 | 1.7 dB  |
| Peaking | 271 Hz  | 1.57 | -0.9 dB |
| Peaking | 710 Hz  | 2.59 | 1.8 dB  |
| Peaking | 5763 Hz | 7.27 | -1.9 dB |
| Peaking | 7043 Hz | 9.26 | 2.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K550/AKG%20K550.png)