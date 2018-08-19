# AKG K67 Tiesto

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 1.1; 22 0.5; 23 0.3; 25 -0.1; 26 -0.3; 28 -0.6; 30 -0.8; 32 -0.9; 35 -1.0; 37 -1.1; 40 -1.2; 42 -1.1; 45 -0.9; 49 -0.5; 52 -0.3; 56 -0.3; 59 -0.4; 64 -0.6; 68 -0.8; 73 -1.0; 78 -1.4; 83 -1.9; 89 -2.2; 95 -2.4; 102 -2.6; 109 -2.7; 117 -2.7; 125 -2.6; 134 -2.2; 143 -1.5; 153 -0.3; 164 1.3; 175 2.3; 188 4.1; 201 4.9; 215 5.5; 230 5.9; 246 6.0; 263 6.0; 282 6.0; 301 6.0; 323 6.0; 345 6.0; 369 6.0; 395 5.7; 423 5.2; 452 4.7; 484 4.2; 518 3.8; 554 3.7; 593 3.6; 635 3.2; 679 2.6; 726 2.2; 777 1.8; 832 1.2; 890 0.6; 952 0.3; 1019 -0.0; 1090 -0.2; 1167 -0.4; 1248 -0.4; 1336 -0.4; 1429 -0.6; 1529 -0.9; 1636 -0.7; 1751 -0.2; 1873 1.0; 2004 2.3; 2145 2.8; 2295 3.7; 2455 4.6; 2627 5.6; 2811 5.9; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 5.8; 4514 5.4; 4830 5.5; 5168 5.1; 5530 2.0; 5917 2.6; 6331 3.6; 6775 3.5; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K67 Tiesto ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 104 Hz  | 0.59 | -3.6 dB |
| Peaking | 130 Hz  | 1.41 | -6.0 dB |
| Peaking | 224 Hz  | 0.49 | 9.0 dB  |
| Peaking | 1436 Hz | 1.05 | -3.7 dB |
| Peaking | 3283 Hz | 0.89 | 7.2 dB  |
| Peaking | 36 Hz   | 2.98 | -0.7 dB |
| Peaking | 3744 Hz | 2.46 | -2.2 dB |
| Peaking | 4749 Hz | 1.34 | 4.9 dB  |
| Peaking | 6184 Hz | 1.33 | -5.5 dB |
| Peaking | 6585 Hz | 4.87 | 4.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K67%20Tiesto/AKG%20K67%20Tiesto.png)