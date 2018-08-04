# Sennheiser HD 558

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.7dB
GraphicEQ: 10 -84; 20 5.2; 22 4.4; 23 4.0; 25 3.4; 26 3.1; 28 2.5; 30 2.0; 32 1.6; 35 1.1; 37 0.8; 40 0.3; 42 0.0; 45 -0.4; 49 -0.8; 52 -1.1; 56 -1.4; 59 -1.6; 64 -1.7; 68 -1.8; 73 -1.9; 78 -2.1; 83 -1.4; 89 -0.5; 95 -1.3; 102 -2.2; 109 -2.4; 117 -2.4; 125 -2.4; 134 -2.4; 143 -2.6; 153 -2.6; 164 -2.7; 175 -2.6; 188 -2.6; 201 -2.4; 215 -2.3; 230 -2.4; 246 -2.4; 263 -2.4; 282 -2.3; 301 -2.2; 323 -2.1; 345 -1.7; 369 -1.7; 395 -1.7; 423 -1.3; 452 -1.3; 484 -1.3; 518 -1.2; 554 -0.7; 593 -0.3; 635 -0.4; 679 -0.5; 726 -0.5; 777 0.1; 832 0.2; 890 0.1; 952 0.1; 1019 -0.1; 1090 -0.1; 1167 -0.1; 1248 -0.2; 1336 -0.3; 1429 -0.4; 1529 -0.4; 1636 -0.1; 1751 -0.6; 1873 -1.0; 2004 -1.6; 2145 -2.1; 2295 -1.7; 2455 -1.4; 2627 -2.4; 2811 -3.2; 3008 -3.2; 3219 -3.8; 3444 -3.0; 3685 -2.1; 3943 -1.1; 4219 -2.9; 4514 -4.0; 4830 -3.1; 5168 -1.3; 5530 0.4; 5917 1.6; 6331 2.3; 6775 1.3; 7249 1.1; 7756 0.3; 8299 0.0; 8880 -1.5; 9502 -1.3; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -0.9; 18692 -3.9; 20000 -3.8
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.7dB` and instead set Global volume in the UI for both channels to **-57**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 558 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 20 Hz    |  1.56 | 5.1 dB  |
| Peaking | 158 Hz   |  0.45 | -2.7 dB |
| Peaking | 4619 Hz  |  5.8  | -3.7 dB |
| Peaking | 3014 Hz  |  2.08 | -3.4 dB |
| Peaking | 6249 Hz  |  4.53 | 2.9 dB  |
| Peaking | 72 Hz    |  2.01 | -0.7 dB |
| Peaking | 89 Hz    |  7.06 | 1.8 dB  |
| Peaking | 876 Hz   |  2.5  | 0.7 dB  |
| Peaking | 2086 Hz  | 10.38 | -1.1 dB |
| Peaking | 19371 Hz |  2.36 | -4.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20558/Sennheiser%20HD%20558.png)