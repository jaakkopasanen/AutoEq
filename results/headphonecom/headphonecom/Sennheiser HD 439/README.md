# Sennheiser HD 439

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -4.0; 22 -4.3; 23 -4.4; 25 -4.6; 26 -4.7; 28 -4.9; 30 -5.1; 32 -5.3; 35 -5.4; 37 -5.5; 40 -5.6; 42 -5.7; 45 -5.8; 49 -5.8; 52 -5.8; 56 -5.8; 59 -5.8; 64 -5.7; 68 -5.5; 73 -5.2; 78 -4.7; 83 -5.0; 89 -5.1; 95 -4.4; 102 -2.3; 109 -1.4; 117 -3.0; 125 -4.4; 134 -4.8; 143 -4.8; 153 -4.7; 164 -4.2; 175 -4.3; 188 -4.0; 201 -4.1; 215 -4.3; 230 -4.3; 246 -4.0; 263 -4.0; 282 -3.2; 301 -2.7; 323 -2.8; 345 -2.1; 369 -0.9; 395 -0.8; 423 -0.7; 452 -0.3; 484 0.1; 518 0.5; 554 0.4; 593 0.3; 635 0.1; 679 0.3; 726 0.4; 777 0.2; 832 -0.2; 890 -0.3; 952 -0.7; 1019 0.1; 1090 0.2; 1167 0.5; 1248 1.2; 1336 0.7; 1429 0.7; 1529 1.2; 1636 1.6; 1751 2.0; 1873 2.8; 2004 3.8; 2145 5.1; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 439 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 3 Hz    |  1.74 | -3.3 dB |
| Peaking | 29 Hz   |  0.7  | -4.3 dB |
| Peaking | 62 Hz   |  1.14 | -3.6 dB |
| Peaking | 197 Hz  |  1.02 | -4.2 dB |
| Peaking | 3616 Hz |  0.8  | 6.9 dB  |
| Peaking | 110 Hz  | 10.15 | 2.4 dB  |
| Peaking | 128 Hz  |  5.35 | -1.3 dB |
| Peaking | 2317 Hz |  5.22 | 2.3 dB  |
| Peaking | 5996 Hz |  2.07 | 7.0 dB  |
| Peaking | 6406 Hz |  0.93 | -4.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Sennheiser%20HD%20439/Sennheiser%20HD%20439.png)