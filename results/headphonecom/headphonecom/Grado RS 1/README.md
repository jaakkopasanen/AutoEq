# Grado RS 1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 5.9; 30 5.4; 32 4.7; 35 3.5; 37 2.7; 40 1.7; 42 1.1; 45 0.2; 49 -0.7; 52 -1.3; 56 -2.2; 59 -2.8; 64 -3.7; 68 -4.3; 73 -5.0; 78 -5.5; 83 -5.8; 89 -6.1; 95 -6.2; 102 -6.4; 109 -6.4; 117 -6.4; 125 -6.2; 134 -6.0; 143 -5.7; 153 -5.4; 164 -5.0; 175 -4.6; 188 -4.5; 201 -4.4; 215 -4.1; 230 -3.8; 246 -3.5; 263 -3.2; 282 -2.7; 301 -2.0; 323 -1.7; 345 -3.0; 369 -2.9; 395 -2.6; 423 -2.1; 452 -1.8; 484 -1.4; 518 -1.1; 554 -0.8; 593 -0.5; 635 -0.2; 679 0.0; 726 0.1; 777 0.1; 832 0.2; 890 0.1; 952 0.1; 1019 -0.0; 1090 -0.1; 1167 -0.1; 1248 0.1; 1336 0.2; 1429 0.3; 1529 0.2; 1636 -0.9; 1751 -3.9; 1873 -6.5; 2004 -5.5; 2145 -4.7; 2295 -3.9; 2455 -3.2; 2627 -2.1; 2811 -1.0; 3008 0.3; 3219 1.2; 3444 2.1; 3685 2.7; 3943 1.9; 4219 -2.0; 4514 -6.9; 4830 -8.2; 5168 -4.7; 5530 -4.6; 5917 -4.6; 6331 -1.8; 6775 1.2; 7249 0.4; 7756 -2.7; 8299 -7.0; 8880 -10.1; 9502 -10.1; 10167 -6.9; 10879 -2.3; 11640 -0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado RS 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 26 Hz    | 0.67 | 8.3 dB   |
| Peaking | 94 Hz    | 0.48 | -7.7 dB  |
| Peaking | 2004 Hz  | 3.87 | -6.3 dB  |
| Peaking | 9186 Hz  | 3.65 | -11.3 dB |
| Peaking | 24000 Hz | 2.2  | -7.8 dB  |
| Peaking | 1406 Hz  | 3.31 | 1.6 dB   |
| Peaking | 3892 Hz  | 2.72 | 11.8 dB  |
| Peaking | 4519 Hz  | 1.98 | -13.0 dB |
| Peaking | 6973 Hz  | 5.6  | 5.6 dB   |
| Peaking | 11833 Hz | 4.23 | 2.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Grado%20RS%201/Grado%20RS%201.png)