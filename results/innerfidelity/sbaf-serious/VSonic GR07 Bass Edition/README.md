# VSonic GR07 Bass Edition

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.0dB
GraphicEQ: 10 -84; 20 0.7; 22 0.4; 23 0.3; 25 0.0; 26 -0.1; 28 -0.3; 30 -0.5; 32 -0.6; 35 -0.8; 37 -0.9; 40 -1.1; 42 -1.2; 45 -1.3; 49 -1.5; 52 -1.6; 56 -1.7; 59 -1.8; 64 -2.1; 68 -2.2; 73 -2.4; 78 -2.6; 83 -2.7; 89 -2.9; 95 -3.1; 102 -3.2; 109 -3.2; 117 -3.2; 125 -3.3; 134 -3.2; 143 -3.3; 153 -3.2; 164 -3.2; 175 -3.1; 188 -3.0; 201 -2.9; 215 -2.7; 230 -2.5; 246 -2.4; 263 -2.3; 282 -2.0; 301 -1.9; 323 -1.7; 345 -1.5; 369 -1.4; 395 -1.2; 423 -0.9; 452 -0.7; 484 -0.6; 518 -0.5; 554 -0.2; 593 0.0; 635 0.2; 679 0.1; 726 0.3; 777 0.5; 832 0.4; 890 0.3; 952 0.2; 1019 0.0; 1090 -0.1; 1167 -0.2; 1248 -0.3; 1336 -0.5; 1429 -0.8; 1529 -1.1; 1636 -1.3; 1751 -1.3; 1873 -1.0; 2004 -0.9; 2145 -0.8; 2295 0.0; 2455 0.9; 2627 1.5; 2811 1.6; 3008 2.4; 3219 3.5; 3444 4.6; 3685 4.9; 3943 4.3; 4219 2.6; 4514 0.8; 4830 -0.5; 5168 -1.9; 5530 -3.6; 5917 -2.8; 6331 -0.1; 6775 2.3; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.966976387226952dB` and instead set Global volume in the UI for both channels to **-49**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `VSonic GR07 Bass Edition ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.4dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 108 Hz  | 0.65 | -2.9 dB |
| Peaking | 230 Hz  | 1.12 | -1.3 dB |
| Peaking | 3654 Hz | 3.05 | 5.7 dB  |
| Peaking | 5660 Hz | 3.46 | -4.8 dB |
| Peaking | 6762 Hz | 5.65 | 3.8 dB  |
| Peaking | 15 Hz   | 1.83 | 0.9 dB  |
| Peaking | 376 Hz  | 2.71 | -0.3 dB |
| Peaking | 780 Hz  | 1.54 | 0.8 dB  |
| Peaking | 1862 Hz | 1.51 | -1.8 dB |
| Peaking | 2616 Hz | 2.53 | 1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/VSonic%20GR07%20Bass%20Edition/VSonic%20GR07%20Bass%20Edition.png)