# Shure SE846 White Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -3.4; 22 -3.5; 23 -3.5; 25 -3.5; 26 -3.5; 28 -3.5; 30 -3.5; 32 -3.5; 35 -3.4; 37 -3.4; 40 -3.4; 42 -3.4; 45 -3.4; 49 -3.4; 52 -3.4; 56 -3.4; 59 -3.4; 64 -3.5; 68 -3.5; 73 -3.5; 78 -3.5; 83 -3.5; 89 -3.5; 95 -3.4; 102 -3.4; 109 -3.3; 117 -3.2; 125 -3.1; 134 -3.0; 143 -3.0; 153 -2.9; 164 -2.8; 175 -2.6; 188 -2.4; 201 -2.2; 215 -2.1; 230 -1.9; 246 -1.7; 263 -1.7; 282 -1.4; 301 -1.4; 323 -1.2; 345 -0.9; 369 -0.8; 395 -0.7; 423 -0.4; 452 -0.4; 484 -0.3; 518 -0.2; 554 -0.1; 593 0.1; 635 0.3; 679 0.4; 726 0.5; 777 0.6; 832 0.5; 890 0.4; 952 0.2; 1019 -0.1; 1090 -0.4; 1167 -0.6; 1248 -0.8; 1336 -1.2; 1429 -1.6; 1529 -2.1; 1636 -2.5; 1751 -2.6; 1873 -2.6; 2004 -2.5; 2145 -2.2; 2295 -1.3; 2455 0.0; 2627 1.9; 2811 4.0; 3008 5.8; 3219 6.0; 3444 6.0; 3685 6.0; 3943 5.7; 4219 4.3; 4514 3.8; 4830 4.5; 5168 5.8; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 -0.2; 8299 -0.9; 8880 -0.9; 9502 -0.7; 10167 -0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999998308316dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE846 White Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 51 Hz   | 0.25 | -3.7 dB |
| Peaking | 2032 Hz | 1.73 | -4.8 dB |
| Peaking | 3237 Hz | 1.73 | 7.0 dB  |
| Peaking | 6022 Hz | 2.05 | 6.3 dB  |
| Peaking | 8051 Hz | 2.27 | -3.3 dB |
| Peaking | 15 Hz   | 0.99 | -0.5 dB |
| Peaking | 46 Hz   | 2.17 | 0.5 dB  |
| Peaking | 758 Hz  | 1.9  | 1.0 dB  |
| Peaking | 1470 Hz | 4.24 | -0.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SE846%20White%20Filter/Shure%20SE846%20White%20Filter.png)