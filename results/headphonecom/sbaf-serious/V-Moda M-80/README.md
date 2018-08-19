# V-Moda M-80

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.3dB
GraphicEQ: 10 -84; 20 1.9; 22 1.3; 23 1.1; 25 0.6; 26 0.4; 28 0.0; 30 -0.3; 32 -0.6; 35 -0.9; 37 -1.1; 40 -1.4; 42 -1.5; 45 -1.7; 49 -1.9; 52 -2.1; 56 -2.3; 59 -2.4; 64 -2.6; 68 -2.6; 73 -2.6; 78 -2.6; 83 -2.6; 89 -2.8; 95 -3.0; 102 -2.9; 109 -2.6; 117 -2.7; 125 -2.8; 134 -2.8; 143 -2.9; 153 -2.9; 164 -2.8; 175 -2.7; 188 -2.6; 201 -2.5; 215 -2.4; 230 -2.8; 246 -2.9; 263 -2.3; 282 -1.5; 301 -0.8; 323 -0.5; 345 -0.3; 369 0.3; 395 0.8; 423 1.2; 452 1.7; 484 2.5; 518 3.2; 554 3.9; 593 4.2; 635 4.1; 679 3.9; 726 3.5; 777 3.0; 832 2.3; 890 1.5; 952 0.7; 1019 -0.2; 1090 -1.1; 1167 -1.9; 1248 -2.7; 1336 -3.2; 1429 -3.4; 1529 -3.4; 1636 -3.2; 1751 -2.2; 1873 -1.0; 2004 -0.0; 2145 0.6; 2295 1.2; 2455 1.5; 2627 1.3; 2811 0.7; 3008 0.2; 3219 -0.5; 3444 -0.9; 3685 0.3; 3943 1.7; 4219 2.0; 4514 2.0; 4830 2.0; 5168 3.8; 5530 5.1; 5917 4.4; 6331 3.9; 6775 3.7; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -1.1; 9502 -0.2; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.2573522243989474dB` and instead set Global volume in the UI for both channels to **-52**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-Moda M-80 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.2dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 75 Hz   | 0.86 | -2.3 dB |
| Peaking | 209 Hz  | 0.79 | -2.8 dB |
| Peaking | 614 Hz  | 1.24 | 5.0 dB  |
| Peaking | 1379 Hz | 2.35 | -4.6 dB |
| Peaking | 5695 Hz | 2.73 | 5.2 dB  |
| Peaking | 17 Hz   | 2.28 | 1.9 dB  |
| Peaking | 1705 Hz | 5.16 | -1.7 dB |
| Peaking | 2533 Hz | 1.39 | 1.7 dB  |
| Peaking | 3292 Hz | 5.57 | -2.4 dB |
| Peaking | 8872 Hz | 5.11 | -1.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/V-Moda%20M-80/V-Moda%20M-80.png)