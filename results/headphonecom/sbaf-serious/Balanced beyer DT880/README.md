# Balanced beyer DT880

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.7dB
GraphicEQ: 10 -84; 20 5.1; 22 4.7; 23 4.5; 25 4.0; 26 3.8; 28 3.5; 30 3.2; 32 2.9; 35 2.5; 37 2.3; 40 1.9; 42 1.7; 45 1.4; 49 1.0; 52 0.7; 56 0.4; 59 0.3; 64 0.3; 68 0.5; 73 0.5; 78 -0.1; 83 -0.9; 89 -1.3; 95 -1.6; 102 -1.8; 109 -1.9; 117 -2.1; 125 -2.4; 134 -2.7; 143 -2.9; 153 -3.1; 164 -3.2; 175 -3.3; 188 -3.6; 201 -3.7; 215 -3.7; 230 -3.6; 246 -3.6; 263 -3.8; 282 -3.7; 301 -3.6; 323 -3.3; 345 -3.0; 369 -2.9; 395 -2.7; 423 -2.5; 452 -2.0; 484 -1.4; 518 -1.7; 554 -1.5; 593 -1.1; 635 -0.8; 679 -0.8; 726 -0.7; 777 -0.4; 832 -0.4; 890 -0.3; 952 -0.1; 1019 0.1; 1090 0.5; 1167 0.9; 1248 1.3; 1336 1.3; 1429 0.9; 1529 0.5; 1636 0.1; 1751 -0.3; 1873 -0.4; 2004 -0.3; 2145 -0.2; 2295 0.0; 2455 0.4; 2627 -0.0; 2811 -0.5; 3008 -0.8; 3219 -1.1; 3444 -0.9; 3685 -0.5; 3943 0.4; 4219 0.9; 4514 0.7; 4830 0.4; 5168 -0.6; 5530 -2.5; 5917 -4.0; 6331 -4.2; 6775 -3.0; 7249 -2.6; 7756 -3.4; 8299 -4.9; 8880 -5.4; 9502 -3.5; 10167 -0.4; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.7dB` and instead set Global volume in the UI for both channels to **-57**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Balanced beyer DT880 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 14 Hz   | 0.5  | 5.8 dB  |
| Peaking | 227 Hz  | 0.59 | -4.2 dB |
| Peaking | 2548 Hz | 0.1  | 0.5 dB  |
| Peaking | 6169 Hz | 4.34 | -4.4 dB |
| Peaking | 8626 Hz | 3.92 | -5.9 dB |
| Peaking | 1296 Hz | 3.61 | 1.4 dB  |
| Peaking | 3324 Hz | 3.33 | -1.8 dB |
| Peaking | 1854 Hz | 3.39 | -0.8 dB |
| Peaking | 4415 Hz | 2.5  | 1.4 dB  |
| Peaking | 5592 Hz | 8.36 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Balanced%20beyer%20DT880/Balanced%20beyer%20DT880.png)