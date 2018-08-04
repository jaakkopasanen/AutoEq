# Sennheiser HD600

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 5.9; 22 5.1; 23 4.7; 25 4.0; 26 3.6; 28 3.0; 30 2.5; 32 2.0; 35 1.3; 37 0.9; 40 0.4; 42 0.1; 45 -0.3; 49 -0.7; 52 -0.8; 56 -0.5; 59 -0.6; 64 -1.6; 68 -2.3; 73 -2.8; 78 -3.0; 83 -3.2; 89 -3.4; 95 -3.5; 102 -3.7; 109 -3.7; 117 -3.8; 125 -3.9; 134 -3.8; 143 -3.6; 153 -3.6; 164 -3.5; 175 -3.5; 188 -3.3; 201 -3.3; 215 -3.1; 230 -3.0; 246 -2.9; 263 -2.7; 282 -2.5; 301 -2.2; 323 -2.1; 345 -2.0; 369 -1.6; 395 -1.4; 423 -1.0; 452 -0.7; 484 -0.5; 518 -0.3; 554 -0.1; 593 0.2; 635 0.5; 679 0.7; 726 0.9; 777 0.8; 832 0.6; 890 0.4; 952 0.1; 1019 0.2; 1090 0.5; 1167 0.5; 1248 0.8; 1336 1.2; 1429 1.7; 1529 2.2; 1636 2.3; 1751 2.4; 1873 2.2; 2004 2.3; 2145 2.1; 2295 1.7; 2455 1.5; 2627 1.2; 2811 0.7; 3008 -0.0; 3219 -1.2; 3444 -2.1; 3685 -2.4; 3943 -1.6; 4219 -0.7; 4514 0.1; 4830 1.3; 5168 3.2; 5530 5.6; 5917 5.9; 6331 4.1; 6775 2.6; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 17 Hz   | 0.87 | 6.8 dB  |
| Peaking | 130 Hz  | 0.51 | -4.1 dB |
| Peaking | 2032 Hz | 0.86 | 2.6 dB  |
| Peaking | 3623 Hz | 2.4  | -4.0 dB |
| Peaking | 5770 Hz | 3.88 | 6.5 dB  |
| Peaking | 705 Hz  | 2.61 | 1.0 dB  |
| Peaking | 1030 Hz | 2.96 | -0.7 dB |
| Peaking | 8415 Hz | 4.65 | -0.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Sennheiser%20HD600/Sennheiser%20HD600.png)