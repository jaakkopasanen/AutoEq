# Grado GR10

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 3.7; 22 3.6; 23 3.6; 25 3.5; 26 3.5; 28 3.5; 30 3.4; 32 3.5; 35 3.5; 37 3.4; 40 3.3; 42 3.3; 45 3.3; 49 3.2; 52 3.2; 56 3.2; 59 3.2; 64 3.1; 68 3.0; 73 2.7; 78 2.6; 83 2.4; 89 2.1; 95 1.7; 102 1.2; 109 0.7; 117 0.2; 125 -0.4; 134 -0.9; 143 -1.3; 153 -1.5; 164 -1.7; 175 -1.8; 188 -1.8; 201 -1.9; 215 -1.8; 230 -1.8; 246 -1.8; 263 -1.7; 282 -1.6; 301 -1.6; 323 -1.4; 345 -1.3; 369 -1.1; 395 -1.1; 423 -0.9; 452 -0.8; 484 -0.9; 518 -0.8; 554 -0.6; 593 -0.3; 635 -0.3; 679 -0.4; 726 -0.1; 777 0.7; 832 0.8; 890 0.6; 952 0.4; 1019 0.0; 1090 -0.3; 1167 -0.5; 1248 -0.7; 1336 -1.1; 1429 -1.4; 1529 -1.6; 1636 -1.9; 1751 -1.9; 1873 -1.6; 2004 -1.5; 2145 -1.4; 2295 -1.2; 2455 -1.1; 2627 -1.2; 2811 -1.0; 3008 1.2; 3219 4.6; 3444 6.0; 3685 6.0; 3943 5.6; 4219 0.8; 4514 -0.4; 4830 1.5; 5168 3.6; 5530 5.0; 5917 5.1; 6331 4.0; 6775 1.3; 7249 -2.8; 7756 -5.3; 8299 -5.6; 8880 -3.7; 9502 -0.8; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado GR10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 1.06 | 3.8 dB  |
| Peaking | 63 Hz   | 2.23 | 2.7 dB  |
| Peaking | 3615 Hz | 2.71 | 12.7 dB |
| Peaking | 5711 Hz | 3.26 | 11.7 dB |
| Peaking | 4654 Hz | 0.65 | -7.8 dB |
| Peaking | 92 Hz   | 1.91 | 1.9 dB  |
| Peaking | 193 Hz  | 0.67 | -2.2 dB |
| Peaking | 854 Hz  | 3.34 | 1.5 dB  |
| Peaking | 8161 Hz | 4.14 | -6.7 dB |
| Peaking | 9369 Hz | 1.19 | 3.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20GR10/Grado%20GR10.png)