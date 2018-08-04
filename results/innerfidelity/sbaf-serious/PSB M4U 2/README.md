# PSB M4U 2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.9dB
GraphicEQ: 10 -84; 20 3.1; 22 0.9; 23 0.1; 25 -1.1; 26 -1.4; 28 -1.5; 30 -1.3; 32 -0.8; 35 -0.1; 37 0.3; 40 0.8; 42 1.0; 45 1.4; 49 1.8; 52 2.0; 56 2.2; 59 2.3; 64 2.5; 68 2.7; 73 3.0; 78 3.1; 83 3.1; 89 2.7; 95 1.8; 102 0.9; 109 0.5; 117 0.3; 125 0.1; 134 -0.0; 143 -0.2; 153 -0.2; 164 0.3; 175 -0.1; 188 -0.2; 201 0.0; 215 0.3; 230 0.6; 246 0.8; 263 1.1; 282 1.6; 301 2.0; 323 2.2; 345 2.7; 369 2.8; 395 3.0; 423 3.7; 452 3.9; 484 3.6; 518 3.5; 554 3.5; 593 3.4; 635 3.3; 679 3.1; 726 2.7; 777 2.3; 832 1.9; 890 1.2; 952 0.6; 1019 -0.1; 1090 -0.5; 1167 -0.9; 1248 -1.4; 1336 -2.1; 1429 -2.9; 1529 -3.6; 1636 -3.7; 1751 -3.5; 1873 -2.8; 2004 -2.2; 2145 -1.6; 2295 -1.2; 2455 -0.3; 2627 0.4; 2811 0.9; 3008 1.0; 3219 0.5; 3444 0.2; 3685 -0.4; 3943 -0.0; 4219 0.8; 4514 1.0; 4830 1.9; 5168 3.1; 5530 4.5; 5917 5.2; 6331 4.3; 6775 3.6; 7249 1.3; 7756 0.3; 8299 -0.1; 8880 -0.7; 9502 -0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.9dB` and instead set Global volume in the UI for both channels to **-59**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `PSB M4U 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 72 Hz   | 2.08 | 3.3 dB  |
| Peaking | 529 Hz  | 1.04 | 4.1 dB  |
| Peaking | 1617 Hz | 1.72 | -4.3 dB |
| Peaking | 2819 Hz | 4.82 | 1.6 dB  |
| Peaking | 5873 Hz | 3.46 | 5.6 dB  |
| Peaking | 29 Hz   | 2.92 | -2.6 dB |
| Peaking | 47 Hz   | 2.43 | 0.1 dB  |
| Peaking | 30 Hz   | 0.09 | 1.1 dB  |
| Peaking | 143 Hz  | 0.91 | -1.7 dB |
| Peaking | 8658 Hz | 5.84 | -1.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/PSB%20M4U%202/PSB%20M4U%202.png)