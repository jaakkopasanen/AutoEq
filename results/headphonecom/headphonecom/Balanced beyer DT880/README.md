# Balanced beyer DT880

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.4dB
GraphicEQ: 10 -84; 20 4.6; 22 4.2; 23 3.9; 25 3.5; 26 3.3; 28 3.0; 30 2.6; 32 2.3; 35 1.9; 37 1.7; 40 1.3; 42 1.1; 45 0.8; 49 0.4; 52 0.2; 56 -0.2; 59 -0.3; 64 -0.2; 68 -0.0; 73 -0.1; 78 -0.8; 83 -1.6; 89 -2.2; 95 -2.4; 102 -2.8; 109 -3.0; 117 -3.4; 125 -3.7; 134 -4.0; 143 -4.2; 153 -4.4; 164 -4.5; 175 -4.7; 188 -4.9; 201 -5.0; 215 -5.1; 230 -5.0; 246 -5.0; 263 -5.1; 282 -5.1; 301 -5.0; 323 -4.7; 345 -4.5; 369 -4.3; 395 -3.9; 423 -3.7; 452 -3.0; 484 -2.1; 518 -2.2; 554 -1.9; 593 -1.6; 635 -1.1; 679 -0.9; 726 -0.7; 777 -0.6; 832 -0.5; 890 -0.4; 952 -0.1; 1019 0.1; 1090 0.6; 1167 1.2; 1248 2.0; 1336 2.6; 1429 3.0; 1529 3.2; 1636 3.1; 1751 2.8; 1873 2.5; 2004 2.6; 2145 2.8; 2295 3.1; 2455 3.3; 2627 3.0; 2811 2.4; 3008 1.7; 3219 1.2; 3444 1.1; 3685 1.6; 3943 2.7; 4219 4.5; 4514 5.5; 4830 5.9; 5168 4.8; 5530 2.2; 5917 -0.5; 6331 -1.9; 6775 -1.6; 7249 -1.6; 7756 -2.4; 8299 -3.5; 8880 -3.4; 9502 -1.1; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.4dB` and instead set Global volume in the UI for both channels to **-64**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Balanced beyer DT880 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 14 Hz   |  0.52 | 5.4 dB  |
| Peaking | 219 Hz  |  0.55 | -5.4 dB |
| Peaking | 1504 Hz |  1.87 | 3.4 dB  |
| Peaking | 2459 Hz |  2.94 | 2.7 dB  |
| Peaking | 4661 Hz |  4.81 | 6.4 dB  |
| Peaking | 70 Hz   |  6.82 | 0.9 dB  |
| Peaking | 389 Hz  |  2.13 | -1.5 dB |
| Peaking | 435 Hz  |  1.27 | 1.1 dB  |
| Peaking | 5191 Hz | 10.16 | 2.3 dB  |
| Peaking | 7993 Hz |  2.36 | -3.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Balanced%20beyer%20DT880/Balanced%20beyer%20DT880.png)