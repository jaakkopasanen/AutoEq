# Sennheiser Momentum

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 3.7; 22 3.4; 23 3.3; 25 3.1; 26 3.0; 28 2.8; 30 2.7; 32 2.5; 35 2.4; 37 2.3; 40 2.1; 42 2.1; 45 1.9; 49 1.8; 52 1.6; 56 1.4; 59 1.3; 64 1.1; 68 1.0; 73 0.7; 78 0.5; 83 0.3; 89 0.2; 95 0.0; 102 -0.1; 109 -0.2; 117 -0.1; 125 -0.1; 134 -0.1; 143 -0.4; 153 -0.8; 164 -1.1; 175 -0.7; 188 -1.0; 201 -1.2; 215 -1.2; 230 -1.1; 246 -1.0; 263 -0.8; 282 -0.3; 301 -0.3; 323 0.2; 345 0.8; 369 1.2; 395 1.5; 423 1.6; 452 1.6; 484 1.7; 518 1.6; 554 1.6; 593 1.6; 635 1.3; 679 1.0; 726 0.6; 777 0.5; 832 0.3; 890 0.2; 952 0.1; 1019 0.0; 1090 0.2; 1167 0.2; 1248 -0.1; 1336 -0.7; 1429 -1.2; 1529 -1.5; 1636 -1.5; 1751 -1.5; 1873 -1.2; 2004 -0.4; 2145 0.5; 2295 1.8; 2455 3.3; 2627 4.9; 2811 5.8; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999755221dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 1.34 | 3.4 dB  |
| Peaking | 44 Hz   | 2.03 | 1.5 dB  |
| Peaking | 504 Hz  | 2.39 | 1.9 dB  |
| Peaking | 1750 Hz | 1.94 | -4.1 dB |
| Peaking | 3748 Hz | 0.86 | 7.2 dB  |
| Peaking | 203 Hz  | 2.02 | -1.4 dB |
| Peaking | 2777 Hz | 5.9  | 1.5 dB  |
| Peaking | 3826 Hz | 2.53 | -1.0 dB |
| Peaking | 6322 Hz | 2.36 | 5.4 dB  |
| Peaking | 7311 Hz | 1.48 | -4.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20Momentum/Sennheiser%20Momentum.png)