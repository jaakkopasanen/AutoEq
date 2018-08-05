# Sennheiser HD 439

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 0.5; 22 0.3; 23 0.1; 25 -0.1; 26 -0.2; 28 -0.4; 30 -0.6; 32 -0.7; 35 -0.8; 37 -0.9; 40 -1.0; 42 -1.1; 45 -1.2; 49 -1.2; 52 -1.2; 56 -1.3; 59 -1.3; 64 -1.2; 68 -1.1; 73 -0.8; 78 -0.4; 83 -0.8; 89 -1.1; 95 -0.6; 102 1.1; 109 1.7; 117 -0.2; 125 -1.9; 134 -2.7; 143 -2.9; 153 -3.0; 164 -2.6; 175 -2.7; 188 -2.6; 201 -2.6; 215 -2.9; 230 -2.8; 246 -2.6; 263 -2.6; 282 -1.8; 301 -1.3; 323 -1.4; 345 -0.7; 369 0.4; 395 0.4; 423 0.5; 452 0.7; 484 0.9; 518 1.0; 554 0.8; 593 0.8; 635 0.4; 679 0.3; 726 0.4; 777 0.3; 832 -0.1; 890 -0.3; 952 -0.7; 1019 0.1; 1090 0.1; 1167 0.3; 1248 0.5; 1336 -0.6; 1429 -1.4; 1529 -1.5; 1636 -1.4; 1751 -1.1; 1873 -0.1; 2004 0.9; 2145 2.1; 2295 3.6; 2455 4.8; 2627 5.2; 2811 5.4; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 439 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 49 Hz   | 1.93 | -1.3 dB |
| Peaking | 206 Hz  | 1.17 | -3.2 dB |
| Peaking | 462 Hz  | 1.99 | 1.5 dB  |
| Peaking | 1628 Hz | 2.51 | -3.8 dB |
| Peaking | 3736 Hz | 0.84 | 7.0 dB  |
| Peaking | 108 Hz  | 7.94 | 3.2 dB  |
| Peaking | 136 Hz  | 4.33 | -1.4 dB |
| Peaking | 2526 Hz | 6.15 | 1.4 dB  |
| Peaking | 6083 Hz | 2.38 | 6.5 dB  |
| Peaking | 6878 Hz | 1.14 | -4.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20439/Sennheiser%20HD%20439.png)