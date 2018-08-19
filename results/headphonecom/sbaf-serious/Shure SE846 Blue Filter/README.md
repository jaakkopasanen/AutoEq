# Shure SE846 Blue Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -4.4; 22 -4.4; 23 -4.4; 25 -4.4; 26 -4.4; 28 -4.4; 30 -4.4; 32 -4.4; 35 -4.4; 37 -4.4; 40 -4.4; 42 -4.4; 45 -4.3; 49 -4.3; 52 -4.3; 56 -4.3; 59 -4.3; 64 -4.4; 68 -4.4; 73 -4.4; 78 -4.4; 83 -4.4; 89 -4.4; 95 -4.3; 102 -4.3; 109 -4.2; 117 -4.1; 125 -4.0; 134 -3.9; 143 -3.9; 153 -3.8; 164 -3.6; 175 -3.5; 188 -3.3; 201 -3.2; 215 -3.0; 230 -2.8; 246 -2.6; 263 -2.5; 282 -2.3; 301 -2.1; 323 -1.8; 345 -1.6; 369 -1.5; 395 -1.3; 423 -1.1; 452 -1.1; 484 -0.9; 518 -0.6; 554 -0.5; 593 -0.4; 635 -0.0; 679 0.2; 726 0.3; 777 0.4; 832 0.3; 890 0.3; 952 0.1; 1019 -0.1; 1090 -0.3; 1167 -0.4; 1248 -0.6; 1336 -0.9; 1429 -1.2; 1529 -1.5; 1636 -1.6; 1751 -1.6; 1873 -1.4; 2004 -1.1; 2145 -0.6; 2295 0.4; 2455 1.6; 2627 3.4; 2811 5.4; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999678132dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE846 Blue Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 51 Hz   | 0.2  | -4.6 dB |
| Peaking | 1917 Hz | 1.91 | -2.9 dB |
| Peaking | 3080 Hz | 2.11 | 5.8 dB  |
| Peaking | 4547 Hz | 2.26 | 4.5 dB  |
| Peaking | 6015 Hz | 4.07 | 4.4 dB  |
| Peaking | 11 Hz   | 1.6  | -0.7 dB |
| Peaking | 761 Hz  | 2.4  | 0.9 dB  |
| Peaking | 1459 Hz | 5.28 | -0.5 dB |
| Peaking | 8272 Hz | 4.12 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SE846%20Blue%20Filter/Shure%20SE846%20Blue%20Filter.png)