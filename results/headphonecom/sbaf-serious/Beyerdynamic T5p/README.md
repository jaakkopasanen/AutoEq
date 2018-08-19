# Beyerdynamic T5p

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -3.6; 22 -3.6; 23 -3.6; 25 -3.6; 26 -3.5; 28 -3.4; 30 -3.3; 32 -3.1; 35 -2.8; 37 -2.5; 40 -2.3; 42 -2.2; 45 -2.2; 49 -1.9; 52 -1.4; 56 -0.8; 59 -0.3; 64 0.5; 68 1.1; 73 1.3; 78 0.6; 83 -0.9; 89 -2.9; 95 -4.0; 102 -3.5; 109 -4.0; 117 -4.3; 125 -4.0; 134 -3.5; 143 -3.1; 153 -2.5; 164 -1.9; 175 -3.2; 188 -2.7; 201 -2.2; 215 -1.8; 230 -1.4; 246 -1.1; 263 -0.8; 282 -0.5; 301 -0.3; 323 -0.2; 345 -0.3; 369 -0.2; 395 -0.3; 423 -0.5; 452 -0.7; 484 -0.9; 518 -0.9; 554 -0.7; 593 1.5; 635 2.5; 679 1.0; 726 0.7; 777 0.6; 832 0.8; 890 1.0; 952 0.7; 1019 -0.3; 1090 -2.0; 1167 -4.1; 1248 -2.9; 1336 -2.1; 1429 -3.3; 1529 -3.3; 1636 -3.3; 1751 -3.4; 1873 -3.4; 2004 -4.9; 2145 -5.5; 2295 -4.7; 2455 -2.0; 2627 0.1; 2811 0.5; 3008 0.6; 3219 -0.4; 3444 -0.7; 3685 -0.6; 3943 -0.5; 4219 0.3; 4514 1.2; 4830 2.8; 5168 5.1; 5530 6.0; 5917 1.4; 6331 0.7; 6775 2.6; 7249 1.3; 7756 0.3; 8299 -0.2; 8880 -1.1; 9502 -0.4; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.093091504264768dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T5p ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.4dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 26 Hz   |  1.41 | -3.9 dB |
| Peaking | 126 Hz  |  1.51 | -4.1 dB |
| Peaking | 1440 Hz |  2.49 | -3.2 dB |
| Peaking | 2134 Hz |  4.96 | -5.4 dB |
| Peaking | 5370 Hz |  5.56 | 6.4 dB  |
| Peaking | 72 Hz   |  6.15 | 2.9 dB  |
| Peaking | 631 Hz  |  6.58 | 3.9 dB  |
| Peaking | 792 Hz  |  1.12 | -2.2 dB |
| Peaking | 861 Hz  |  3.06 | 3.6 dB  |
| Peaking | 6910 Hz | 12.08 | 2.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20T5p/Beyerdynamic%20T5p.png)