# Sennheiser HD 439

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -3.5; 22 -3.7; 23 -3.9; 25 -4.1; 26 -4.2; 28 -4.4; 30 -4.6; 32 -4.7; 35 -4.8; 37 -4.9; 40 -5.0; 42 -5.1; 45 -5.2; 49 -5.2; 52 -5.2; 56 -5.2; 59 -5.2; 64 -5.1; 68 -5.0; 73 -4.6; 78 -4.0; 83 -4.3; 89 -4.3; 95 -3.5; 102 -1.3; 109 -0.3; 117 -1.7; 125 -3.1; 134 -3.5; 143 -3.5; 153 -3.4; 164 -2.9; 175 -2.9; 188 -2.7; 201 -2.7; 215 -3.0; 230 -2.9; 246 -2.7; 263 -2.6; 282 -1.9; 301 -1.3; 323 -1.4; 345 -0.7; 369 0.4; 395 0.4; 423 0.5; 452 0.7; 484 0.9; 518 1.0; 554 0.8; 593 0.8; 635 0.4; 679 0.3; 726 0.4; 777 0.3; 832 -0.1; 890 -0.3; 952 -0.7; 1019 0.1; 1090 0.1; 1167 0.3; 1248 0.5; 1336 -0.6; 1429 -1.4; 1529 -1.5; 1636 -1.4; 1751 -1.1; 1873 -0.1; 2004 0.9; 2145 2.1; 2295 3.6; 2455 4.8; 2627 5.2; 2811 5.4; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
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
| Peaking | 14 Hz   | 1.11 | -3.3 dB |
| Peaking | 38 Hz   | 0.86 | -4.1 dB |
| Peaking | 68 Hz   | 1.61 | -2.9 dB |
| Peaking | 189 Hz  | 1.35 | -2.9 dB |
| Peaking | 4101 Hz | 1.07 | 7.0 dB  |
| Peaking | 495 Hz  | 2.47 | 1.4 dB  |
| Peaking | 1662 Hz | 2.46 | -3.1 dB |
| Peaking | 2577 Hz | 2.48 | 2.9 dB  |
| Peaking | 6119 Hz | 2.56 | 6.6 dB  |
| Peaking | 6347 Hz | 1.05 | -4.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20439/Sennheiser%20HD%20439.png)