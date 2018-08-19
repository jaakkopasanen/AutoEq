# Grado SR225i TTVJ Flat Pads

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 5.5; 42 5.0; 45 4.0; 49 2.9; 52 2.2; 56 1.4; 59 0.9; 64 0.1; 68 -0.3; 73 -0.7; 78 -1.0; 83 -1.3; 89 -1.6; 95 -1.9; 102 -2.2; 109 -2.2; 117 -2.3; 125 -2.5; 134 -2.4; 143 -2.5; 153 -2.5; 164 -2.5; 175 -2.4; 188 -2.3; 201 -2.4; 215 -2.1; 230 -1.9; 246 -1.7; 263 -1.4; 282 -1.3; 301 -1.3; 323 -1.7; 345 -1.4; 369 -1.3; 395 -1.2; 423 -1.0; 452 -0.9; 484 -0.8; 518 -0.8; 554 -0.5; 593 -0.2; 635 -0.1; 679 -0.2; 726 -0.1; 777 0.1; 832 0.0; 890 -0.1; 952 0.1; 1019 0.0; 1090 0.1; 1167 -0.1; 1248 -0.2; 1336 -0.3; 1429 -0.9; 1529 -1.2; 1636 -1.1; 1751 -0.8; 1873 -1.9; 2004 -4.4; 2145 -5.1; 2295 -2.8; 2455 -0.2; 2627 1.5; 2811 2.9; 3008 3.5; 3219 4.3; 3444 3.9; 3685 3.7; 3943 4.9; 4219 6.0; 4514 6.0; 4830 6.0; 5168 5.1; 5530 5.7; 5917 5.9; 6331 5.1; 6775 2.3; 7249 -0.2; 7756 -1.2; 8299 -1.7; 8880 -2.0; 9502 -1.1; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR225i TTVJ Flat Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 0.62 | 9.1 dB  |
| Peaking | 82 Hz    | 0.36 | -4.4 dB |
| Peaking | 2102 Hz  | 4.07 | -7.1 dB |
| Peaking | 5341 Hz  | 0.8  | 7.8 dB  |
| Peaking | 8171 Hz  | 1.76 | -6.6 dB |
| Peaking | 1491 Hz  | 6.32 | -1.3 dB |
| Peaking | 3170 Hz  | 3.26 | 1.2 dB  |
| Peaking | 3615 Hz  | 8.16 | -1.6 dB |
| Peaking | 10045 Hz | 6.88 | 0.7 dB  |
| Peaking | 13619 Hz | 1.05 | -0.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20SR225i%20TTVJ%20Flat%20Pads/Grado%20SR225i%20TTVJ%20Flat%20Pads.png)