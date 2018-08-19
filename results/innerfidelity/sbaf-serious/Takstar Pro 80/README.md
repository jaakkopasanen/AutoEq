# Takstar Pro 80

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 3.2; 22 2.8; 23 2.6; 25 2.3; 26 2.2; 28 1.9; 30 1.7; 32 1.6; 35 1.4; 37 1.3; 40 1.2; 42 1.2; 45 1.1; 49 1.0; 52 0.9; 56 0.8; 59 0.8; 64 0.7; 68 0.6; 73 0.5; 78 0.3; 83 0.2; 89 -0.1; 95 -0.2; 102 -0.3; 109 -0.2; 117 -0.4; 125 -0.8; 134 -1.2; 143 -1.5; 153 -1.4; 164 -1.0; 175 -1.2; 188 -1.4; 201 -1.3; 215 -1.3; 230 -1.0; 246 -0.9; 263 -0.8; 282 -0.5; 301 -0.2; 323 0.1; 345 0.5; 369 0.8; 395 1.3; 423 1.8; 452 2.1; 484 2.0; 518 2.0; 554 1.9; 593 1.8; 635 1.5; 679 1.1; 726 0.9; 777 0.9; 832 1.3; 890 1.0; 952 0.5; 1019 0.1; 1090 -0.2; 1167 -0.5; 1248 -1.1; 1336 -1.6; 1429 -2.2; 1529 -3.0; 1636 -3.5; 1751 -3.6; 1873 -4.0; 2004 -3.9; 2145 -3.0; 2295 -1.5; 2455 0.6; 2627 2.7; 2811 4.5; 3008 5.9; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 5.7; 4830 2.5; 5168 3.3; 5530 5.4; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -1.2; 8880 -3.6; 9502 -4.1; 10167 -3.0; 10879 -0.5; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.09999999925969dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Takstar Pro 80 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.2dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 21 Hz   | 1.11 | 2.8 dB   |
| Peaking | 1963 Hz | 1.1  | -16.7 dB |
| Peaking | 2604 Hz | 0.54 | 13.9 dB  |
| Peaking | 6228 Hz | 6.4  | 2.9 dB   |
| Peaking | 9214 Hz | 2.45 | -6.7 dB  |
| Peaking | 196 Hz  | 1.14 | -1.7 dB  |
| Peaking | 474 Hz  | 1.92 | 1.9 dB   |
| Peaking | 1312 Hz | 3.15 | -0.9 dB  |
| Peaking | 4767 Hz | 2.33 | 1.6 dB   |
| Peaking | 4927 Hz | 8.39 | -4.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Takstar%20Pro%2080/Takstar%20Pro%2080.png)