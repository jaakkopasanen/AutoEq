# Sennheiser HD 598

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 5.8; 30 5.4; 32 5.0; 35 4.2; 37 3.8; 40 3.2; 42 2.8; 45 2.4; 49 1.9; 52 1.5; 56 1.0; 59 0.8; 64 0.8; 68 0.6; 73 0.0; 78 -0.4; 83 -0.7; 89 -1.3; 95 -2.1; 102 -2.5; 109 -2.8; 117 -3.0; 125 -3.4; 134 -3.7; 143 -3.8; 153 -3.9; 164 -3.9; 175 -3.9; 188 -3.8; 201 -3.9; 215 -3.7; 230 -3.6; 246 -3.5; 263 -3.5; 282 -3.2; 301 -3.2; 323 -2.9; 345 -2.8; 369 -2.6; 395 -2.5; 423 -2.1; 452 -1.9; 484 -2.0; 518 -1.8; 554 -1.6; 593 -0.0; 635 -0.5; 679 -0.7; 726 -0.6; 777 -0.4; 832 -0.3; 890 -0.4; 952 -0.2; 1019 -0.1; 1090 -0.0; 1167 0.3; 1248 0.4; 1336 0.6; 1429 0.9; 1529 1.3; 1636 2.0; 1751 2.2; 1873 2.3; 2004 1.6; 2145 0.8; 2295 0.4; 2455 0.2; 2627 -0.0; 2811 0.2; 3008 0.4; 3219 -0.6; 3444 -0.9; 3685 -0.8; 3943 -0.9; 4219 -2.6; 4514 -3.7; 4830 -3.3; 5168 -1.8; 5530 -0.0; 5917 0.6; 6331 1.2; 6775 1.7; 7249 1.2; 7756 0.3; 8299 -1.1; 8880 -3.1; 9502 -2.6; 10167 -0.2; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -0.3; 18692 -1.3; 20000 -1.6
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 598 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.3dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 0.54 | 6.4 dB  |
| Peaking | 177 Hz   | 0.54 | -4.4 dB |
| Peaking | 1753 Hz  | 2.82 | 2.6 dB  |
| Peaking | 4553 Hz  | 5.38 | -4.2 dB |
| Peaking | 19532 Hz | 2    | -1.8 dB |
| Peaking | 43 Hz    | 2.77 | -0.4 dB |
| Peaking | 544 Hz   | 4.27 | -0.9 dB |
| Peaking | 602 Hz   | 8.25 | 1.7 dB  |
| Peaking | 6766 Hz  | 4.23 | 2.2 dB  |
| Peaking | 9013 Hz  | 6.43 | -3.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20598/Sennheiser%20HD%20598.png)