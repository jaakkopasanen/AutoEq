# Shure SE310

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 5.4; 22 5.3; 23 5.3; 25 5.3; 26 5.3; 28 5.2; 30 5.2; 32 5.1; 35 5.1; 37 5.1; 40 5.1; 42 5.0; 45 4.9; 49 4.8; 52 4.8; 56 4.8; 59 4.8; 64 4.7; 68 4.5; 73 4.3; 78 4.2; 83 4.0; 89 3.7; 95 3.3; 102 2.8; 109 2.3; 117 1.8; 125 1.2; 134 0.7; 143 0.4; 153 0.1; 164 -0.1; 175 -0.1; 188 -0.2; 201 -0.2; 215 -0.2; 230 -0.1; 246 -0.1; 263 -0.1; 282 -0.0; 301 0.1; 323 0.2; 345 0.4; 369 0.5; 395 0.5; 423 0.7; 452 1.0; 484 1.0; 518 1.0; 554 1.3; 593 1.5; 635 1.4; 679 1.4; 726 1.3; 777 1.4; 832 1.2; 890 0.8; 952 0.3; 1019 -0.1; 1090 -0.6; 1167 -1.2; 1248 -1.7; 1336 -2.4; 1429 -3.1; 1529 -3.6; 1636 -4.1; 1751 -4.3; 1873 -4.1; 2004 -3.8; 2145 -3.2; 2295 -2.2; 2455 -0.6; 2627 1.2; 2811 3.2; 3008 5.6; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 5.6; 4514 4.5; 4830 5.2; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE310 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.63 | 5.3 dB  |
| Peaking | 72 Hz   | 1.51 | 3.0 dB  |
| Peaking | 1905 Hz | 1.79 | -6.1 dB |
| Peaking | 5733 Hz | 3.05 | 5.3 dB  |
| Peaking | 3418 Hz | 1.66 | 7.2 dB  |
| Peaking | 191 Hz  | 1.86 | -0.9 dB |
| Peaking | 611 Hz  | 1.38 | 1.4 dB  |
| Peaking | 1374 Hz | 3.54 | -1.1 dB |
| Peaking | 820 Hz  | 3.13 | 0.8 dB  |
| Peaking | 8312 Hz | 4.17 | -1.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SE310/Shure%20SE310.png)