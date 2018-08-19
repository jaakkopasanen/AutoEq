# Teac CT-H02

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 0.5; 22 0.4; 23 0.4; 25 0.3; 26 0.3; 28 0.2; 30 0.1; 32 0.1; 35 0.1; 37 0.1; 40 0.0; 42 0.0; 45 0.0; 49 0.0; 52 0.1; 56 -0.0; 59 -0.1; 64 -0.2; 68 -0.4; 73 -0.5; 78 -0.7; 83 -0.7; 89 -0.6; 95 -0.4; 102 -0.9; 109 -1.2; 117 -1.2; 125 -0.9; 134 0.1; 143 0.0; 153 -1.3; 164 -1.2; 175 -0.6; 188 -1.8; 201 -2.3; 215 -2.5; 230 -2.6; 246 -2.6; 263 -2.4; 282 -2.2; 301 -2.2; 323 -2.0; 345 -1.9; 369 -1.8; 395 -1.5; 423 -1.4; 452 -1.3; 484 -1.3; 518 -1.5; 554 -1.5; 593 -1.5; 635 -1.5; 679 -1.5; 726 -1.3; 777 -1.2; 832 -1.1; 890 -0.7; 952 -0.3; 1019 0.0; 1090 -0.2; 1167 -0.6; 1248 -0.6; 1336 -0.8; 1429 -0.8; 1529 -1.1; 1636 -1.0; 1751 -0.5; 1873 0.3; 2004 1.5; 2145 2.0; 2295 2.9; 2455 4.0; 2627 4.9; 2811 5.8; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 5.5; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 -1.7; 8299 -5.7; 8880 -7.9; 9502 -7.2; 10167 -3.8; 10879 -0.2; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999678133dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Teac CT-H02 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 342 Hz  |  0.48 | -2.2 dB  |
| Peaking | 1441 Hz |  1.98 | -1.8 dB  |
| Peaking | 1754 Hz |  3.04 | -2.2 dB  |
| Peaking | 4651 Hz |  0.51 | 7.5 dB   |
| Peaking | 8942 Hz |  2.84 | -13.1 dB |
| Peaking | 140 Hz  | 10.47 | 1.6 dB   |
| Peaking | 225 Hz  |  5.07 | -0.9 dB  |
| Peaking | 2905 Hz |  3.83 | 1.4 dB   |
| Peaking | 5093 Hz |  0.82 | -1.1 dB  |
| Peaking | 6232 Hz |  3.56 | 2.3 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Teac%20CT-H02/Teac%20CT-H02.png)