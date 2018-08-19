# Shure SE535

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 4.7; 22 4.6; 23 4.5; 25 4.4; 26 4.3; 28 4.2; 30 4.1; 32 4.1; 35 3.9; 37 3.8; 40 3.7; 42 3.6; 45 3.5; 49 3.3; 52 3.1; 56 2.9; 59 2.7; 64 2.4; 68 2.1; 73 1.8; 78 1.6; 83 1.3; 89 1.0; 95 0.7; 102 0.4; 109 0.3; 117 0.1; 125 -0.2; 134 -0.4; 143 -0.6; 153 -0.8; 164 -0.9; 175 -1.0; 188 -1.2; 201 -1.3; 215 -1.3; 230 -1.4; 246 -1.4; 263 -1.4; 282 -1.3; 301 -1.3; 323 -1.2; 345 -1.1; 369 -1.1; 395 -1.0; 423 -0.8; 452 -0.7; 484 -0.6; 518 -0.6; 554 -0.2; 593 0.0; 635 0.1; 679 0.1; 726 0.2; 777 0.4; 832 0.4; 890 0.2; 952 0.1; 1019 -0.0; 1090 -0.1; 1167 -0.2; 1248 -0.3; 1336 -0.5; 1429 -0.7; 1529 -0.9; 1636 -0.9; 1751 -0.9; 1873 -0.7; 2004 -0.5; 2145 -0.2; 2295 0.6; 2455 2.1; 2627 3.3; 2811 4.4; 3008 5.7; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999997757683dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE535 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.67 | 4.2 dB  |
| Peaking | 53 Hz   | 0.94 | 1.9 dB  |
| Peaking | 227 Hz  | 0.81 | -1.7 dB |
| Peaking | 1870 Hz | 1.81 | -3.0 dB |
| Peaking | 3971 Hz | 0.96 | 7.2 dB  |
| Peaking | 777 Hz  | 3.94 | 0.6 dB  |
| Peaking | 3062 Hz | 3.8  | 2.2 dB  |
| Peaking | 3605 Hz | 1.41 | -1.4 dB |
| Peaking | 6257 Hz | 2.48 | 5.1 dB  |
| Peaking | 7443 Hz | 1.57 | -3.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SE535/Shure%20SE535.png)