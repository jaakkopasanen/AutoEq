# Grado RS1e Yellow Pads

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 5.9; 40 5.5; 42 5.0; 45 4.3; 49 3.4; 52 2.8; 56 2.1; 59 1.6; 64 0.8; 68 0.2; 73 -0.4; 78 -0.9; 83 -1.4; 89 -1.8; 95 -2.2; 102 -2.5; 109 -2.7; 117 -2.8; 125 -3.0; 134 -3.2; 143 -3.2; 153 -3.2; 164 -3.2; 175 -3.0; 188 -2.9; 201 -2.8; 215 -2.4; 230 -2.1; 246 -2.0; 263 -1.6; 282 -1.9; 301 -2.2; 323 -1.9; 345 -1.6; 369 -1.4; 395 -1.1; 423 -0.8; 452 -0.6; 484 -0.5; 518 -0.5; 554 -0.2; 593 0.1; 635 0.1; 679 0.1; 726 0.2; 777 0.4; 832 0.3; 890 0.2; 952 0.1; 1019 0.0; 1090 -0.0; 1167 -0.0; 1248 -0.1; 1336 -0.3; 1429 -0.2; 1529 0.5; 1636 -0.1; 1751 -4.7; 1873 -7.8; 2004 -7.1; 2145 -5.2; 2295 -2.9; 2455 -0.3; 2627 1.8; 2811 3.6; 3008 5.1; 3219 5.9; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado RS1e Yellow Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 32 Hz   |  0.49 | 7.6 dB   |
| Peaking | 88 Hz   |  0.63 | -4.3 dB  |
| Peaking | 182 Hz  |  0.78 | -1.8 dB  |
| Peaking | 1991 Hz |  3.77 | -10.4 dB |
| Peaking | 4012 Hz |  0.97 | 7.2 dB   |
| Peaking | 1581 Hz | 13.03 | 2.3 dB   |
| Peaking | 4277 Hz |  5.08 | -1.2 dB  |
| Peaking | 6484 Hz |  2.56 | 4.1 dB   |
| Peaking | 7358 Hz |  3.03 | -3.1 dB  |
| Peaking | 9125 Hz |  1.11 | -1.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20RS1e%20Yellow%20Pads/Grado%20RS1e%20Yellow%20Pads.png)