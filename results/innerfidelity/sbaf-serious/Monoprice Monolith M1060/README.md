# Monoprice Monolith M1060

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 4.3; 22 4.2; 23 4.2; 25 4.3; 26 4.3; 28 4.3; 30 4.4; 32 4.4; 35 4.4; 37 4.3; 40 4.0; 42 3.7; 45 3.3; 49 3.0; 52 3.0; 56 3.0; 59 2.9; 64 2.8; 68 2.7; 73 2.6; 78 2.5; 83 2.2; 89 1.8; 95 1.5; 102 1.3; 109 1.2; 117 1.1; 125 0.9; 134 0.7; 143 0.5; 153 0.4; 164 0.3; 175 0.1; 188 -0.1; 201 -0.3; 215 -0.3; 230 -0.3; 246 -0.3; 263 -0.2; 282 0.2; 301 0.1; 323 -0.1; 345 0.2; 369 0.5; 395 0.9; 423 0.9; 452 0.7; 484 0.4; 518 0.2; 554 0.2; 593 -0.1; 635 -0.3; 679 -0.6; 726 -0.5; 777 -0.3; 832 0.2; 890 0.6; 952 0.1; 1019 0.2; 1090 0.1; 1167 -0.3; 1248 -0.5; 1336 -0.5; 1429 -1.1; 1529 -1.6; 1636 -1.2; 1751 0.2; 1873 1.7; 2004 2.7; 2145 3.1; 2295 3.3; 2455 2.7; 2627 2.7; 2811 3.4; 3008 3.7; 3219 3.3; 3444 3.7; 3685 3.0; 3943 2.8; 4219 5.9; 4514 5.9; 4830 5.4; 5168 6.0; 5530 6.0; 5917 5.9; 6331 4.6; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -0.0; 18692 -2.8; 20000 -7.5
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099993182728349dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monoprice Monolith M1060 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.49 | 4.5 dB  |
| Peaking | 1161 Hz | 0.84 | -0.7 dB |
| Peaking | 1545 Hz | 3.31 | -3.6 dB |
| Peaking | 2242 Hz | 0.94 | 3.5 dB  |
| Peaking | 5218 Hz | 2.03 | 5.9 dB  |
| Peaking | 214 Hz  | 2.46 | -0.8 dB |
| Peaking | 420 Hz  | 3.94 | 1.0 dB  |
| Peaking | 684 Hz  | 7.11 | -0.8 dB |
| Peaking | 6586 Hz | 4.27 | 2.7 dB  |
| Peaking | 7543 Hz | 1.96 | -2.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monoprice%20Monolith%20M1060/Monoprice%20Monolith%20M1060.png)