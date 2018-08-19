# Grado GR10

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 3.6; 22 3.5; 23 3.5; 25 3.4; 26 3.4; 28 3.3; 30 3.3; 32 3.3; 35 3.2; 37 3.1; 40 2.9; 42 2.8; 45 2.7; 49 2.5; 52 2.4; 56 2.2; 59 2.1; 64 1.8; 68 1.6; 73 1.2; 78 0.9; 83 0.7; 89 0.5; 95 0.3; 102 0.1; 109 -0.0; 117 -0.2; 125 -0.4; 134 -0.6; 143 -0.8; 153 -1.0; 164 -1.1; 175 -1.3; 188 -1.3; 201 -1.4; 215 -1.4; 230 -1.5; 246 -1.5; 263 -1.5; 282 -1.5; 301 -1.4; 323 -1.3; 345 -1.2; 369 -1.0; 395 -1.0; 423 -0.9; 452 -0.9; 484 -0.8; 518 -0.7; 554 -0.5; 593 -0.4; 635 -0.3; 679 -0.3; 726 0.0; 777 0.6; 832 0.7; 890 0.6; 952 0.4; 1019 0.0; 1090 -0.3; 1167 -0.5; 1248 -0.7; 1336 -1.0; 1429 -1.4; 1529 -1.7; 1636 -1.9; 1751 -1.8; 1873 -1.6; 2004 -1.5; 2145 -1.4; 2295 -1.2; 2455 -1.2; 2627 -1.2; 2811 -0.9; 3008 1.1; 3219 4.7; 3444 6.0; 3685 6.0; 3943 5.5; 4219 0.8; 4514 -0.3; 4830 1.5; 5168 3.6; 5530 5.0; 5917 5.2; 6331 4.0; 6775 1.2; 7249 -2.9; 7756 -5.3; 8299 -5.4; 8880 -3.6; 9502 -0.9; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999984438796dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado GR10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 1.25 | 3.6 dB  |
| Peaking | 51 Hz   | 2.11 | 2.0 dB  |
| Peaking | 3586 Hz | 2.72 | 12.6 dB |
| Peaking | 4668 Hz | 0.65 | -7.7 dB |
| Peaking | 5759 Hz | 3.28 | 11.6 dB |
| Peaking | 247 Hz  | 0.89 | -1.6 dB |
| Peaking | 857 Hz  | 3.6  | 1.5 dB  |
| Peaking | 6613 Hz | 8.27 | 2.9 dB  |
| Peaking | 8090 Hz | 2.78 | -6.8 dB |
| Peaking | 9536 Hz | 1.31 | 3.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20GR10/Grado%20GR10.png)