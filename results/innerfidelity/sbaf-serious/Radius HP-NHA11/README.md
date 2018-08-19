# Radius HP-NHA11

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.1dB
GraphicEQ: 10 -84; 20 -13.1; 22 -13.0; 23 -13.0; 25 -12.8; 26 -12.8; 28 -12.6; 30 -12.5; 32 -12.4; 35 -12.2; 37 -12.1; 40 -11.9; 42 -11.8; 45 -11.7; 49 -11.5; 52 -11.3; 56 -11.2; 59 -11.1; 64 -10.9; 68 -10.8; 73 -10.7; 78 -10.6; 83 -10.5; 89 -10.4; 95 -10.3; 102 -10.1; 109 -9.9; 117 -9.6; 125 -9.4; 134 -9.2; 143 -8.9; 153 -8.6; 164 -8.3; 175 -7.9; 188 -7.5; 201 -7.2; 215 -6.8; 230 -6.3; 246 -5.9; 263 -5.5; 282 -5.0; 301 -4.6; 323 -4.1; 345 -3.6; 369 -3.2; 395 -2.9; 423 -2.4; 452 -1.9; 484 -1.5; 518 -1.3; 554 -0.8; 593 -0.3; 635 -0.0; 679 0.1; 726 0.4; 777 0.7; 832 0.6; 890 0.4; 952 0.2; 1019 -0.0; 1090 -0.4; 1167 -0.7; 1248 -1.1; 1336 -1.7; 1429 -2.4; 1529 -3.2; 1636 -3.9; 1751 -4.4; 1873 -4.7; 2004 -4.8; 2145 -5.0; 2295 -4.8; 2455 -4.1; 2627 -3.8; 2811 -3.0; 3008 -1.6; 3219 -0.5; 3444 0.3; 3685 -0.1; 3943 -1.5; 4219 -4.3; 4514 -7.2; 4830 -8.7; 5168 -6.7; 5530 -3.0; 5917 0.2; 6331 2.1; 6775 3.0; 7249 1.3; 7756 0.3; 8299 -0.2; 8880 -0.9; 9502 -0.8; 10167 -0.1; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.144105690813167dB` and instead set Global volume in the UI for both channels to **-31**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Radius HP-NHA11 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -3.1dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 21 Hz   | 0.19 | -12.6 dB |
| Peaking | 160 Hz  | 0.73 | -4.2 dB  |
| Peaking | 2037 Hz | 2.12 | -5.4 dB  |
| Peaking | 4847 Hz | 4.74 | -9.5 dB  |
| Peaking | 6557 Hz | 4.57 | 4.1 dB   |
| Peaking | 793 Hz  | 2.08 | 1.7 dB   |
| Peaking | 1529 Hz | 5.62 | -1.2 dB  |
| Peaking | 2688 Hz | 6.79 | -1.4 dB  |
| Peaking | 3497 Hz | 6.24 | 2.2 dB   |
| Peaking | 8928 Hz | 6.7  | -1.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Radius%20HP-NHA11/Radius%20HP-NHA11.png)