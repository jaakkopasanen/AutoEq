# Nocs NS700

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.4dB
GraphicEQ: 10 -84; 20 1.4; 22 0.8; 23 0.6; 25 0.1; 26 -0.1; 28 -0.5; 30 -0.8; 32 -1.1; 35 -1.5; 37 -1.7; 40 -1.9; 42 -2.0; 45 -2.0; 49 -2.1; 52 -2.3; 56 -2.5; 59 -2.7; 64 -2.9; 68 -3.1; 73 -3.3; 78 -3.3; 83 -3.2; 89 -2.6; 95 -1.4; 102 -1.3; 109 -1.8; 117 -2.5; 125 -2.7; 134 -2.7; 143 -2.6; 153 -2.2; 164 -1.5; 175 -1.4; 188 -0.8; 201 -0.1; 215 0.5; 230 1.3; 246 2.1; 263 2.8; 282 3.4; 301 2.6; 323 -0.9; 345 -2.2; 369 -1.5; 395 -1.1; 423 -0.9; 452 -0.8; 484 -0.8; 518 -0.7; 554 -0.5; 593 -0.3; 635 -0.2; 679 -0.2; 726 -0.2; 777 -0.2; 832 -0.2; 890 -0.1; 952 -0.1; 1019 0.0; 1090 -0.0; 1167 -0.0; 1248 0.0; 1336 0.2; 1429 0.0; 1529 -0.5; 1636 0.4; 1751 0.7; 1873 0.8; 2004 0.8; 2145 0.8; 2295 0.7; 2455 0.5; 2627 0.0; 2811 -0.5; 3008 -1.5; 3219 -1.4; 3444 -1.4; 3685 -0.6; 3943 1.3; 4219 3.2; 4514 4.3; 4830 2.3; 5168 0.1; 5530 1.2; 5917 2.7; 6331 2.0; 6775 -4.0; 7249 -4.1; 7756 -2.2; 8299 -0.1; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.379582583420295dB` and instead set Global volume in the UI for both channels to **-43**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Nocs NS700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.7dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 90 Hz   |  0.46 | -2.8 dB |
| Peaking | 286 Hz  |  2.46 | 7.0 dB  |
| Peaking | 336 Hz  |  2.94 | -5.1 dB |
| Peaking | 4495 Hz |  6.56 | 4.7 dB  |
| Peaking | 7129 Hz |  9.66 | -5.5 dB |
| Peaking | 17 Hz   |  1.95 | 1.8 dB  |
| Peaking | 71 Hz   |  4.26 | -0.6 dB |
| Peaking | 2122 Hz |  2.66 | 1.1 dB  |
| Peaking | 3208 Hz |  4.01 | -2.1 dB |
| Peaking | 6070 Hz | 11.5  | 3.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Nocs%20NS700/Nocs%20NS700.png)