# HiFiMAN HE-5LE

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 -2.6; 22 -3.1; 23 -3.3; 25 -3.6; 26 -3.7; 28 -3.8; 30 -3.8; 32 -3.7; 35 -3.6; 37 -3.5; 40 -3.3; 42 -3.3; 45 -3.3; 49 -3.3; 52 -3.3; 56 -3.2; 59 -3.1; 64 -2.9; 68 -2.9; 73 -3.0; 78 -3.0; 83 -2.8; 89 -2.8; 95 -2.9; 102 -3.0; 109 -3.0; 117 -3.0; 125 -3.3; 134 -3.5; 143 -3.9; 153 -4.3; 164 -4.7; 175 -4.9; 188 -4.9; 201 -4.9; 215 -4.9; 230 -5.0; 246 -5.1; 263 -5.1; 282 -5.0; 301 -5.0; 323 -5.1; 345 -4.8; 369 -4.8; 395 -4.8; 423 -4.6; 452 -4.4; 484 -4.4; 518 -5.0; 554 -5.2; 593 -3.7; 635 -0.9; 679 0.6; 726 1.2; 777 1.4; 832 0.9; 890 0.1; 952 -0.1; 1019 0.2; 1090 1.2; 1167 2.3; 1248 3.0; 1336 4.3; 1429 5.3; 1529 5.8; 1636 6.0; 1751 6.0; 1873 6.0; 2004 6.0; 2145 5.8; 2295 5.1; 2455 5.9; 2627 6.0; 2811 5.5; 3008 4.2; 3219 3.9; 3444 4.2; 3685 5.1; 3943 3.5; 4219 1.8; 4514 1.2; 4830 2.1; 5168 5.0; 5530 4.6; 5917 1.4; 6331 -1.8; 6775 -2.1; 7249 -2.1; 7756 -2.8; 8299 -4.4; 8880 -5.4; 9502 -3.7; 10167 -0.3; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE-5LE ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 25 Hz   |  0.07 | -2.9 dB |
| Peaking | 380 Hz  |  0.65 | -4.6 dB |
| Peaking | 1813 Hz |  1.35 | 3.3 dB  |
| Peaking | 3033 Hz |  0.28 | 4.0 dB  |
| Peaking | 8340 Hz |  1.94 | -7.5 dB |
| Peaking | 563 Hz  |  3.98 | -4.6 dB |
| Peaking | 710 Hz  |  1.41 | 4.2 dB  |
| Peaking | 949 Hz  |  2.88 | -3.6 dB |
| Peaking | 4503 Hz |  7.1  | -2.6 dB |
| Peaking | 5319 Hz | 10.51 | 4.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/HiFiMAN%20HE-5LE/HiFiMAN%20HE-5LE.png)