# Sennheiser HD 598

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.7dB
GraphicEQ: 10 -84; 20 5.2; 22 4.4; 23 4.1; 25 3.5; 26 3.2; 28 2.7; 30 2.3; 32 1.9; 35 1.4; 37 1.1; 40 0.6; 42 0.4; 45 0.0; 49 -0.4; 52 -0.6; 56 -1.0; 59 -1.1; 64 -0.9; 68 -1.0; 73 -1.5; 78 -1.1; 83 -0.4; 89 -1.0; 95 -1.6; 102 -1.8; 109 -1.9; 117 -1.9; 125 -2.0; 134 -2.2; 143 -2.1; 153 -2.2; 164 -2.2; 175 -2.1; 188 -2.2; 201 -2.2; 215 -2.0; 230 -1.9; 246 -2.0; 263 -2.1; 282 -2.1; 301 -2.0; 323 -1.9; 345 -1.7; 369 -1.6; 395 -1.5; 423 -1.3; 452 -1.3; 484 -1.3; 518 -1.2; 554 -0.8; 593 -0.8; 635 -1.0; 679 0.7; 726 0.0; 777 -0.2; 832 -0.4; 890 -0.2; 952 0.1; 1019 -0.0; 1090 -0.1; 1167 0.1; 1248 -0.2; 1336 -0.1; 1429 -0.0; 1529 0.2; 1636 1.1; 1751 1.2; 1873 1.2; 2004 1.0; 2145 0.6; 2295 1.2; 2455 2.0; 2627 1.0; 2811 0.0; 3008 0.4; 3219 -0.4; 3444 -0.5; 3685 -0.1; 3943 0.1; 4219 -2.4; 4514 -4.0; 4830 -3.2; 5168 -1.4; 5530 -0.5; 5917 -0.1; 6331 -0.1; 6775 0.2; 7249 0.7; 7756 0.3; 8299 -0.5; 8880 -1.4; 9502 -0.2; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.0; 17469 -2.2; 18692 -4.8; 20000 -5.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.7dB` and instead set Global volume in the UI for both channels to **-57**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 598 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 20 Hz    |  0.91 | 5.6 dB  |
| Peaking | 71 Hz    |  0.33 | -1.2 dB |
| Peaking | 235 Hz   |  0.61 | -1.6 dB |
| Peaking | 2142 Hz  |  1.66 | 1.4 dB  |
| Peaking | 4588 Hz  |  5.84 | -4.5 dB |
| Peaking | 692 Hz   | 13.59 | 1.2 dB  |
| Peaking | 8806 Hz  |  5.59 | -2.5 dB |
| Peaking | 8540 Hz  |  1.84 | 1.2 dB  |
| Peaking | 19322 Hz |  1.97 | -6.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20598/Sennheiser%20HD%20598.png)