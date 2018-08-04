# Sennheiser PXC 450

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -2.7; 22 -3.9; 23 -4.4; 25 -5.1; 26 -5.3; 28 -5.5; 30 -5.5; 32 -5.4; 35 -5.2; 37 -5.0; 40 -4.8; 42 -4.6; 45 -4.3; 49 -4.0; 52 -3.9; 56 -3.8; 59 -3.8; 64 -3.8; 68 -3.8; 73 -3.8; 78 -3.6; 83 -3.4; 89 -3.4; 95 -3.3; 102 -3.2; 109 -3.0; 117 -2.9; 125 -2.9; 134 -3.1; 143 -3.0; 153 -3.0; 164 -2.7; 175 -2.8; 188 -3.0; 201 -3.1; 215 -3.0; 230 -3.0; 246 -3.2; 263 -3.5; 282 -3.8; 301 -3.8; 323 -3.7; 345 -3.8; 369 -3.9; 395 -4.1; 423 -4.2; 452 -4.4; 484 -4.5; 518 -4.5; 554 -4.2; 593 -3.7; 635 -3.3; 679 -2.8; 726 -2.2; 777 -1.4; 832 -0.7; 890 -0.6; 952 -0.3; 1019 0.2; 1090 0.6; 1167 1.1; 1248 1.3; 1336 1.5; 1429 1.7; 1529 0.7; 1636 0.1; 1751 0.6; 1873 2.5; 2004 5.7; 2145 6.0; 2295 6.0; 2455 2.0; 2627 -2.2; 2811 -0.3; 3008 3.1; 3219 5.2; 3444 4.2; 3685 3.8; 3943 5.6; 4219 6.0; 4514 6.0; 4830 5.6; 5168 4.8; 5530 4.4; 5917 5.1; 6331 4.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 -2.8
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PXC 450 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 28 Hz   | 1.26 | -3.8 dB  |
| Peaking | 67 Hz   | 0.44 | -2.9 dB  |
| Peaking | 511 Hz  | 0.64 | -5.6 dB  |
| Peaking | 1308 Hz | 0.47 | 3.3 dB   |
| Peaking | 4714 Hz | 1.58 | 5.4 dB   |
| Peaking | 1714 Hz | 2.98 | -5.8 dB  |
| Peaking | 2232 Hz | 1.68 | 8.0 dB   |
| Peaking | 2636 Hz | 5.75 | -10.5 dB |
| Peaking | 6423 Hz | 3.59 | 5.1 dB   |
| Peaking | 6610 Hz | 1.38 | -3.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20PXC%20450/Sennheiser%20PXC%20450.png)