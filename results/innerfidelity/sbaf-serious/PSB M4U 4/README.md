# PSB M4U 4

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -1.0; 22 -1.3; 23 -1.4; 25 -1.7; 26 -1.8; 28 -1.9; 30 -2.0; 32 -2.0; 35 -2.1; 37 -2.1; 40 -2.0; 42 -2.0; 45 -1.9; 49 -1.7; 52 -1.6; 56 -1.4; 59 -1.3; 64 -1.1; 68 -1.0; 73 -0.9; 78 -0.8; 83 -0.8; 89 -0.9; 95 -1.0; 102 -1.3; 109 -1.4; 117 -1.7; 125 -2.0; 134 -2.1; 143 -2.2; 153 -2.1; 164 -2.0; 175 -1.8; 188 -1.5; 201 -1.3; 215 -1.0; 230 -0.7; 246 -0.5; 263 -0.3; 282 -0.0; 301 0.2; 323 0.4; 345 0.6; 369 0.7; 395 0.8; 423 1.1; 452 1.2; 484 1.2; 518 1.2; 554 1.3; 593 1.5; 635 1.5; 679 1.3; 726 1.2; 777 1.2; 832 1.0; 890 0.6; 952 0.3; 1019 -0.1; 1090 -0.3; 1167 -0.7; 1248 -0.6; 1336 -0.9; 1429 -1.2; 1529 -1.7; 1636 -1.8; 1751 -1.9; 1873 -1.8; 2004 -1.6; 2145 -1.5; 2295 -1.4; 2455 -0.9; 2627 -0.4; 2811 0.1; 3008 0.8; 3219 1.2; 3444 1.4; 3685 1.7; 3943 2.1; 4219 1.4; 4514 1.8; 4830 3.7; 5168 5.9; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `PSB M4U 4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.88 | -2.1 dB |
| Peaking | 146 Hz  | 2.03 | -2.2 dB |
| Peaking | 1877 Hz | 2.11 | -2.2 dB |
| Peaking | 3490 Hz | 3.16 | 1.2 dB  |
| Peaking | 5685 Hz | 2.9  | 6.8 dB  |
| Peaking | 213 Hz  | 2.14 | -0.7 dB |
| Peaking | 687 Hz  | 0.71 | 1.9 dB  |
| Peaking | 1185 Hz | 1.3  | -1.4 dB |
| Peaking | 6595 Hz | 7.76 | 2.3 dB  |
| Peaking | 7626 Hz | 2.19 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/PSB%20M4U%204/PSB%20M4U%204.png)