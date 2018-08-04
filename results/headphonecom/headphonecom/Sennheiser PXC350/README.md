# Sennheiser PXC350

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -0.7; 22 -1.5; 23 -1.8; 25 -2.4; 26 -2.6; 28 -3.0; 30 -3.3; 32 -3.4; 35 -3.5; 37 -3.5; 40 -3.5; 42 -3.5; 45 -3.4; 49 -3.2; 52 -3.1; 56 -2.8; 59 -2.6; 64 -2.4; 68 -2.3; 73 -2.1; 78 -1.8; 83 -1.5; 89 -1.5; 95 -1.7; 102 -1.6; 109 -1.4; 117 -1.4; 125 -1.2; 134 -1.0; 143 -0.9; 153 -0.7; 164 -0.2; 175 0.1; 188 0.2; 201 0.6; 215 0.9; 230 0.8; 246 0.7; 263 0.6; 282 0.5; 301 0.4; 323 0.2; 345 0.1; 369 -0.2; 395 -0.4; 423 -0.6; 452 -0.8; 484 -1.0; 518 -1.1; 554 -1.0; 593 -0.8; 635 -0.8; 679 -0.7; 726 -0.5; 777 -0.3; 832 0.0; 890 0.2; 952 -0.0; 1019 0.1; 1090 0.3; 1167 0.6; 1248 0.9; 1336 1.3; 1429 1.6; 1529 1.5; 1636 0.7; 1751 -0.5; 1873 -1.0; 2004 3.3; 2145 6.0; 2295 5.9; 2455 0.4; 2627 -2.3; 2811 -0.0; 3008 3.1; 3219 4.9; 3444 4.8; 3685 4.6; 3943 5.9; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.3; 6331 2.8; 6775 0.7; 7249 0.9; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PXC350 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 41 Hz   |  0.71 | -3.6 dB |
| Peaking | 546 Hz  |  2.81 | -1.2 dB |
| Peaking | 1391 Hz |  6.24 | 1.4 dB  |
| Peaking | 2176 Hz | 10.16 | 6.2 dB  |
| Peaking | 4564 Hz |  1.76 | 6.9 dB  |
| Peaking | 231 Hz  |  3.06 | 1.2 dB  |
| Peaking | 2661 Hz |  9.16 | -5.1 dB |
| Peaking | 3227 Hz |  3.21 | 2.8 dB  |
| Peaking | 5755 Hz |  4.67 | 4.4 dB  |
| Peaking | 5787 Hz |  1.18 | -2.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Sennheiser%20PXC350/Sennheiser%20PXC350.png)