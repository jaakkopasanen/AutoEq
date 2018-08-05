# Grado RS2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 5.8; 42 5.4; 45 4.7; 49 3.8; 52 3.2; 56 2.5; 59 2.0; 64 1.6; 68 1.2; 73 0.5; 78 -0.0; 83 -0.4; 89 -0.8; 95 -1.2; 102 -1.6; 109 -1.9; 117 -2.1; 125 -2.4; 134 -2.4; 143 -2.4; 153 -2.4; 164 -2.2; 175 -2.0; 188 -1.7; 201 -1.9; 215 -1.8; 230 -1.6; 246 -1.4; 263 -1.2; 282 -0.8; 301 -0.6; 323 -0.7; 345 -0.8; 369 -0.6; 395 -0.4; 423 -0.2; 452 -0.1; 484 -0.2; 518 -0.1; 554 0.1; 593 0.4; 635 0.6; 679 0.4; 726 0.4; 777 0.5; 832 0.4; 890 0.3; 952 0.2; 1019 0.0; 1090 -0.1; 1167 -0.3; 1248 -0.5; 1336 -1.0; 1429 -1.7; 1529 -2.4; 1636 -3.2; 1751 -3.8; 1873 -5.4; 2004 -7.8; 2145 -8.5; 2295 -7.4; 2455 -5.9; 2627 -4.8; 2811 -3.6; 3008 -2.1; 3219 -1.2; 3444 -1.3; 3685 -4.7; 3943 -8.0; 4219 -7.1; 4514 -5.3; 4830 -3.3; 5168 -3.1; 5530 -4.3; 5917 -3.7; 6331 -5.2; 6775 -6.7; 7249 -6.3; 7756 -5.3; 8299 -6.0; 8880 -8.7; 9502 -10.8; 10167 -9.5; 10879 -5.2; 11640 -0.6; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado RS2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 29 Hz    |  0.62 | 6.7 dB  |
| Peaking | 123 Hz   |  0.8  | -3.4 dB |
| Peaking | 2136 Hz  |  2.97 | -8.5 dB |
| Peaking | 4140 Hz  |  4.05 | -6.6 dB |
| Peaking | 9125 Hz  |  2    | -9.8 dB |
| Peaking | 755 Hz   |  1.86 | 0.9 dB  |
| Peaking | 3342 Hz  | 10.88 | 2.4 dB  |
| Peaking | 6652 Hz  |  6.27 | -3.2 dB |
| Peaking | 13745 Hz |  3.15 | 1.5 dB  |
| Peaking | 11905 Hz |  7.98 | 2.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20RS2/Grado%20RS2.png)