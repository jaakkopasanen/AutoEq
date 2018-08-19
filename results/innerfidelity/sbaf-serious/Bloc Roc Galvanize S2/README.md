# Bloc Roc Galvanize S2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.8dB
GraphicEQ: 10 -84; 20 2.7; 22 1.7; 23 1.3; 25 0.4; 26 -0.1; 28 -0.9; 30 -1.7; 32 -2.3; 35 -3.3; 37 -3.9; 40 -4.7; 42 -5.1; 45 -5.7; 49 -6.3; 52 -6.7; 56 -7.1; 59 -7.3; 64 -7.5; 68 -7.6; 73 -7.7; 78 -7.7; 83 -7.4; 89 -7.1; 95 -7.0; 102 -7.2; 109 -7.3; 117 -7.3; 125 -7.3; 134 -7.3; 143 -7.1; 153 -7.1; 164 -6.6; 175 -6.6; 188 -6.4; 201 -6.2; 215 -5.8; 230 -5.4; 246 -4.9; 263 -4.5; 282 -4.0; 301 -4.3; 323 -4.3; 345 -3.9; 369 -3.6; 395 -3.3; 423 -2.8; 452 -2.7; 484 -2.5; 518 -2.0; 554 -1.2; 593 -0.3; 635 0.5; 679 1.0; 726 1.3; 777 1.3; 832 1.0; 890 0.7; 952 0.3; 1019 -0.1; 1090 -0.7; 1167 -1.1; 1248 -1.4; 1336 -2.4; 1429 -3.1; 1529 -4.2; 1636 -4.8; 1751 -5.0; 1873 -4.5; 2004 -4.3; 2145 -3.6; 2295 -2.8; 2455 -1.7; 2627 -0.5; 2811 0.9; 3008 1.3; 3219 0.7; 3444 2.3; 3685 3.5; 3943 3.5; 4219 3.2; 4514 0.6; 4830 -2.0; 5168 -1.8; 5530 -1.8; 5917 -0.3; 6331 -0.4; 6775 -0.9; 7249 0.9; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.8499784726993513dB` and instead set Global volume in the UI for both channels to **-38**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bloc Roc Galvanize S2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.2dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.97 | 5.0 dB  |
| Peaking | 63 Hz   | 0.49 | -7.3 dB |
| Peaking | 198 Hz  | 0.79 | -3.9 dB |
| Peaking | 1788 Hz | 2.48 | -5.4 dB |
| Peaking | 3774 Hz | 4.72 | 4.5 dB  |
| Peaking | 486 Hz  | 1.73 | -2.1 dB |
| Peaking | 700 Hz  | 1.51 | 3.0 dB  |
| Peaking | 1414 Hz | 4.01 | -1.1 dB |
| Peaking | 4306 Hz | 9.2  | 2.8 dB  |
| Peaking | 4931 Hz | 4.18 | -3.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bloc%20Roc%20Galvanize%20S2/Bloc%20Roc%20Galvanize%20S2.png)