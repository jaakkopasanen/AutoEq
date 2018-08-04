# Grado SR60

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 10 -84; 20 5.5; 22 4.3; 23 3.7; 25 2.7; 26 2.3; 28 1.5; 30 0.8; 32 0.1; 35 -0.7; 37 -1.2; 40 -1.9; 42 -2.3; 45 -2.8; 49 -3.3; 52 -3.6; 56 -3.9; 59 -4.2; 64 -4.4; 68 -4.2; 73 -4.3; 78 -4.5; 83 -4.6; 89 -4.6; 95 -4.5; 102 -4.4; 109 -4.3; 117 -4.1; 125 -3.9; 134 -3.5; 143 -3.1; 153 -2.9; 164 -2.9; 175 -2.8; 188 -2.6; 201 -2.3; 215 -1.9; 230 -2.3; 246 -2.9; 263 -2.9; 282 -2.6; 301 -2.4; 323 -2.1; 345 -2.0; 369 -1.8; 395 -1.5; 423 -1.2; 452 -1.0; 484 -0.7; 518 -0.4; 554 -0.2; 593 -0.1; 635 0.2; 679 0.3; 726 0.4; 777 0.4; 832 0.3; 890 0.2; 952 0.1; 1019 -0.1; 1090 -0.2; 1167 -0.2; 1248 -0.2; 1336 -0.0; 1429 -0.0; 1529 -0.1; 1636 -0.6; 1751 -1.3; 1873 -1.8; 2004 -2.3; 2145 -2.6; 2295 -2.8; 2455 -2.6; 2627 -2.1; 2811 -0.8; 3008 0.9; 3219 2.2; 3444 2.8; 3685 3.6; 3943 2.6; 4219 1.6; 4514 -1.3; 4830 -2.0; 5168 1.0; 5530 1.0; 5917 1.5; 6331 1.6; 6775 -0.7; 7249 -3.1; 7756 -4.9; 8299 -6.5; 8880 -6.4; 9502 -2.9; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.0dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR60 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 20 Hz    |  0.89 | 8.2 dB  |
| Peaking | 61 Hz    |  0.31 | -5.3 dB |
| Peaking | 2317 Hz  |  2.64 | -3.4 dB |
| Peaking | 3552 Hz  |  3.47 | 4.2 dB  |
| Peaking | 8447 Hz  |  4.67 | -7.6 dB |
| Peaking | 311 Hz   |  2.85 | -1.0 dB |
| Peaking | 718 Hz   |  1.92 | 0.9 dB  |
| Peaking | 4695 Hz  | 13.79 | -3.6 dB |
| Peaking | 6028 Hz  |  6.33 | 2.5 dB  |
| Peaking | 10299 Hz |  9.25 | 1.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Grado%20SR60/Grado%20SR60.png)