# Sennheiser HD 595

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 5.9; 40 5.4; 42 5.1; 45 4.7; 49 4.1; 52 4.0; 56 4.0; 59 3.8; 64 3.2; 68 3.7; 73 4.1; 78 2.8; 83 1.9; 89 1.3; 95 0.9; 102 0.5; 109 0.2; 117 0.1; 125 -0.3; 134 -0.6; 143 -0.9; 153 -1.0; 164 -0.9; 175 -1.1; 188 -1.2; 201 -1.2; 215 -1.2; 230 -1.2; 246 -1.4; 263 -1.4; 282 -1.3; 301 -1.2; 323 -1.1; 345 -0.9; 369 -0.6; 395 -0.5; 423 -0.2; 452 0.0; 484 -0.2; 518 -0.3; 554 -0.4; 593 -0.4; 635 -0.3; 679 0.8; 726 0.4; 777 0.3; 832 0.3; 890 0.3; 952 0.0; 1019 -0.0; 1090 0.2; 1167 0.5; 1248 0.7; 1336 1.1; 1429 1.3; 1529 1.4; 1636 1.5; 1751 1.7; 1873 1.4; 2004 0.9; 2145 0.6; 2295 0.4; 2455 1.0; 2627 1.7; 2811 1.8; 3008 1.3; 3219 1.0; 3444 1.3; 3685 1.9; 3943 2.4; 4219 3.5; 4514 3.5; 4830 2.6; 5168 3.0; 5530 5.3; 5917 5.9; 6331 5.1; 6775 0.8; 7249 0.8; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -0.9; 20000 -5.7
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 595 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.24 | 6.4 dB  |
| Peaking | 145 Hz  | 0.56 | -3.4 dB |
| Peaking | 717 Hz  | 2.96 | 0.4 dB  |
| Peaking | 3107 Hz | 0.66 | 1.6 dB  |
| Peaking | 5821 Hz | 4.6  | 5.5 dB  |
| Peaking | 1636 Hz | 3.12 | 0.9 dB  |
| Peaking | 2235 Hz | 6.11 | -1.2 dB |
| Peaking | 3250 Hz | 7.99 | -0.9 dB |
| Peaking | 4311 Hz | 7.23 | 2.1 dB  |
| Peaking | 8105 Hz | 1.96 | -0.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20595/Sennheiser%20HD%20595.png)