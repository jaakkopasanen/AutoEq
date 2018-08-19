# V-Moda M-100

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -2.4; 22 -2.7; 23 -2.8; 25 -3.0; 26 -3.1; 28 -3.3; 30 -3.4; 32 -3.5; 35 -3.6; 37 -3.6; 40 -3.7; 42 -3.8; 45 -3.9; 49 -4.0; 52 -4.0; 56 -4.1; 59 -4.2; 64 -4.3; 68 -4.3; 73 -4.1; 78 -4.2; 83 -4.8; 89 -5.2; 95 -5.0; 102 -4.5; 109 -4.7; 117 -5.3; 125 -5.6; 134 -5.5; 143 -5.4; 153 -5.2; 164 -4.6; 175 -4.3; 188 -4.1; 201 -3.4; 215 -2.7; 230 -2.0; 246 -1.2; 263 -0.2; 282 0.3; 301 0.4; 323 1.9; 345 2.9; 369 3.5; 395 3.8; 423 3.8; 452 3.6; 484 3.5; 518 3.3; 554 3.1; 593 2.8; 635 2.2; 679 1.7; 726 1.2; 777 0.8; 832 0.5; 890 0.2; 952 -0.0; 1019 -0.1; 1090 -0.1; 1167 0.1; 1248 0.3; 1336 0.4; 1429 0.4; 1529 0.5; 1636 0.5; 1751 0.6; 1873 0.7; 2004 0.5; 2145 -0.1; 2295 0.6; 2455 0.6; 2627 0.6; 2811 0.9; 3008 1.5; 3219 2.0; 3444 1.8; 3685 1.4; 3943 1.5; 4219 2.4; 4514 3.7; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.0; 8880 -2.5; 9502 -4.3; 10167 -3.6; 10879 -0.6; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099750969753474dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-Moda M-100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 45 Hz   | 0.37 | -3.4 dB |
| Peaking | 150 Hz  | 0.89 | -4.2 dB |
| Peaking | 415 Hz  | 1.28 | 5.1 dB  |
| Peaking | 5544 Hz | 1.89 | 6.8 dB  |
| Peaking | 9518 Hz | 3.91 | -5.5 dB |
| Peaking | 604 Hz  | 6.12 | 0.7 dB  |
| Peaking | 974 Hz  | 2.85 | -0.8 dB |
| Peaking | 1889 Hz | 0.49 | 0.1 dB  |
| Peaking | 3246 Hz | 6.67 | 1.0 dB  |
| Peaking | 3892 Hz | 6.66 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/V-Moda%20M-100/V-Moda%20M-100.png)