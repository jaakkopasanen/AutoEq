# AKG K267 Tiesto Stage Setting

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -2.4; 22 -2.6; 23 -2.7; 25 -2.8; 26 -2.9; 28 -2.9; 30 -3.0; 32 -3.0; 35 -2.9; 37 -2.9; 40 -2.9; 42 -2.8; 45 -2.6; 49 -2.4; 52 -2.3; 56 -2.1; 59 -2.1; 64 -2.0; 68 -1.9; 73 -1.7; 78 -1.3; 83 -1.2; 89 -1.5; 95 -2.0; 102 -2.6; 109 -2.9; 117 -3.3; 125 -3.5; 134 -3.6; 143 -3.6; 153 -3.4; 164 -2.7; 175 -3.0; 188 -3.1; 201 -2.8; 215 -2.7; 230 -2.6; 246 -2.3; 263 -1.9; 282 -1.0; 301 -0.1; 323 1.2; 345 2.5; 369 2.7; 395 2.2; 423 1.7; 452 1.2; 484 0.7; 518 0.4; 554 0.5; 593 0.5; 635 0.4; 679 0.2; 726 0.2; 777 0.4; 832 0.3; 890 0.1; 952 -0.0; 1019 -0.2; 1090 -0.3; 1167 -0.4; 1248 -1.0; 1336 -2.3; 1429 -3.5; 1529 -4.1; 1636 -3.8; 1751 -2.8; 1873 -2.2; 2004 -1.5; 2145 -0.9; 2295 -0.1; 2455 1.2; 2627 1.4; 2811 1.5; 3008 2.2; 3219 2.3; 3444 2.7; 3685 3.5; 3943 5.0; 4219 6.0; 4514 6.0; 4830 5.8; 5168 2.8; 5530 3.9; 5917 5.8; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -1.2; 9502 -1.2; 10167 -0.1; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.0999931827283485dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K267 Tiesto Stage Setting ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.4dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.7  | -3.0 dB |
| Peaking | 145 Hz  | 1.47 | -3.6 dB |
| Peaking | 1580 Hz | 3.41 | -4.6 dB |
| Peaking | 4281 Hz | 2.28 | 6.0 dB  |
| Peaking | 6200 Hz | 5.73 | 5.0 dB  |
| Peaking | 255 Hz  | 2.41 | -2.4 dB |
| Peaking | 358 Hz  | 2.15 | 3.6 dB  |
| Peaking | 2147 Hz | 4    | -1.2 dB |
| Peaking | 2506 Hz | 3.68 | 1.4 dB  |
| Peaking | 9122 Hz | 5.37 | -1.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K267%20Tiesto%20Stage%20Setting/AKG%20K267%20Tiesto%20Stage%20Setting.png)