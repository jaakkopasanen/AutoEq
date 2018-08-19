# Sennheiser HD 205 II

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -0.3; 22 -0.5; 23 -0.6; 25 -0.7; 26 -0.7; 28 -0.7; 30 -0.7; 32 -0.7; 35 -1.0; 37 -1.2; 40 -1.4; 42 -1.4; 45 -1.6; 49 -1.7; 52 -1.8; 56 -1.9; 59 -1.7; 64 -1.3; 68 -1.4; 73 -2.2; 78 -2.9; 83 -3.3; 89 -3.5; 95 -3.8; 102 -3.8; 109 -3.9; 117 -3.9; 125 -3.7; 134 -3.2; 143 -2.6; 153 -2.8; 164 -2.8; 175 -2.9; 188 -2.9; 201 -2.7; 215 -2.7; 230 -2.8; 246 -2.4; 263 -2.3; 282 -2.1; 301 -1.7; 323 -0.8; 345 0.2; 369 1.2; 395 2.1; 423 2.5; 452 2.3; 484 1.5; 518 0.6; 554 -0.0; 593 0.2; 635 1.4; 679 3.3; 726 4.4; 777 4.1; 832 2.8; 890 1.5; 952 0.5; 1019 -0.2; 1090 -0.8; 1167 -1.3; 1248 -1.6; 1336 -1.9; 1429 -2.0; 1529 -2.5; 1636 -2.6; 1751 -2.1; 1873 -1.7; 2004 -1.3; 2145 -0.7; 2295 0.4; 2455 1.5; 2627 2.9; 2811 4.1; 3008 4.3; 3219 4.6; 3444 5.5; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 4.4; 5168 2.7; 5530 3.7; 5917 5.7; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.2; 8880 -0.9; 9502 -0.1; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999813384083dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 205 II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 106 Hz  | 0.81 | -3.6 dB |
| Peaking | 280 Hz  | 1.3  | -4.0 dB |
| Peaking | 394 Hz  | 1.07 | 4.2 dB  |
| Peaking | 3858 Hz | 2.2  | 6.7 dB  |
| Peaking | 6181 Hz | 5.12 | 5.1 dB  |
| Peaking | 576 Hz  | 4.67 | -2.8 dB |
| Peaking | 743 Hz  | 3.14 | 4.7 dB  |
| Peaking | 1568 Hz | 1.23 | -3.2 dB |
| Peaking | 2787 Hz | 3.87 | 2.8 dB  |
| Peaking | 8684 Hz | 5.61 | -1.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20205%20II/Sennheiser%20HD%20205%20II.png)