# Sennheiser Momentum M2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 5.8; 23 5.6; 25 5.3; 26 5.1; 28 4.7; 30 4.4; 32 4.1; 35 3.7; 37 3.5; 40 3.2; 42 3.1; 45 2.9; 49 2.6; 52 2.4; 56 2.3; 59 2.1; 64 1.8; 68 1.6; 73 1.4; 78 1.3; 83 1.1; 89 0.9; 95 0.7; 102 0.7; 109 0.7; 117 0.7; 125 0.8; 134 0.8; 143 1.1; 153 0.8; 164 0.9; 175 1.2; 188 1.3; 201 1.4; 215 1.3; 230 1.5; 246 2.1; 263 2.2; 282 1.5; 301 1.2; 323 1.4; 345 1.3; 369 1.2; 395 1.2; 423 1.1; 452 1.1; 484 0.6; 518 0.3; 554 0.3; 593 0.4; 635 0.3; 679 0.2; 726 -0.0; 777 0.0; 832 -0.0; 890 -0.1; 952 -0.2; 1019 -0.1; 1090 0.1; 1167 0.0; 1248 -0.6; 1336 -0.2; 1429 -0.7; 1529 -1.6; 1636 -1.9; 1751 -2.0; 1873 -2.3; 2004 -1.8; 2145 -1.0; 2295 0.0; 2455 1.3; 2627 2.2; 2811 3.2; 3008 5.1; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 2.0; 5168 2.8; 5530 5.7; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum M2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 17 Hz   | 0.51 | 6.1 dB  |
| Peaking | 276 Hz  | 1.12 | 1.7 dB  |
| Peaking | 1881 Hz | 2.11 | -3.5 dB |
| Peaking | 3558 Hz | 1.65 | 6.9 dB  |
| Peaking | 6061 Hz | 4.86 | 5.2 dB  |
| Peaking | 54 Hz   | 2.09 | 0.3 dB  |
| Peaking | 6636 Hz | 9.25 | 1.6 dB  |
| Peaking | 7889 Hz | 2.33 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20Momentum%20M2/Sennheiser%20Momentum%20M2.png)