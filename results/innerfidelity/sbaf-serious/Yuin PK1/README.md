# Yuin PK1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 5.9; 68 5.4; 73 4.6; 78 3.9; 83 3.3; 89 2.8; 95 2.4; 102 2.2; 109 2.1; 117 2.0; 125 2.0; 134 1.7; 143 1.8; 153 1.8; 164 1.8; 175 1.9; 188 1.7; 201 1.9; 215 1.9; 230 1.9; 246 1.9; 263 1.6; 282 1.8; 301 1.6; 323 1.6; 345 1.5; 369 1.6; 395 1.4; 423 1.6; 452 1.7; 484 1.4; 518 1.1; 554 1.2; 593 1.3; 635 1.1; 679 0.9; 726 0.7; 777 0.7; 832 0.5; 890 0.3; 952 0.1; 1019 -0.1; 1090 -0.2; 1167 -0.4; 1248 -0.9; 1336 -1.4; 1429 -1.9; 1529 -2.4; 1636 -2.9; 1751 -3.1; 1873 -2.8; 2004 -2.2; 2145 -1.5; 2295 -0.7; 2455 0.5; 2627 1.1; 2811 2.0; 3008 3.4; 3219 4.1; 3444 4.9; 3685 4.6; 3943 3.6; 4219 1.8; 4514 0.3; 4830 -0.5; 5168 -0.5; 5530 -1.2; 5917 -1.9; 6331 -1.1; 6775 -0.4; 7249 -0.1; 7756 0.0; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yuin PK1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.51 | 6.6 dB  |
| Peaking | 392 Hz  | 0.61 | 1.5 dB  |
| Peaking | 1765 Hz | 1.79 | -3.9 dB |
| Peaking | 3490 Hz | 2.01 | 6.0 dB  |
| Peaking | 5245 Hz | 1.97 | -2.6 dB |
| Peaking | 40 Hz   | 2.56 | -0.8 dB |
| Peaking | 66 Hz   | 2.82 | 1.3 dB  |
| Peaking | 94 Hz   | 2.65 | -0.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Yuin%20PK1/Yuin%20PK1.png)