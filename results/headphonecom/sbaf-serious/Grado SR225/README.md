# Grado SR225

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 5.7; 52 5.1; 56 4.1; 59 3.5; 64 2.6; 68 2.0; 73 1.3; 78 0.8; 83 0.3; 89 -0.0; 95 -0.4; 102 -0.7; 109 -0.9; 117 -1.1; 125 -1.1; 134 -1.1; 143 -1.1; 153 -1.1; 164 -1.1; 175 -1.0; 188 -1.0; 201 -1.0; 215 -1.0; 230 -0.8; 246 -0.7; 263 -0.7; 282 -0.7; 301 -0.6; 323 -0.3; 345 0.1; 369 0.3; 395 0.4; 423 0.3; 452 0.3; 484 0.3; 518 0.5; 554 0.4; 593 0.5; 635 0.7; 679 0.7; 726 0.7; 777 0.6; 832 0.5; 890 0.4; 952 0.2; 1019 -0.1; 1090 -0.3; 1167 -0.6; 1248 -0.9; 1336 -1.6; 1429 -2.3; 1529 -3.1; 1636 -3.9; 1751 -4.3; 1873 -4.9; 2004 -5.2; 2145 -5.5; 2295 -5.4; 2455 -4.8; 2627 -4.5; 2811 -4.5; 3008 -4.4; 3219 -4.3; 3444 -4.5; 3685 -6.1; 3943 -9.2; 4219 -11.1; 4514 -9.8; 4830 -8.2; 5168 -7.5; 5530 -7.9; 5917 -7.6; 6331 -5.8; 6775 -4.4; 7249 -1.4; 7756 -2.0; 8299 -4.6; 8880 -8.7; 9502 -11.9; 10167 -11.6; 10879 -8.3; 11640 -4.9; 12455 -3.2; 13327 -3.3; 14260 -3.9; 15258 -3.0; 16326 -0.3; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR225 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.4dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 41 Hz    | 0.34 | 7.9 dB   |
| Peaking | 101 Hz   | 0.69 | -6.1 dB  |
| Peaking | 2033 Hz  | 2.06 | -4.8 dB  |
| Peaking | 4479 Hz  | 1.86 | -9.7 dB  |
| Peaking | 9980 Hz  | 2.9  | -11.9 dB |
| Peaking | 716 Hz   | 1.7  | 1.1 dB   |
| Peaking | 4898 Hz  | 6.17 | 3.0 dB   |
| Peaking | 5937 Hz  | 2.13 | -2.9 dB  |
| Peaking | 7483 Hz  | 5.53 | 4.6 dB   |
| Peaking | 14500 Hz | 4.77 | -3.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20SR225/Grado%20SR225.png)