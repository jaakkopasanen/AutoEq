# Sennheiser HD 650

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 5.6; 22 4.9; 23 4.6; 25 3.9; 26 3.6; 28 3.1; 30 2.6; 32 2.2; 35 1.7; 37 1.5; 40 1.5; 42 1.7; 45 2.0; 49 1.5; 52 0.8; 56 0.3; 59 0.1; 64 -0.0; 68 0.1; 73 -0.1; 78 -0.5; 83 -0.8; 89 -1.2; 95 -1.6; 102 -1.9; 109 -2.1; 117 -2.4; 125 -2.8; 134 -3.1; 143 -3.4; 153 -3.4; 164 -3.4; 175 -3.4; 188 -3.2; 201 -3.2; 215 -3.0; 230 -2.7; 246 -2.5; 263 -2.4; 282 -2.3; 301 -2.1; 323 -1.9; 345 -1.7; 369 -1.4; 395 -1.3; 423 -1.1; 452 -0.9; 484 -0.9; 518 -0.8; 554 -0.5; 593 -0.0; 635 0.1; 679 -0.0; 726 -0.0; 777 0.4; 832 0.1; 890 -0.1; 952 0.1; 1019 -0.0; 1090 -0.2; 1167 -0.4; 1248 -0.5; 1336 -0.5; 1429 -0.6; 1529 -0.8; 1636 -1.0; 1751 -1.1; 1873 -1.3; 2004 -1.4; 2145 -1.4; 2295 -1.2; 2455 -1.0; 2627 -1.0; 2811 -1.0; 3008 -0.5; 3219 -0.4; 3444 0.4; 3685 1.3; 3943 2.1; 4219 1.1; 4514 -0.2; 4830 0.4; 5168 2.5; 5530 3.3; 5917 2.3; 6331 1.6; 6775 2.2; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -1.1; 9502 -1.1; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 650 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 11 Hz   | 0.51 | 7.6 dB  |
| Peaking | 167 Hz  | 0.8  | -3.6 dB |
| Peaking | 4387 Hz | 0.74 | -3.3 dB |
| Peaking | 5711 Hz | 2.06 | 5.4 dB  |
| Peaking | 3805 Hz | 3.82 | 3.9 dB  |
| Peaking | 32 Hz   | 2.83 | -0.5 dB |
| Peaking | 779 Hz  | 2.71 | 0.7 dB  |
| Peaking | 1906 Hz | 4.06 | -0.6 dB |
| Peaking | 9203 Hz | 1.78 | 1.0 dB  |
| Peaking | 9274 Hz | 5.64 | -2.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20650/Sennheiser%20HD%20650.png)