# Sennheiser HD 650

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 5.9; 28 5.6; 30 5.2; 32 4.8; 35 4.2; 37 3.8; 40 3.4; 42 3.1; 45 2.8; 49 2.5; 52 2.3; 56 2.1; 59 1.7; 64 1.2; 68 1.3; 73 1.5; 78 1.0; 83 0.1; 89 -0.5; 95 -0.9; 102 -1.3; 109 -1.5; 117 -1.7; 125 -1.9; 134 -2.1; 143 -2.2; 153 -2.4; 164 -2.2; 175 -2.3; 188 -2.4; 201 -2.5; 215 -2.4; 230 -2.3; 246 -2.2; 263 -2.1; 282 -2.0; 301 -1.9; 323 -1.7; 345 -1.5; 369 -1.4; 395 -1.4; 423 -1.2; 452 -1.0; 484 -1.0; 518 -1.0; 554 -0.8; 593 -0.5; 635 -0.4; 679 -0.5; 726 -0.3; 777 -0.2; 832 -0.4; 890 -0.6; 952 -0.4; 1019 -0.1; 1090 -0.5; 1167 -0.8; 1248 -1.0; 1336 -1.1; 1429 -1.3; 1529 -1.3; 1636 -1.6; 1751 -1.6; 1873 -1.4; 2004 -0.9; 2145 -0.7; 2295 -0.5; 2455 -0.2; 2627 0.1; 2811 -0.1; 3008 -0.6; 3219 -1.1; 3444 -1.0; 3685 -0.6; 3943 0.0; 4219 -0.0; 4514 -0.1; 4830 0.9; 5168 3.8; 5530 5.9; 5917 5.2; 6331 4.4; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 650 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.2dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.6  | 6.2 dB  |
| Peaking | 72 Hz   | 3.55 | 1.2 dB  |
| Peaking | 162 Hz  | 0.56 | -2.8 dB |
| Peaking | 3432 Hz | 0.39 | -1.2 dB |
| Peaking | 5834 Hz | 2.97 | 7.0 dB  |
| Peaking | 828 Hz  | 1.92 | 0.4 dB  |
| Peaking | 1660 Hz | 2.43 | -0.9 dB |
| Peaking | 2722 Hz | 2.69 | 1.8 dB  |
| Peaking | 3136 Hz | 2.42 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20650/Sennheiser%20HD%20650.png)