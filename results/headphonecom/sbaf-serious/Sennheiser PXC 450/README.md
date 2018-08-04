# Sennheiser PXC 450

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 1.3; 22 0.1; 23 -0.4; 25 -1.1; 26 -1.3; 28 -1.5; 30 -1.5; 32 -1.4; 35 -1.2; 37 -1.0; 40 -0.8; 42 -0.6; 45 -0.3; 49 -0.0; 52 0.1; 56 0.1; 59 0.1; 64 0.0; 68 -0.0; 73 -0.1; 78 -0.0; 83 0.0; 89 -0.2; 95 -0.4; 102 -0.7; 109 -1.0; 117 -1.3; 125 -1.7; 134 -2.2; 143 -2.4; 153 -2.6; 164 -2.4; 175 -2.7; 188 -2.9; 201 -3.0; 215 -3.0; 230 -3.0; 246 -3.2; 263 -3.5; 282 -3.8; 301 -3.8; 323 -3.7; 345 -3.8; 369 -3.9; 395 -4.1; 423 -4.2; 452 -4.4; 484 -4.5; 518 -4.5; 554 -4.2; 593 -3.7; 635 -3.3; 679 -2.8; 726 -2.2; 777 -1.4; 832 -0.7; 890 -0.6; 952 -0.3; 1019 0.2; 1090 0.6; 1167 1.1; 1248 1.3; 1336 1.5; 1429 1.7; 1529 0.7; 1636 0.1; 1751 0.6; 1873 2.5; 2004 5.7; 2145 6.0; 2295 6.0; 2455 2.0; 2627 -2.2; 2811 -0.3; 3008 3.1; 3219 5.2; 3444 4.2; 3685 3.8; 3943 5.6; 4219 6.0; 4514 6.0; 4830 5.6; 5168 4.8; 5530 4.4; 5917 5.1; 6331 4.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 -2.8
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PXC 450 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 30 Hz   |  2.88 | -1.3 dB |
| Peaking | 341 Hz  |  0.89 | -7.3 dB |
| Peaking | 323 Hz  |  2.01 | 3.7 dB  |
| Peaking | 2116 Hz |  5.73 | 6.3 dB  |
| Peaking | 4602 Hz |  1.48 | 6.2 dB  |
| Peaking | 1222 Hz |  3.05 | 1.9 dB  |
| Peaking | 2660 Hz | 10.28 | -5.1 dB |
| Peaking | 3183 Hz |  7.83 | 2.8 dB  |
| Peaking | 6501 Hz |  3.77 | 4.4 dB  |
| Peaking | 6993 Hz |  1.55 | -2.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20PXC%20450/Sennheiser%20PXC%20450.png)