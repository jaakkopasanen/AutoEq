# Sennheiser HD 205 II

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -0.3; 22 -0.5; 23 -0.6; 25 -0.7; 26 -0.7; 28 -0.7; 30 -0.6; 32 -0.7; 35 -1.0; 37 -1.1; 40 -1.2; 42 -1.3; 45 -1.4; 49 -1.5; 52 -1.5; 56 -1.5; 59 -1.3; 64 -0.8; 68 -0.9; 73 -1.5; 78 -2.1; 83 -2.5; 89 -2.7; 95 -3.1; 102 -3.2; 109 -3.5; 117 -3.7; 125 -3.7; 134 -3.4; 143 -2.8; 153 -3.1; 164 -3.1; 175 -3.2; 188 -3.1; 201 -2.9; 215 -2.8; 230 -2.9; 246 -2.5; 263 -2.4; 282 -2.1; 301 -1.7; 323 -0.8; 345 0.2; 369 1.1; 395 2.0; 423 2.6; 452 2.4; 484 1.4; 518 0.4; 554 -0.0; 593 0.3; 635 1.4; 679 3.3; 726 4.3; 777 4.2; 832 2.9; 890 1.5; 952 0.5; 1019 -0.2; 1090 -0.8; 1167 -1.3; 1248 -1.6; 1336 -1.9; 1429 -2.0; 1529 -2.4; 1636 -2.6; 1751 -2.1; 1873 -1.7; 2004 -1.2; 2145 -0.7; 2295 0.4; 2455 1.6; 2627 2.9; 2811 4.0; 3008 4.4; 3219 4.6; 3444 5.4; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 4.4; 5168 2.8; 5530 3.7; 5917 5.7; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.4; 8880 -1.0; 9502 -0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 205 II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 867 Hz  | 0.16 | -9.5 dB |
| Peaking | 110 Hz  | 2.56 | -1.1 dB |
| Peaking | 608 Hz  | 0.54 | 11.6 dB |
| Peaking | 3658 Hz | 1.07 | 11.7 dB |
| Peaking | 6227 Hz | 4.83 | 5.3 dB  |
| Peaking | 419 Hz  | 2.99 | 3.2 dB  |
| Peaking | 579 Hz  | 2.63 | -3.8 dB |
| Peaking | 738 Hz  | 2.81 | 4.7 dB  |
| Peaking | 732 Hz  | 0.33 | -1.1 dB |
| Peaking | 2657 Hz | 4.9  | 1.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20205%20II/Sennheiser%20HD%20205%20II.png)