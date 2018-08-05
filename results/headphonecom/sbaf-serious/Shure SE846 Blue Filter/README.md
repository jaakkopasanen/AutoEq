# Shure SE846 Blue Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -4.3; 22 -4.3; 23 -4.3; 25 -4.3; 26 -4.3; 28 -4.3; 30 -4.3; 32 -4.2; 35 -4.1; 37 -4.0; 40 -3.9; 42 -3.9; 45 -3.8; 49 -3.6; 52 -3.5; 56 -3.3; 59 -3.2; 64 -3.1; 68 -3.0; 73 -2.9; 78 -2.8; 83 -2.8; 89 -2.8; 95 -3.0; 102 -3.2; 109 -3.4; 117 -3.7; 125 -4.0; 134 -4.2; 143 -4.3; 153 -4.3; 164 -4.1; 175 -4.0; 188 -3.8; 201 -3.6; 215 -3.4; 230 -3.1; 246 -2.9; 263 -2.7; 282 -2.5; 301 -2.2; 323 -2.0; 345 -1.7; 369 -1.6; 395 -1.4; 423 -1.1; 452 -1.1; 484 -1.0; 518 -0.8; 554 -0.5; 593 -0.3; 635 0.0; 679 0.1; 726 0.2; 777 0.4; 832 0.3; 890 0.2; 952 0.1; 1019 -0.1; 1090 -0.3; 1167 -0.5; 1248 -0.6; 1336 -0.9; 1429 -1.2; 1529 -1.5; 1636 -1.7; 1751 -1.6; 1873 -1.4; 2004 -1.1; 2145 -0.6; 2295 0.3; 2455 1.7; 2627 3.3; 2811 5.3; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE846 Blue Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.54 | -4.2 dB |
| Peaking | 167 Hz  | 0.72 | -3.8 dB |
| Peaking | 773 Hz  | 3.04 | 0.8 dB  |
| Peaking | 1857 Hz | 1.59 | -4.1 dB |
| Peaking | 3814 Hz | 0.91 | 7.5 dB  |
| Peaking | 2345 Hz | 5.62 | -0.8 dB |
| Peaking | 2894 Hz | 5.42 | 1.8 dB  |
| Peaking | 3898 Hz | 3.24 | -1.1 dB |
| Peaking | 6275 Hz | 2.5  | 5.1 dB  |
| Peaking | 7406 Hz | 1.54 | -3.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SE846%20Blue%20Filter/Shure%20SE846%20Blue%20Filter.png)