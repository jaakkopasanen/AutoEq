# Shure SE110

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 5.9; 26 5.8; 28 5.7; 30 5.6; 32 5.5; 35 5.4; 37 5.3; 40 5.1; 42 5.0; 45 4.9; 49 4.6; 52 4.5; 56 4.3; 59 4.0; 64 3.7; 68 3.5; 73 3.3; 78 3.0; 83 2.6; 89 2.4; 95 2.2; 102 2.0; 109 1.8; 117 1.6; 125 1.2; 134 1.0; 143 0.8; 153 0.6; 164 0.5; 175 0.4; 188 0.3; 201 0.2; 215 0.2; 230 0.2; 246 -0.0; 263 -0.1; 282 -0.1; 301 0.0; 323 0.1; 345 0.2; 369 0.3; 395 0.4; 423 0.5; 452 0.5; 484 0.6; 518 0.7; 554 0.7; 593 0.8; 635 1.0; 679 0.9; 726 0.9; 777 0.9; 832 0.8; 890 0.5; 952 0.2; 1019 -0.1; 1090 -0.4; 1167 -0.7; 1248 -1.2; 1336 -2.0; 1429 -3.1; 1529 -4.1; 1636 -4.7; 1751 -4.9; 1873 -4.6; 2004 -3.6; 2145 -2.1; 2295 -1.4; 2455 -0.5; 2627 1.2; 2811 3.2; 3008 5.2; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE110 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.62 | 5.6 dB  |
| Peaking | 59 Hz   | 0.94 | 2.2 dB  |
| Peaking | 771 Hz  | 1.27 | 1.3 dB  |
| Peaking | 1804 Hz | 1.63 | -7.1 dB |
| Peaking | 3972 Hz | 1    | 7.7 dB  |
| Peaking | 3108 Hz | 7.53 | 2.0 dB  |
| Peaking | 4102 Hz | 3.1  | -0.7 dB |
| Peaking | 5581 Hz | 3.02 | 2.5 dB  |
| Peaking | 6452 Hz | 4.18 | 4.2 dB  |
| Peaking | 6861 Hz | 1.27 | -3.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SE110/Shure%20SE110.png)