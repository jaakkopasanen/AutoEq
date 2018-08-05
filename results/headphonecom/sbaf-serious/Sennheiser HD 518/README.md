# Sennheiser HD 518

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.8dB
GraphicEQ: 10 -84; 20 6.2; 22 5.5; 23 5.2; 25 4.5; 26 4.2; 28 3.7; 30 3.2; 32 2.7; 35 2.1; 37 1.8; 40 1.3; 42 1.0; 45 0.7; 49 0.2; 52 -0.1; 56 -0.4; 59 -0.7; 64 -1.0; 68 -1.3; 73 -1.4; 78 -1.7; 83 -1.8; 89 -1.3; 95 -0.9; 102 -1.8; 109 -2.6; 117 -3.2; 125 -3.9; 134 -4.3; 143 -4.5; 153 -4.9; 164 -4.6; 175 -4.6; 188 -4.8; 201 -4.7; 215 -4.5; 230 -4.5; 246 -4.5; 263 -4.5; 282 -4.2; 301 -4.0; 323 -3.8; 345 -3.5; 369 -3.4; 395 -3.1; 423 -2.9; 452 -2.7; 484 -2.6; 518 -2.2; 554 -1.7; 593 -1.4; 635 -1.4; 679 -1.7; 726 -1.6; 777 -0.4; 832 -0.8; 890 -0.7; 952 -0.1; 1019 0.0; 1090 0.7; 1167 1.5; 1248 1.8; 1336 2.7; 1429 3.4; 1529 4.0; 1636 4.9; 1751 4.8; 1873 4.1; 2004 3.1; 2145 2.0; 2295 2.1; 2455 2.4; 2627 1.6; 2811 0.9; 3008 0.3; 3219 -0.5; 3444 0.6; 3685 1.5; 3943 1.7; 4219 -1.1; 4514 -2.4; 4830 -1.8; 5168 -0.6; 5530 0.5; 5917 2.0; 6331 3.1; 6775 2.8; 7249 1.3; 7756 0.3; 8299 -0.5; 8880 -1.3; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -0.9; 18692 -3.0; 20000 -3.2
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.8dB` and instead set Global volume in the UI for both channels to **-68**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 518 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 19 Hz    |  0.9  | 6.4 dB  |
| Peaking | 218 Hz   |  0.52 | -4.9 dB |
| Peaking | 1678 Hz  |  1.83 | 5.1 dB  |
| Peaking | 4645 Hz  |  6.8  | -3.1 dB |
| Peaking | 6423 Hz  |  5.31 | 3.5 dB  |
| Peaking | 95 Hz    |  7.44 | 1.5 dB  |
| Peaking | 136 Hz   |  3.45 | -0.8 dB |
| Peaking | 886 Hz   |  5.56 | -0.3 dB |
| Peaking | 3842 Hz  | 12.57 | 2.1 dB  |
| Peaking | 19335 Hz |  2.15 | -3.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20518/Sennheiser%20HD%20518.png)