# Massdrop x Sennheiser HD 6XX

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 5.8; 42 5.5; 45 5.0; 49 4.5; 52 4.2; 56 4.0; 59 3.8; 64 3.2; 68 2.8; 73 2.7; 78 2.1; 83 1.1; 89 0.3; 95 -0.2; 102 -0.7; 109 -1.0; 117 -1.3; 125 -1.7; 134 -2.0; 143 -2.2; 153 -2.4; 164 -2.3; 175 -2.3; 188 -2.5; 201 -2.7; 215 -2.5; 230 -2.4; 246 -2.4; 263 -2.2; 282 -2.0; 301 -1.8; 323 -1.8; 345 -1.7; 369 -1.6; 395 -1.5; 423 -1.3; 452 -1.2; 484 -1.2; 518 -1.1; 554 -0.9; 593 -0.6; 635 -0.6; 679 -0.6; 726 -0.4; 777 -0.1; 832 -0.3; 890 -0.6; 952 -0.6; 1019 0.0; 1090 -0.5; 1167 -1.0; 1248 -1.0; 1336 -1.2; 1429 -1.5; 1529 -1.7; 1636 -2.0; 1751 -1.9; 1873 -1.6; 2004 -1.1; 2145 -0.8; 2295 -0.6; 2455 -0.3; 2627 0.1; 2811 0.0; 3008 -0.2; 3219 -0.1; 3444 -0.2; 3685 -0.3; 3943 0.2; 4219 0.4; 4514 0.5; 4830 1.1; 5168 2.6; 5530 4.0; 5917 5.0; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Massdrop x Sennheiser HD 6XX ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.2dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.27 | 6.5 dB  |
| Peaking | 117 Hz  | 0.8  | -4.1 dB |
| Peaking | 240 Hz  | 0.89 | -2.0 dB |
| Peaking | 2880 Hz | 0.26 | -0.9 dB |
| Peaking | 6049 Hz | 2.99 | 6.4 dB  |
| Peaking | 940 Hz  | 1.89 | 0.6 dB  |
| Peaking | 1668 Hz | 2.17 | -1.4 dB |
| Peaking | 2623 Hz | 2.19 | 1.0 dB  |
| Peaking | 7762 Hz | 7.49 | -0.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Massdrop%20x%20Sennheiser%20HD%206XX/Massdrop%20x%20Sennheiser%20HD%206XX.png)