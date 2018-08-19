# Westone W10

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 5.9; 23 5.8; 25 5.6; 26 5.5; 28 5.2; 30 4.9; 32 4.6; 35 4.3; 37 4.1; 40 3.8; 42 3.6; 45 3.3; 49 3.0; 52 2.8; 56 2.5; 59 2.2; 64 1.9; 68 1.6; 73 1.3; 78 0.9; 83 0.6; 89 0.3; 95 -0.1; 102 -0.3; 109 -0.6; 117 -0.8; 125 -1.1; 134 -1.3; 143 -1.5; 153 -1.7; 164 -1.8; 175 -1.8; 188 -2.0; 201 -2.1; 215 -2.1; 230 -2.0; 246 -2.2; 263 -2.2; 282 -2.0; 301 -2.0; 323 -1.9; 345 -1.8; 369 -1.8; 395 -1.8; 423 -1.5; 452 -1.4; 484 -1.3; 518 -1.1; 554 -0.8; 593 -0.4; 635 -0.2; 679 -0.2; 726 -0.1; 777 0.2; 832 0.1; 890 0.1; 952 0.1; 1019 -0.1; 1090 -0.1; 1167 0.0; 1248 0.0; 1336 -0.0; 1429 -0.1; 1529 -0.0; 1636 0.2; 1751 0.6; 1873 1.3; 2004 2.1; 2145 2.9; 2295 3.7; 2455 4.6; 2627 5.3; 2811 5.7; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone W10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.64 | 5.8 dB  |
| Peaking | 55 Hz   | 0.79 | 1.5 dB  |
| Peaking | 209 Hz  | 0.46 | -2.4 dB |
| Peaking | 3941 Hz | 0.95 | 7.0 dB  |
| Peaking | 1612 Hz | 2.64 | -1.5 dB |
| Peaking | 2672 Hz | 2.13 | 1.7 dB  |
| Peaking | 3850 Hz | 2.6  | -1.4 dB |
| Peaking | 6294 Hz | 2.57 | 5.0 dB  |
| Peaking | 7386 Hz | 1.55 | -3.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Westone%20W10/Westone%20W10.png)