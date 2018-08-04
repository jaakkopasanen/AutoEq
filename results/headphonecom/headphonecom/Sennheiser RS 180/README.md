# Sennheiser RS 180

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.5dB
GraphicEQ: 10 -84; 20 -1.4; 22 -2.2; 23 -2.5; 25 -3.2; 26 -3.5; 28 -4.0; 30 -4.5; 32 -5.0; 35 -5.5; 37 -5.8; 40 -6.2; 42 -6.4; 45 -6.7; 49 -7.1; 52 -7.1; 56 -7.1; 59 -7.1; 64 -7.7; 68 -8.1; 73 -7.9; 78 -7.7; 83 -8.0; 89 -8.0; 95 -8.1; 102 -8.3; 109 -8.2; 117 -7.9; 125 -7.8; 134 -7.8; 143 -7.8; 153 -7.7; 164 -7.5; 175 -7.5; 188 -7.4; 201 -7.2; 215 -6.9; 230 -6.4; 246 -6.1; 263 -6.0; 282 -5.8; 301 -5.4; 323 -5.2; 345 -4.9; 369 -4.6; 395 -4.4; 423 -4.0; 452 -3.6; 484 -3.1; 518 -2.7; 554 -2.4; 593 -2.1; 635 -1.7; 679 -1.4; 726 -1.5; 777 -0.8; 832 0.9; 890 0.3; 952 0.1; 1019 0.0; 1090 0.4; 1167 0.7; 1248 1.3; 1336 2.4; 1429 2.8; 1529 2.0; 1636 0.6; 1751 -0.9; 1873 -2.0; 2004 -2.8; 2145 -3.2; 2295 -2.7; 2455 -1.3; 2627 0.6; 2811 3.4; 3008 4.8; 3219 0.6; 3444 1.5; 3685 4.3; 3943 3.7; 4219 4.1; 4514 2.7; 4830 -0.1; 5168 0.7; 5530 2.1; 5917 1.2; 6331 -0.9; 6775 2.8; 7249 1.3; 7756 -1.0; 8299 -4.8; 8880 -6.8; 9502 -4.9; 10167 -0.6; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.5dB` and instead set Global volume in the UI for both channels to **-55**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser RS 180 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 51 Hz   |  0.56 | -4.0 dB |
| Peaking | 167 Hz  |  0.34 | -6.5 dB |
| Peaking | 2135 Hz |  2.34 | -9.4 dB |
| Peaking | 2269 Hz |  0.61 | 6.2 dB  |
| Peaking | 8829 Hz |  5.23 | -8.3 dB |
| Peaking | 1411 Hz |  2.29 | -2.0 dB |
| Peaking | 1422 Hz |  5.11 | 3.3 dB  |
| Peaking | 4299 Hz |  5.75 | 2.3 dB  |
| Peaking | 4872 Hz |  7.36 | -3.0 dB |
| Peaking | 7012 Hz | 12.88 | 2.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Sennheiser%20RS%20180/Sennheiser%20RS%20180.png)