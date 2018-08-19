# Sennheiser HD 700

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.4dB
GraphicEQ: 10 -84; 20 5.0; 22 4.4; 23 4.1; 25 3.5; 26 3.3; 28 2.9; 30 2.5; 32 2.1; 35 1.7; 37 1.4; 40 1.1; 42 0.9; 45 0.6; 49 0.2; 52 -0.0; 56 -0.3; 59 -0.6; 64 -0.9; 68 -1.1; 73 -1.4; 78 -1.6; 83 -1.8; 89 -2.1; 95 -2.3; 102 -2.4; 109 -2.5; 117 -2.7; 125 -3.1; 134 -3.1; 143 -3.3; 153 -3.5; 164 -3.5; 175 -3.4; 188 -3.6; 201 -3.6; 215 -3.5; 230 -3.5; 246 -3.5; 263 -3.4; 282 -3.4; 301 -3.1; 323 -2.9; 345 -2.6; 369 -2.5; 395 -2.3; 423 -2.1; 452 -2.0; 484 -1.7; 518 -1.6; 554 -1.5; 593 -1.2; 635 -0.9; 679 -0.8; 726 -0.6; 777 -0.5; 832 -0.5; 890 -0.4; 952 0.1; 1019 -0.0; 1090 0.3; 1167 0.9; 1248 0.9; 1336 1.1; 1429 1.5; 1529 1.6; 1636 2.2; 1751 2.5; 1873 3.2; 2004 3.7; 2145 3.6; 2295 3.3; 2455 4.7; 2627 5.3; 2811 4.4; 3008 3.6; 3219 4.1; 3444 4.7; 3685 4.3; 3943 3.1; 4219 -0.4; 4514 -2.8; 4830 -2.7; 5168 -2.4; 5530 -0.4; 5917 0.1; 6331 -4.8; 6775 -5.4; 7249 -2.1; 7756 -0.4; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 -0.2; 16326 -3.3; 17469 -6.0; 18692 -7.3; 20000 -7.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.379224431817692dB` and instead set Global volume in the UI for both channels to **-53**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.9dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 15 Hz    | 0.65 | 5.9 dB   |
| Peaking | 192 Hz   | 0.41 | -3.7 dB  |
| Peaking | 3610 Hz  | 0.81 | 10.6 dB  |
| Peaking | 4791 Hz  | 1.12 | -10.4 dB |
| Peaking | 19020 Hz | 1.58 | -8.4 dB  |
| Peaking | 3018 Hz  | 7.23 | -3.1 dB  |
| Peaking | 3075 Hz  | 3    | 1.7 dB   |
| Peaking | 5814 Hz  | 8.34 | 3.9 dB   |
| Peaking | 6537 Hz  | 8.18 | -6.1 dB  |
| Peaking | 11553 Hz | 1.07 | 0.7 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20700/Sennheiser%20HD%20700.png)