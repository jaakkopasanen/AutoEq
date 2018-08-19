# Sennheiser Urbanite

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -0.7; 22 -0.8; 23 -0.9; 25 -1.0; 26 -1.0; 28 -1.1; 30 -1.1; 32 -1.1; 35 -1.1; 37 -1.1; 40 -1.1; 42 -1.1; 45 -1.1; 49 -1.1; 52 -1.2; 56 -1.2; 59 -1.3; 64 -1.4; 68 -1.4; 73 -1.4; 78 -1.6; 83 -1.8; 89 -1.9; 95 -1.9; 102 -1.9; 109 -1.8; 117 -1.7; 125 -1.6; 134 -1.6; 143 -1.8; 153 -2.1; 164 -1.6; 175 -1.4; 188 -1.7; 201 -1.7; 215 -1.4; 230 -1.1; 246 -0.8; 263 -0.6; 282 -0.2; 301 0.0; 323 0.3; 345 0.5; 369 0.6; 395 0.7; 423 0.8; 452 0.9; 484 0.9; 518 1.0; 554 1.0; 593 1.0; 635 0.7; 679 0.4; 726 0.3; 777 0.4; 832 0.3; 890 0.2; 952 0.1; 1019 0.0; 1090 0.0; 1167 0.2; 1248 0.3; 1336 0.3; 1429 0.0; 1529 -0.2; 1636 -0.2; 1751 0.3; 1873 1.3; 2004 2.7; 2145 4.0; 2295 5.4; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999998726dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Urbanite ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 48 Hz   | 0.27 | -0.9 dB |
| Peaking | 203 Hz  | 3.67 | -0.3 dB |
| Peaking | 472 Hz  | 0.56 | 5.6 dB  |
| Peaking | 561 Hz  | 0.24 | -4.8 dB |
| Peaking | 3434 Hz | 0.76 | 8.1 dB  |
| Peaking | 1704 Hz | 4.67 | -1.7 dB |
| Peaking | 2376 Hz | 3.69 | 2.0 dB  |
| Peaking | 3519 Hz | 2.61 | -1.2 dB |
| Peaking | 6261 Hz | 2.2  | 5.7 dB  |
| Peaking | 7388 Hz | 1.49 | -4.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20Urbanite/Sennheiser%20Urbanite.png)