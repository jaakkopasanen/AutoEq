# VSonic GR07

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 4.2; 22 3.8; 23 3.6; 25 3.3; 26 3.1; 28 2.9; 30 2.7; 32 2.5; 35 2.3; 37 2.2; 40 2.0; 42 1.9; 45 1.8; 49 1.7; 52 1.7; 56 1.7; 59 1.7; 64 1.5; 68 1.4; 73 1.4; 78 1.2; 83 1.0; 89 0.7; 95 0.2; 102 -0.2; 109 -0.7; 117 -1.2; 125 -1.7; 134 -2.1; 143 -2.3; 153 -2.6; 164 -2.6; 175 -2.6; 188 -2.6; 201 -2.6; 215 -2.4; 230 -2.3; 246 -2.3; 263 -2.2; 282 -2.0; 301 -1.9; 323 -1.8; 345 -1.6; 369 -1.5; 395 -1.4; 423 -1.1; 452 -0.9; 484 -1.0; 518 -0.8; 554 -0.6; 593 -0.2; 635 -0.1; 679 -0.1; 726 0.1; 777 0.3; 832 0.3; 890 0.2; 952 0.1; 1019 0.0; 1090 -0.1; 1167 -0.2; 1248 -0.2; 1336 -0.5; 1429 -0.7; 1529 -0.9; 1636 -0.9; 1751 -0.5; 1873 -0.5; 2004 -0.5; 2145 -0.0; 2295 0.5; 2455 1.4; 2627 2.2; 2811 3.0; 3008 4.4; 3219 5.5; 3444 6.0; 3685 6.0; 3943 5.7; 4219 4.0; 4514 2.2; 4830 1.1; 5168 0.4; 5530 -0.2; 5917 -0.5; 6331 0.8; 6775 2.4; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.4; 9502 -0.2; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `VSonic GR07 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 14 Hz   | 0.52 | 4.5 dB  |
| Peaking | 80 Hz   | 0.95 | 2.7 dB  |
| Peaking | 155 Hz  | 0.61 | -3.6 dB |
| Peaking | 3535 Hz | 2.7  | 6.8 dB  |
| Peaking | 9674 Hz | 2.46 | -0.2 dB |
| Peaking | 814 Hz  | 2.27 | 0.8 dB  |
| Peaking | 1782 Hz | 1.48 | -1.2 dB |
| Peaking | 2790 Hz | 3.22 | 1.0 dB  |
| Peaking | 5785 Hz | 4.49 | -1.5 dB |
| Peaking | 6843 Hz | 7.58 | 2.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/VSonic%20GR07/VSonic%20GR07.png)