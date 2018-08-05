# Grado GR8

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 2.6; 22 2.5; 23 2.4; 25 2.4; 26 2.3; 28 2.3; 30 2.3; 32 2.3; 35 2.2; 37 2.2; 40 2.2; 42 2.2; 45 2.2; 49 2.1; 52 2.0; 56 1.9; 59 1.8; 64 1.8; 68 1.7; 73 1.6; 78 1.5; 83 1.3; 89 1.0; 95 0.6; 102 0.1; 109 -0.6; 117 -1.2; 125 -1.8; 134 -2.3; 143 -2.6; 153 -2.9; 164 -3.0; 175 -3.1; 188 -3.2; 201 -3.2; 215 -3.2; 230 -3.1; 246 -3.0; 263 -2.8; 282 -2.8; 301 -2.7; 323 -2.5; 345 -2.4; 369 -2.2; 395 -1.7; 423 -1.3; 452 -1.3; 484 -1.2; 518 -1.0; 554 -0.8; 593 -0.5; 635 -0.3; 679 -0.2; 726 -0.0; 777 0.3; 832 0.3; 890 0.1; 952 0.1; 1019 0.0; 1090 -0.1; 1167 -0.1; 1248 -0.1; 1336 -0.4; 1429 -0.9; 1529 -1.4; 1636 -1.7; 1751 -1.8; 1873 -1.6; 2004 -1.6; 2145 -1.5; 2295 -0.9; 2455 0.4; 2627 2.5; 2811 5.5; 3008 6.0; 3219 6.0; 3444 6.0; 3685 5.6; 3943 2.1; 4219 1.1; 4514 2.1; 4830 3.7; 5168 5.5; 5530 6.0; 5917 5.9; 6331 4.3; 6775 0.2; 7249 -2.2; 7756 -1.1; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado GR8 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.3  | 2.6 dB  |
| Peaking | 86 Hz   | 1.36 | 1.9 dB  |
| Peaking | 173 Hz  | 0.59 | -4.2 dB |
| Peaking | 3227 Hz | 3.8  | 7.0 dB  |
| Peaking | 5566 Hz | 4.5  | 6.6 dB  |
| Peaking | 856 Hz  | 1.59 | 0.8 dB  |
| Peaking | 1941 Hz | 1.8  | -2.5 dB |
| Peaking | 2798 Hz | 9.12 | 3.2 dB  |
| Peaking | 6327 Hz | 7.48 | 2.8 dB  |
| Peaking | 7197 Hz | 5.86 | -3.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20GR8/Grado%20GR8.png)