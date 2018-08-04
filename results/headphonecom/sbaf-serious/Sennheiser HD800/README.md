# Sennheiser HD800

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.9dB
GraphicEQ: 10 -84; 20 0.6; 22 0.2; 23 0.0; 25 -0.3; 26 -0.5; 28 -0.8; 30 -1.0; 32 -1.2; 35 -1.5; 37 -1.5; 40 -1.5; 42 -1.4; 45 -1.0; 49 -1.0; 52 -1.4; 56 -1.8; 59 -1.9; 64 -2.2; 68 -2.6; 73 -3.0; 78 -3.2; 83 -3.3; 89 -3.4; 95 -3.3; 102 -3.1; 109 -3.2; 117 -3.1; 125 -3.1; 134 -3.1; 143 -3.3; 153 -3.2; 164 -3.0; 175 -3.0; 188 -3.1; 201 -3.1; 215 -3.0; 230 -2.9; 246 -2.9; 263 -2.9; 282 -2.6; 301 -2.4; 323 -2.3; 345 -2.1; 369 -2.0; 395 -2.0; 423 -1.8; 452 -1.6; 484 -1.5; 518 -1.5; 554 -1.2; 593 -0.9; 635 -0.8; 679 -0.8; 726 -0.7; 777 -0.4; 832 -0.4; 890 -0.4; 952 -0.1; 1019 0.0; 1090 0.5; 1167 1.0; 1248 1.4; 1336 1.9; 1429 1.9; 1529 1.6; 1636 1.3; 1751 1.6; 1873 1.9; 2004 1.8; 2145 1.9; 2295 2.5; 2455 3.3; 2627 3.1; 2811 3.1; 3008 2.9; 3219 2.3; 3444 2.4; 3685 1.2; 3943 -0.3; 4219 -1.3; 4514 -1.3; 4830 -1.1; 5168 -2.0; 5530 -4.8; 5917 -8.5; 6331 -5.9; 6775 -1.5; 7249 0.5; 7756 0.3; 8299 0.0; 8880 -0.8; 9502 -1.8; 10167 -0.3; 10879 0.0; 11640 0.0; 12455 -0.2; 13327 -3.5; 14260 -5.4; 15258 -5.0; 16326 -2.9; 17469 -0.4; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.9dB` and instead set Global volume in the UI for both channels to **-39**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD800 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 253 Hz   |  0.26 | -5.8 dB |
| Peaking | 570 Hz   |  0.24 | 3.6 dB  |
| Peaking | 2696 Hz  |  2.46 | 2.5 dB  |
| Peaking | 5898 Hz  |  5.69 | -9.3 dB |
| Peaking | 33304 Hz |  2.91 | -6.1 dB |
| Peaking | 17 Hz    |  1.87 | 1.5 dB  |
| Peaking | 3444 Hz  |  5.57 | 1.1 dB  |
| Peaking | 4203 Hz  |  5.88 | -2.0 dB |
| Peaking | 7399 Hz  |  6.31 | 1.6 dB  |
| Peaking | 9375 Hz  | 11.22 | -1.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD800/Sennheiser%20HD800.png)