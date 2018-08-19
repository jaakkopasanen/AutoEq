# Sennheiser PXC 450

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 1.3; 22 0.1; 23 -0.4; 25 -1.1; 26 -1.4; 28 -1.6; 30 -1.5; 32 -1.4; 35 -1.2; 37 -1.1; 40 -0.9; 42 -0.7; 45 -0.5; 49 -0.2; 52 -0.2; 56 -0.2; 59 -0.3; 64 -0.5; 68 -0.6; 73 -0.7; 78 -0.8; 83 -0.8; 89 -1.0; 95 -1.1; 102 -1.3; 109 -1.4; 117 -1.5; 125 -1.7; 134 -2.1; 143 -2.2; 153 -2.3; 164 -2.2; 175 -2.5; 188 -2.7; 201 -2.8; 215 -2.8; 230 -2.9; 246 -3.1; 263 -3.4; 282 -3.7; 301 -3.7; 323 -3.7; 345 -3.8; 369 -3.9; 395 -4.0; 423 -4.3; 452 -4.4; 484 -4.5; 518 -4.3; 554 -4.2; 593 -3.9; 635 -3.3; 679 -2.7; 726 -2.1; 777 -1.4; 832 -0.7; 890 -0.6; 952 -0.3; 1019 0.2; 1090 0.6; 1167 1.1; 1248 1.3; 1336 1.5; 1429 1.7; 1529 0.6; 1636 0.1; 1751 0.6; 1873 2.5; 2004 5.7; 2145 6.0; 2295 6.0; 2455 1.9; 2627 -2.2; 2811 -0.2; 3008 3.0; 3219 5.2; 3444 4.3; 3685 3.9; 3943 5.4; 4219 6.0; 4514 6.0; 4830 5.7; 5168 4.8; 5530 4.4; 5917 5.2; 6331 4.5; 6775 3.8; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 -2.8
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999999989dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PXC 450 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 231 Hz  |  0.67 | -2.8 dB |
| Peaking | 483 Hz  |  4.02 | 1.8 dB  |
| Peaking | 495 Hz  |  2    | -5.0 dB |
| Peaking | 2100 Hz |  5.93 | 6.2 dB  |
| Peaking | 4614 Hz |  1.49 | 6.2 dB  |
| Peaking | 30 Hz   |  2.45 | -1.4 dB |
| Peaking | 1241 Hz |  3.68 | 1.6 dB  |
| Peaking | 2677 Hz | 10.69 | -5.1 dB |
| Peaking | 3215 Hz |  8.41 | 2.6 dB  |
| Peaking | 8604 Hz |  4.25 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20PXC%20450/Sennheiser%20PXC%20450.png)