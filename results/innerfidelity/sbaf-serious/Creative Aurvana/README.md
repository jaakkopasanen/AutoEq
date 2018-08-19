# Creative Aurvana

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 3.6; 22 2.9; 23 2.7; 25 2.2; 26 2.0; 28 1.6; 30 1.3; 32 1.0; 35 0.7; 37 0.6; 40 0.4; 42 0.3; 45 0.1; 49 -0.2; 52 -0.4; 56 -0.6; 59 -0.7; 64 -0.8; 68 -0.8; 73 -1.0; 78 -1.4; 83 -1.7; 89 -1.9; 95 -2.1; 102 -2.3; 109 -2.3; 117 -2.3; 125 -2.4; 134 -2.4; 143 -2.4; 153 -2.3; 164 -2.0; 175 -1.9; 188 -1.7; 201 -1.6; 215 -1.4; 230 -1.2; 246 -1.0; 263 -0.9; 282 -0.6; 301 -0.4; 323 -0.1; 345 0.2; 369 0.4; 395 0.6; 423 0.9; 452 1.1; 484 1.1; 518 1.2; 554 1.3; 593 1.4; 635 1.2; 679 0.7; 726 0.3; 777 0.1; 832 0.0; 890 0.4; 952 0.3; 1019 0.1; 1090 0.4; 1167 0.5; 1248 0.7; 1336 0.6; 1429 0.6; 1529 0.5; 1636 0.4; 1751 0.7; 1873 1.1; 2004 1.5; 2145 1.9; 2295 2.1; 2455 2.5; 2627 2.1; 2811 0.6; 3008 0.6; 3219 3.0; 3444 6.0; 3685 4.0; 3943 2.2; 4219 0.5; 4514 0.0; 4830 1.5; 5168 3.9; 5530 5.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.2; 9502 -0.8; 10167 -0.1; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 -0.0; 16326 -0.2; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.108395539903382dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Creative Aurvana ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 1.07 | 4.0 dB  |
| Peaking | 134 Hz  | 0.74 | -3.1 dB |
| Peaking | 578 Hz  | 0.18 | 1.0 dB  |
| Peaking | 3485 Hz | 7.22 | 5.4 dB  |
| Peaking | 5976 Hz | 4.06 | 6.3 dB  |
| Peaking | 530 Hz  | 1.34 | 2.6 dB  |
| Peaking | 613 Hz  | 0.69 | -1.9 dB |
| Peaking | 2437 Hz | 3.31 | 2.1 dB  |
| Peaking | 2892 Hz | 7.19 | -1.9 dB |
| Peaking | 9147 Hz | 3.3  | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Creative%20Aurvana/Creative%20Aurvana.png)