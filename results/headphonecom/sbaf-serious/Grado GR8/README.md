# Grado GR8

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 2.5; 22 2.4; 23 2.3; 25 2.3; 26 2.2; 28 2.2; 30 2.1; 32 2.1; 35 1.9; 37 1.8; 40 1.7; 42 1.7; 45 1.6; 49 1.4; 52 1.2; 56 0.9; 59 0.7; 64 0.5; 68 0.3; 73 0.1; 78 -0.2; 83 -0.4; 89 -0.6; 95 -0.8; 102 -1.0; 109 -1.3; 117 -1.6; 125 -1.8; 134 -2.0; 143 -2.2; 153 -2.3; 164 -2.5; 175 -2.6; 188 -2.7; 201 -2.7; 215 -2.8; 230 -2.8; 246 -2.8; 263 -2.6; 282 -2.6; 301 -2.5; 323 -2.4; 345 -2.3; 369 -2.1; 395 -1.6; 423 -1.3; 452 -1.3; 484 -1.1; 518 -0.9; 554 -0.7; 593 -0.6; 635 -0.3; 679 -0.1; 726 0.1; 777 0.2; 832 0.2; 890 0.1; 952 0.1; 1019 0.0; 1090 -0.1; 1167 -0.0; 1248 -0.1; 1336 -0.4; 1429 -0.9; 1529 -1.4; 1636 -1.7; 1751 -1.8; 1873 -1.7; 2004 -1.6; 2145 -1.5; 2295 -0.9; 2455 0.3; 2627 2.5; 2811 5.6; 3008 6.0; 3219 6.0; 3444 6.0; 3685 5.6; 3943 1.8; 4219 1.1; 4514 2.3; 4830 3.7; 5168 5.4; 5530 6.0; 5917 5.9; 6331 4.3; 6775 0.1; 7249 -2.3; 7756 -1.1; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999814357dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado GR8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.2dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.61 | 2.5 dB  |
| Peaking | 201 Hz  | 0.77 | -3.1 dB |
| Peaking | 3200 Hz | 2.27 | 11.2 dB |
| Peaking | 3538 Hz | 0.64 | -4.8 dB |
| Peaking | 5549 Hz | 3.23 | 8.7 dB  |
| Peaking | 374 Hz  | 1.89 | -0.7 dB |
| Peaking | 1330 Hz | 0.62 | 1.5 dB  |
| Peaking | 1874 Hz | 1.61 | -2.4 dB |
| Peaking | 7162 Hz | 6.34 | -5.1 dB |
| Peaking | 7260 Hz | 2.21 | 2.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20GR8/Grado%20GR8.png)