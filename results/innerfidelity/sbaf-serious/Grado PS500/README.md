# Grado PS500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 5.8; 35 5.1; 37 4.4; 40 3.5; 42 2.9; 45 2.0; 49 1.0; 52 0.2; 56 -0.7; 59 -1.3; 64 -2.2; 68 -2.9; 73 -3.6; 78 -4.1; 83 -4.6; 89 -5.0; 95 -5.3; 102 -5.5; 109 -5.3; 117 -5.2; 125 -5.0; 134 -4.8; 143 -4.5; 153 -4.2; 164 -3.8; 175 -3.2; 188 -2.9; 201 -3.1; 215 -2.7; 230 -2.3; 246 -2.0; 263 -1.7; 282 -1.4; 301 -1.1; 323 -0.8; 345 -0.6; 369 -0.3; 395 -0.1; 423 0.1; 452 0.2; 484 0.2; 518 0.3; 554 0.5; 593 0.8; 635 0.8; 679 0.6; 726 0.6; 777 0.8; 832 0.6; 890 0.3; 952 0.2; 1019 -0.0; 1090 -0.3; 1167 -0.6; 1248 -0.9; 1336 -1.6; 1429 -2.3; 1529 -3.1; 1636 -3.7; 1751 -4.1; 1873 -4.6; 2004 -6.0; 2145 -6.3; 2295 -4.8; 2455 -2.1; 2627 0.2; 2811 1.9; 3008 3.7; 3219 4.4; 3444 3.3; 3685 1.7; 3943 1.3; 4219 2.6; 4514 2.4; 4830 4.1; 5168 5.8; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.5; 8880 -3.4; 9502 -4.0; 10167 -1.3; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado PS500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.81 | 7.3 dB  |
| Peaking | 101 Hz  | 0.79 | -6.5 dB |
| Peaking | 2078 Hz | 2.28 | -7.3 dB |
| Peaking | 3071 Hz | 3.09 | 5.6 dB  |
| Peaking | 5636 Hz | 3.19 | 6.9 dB  |
| Peaking | 671 Hz  | 1.31 | 1.2 dB  |
| Peaking | 1515 Hz | 5.82 | -1.2 dB |
| Peaking | 6531 Hz | 8.26 | 2.0 dB  |
| Peaking | 9210 Hz | 5.5  | -5.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20PS500/Grado%20PS500.png)