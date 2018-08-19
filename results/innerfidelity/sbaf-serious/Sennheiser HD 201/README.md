# Sennheiser HD 201

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 6.0; 95 6.0; 102 6.0; 109 6.0; 117 6.0; 125 6.0; 134 6.0; 143 5.7; 153 5.3; 164 5.1; 175 4.7; 188 4.5; 201 4.4; 215 4.3; 230 4.1; 246 3.5; 263 3.2; 282 3.0; 301 2.6; 323 2.2; 345 1.9; 369 1.5; 395 1.1; 423 0.9; 452 0.6; 484 0.3; 518 0.4; 554 0.5; 593 0.7; 635 0.8; 679 0.6; 726 0.3; 777 -0.2; 832 -0.6; 890 -0.7; 952 -0.3; 1019 0.2; 1090 0.2; 1167 -0.2; 1248 0.1; 1336 0.1; 1429 0.0; 1529 0.3; 1636 1.0; 1751 0.3; 1873 0.1; 2004 0.5; 2145 0.9; 2295 1.7; 2455 2.7; 2627 3.4; 2811 3.5; 3008 3.7; 3219 4.2; 3444 3.6; 3685 2.6; 3943 3.0; 4219 5.3; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -2.6; 8880 -4.5; 9502 -3.3; 10167 -0.7; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 201 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 19 Hz   |  0.16 | 6.0 dB  |
| Peaking | 149 Hz  |  0.74 | 3.1 dB  |
| Peaking | 2870 Hz |  3.23 | 2.6 dB  |
| Peaking | 5425 Hz |  1.42 | 6.8 dB  |
| Peaking | 8834 Hz |  3.79 | -6.6 dB |
| Peaking | 266 Hz  |  3.02 | 0.4 dB  |
| Peaking | 470 Hz  |  4.7  | -0.7 dB |
| Peaking | 876 Hz  |  4.76 | -1.2 dB |
| Peaking | 4452 Hz | 12.02 | 1.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20201/Sennheiser%20HD%20201.png)