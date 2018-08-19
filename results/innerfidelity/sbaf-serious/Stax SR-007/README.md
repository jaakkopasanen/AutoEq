# Stax SR-007

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 5.2; 52 3.7; 56 2.4; 59 2.7; 64 3.4; 68 3.6; 73 3.7; 78 3.8; 83 3.7; 89 3.5; 95 3.4; 102 3.2; 109 3.2; 117 3.2; 125 2.9; 134 2.7; 143 2.6; 153 2.4; 164 2.3; 175 2.3; 188 2.1; 201 2.0; 215 1.9; 230 1.9; 246 1.8; 263 1.7; 282 1.6; 301 1.5; 323 1.4; 345 1.4; 369 1.3; 395 1.2; 423 1.3; 452 1.5; 484 2.0; 518 2.6; 554 2.1; 593 1.5; 635 0.7; 679 0.3; 726 0.4; 777 0.6; 832 0.6; 890 0.4; 952 0.2; 1019 0.2; 1090 1.2; 1167 2.3; 1248 3.9; 1336 1.6; 1429 -0.7; 1529 -0.9; 1636 -0.6; 1751 0.6; 1873 2.2; 2004 3.5; 2145 4.7; 2295 5.1; 2455 5.9; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 5.7; 3685 5.1; 3943 4.6; 4219 3.7; 4514 2.6; 4830 2.0; 5168 2.9; 5530 4.8; 5917 5.0; 6331 5.3; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.3; 8880 -1.7; 9502 -0.9; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -0.0; 20000 -3.6
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-007 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 27 Hz   |  0.68 | 6.0 dB  |
| Peaking | 125 Hz  |  0.5  | 2.3 dB  |
| Peaking | 518 Hz  |  4.32 | 1.9 dB  |
| Peaking | 2927 Hz |  1.49 | 6.6 dB  |
| Peaking | 6076 Hz |  4.45 | 4.9 dB  |
| Peaking | 1256 Hz |  5.58 | 5.7 dB  |
| Peaking | 1464 Hz |  2.14 | -3.9 dB |
| Peaking | 2101 Hz |  3.61 | 2.1 dB  |
| Peaking | 6701 Hz | 10.31 | 1.3 dB  |
| Peaking | 8897 Hz |  4.75 | -2.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-007/Stax%20SR-007.png)