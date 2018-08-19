# Sennheiser HD 595

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 5.9; 68 5.5; 73 5.2; 78 4.8; 83 4.3; 89 3.5; 95 2.9; 102 2.4; 109 2.1; 117 1.8; 125 1.3; 134 1.0; 143 0.7; 153 0.5; 164 0.4; 175 0.2; 188 0.0; 201 -0.0; 215 -0.2; 230 -0.1; 246 -0.1; 263 -0.1; 282 -0.2; 301 -0.2; 323 -0.2; 345 -0.2; 369 -0.2; 395 -0.1; 423 -0.0; 452 0.0; 484 -0.1; 518 -0.0; 554 0.5; 593 0.7; 635 0.7; 679 0.4; 726 0.4; 777 0.5; 832 0.3; 890 0.2; 952 0.1; 1019 -0.1; 1090 -0.2; 1167 -0.2; 1248 -0.5; 1336 -0.4; 1429 -0.3; 1529 -0.2; 1636 0.2; 1751 0.7; 1873 1.5; 2004 1.9; 2145 1.8; 2295 1.4; 2455 1.2; 2627 1.0; 2811 1.0; 3008 1.7; 3219 2.2; 3444 2.8; 3685 3.8; 3943 4.8; 4219 4.4; 4514 3.9; 4830 3.2; 5168 3.4; 5530 4.3; 5917 5.3; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.6; 9502 -1.2; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -0.2; 18692 -0.9; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 595 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 38 Hz   | 0.58 | 6.9 dB  |
| Peaking | 649 Hz  | 3.25 | 0.4 dB  |
| Peaking | 4015 Hz | 1.88 | 4.1 dB  |
| Peaking | 6257 Hz | 3.32 | 5.6 dB  |
| Peaking | 8103 Hz | 1.74 | -1.7 dB |
| Peaking | 38 Hz   | 2.59 | -1.1 dB |
| Peaking | 73 Hz   | 1.93 | 1.5 dB  |
| Peaking | 181 Hz  | 0.82 | -0.9 dB |
| Peaking | 1395 Hz | 2.82 | -0.8 dB |
| Peaking | 2001 Hz | 4.86 | 1.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20595/Sennheiser%20HD%20595.png)