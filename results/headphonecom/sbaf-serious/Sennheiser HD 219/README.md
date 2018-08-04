# Sennheiser HD 219

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.5dB
GraphicEQ: 10 -84; 20 2.8; 22 2.1; 23 1.7; 25 1.1; 26 0.8; 28 0.3; 30 -0.2; 32 -0.6; 35 -1.1; 37 -1.4; 40 -1.9; 42 -2.2; 45 -2.5; 49 -2.9; 52 -3.1; 56 -3.4; 59 -3.6; 64 -3.8; 68 -3.9; 73 -3.9; 78 -4.0; 83 -4.0; 89 -4.0; 95 -4.3; 102 -4.5; 109 -4.6; 117 -4.6; 125 -4.5; 134 -4.2; 143 -3.7; 153 -3.7; 164 -4.4; 175 -3.4; 188 -3.9; 201 -3.6; 215 -2.5; 230 -2.2; 246 -2.1; 263 -1.7; 282 -0.9; 301 -0.0; 323 0.9; 345 1.5; 369 1.6; 395 1.9; 423 2.1; 452 2.0; 484 1.7; 518 1.4; 554 1.2; 593 1.1; 635 1.0; 679 1.6; 726 1.9; 777 1.6; 832 1.0; 890 0.6; 952 0.2; 1019 -0.0; 1090 -0.2; 1167 -0.2; 1248 -0.3; 1336 -0.3; 1429 -0.1; 1529 0.3; 1636 -0.6; 1751 -1.6; 1873 -1.4; 2004 -1.2; 2145 -0.9; 2295 -0.4; 2455 -0.0; 2627 0.1; 2811 0.3; 3008 0.5; 3219 0.8; 3444 1.1; 3685 1.6; 3943 0.7; 4219 -1.4; 4514 -1.9; 4830 -0.6; 5168 1.6; 5530 3.3; 5917 4.5; 6331 4.9; 6775 3.8; 7249 1.3; 7756 -1.5; 8299 -4.3; 8880 -5.4; 9502 -4.0; 10167 -0.6; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -1.7; 20000 -6.5
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.5dB` and instead set Global volume in the UI for both channels to **-55**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 219 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 3 Hz    |  2.25 | -2.0 dB |
| Peaking | 84 Hz   |  0.94 | -4.4 dB |
| Peaking | 172 Hz  |  2.32 | -2.8 dB |
| Peaking | 6309 Hz |  3.91 | 6.1 dB  |
| Peaking | 8737 Hz |  4.25 | -6.5 dB |
| Peaking | 20 Hz   |  2.68 | 3.3 dB  |
| Peaking | 418 Hz  |  2.57 | 2.6 dB  |
| Peaking | 727 Hz  |  4.01 | 1.8 dB  |
| Peaking | 1860 Hz |  4.9  | -1.8 dB |
| Peaking | 4488 Hz | 10.48 | -2.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20219/Sennheiser%20HD%20219.png)