# Sennheiser HD 439

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 2.1; 22 1.8; 23 1.6; 25 1.3; 26 1.1; 28 0.9; 30 0.6; 32 0.4; 35 0.2; 37 0.0; 40 -0.2; 42 -0.3; 45 -0.5; 49 -0.7; 52 -0.8; 56 -1.0; 59 -1.1; 64 -1.1; 68 -1.0; 73 -1.0; 78 -1.3; 83 -1.7; 89 -1.6; 95 -0.7; 102 0.8; 109 0.3; 117 -1.2; 125 -2.3; 134 -2.6; 143 -2.8; 153 -3.0; 164 -2.7; 175 -3.1; 188 -3.1; 201 -3.1; 215 -3.2; 230 -3.2; 246 -3.2; 263 -3.1; 282 -2.4; 301 -1.7; 323 -1.0; 345 -0.5; 369 -0.2; 395 -0.3; 423 -0.1; 452 0.3; 484 0.3; 518 0.3; 554 0.3; 593 0.5; 635 0.4; 679 0.3; 726 0.3; 777 0.3; 832 0.0; 890 -0.2; 952 -0.0; 1019 0.2; 1090 0.3; 1167 0.4; 1248 0.3; 1336 -0.7; 1429 -1.5; 1529 -1.6; 1636 -1.7; 1751 -1.2; 1873 -0.3; 2004 0.4; 2145 1.3; 2295 2.6; 2455 3.9; 2627 4.5; 2811 4.4; 3008 4.9; 3219 4.9; 3444 5.0; 3685 4.9; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.0999990177344765dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 439 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.28 | 2.2 dB  |
| Peaking | 60 Hz   | 1.61 | -1.1 dB |
| Peaking | 197 Hz  | 1.37 | -3.6 dB |
| Peaking | 1626 Hz | 3.28 | -3.3 dB |
| Peaking | 4121 Hz | 0.93 | 6.5 dB  |
| Peaking | 105 Hz  | 5.6  | 4.5 dB  |
| Peaking | 105 Hz  | 2.39 | -2.5 dB |
| Peaking | 2575 Hz | 6.52 | 1.7 dB  |
| Peaking | 6178 Hz | 2.49 | 6.5 dB  |
| Peaking | 6852 Hz | 1.23 | -4.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20439/Sennheiser%20HD%20439.png)