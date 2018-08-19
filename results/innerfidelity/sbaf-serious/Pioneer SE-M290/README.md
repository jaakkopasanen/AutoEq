# Pioneer SE-M290

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 5.8; 26 5.6; 28 5.1; 30 4.4; 32 3.7; 35 2.7; 37 2.2; 40 1.4; 42 1.0; 45 0.5; 49 -0.1; 52 -0.5; 56 -0.8; 59 -1.1; 64 -1.6; 68 -1.6; 73 -0.6; 78 0.4; 83 -0.1; 89 -1.4; 95 -2.5; 102 -2.9; 109 -3.1; 117 -3.3; 125 -3.6; 134 -3.7; 143 -3.8; 153 -3.8; 164 -3.4; 175 -3.6; 188 -3.7; 201 -3.7; 215 -3.7; 230 -3.4; 246 -3.2; 263 -2.9; 282 -2.5; 301 -2.5; 323 -2.4; 345 -2.0; 369 -1.7; 395 -1.3; 423 -0.8; 452 -0.5; 484 -0.3; 518 -0.2; 554 -0.1; 593 -0.1; 635 -0.3; 679 -0.5; 726 -0.9; 777 -1.1; 832 -1.1; 890 -0.7; 952 -0.3; 1019 0.2; 1090 0.8; 1167 1.8; 1248 3.1; 1336 4.1; 1429 4.6; 1529 5.3; 1636 5.9; 1751 6.0; 1873 6.0; 2004 6.0; 2145 6.0; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 4.6; 5530 5.8; 5917 5.2; 6331 5.2; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pioneer SE-M290 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.68 | 6.4 dB  |
| Peaking | 51 Hz   | 2.04 | -1.9 dB |
| Peaking | 171 Hz  | 0.63 | -4.3 dB |
| Peaking | 892 Hz  | 1.89 | -3.7 dB |
| Peaking | 2495 Hz | 0.46 | 6.9 dB  |
| Peaking | 114 Hz  | 6    | -0.5 dB |
| Peaking | 1619 Hz | 4.65 | 0.9 dB  |
| Peaking | 2582 Hz | 2.1  | -0.9 dB |
| Peaking | 6407 Hz | 1.62 | 6.0 dB  |
| Peaking | 7534 Hz | 1.41 | -5.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Pioneer%20SE-M290/Pioneer%20SE-M290.png)