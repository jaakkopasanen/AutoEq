# Shure SE210

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 5.8; 52 5.5; 56 5.1; 59 4.8; 64 4.4; 68 4.0; 73 3.6; 78 3.3; 83 3.0; 89 2.6; 95 2.4; 102 2.0; 109 1.8; 117 1.6; 125 1.2; 134 1.0; 143 0.8; 153 0.6; 164 0.5; 175 0.2; 188 0.0; 201 -0.0; 215 -0.1; 230 -0.1; 246 -0.1; 263 -0.1; 282 -0.1; 301 -0.2; 323 -0.1; 345 0.0; 369 0.1; 395 0.2; 423 0.3; 452 0.2; 484 0.1; 518 0.3; 554 0.4; 593 0.6; 635 0.7; 679 0.7; 726 0.7; 777 0.7; 832 0.6; 890 0.4; 952 0.2; 1019 -0.0; 1090 -0.3; 1167 -0.5; 1248 -0.8; 1336 -1.2; 1429 -1.9; 1529 -2.7; 1636 -3.2; 1751 -3.3; 1873 -3.0; 2004 -2.6; 2145 -2.0; 2295 -1.1; 2455 -0.0; 2627 1.2; 2811 2.5; 3008 3.8; 3219 5.1; 3444 5.9; 3685 6.0; 3943 5.1; 4219 3.7; 4514 2.7; 4830 2.9; 5168 3.9; 5530 4.9; 5917 5.0; 6331 3.9; 6775 1.5; 7249 -1.5; 7756 -3.9; 8299 -4.8; 8880 -2.2; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE210 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.56 | 6.6 dB  |
| Peaking | 1819 Hz | 2.17 | -4.1 dB |
| Peaking | 3480 Hz | 2.39 | 6.3 dB  |
| Peaking | 5887 Hz | 3.19 | 5.2 dB  |
| Peaking | 8013 Hz | 4.53 | -6.2 dB |
| Peaking | 20 Hz   | 0.38 | 1.6 dB  |
| Peaking | 31 Hz   | 1.45 | -2.1 dB |
| Peaking | 201 Hz  | 1.05 | -0.7 dB |
| Peaking | 725 Hz  | 2.07 | 1.0 dB  |
| Peaking | 9532 Hz | 9.75 | 0.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SE210/Shure%20SE210.png)