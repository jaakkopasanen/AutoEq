# Grado RS2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 5.7; 42 5.3; 45 4.5; 49 3.6; 52 3.0; 56 2.1; 59 1.6; 64 1.1; 68 0.6; 73 -0.2; 78 -0.8; 83 -1.2; 89 -1.6; 95 -1.9; 102 -2.2; 109 -2.3; 117 -2.3; 125 -2.4; 134 -2.3; 143 -2.2; 153 -2.1; 164 -2.0; 175 -1.7; 188 -1.5; 201 -1.7; 215 -1.7; 230 -1.5; 246 -1.3; 263 -1.1; 282 -0.8; 301 -0.5; 323 -0.7; 345 -0.8; 369 -0.6; 395 -0.3; 423 -0.3; 452 -0.2; 484 -0.1; 518 -0.0; 554 0.2; 593 0.3; 635 0.5; 679 0.5; 726 0.5; 777 0.4; 832 0.4; 890 0.3; 952 0.2; 1019 0.0; 1090 -0.1; 1167 -0.3; 1248 -0.5; 1336 -1.0; 1429 -1.7; 1529 -2.5; 1636 -3.2; 1751 -3.7; 1873 -5.4; 2004 -7.8; 2145 -8.4; 2295 -7.3; 2455 -6.0; 2627 -4.8; 2811 -3.5; 3008 -2.2; 3219 -1.2; 3444 -1.2; 3685 -4.6; 3943 -8.2; 4219 -7.1; 4514 -5.1; 4830 -3.2; 5168 -3.2; 5530 -4.4; 5917 -3.7; 6331 -5.1; 6775 -6.8; 7249 -6.4; 7756 -5.3; 8299 -5.8; 8880 -8.6; 9502 -11.0; 10167 -9.7; 10879 -5.0; 11640 -0.4; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado RS2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 31 Hz    |  0.53 | 7.2 dB  |
| Peaking | 99 Hz    |  0.69 | -4.4 dB |
| Peaking | 2137 Hz  |  2.96 | -8.5 dB |
| Peaking | 4125 Hz  |  4.31 | -6.8 dB |
| Peaking | 9130 Hz  |  2    | -9.8 dB |
| Peaking | 755 Hz   |  1.9  | 0.9 dB  |
| Peaking | 3347 Hz  | 10.99 | 2.4 dB  |
| Peaking | 6610 Hz  |  6.34 | -3.4 dB |
| Peaking | 11884 Hz |  8.17 | 3.0 dB  |
| Peaking | 13583 Hz |  3.18 | 1.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20RS2/Grado%20RS2.png)