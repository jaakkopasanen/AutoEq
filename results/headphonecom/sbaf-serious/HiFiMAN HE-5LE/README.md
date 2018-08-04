# HiFiMAN HE-5LE

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.2dB
GraphicEQ: 10 -84; 20 1.9; 22 1.4; 23 1.2; 25 0.9; 26 0.9; 28 0.8; 30 0.8; 32 0.8; 35 1.0; 37 1.1; 40 1.3; 42 1.3; 45 1.3; 49 1.3; 52 1.3; 56 1.3; 59 1.4; 64 1.5; 68 1.6; 73 1.3; 78 1.3; 83 1.4; 89 1.2; 95 0.9; 102 0.5; 109 0.2; 117 -0.2; 125 -0.8; 134 -1.4; 143 -2.0; 153 -2.6; 164 -3.1; 175 -3.4; 188 -3.5; 201 -3.5; 215 -3.5; 230 -3.6; 246 -3.7; 263 -3.8; 282 -3.7; 301 -3.6; 323 -3.7; 345 -3.4; 369 -3.4; 395 -3.5; 423 -3.4; 452 -3.3; 484 -3.7; 518 -4.5; 554 -4.7; 593 -3.2; 635 -0.6; 679 0.6; 726 1.2; 777 1.5; 832 1.0; 890 0.1; 952 -0.1; 1019 0.2; 1090 1.2; 1167 2.0; 1248 2.4; 1336 2.9; 1429 3.2; 1529 3.1; 1636 3.4; 1751 4.4; 1873 4.4; 2004 3.8; 2145 2.9; 2295 2.0; 2455 3.5; 2627 3.8; 2811 2.6; 3008 1.6; 3219 1.6; 3444 2.2; 3685 3.0; 3943 1.1; 4219 -1.8; 4514 -3.6; 4830 -3.3; 5168 -0.4; 5530 -0.1; 5917 -2.1; 6331 -4.0; 6775 -3.5; 7249 -3.1; 7756 -3.8; 8299 -5.8; 8880 -7.4; 9502 -6.3; 10167 -2.6; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -0.0; 15258 -0.8; 16326 -1.3; 17469 -1.6; 18692 -1.9; 20000 -2.1
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.2dB` and instead set Global volume in the UI for both channels to **-52**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE-5LE ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 338 Hz  |  0.73 | -4.5 dB |
| Peaking | 1775 Hz |  0.82 | 4.2 dB  |
| Peaking | 3820 Hz |  4.82 | 3.5 dB  |
| Peaking | 4470 Hz |  3.61 | -5.1 dB |
| Peaking | 8617 Hz |  2.78 | -7.4 dB |
| Peaking | 42 Hz   |  1.03 | 1.4 dB  |
| Peaking | 81 Hz   |  2.56 | 1.6 dB  |
| Peaking | 550 Hz  |  6.54 | -3.1 dB |
| Peaking | 709 Hz  |  4.9  | 2.5 dB  |
| Peaking | 6428 Hz | 10.99 | -2.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/HiFiMAN%20HE-5LE/HiFiMAN%20HE-5LE.png)