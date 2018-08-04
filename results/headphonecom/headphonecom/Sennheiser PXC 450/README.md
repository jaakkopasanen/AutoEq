# Sennheiser PXC 450

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -3.2; 22 -4.4; 23 -4.9; 25 -5.7; 26 -5.9; 28 -6.1; 30 -6.0; 32 -5.9; 35 -5.7; 37 -5.6; 40 -5.4; 42 -5.2; 45 -4.9; 49 -4.6; 52 -4.4; 56 -4.4; 59 -4.4; 64 -4.4; 68 -4.4; 73 -4.4; 78 -4.3; 83 -4.2; 89 -4.2; 95 -4.2; 102 -4.2; 109 -4.1; 117 -4.1; 125 -4.2; 134 -4.3; 143 -4.3; 153 -4.3; 164 -4.0; 175 -4.2; 188 -4.3; 201 -4.4; 215 -4.4; 230 -4.5; 246 -4.6; 263 -4.9; 282 -5.1; 301 -5.1; 323 -5.1; 345 -5.2; 369 -5.3; 395 -5.3; 423 -5.4; 452 -5.4; 484 -5.3; 518 -5.0; 554 -4.7; 593 -4.2; 635 -3.6; 679 -2.9; 726 -2.2; 777 -1.5; 832 -0.8; 890 -0.6; 952 -0.3; 1019 0.2; 1090 0.7; 1167 1.4; 1248 2.0; 1336 2.9; 1429 3.8; 1529 3.3; 1636 3.1; 1751 3.6; 1873 5.3; 2004 6.0; 2145 6.0; 2295 6.0; 2455 4.6; 2627 0.8; 2811 2.6; 3008 5.5; 3219 6.0; 3444 6.0; 3685 5.7; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PXC 450 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 1.07 | -4.3 dB |
| Peaking | 118 Hz  | 0.28 | -3.7 dB |
| Peaking | 457 Hz  | 0.94 | -4.0 dB |
| Peaking | 1886 Hz | 1.04 | 4.8 dB  |
| Peaking | 4728 Hz | 1.4  | 6.1 dB  |
| Peaking | 2364 Hz | 5.16 | 3.0 dB  |
| Peaking | 2650 Hz | 6.06 | -5.9 dB |
| Peaking | 3148 Hz | 3.55 | 2.8 dB  |
| Peaking | 6267 Hz | 3.33 | 5.4 dB  |
| Peaking | 6735 Hz | 1.28 | -3.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Sennheiser%20PXC%20450/Sennheiser%20PXC%20450.png)