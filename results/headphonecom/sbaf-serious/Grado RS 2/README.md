# Grado RS 2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 5.8; 30 5.2; 32 4.6; 35 3.5; 37 2.9; 40 2.0; 42 1.5; 45 0.7; 49 -0.2; 52 -0.7; 56 -1.5; 59 -1.9; 64 -2.3; 68 -2.6; 73 -3.3; 78 -3.6; 83 -3.8; 89 -4.0; 95 -4.1; 102 -4.1; 109 -3.9; 117 -3.7; 125 -3.5; 134 -3.3; 143 -3.0; 153 -2.8; 164 -2.5; 175 -2.1; 188 -1.8; 201 -1.9; 215 -1.9; 230 -1.7; 246 -1.5; 263 -1.2; 282 -0.8; 301 -0.6; 323 -0.7; 345 -0.8; 369 -0.6; 395 -0.4; 423 -0.2; 452 -0.1; 484 -0.2; 518 -0.1; 554 0.1; 593 0.4; 635 0.6; 679 0.4; 726 0.4; 777 0.5; 832 0.4; 890 0.3; 952 0.2; 1019 0.0; 1090 -0.1; 1167 -0.3; 1248 -0.5; 1336 -1.0; 1429 -1.7; 1529 -2.4; 1636 -3.2; 1751 -3.8; 1873 -5.4; 2004 -7.8; 2145 -8.5; 2295 -7.4; 2455 -5.9; 2627 -4.8; 2811 -3.6; 3008 -2.1; 3219 -1.2; 3444 -1.3; 3685 -4.7; 3943 -8.0; 4219 -7.1; 4514 -5.3; 4830 -3.3; 5168 -3.1; 5530 -4.3; 5917 -3.7; 6331 -5.2; 6775 -6.7; 7249 -6.3; 7756 -5.3; 8299 -6.0; 8880 -8.7; 9502 -10.8; 10167 -9.5; 10879 -5.2; 11640 -0.6; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado RS 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 25 Hz    |  0.92 | 7.0 dB  |
| Peaking | 90 Hz    |  0.71 | -4.8 dB |
| Peaking | 2137 Hz  |  2.96 | -8.5 dB |
| Peaking | 4119 Hz  |  4.18 | -6.7 dB |
| Peaking | 9120 Hz  |  1.98 | -9.8 dB |
| Peaking | 749 Hz   |  1.81 | 0.9 dB  |
| Peaking | 3338 Hz  | 10.85 | 2.4 dB  |
| Peaking | 6645 Hz  |  6.11 | -3.2 dB |
| Peaking | 13650 Hz |  3.18 | 1.6 dB  |
| Peaking | 11912 Hz |  8.35 | 3.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20RS%202/Grado%20RS%202.png)