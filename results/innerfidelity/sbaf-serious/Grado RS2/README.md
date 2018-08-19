# Grado RS2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 5.8; 52 5.2; 56 4.2; 59 3.6; 64 2.7; 68 2.2; 73 1.4; 78 0.6; 83 0.0; 89 -0.6; 95 -1.1; 102 -1.5; 109 -1.7; 117 -1.8; 125 -2.0; 134 -2.0; 143 -1.9; 153 -1.9; 164 -1.7; 175 -1.5; 188 -1.3; 201 -1.3; 215 -1.4; 230 -1.2; 246 -1.1; 263 -1.0; 282 -0.6; 301 -0.4; 323 -0.1; 345 -0.4; 369 -0.5; 395 -0.3; 423 -0.1; 452 0.1; 484 -0.1; 518 -0.1; 554 0.1; 593 0.3; 635 0.5; 679 0.4; 726 0.3; 777 0.5; 832 0.4; 890 0.2; 952 0.1; 1019 0.0; 1090 -0.0; 1167 -0.3; 1248 -0.8; 1336 -1.4; 1429 -2.6; 1529 -3.5; 1636 -4.1; 1751 -4.2; 1873 -6.7; 2004 -9.1; 2145 -8.0; 2295 -6.3; 2455 -5.3; 2627 -4.7; 2811 -3.3; 3008 -2.1; 3219 -1.4; 3444 -0.6; 3685 -1.7; 3943 -5.0; 4219 -6.7; 4514 -9.4; 4830 -8.8; 5168 -6.6; 5530 -6.0; 5917 -6.6; 6331 -7.8; 6775 -8.8; 7249 -9.6; 7756 -9.5; 8299 -10.3; 8880 -11.4; 9502 -10.1; 10167 -5.3; 10879 -0.5; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.5; 17469 -1.9; 18692 -1.3; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado RS2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 42 Hz    |  0.37 | 8.0 dB   |
| Peaking | 105 Hz   |  0.72 | -6.6 dB  |
| Peaking | 2051 Hz  |  2.92 | -8.6 dB  |
| Peaking | 4666 Hz  |  3.75 | -7.5 dB  |
| Peaking | 8103 Hz  |  1.92 | -11.2 dB |
| Peaking | 3466 Hz  | 11.14 | 2.5 dB   |
| Peaking | 6499 Hz  |  3.7  | -2.9 dB  |
| Peaking | 9442 Hz  |  4.49 | -9.0 dB  |
| Peaking | 9914 Hz  |  1.4  | 5.8 dB   |
| Peaking | 17835 Hz |  3.05 | -2.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20RS2/Grado%20RS2.png)