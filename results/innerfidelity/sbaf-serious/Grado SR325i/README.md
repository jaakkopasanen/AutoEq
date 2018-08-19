# Grado SR325i

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 5.9; 40 5.5; 42 5.0; 45 4.4; 49 3.5; 52 2.9; 56 2.2; 59 1.6; 64 0.7; 68 0.1; 73 -0.4; 78 -0.9; 83 -1.4; 89 -1.8; 95 -2.2; 102 -2.3; 109 -2.4; 117 -2.5; 125 -2.5; 134 -2.5; 143 -2.4; 153 -2.4; 164 -2.3; 175 -2.0; 188 -1.8; 201 -1.6; 215 -1.4; 230 -1.2; 246 -1.1; 263 -1.0; 282 -0.7; 301 -0.8; 323 -0.8; 345 -0.5; 369 -0.4; 395 -0.3; 423 0.1; 452 0.3; 484 0.0; 518 -0.2; 554 0.1; 593 0.3; 635 0.4; 679 0.3; 726 0.3; 777 0.4; 832 0.3; 890 0.1; 952 0.0; 1019 -0.0; 1090 -0.1; 1167 -0.3; 1248 -0.7; 1336 -1.3; 1429 -2.2; 1529 -3.1; 1636 -3.7; 1751 -4.0; 1873 -5.9; 2004 -8.6; 2145 -8.3; 2295 -6.9; 2455 -5.2; 2627 -4.0; 2811 -2.4; 3008 -1.0; 3219 0.0; 3444 0.9; 3685 0.7; 3943 -2.0; 4219 -7.5; 4514 -7.9; 4830 -4.4; 5168 -2.2; 5530 -1.2; 5917 -1.2; 6331 -1.3; 6775 -2.4; 7249 -4.4; 7756 -5.3; 8299 -6.8; 8880 -9.2; 9502 -10.5; 10167 -8.1; 10879 -2.8; 11640 -0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR325i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.4dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 30 Hz    | 0.57 | 7.1 dB   |
| Peaking | 99 Hz    | 0.73 | -4.4 dB  |
| Peaking | 2096 Hz  | 2.65 | -8.6 dB  |
| Peaking | 9130 Hz  | 2.68 | -10.5 dB |
| Peaking | 24000 Hz | 2.3  | -7.5 dB  |
| Peaking | 743 Hz   | 1.48 | 0.8 dB   |
| Peaking | 3685 Hz  | 3.68 | 5.2 dB   |
| Peaking | 4345 Hz  | 4.39 | -9.9 dB  |
| Peaking | 5585 Hz  | 4.17 | 1.5 dB   |
| Peaking | 11924 Hz | 5.02 | 2.7 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20SR325i/Grado%20SR325i.png)