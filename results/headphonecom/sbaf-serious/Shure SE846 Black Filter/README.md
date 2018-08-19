# Shure SE846 Black Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -6.4; 22 -6.4; 23 -6.4; 25 -6.5; 26 -6.5; 28 -6.4; 30 -6.4; 32 -6.4; 35 -6.3; 37 -6.3; 40 -6.2; 42 -6.2; 45 -6.2; 49 -6.1; 52 -6.1; 56 -6.1; 59 -6.1; 64 -6.1; 68 -6.1; 73 -6.1; 78 -6.1; 83 -6.1; 89 -6.0; 95 -5.9; 102 -5.8; 109 -5.7; 117 -5.5; 125 -5.4; 134 -5.4; 143 -5.2; 153 -5.1; 164 -4.9; 175 -4.7; 188 -4.5; 201 -4.3; 215 -4.1; 230 -3.8; 246 -3.6; 263 -3.4; 282 -3.1; 301 -2.9; 323 -2.6; 345 -2.3; 369 -2.1; 395 -1.8; 423 -1.6; 452 -1.5; 484 -1.2; 518 -1.1; 554 -0.7; 593 -0.6; 635 -0.2; 679 -0.1; 726 0.1; 777 0.2; 832 0.3; 890 0.2; 952 0.1; 1019 -0.1; 1090 -0.2; 1167 -0.3; 1248 -0.5; 1336 -0.7; 1429 -0.9; 1529 -1.1; 1636 -1.1; 1751 -1.0; 1873 -0.7; 2004 -0.3; 2145 0.2; 2295 0.9; 2455 2.0; 2627 3.5; 2811 5.3; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999573947dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE846 Black Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.28 | -6.0 dB |
| Peaking | 142 Hz  | 0.51 | -3.9 dB |
| Peaking | 1829 Hz | 1.84 | -3.2 dB |
| Peaking | 3895 Hz | 0.92 | 7.2 dB  |
| Peaking | 770 Hz  | 3.02 | 0.8 dB  |
| Peaking | 2957 Hz | 4.84 | 2.4 dB  |
| Peaking | 3440 Hz | 1.26 | -1.2 dB |
| Peaking | 6249 Hz | 2.48 | 5.1 dB  |
| Peaking | 7439 Hz | 1.54 | -3.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SE846%20Black%20Filter/Shure%20SE846%20Black%20Filter.png)