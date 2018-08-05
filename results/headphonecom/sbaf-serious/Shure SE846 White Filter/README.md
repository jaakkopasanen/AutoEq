# Shure SE846 White Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -3.4; 22 -3.4; 23 -3.4; 25 -3.4; 26 -3.4; 28 -3.4; 30 -3.3; 32 -3.3; 35 -3.1; 37 -3.1; 40 -3.0; 42 -2.9; 45 -2.8; 49 -2.7; 52 -2.6; 56 -2.4; 59 -2.3; 64 -2.2; 68 -2.1; 73 -1.9; 78 -1.9; 83 -1.9; 89 -1.9; 95 -2.1; 102 -2.3; 109 -2.5; 117 -2.8; 125 -3.1; 134 -3.3; 143 -3.4; 153 -3.4; 164 -3.3; 175 -3.1; 188 -2.9; 201 -2.7; 215 -2.4; 230 -2.2; 246 -2.0; 263 -1.9; 282 -1.6; 301 -1.5; 323 -1.4; 345 -1.0; 369 -0.9; 395 -0.8; 423 -0.4; 452 -0.4; 484 -0.4; 518 -0.3; 554 -0.1; 593 0.2; 635 0.3; 679 0.3; 726 0.4; 777 0.7; 832 0.6; 890 0.4; 952 0.2; 1019 -0.1; 1090 -0.4; 1167 -0.6; 1248 -0.8; 1336 -1.3; 1429 -1.7; 1529 -2.1; 1636 -2.5; 1751 -2.7; 1873 -2.6; 2004 -2.5; 2145 -2.2; 2295 -1.3; 2455 0.1; 2627 1.9; 2811 4.0; 3008 5.8; 3219 6.0; 3444 6.0; 3685 6.0; 3943 5.9; 4219 4.3; 4514 3.7; 4830 4.4; 5168 5.8; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 -0.2; 8299 -1.1; 8880 -1.0; 9502 -0.5; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE846 White Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.53 | -3.4 dB |
| Peaking | 162 Hz  | 1.02 | -3.1 dB |
| Peaking | 2006 Hz | 1.72 | -4.6 dB |
| Peaking | 3300 Hz | 1.76 | 7.3 dB  |
| Peaking | 5761 Hz | 3.44 | 5.6 dB  |
| Peaking | 308 Hz  | 3.5  | -0.4 dB |
| Peaking | 778 Hz  | 2.08 | 0.9 dB  |
| Peaking | 1452 Hz | 4.35 | -0.6 dB |
| Peaking | 6633 Hz | 8.31 | 2.0 dB  |
| Peaking | 8338 Hz | 3.29 | -2.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SE846%20White%20Filter/Shure%20SE846%20White%20Filter.png)