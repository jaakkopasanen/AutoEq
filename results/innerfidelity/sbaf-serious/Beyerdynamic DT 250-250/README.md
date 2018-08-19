# Beyerdynamic DT 250-250

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 5.8; 32 5.6; 35 5.2; 37 5.0; 40 4.7; 42 4.5; 45 4.3; 49 4.0; 52 3.8; 56 3.7; 59 3.5; 64 3.4; 68 3.3; 73 3.4; 78 3.9; 83 4.6; 89 4.5; 95 4.1; 102 3.8; 109 3.9; 117 3.4; 125 2.3; 134 1.7; 143 1.5; 153 1.4; 164 2.1; 175 1.6; 188 1.1; 201 1.1; 215 1.0; 230 1.1; 246 1.2; 263 1.3; 282 1.2; 301 1.0; 323 1.1; 345 1.3; 369 1.3; 395 1.3; 423 1.4; 452 1.2; 484 1.1; 518 0.9; 554 0.9; 593 1.0; 635 0.8; 679 0.6; 726 0.3; 777 0.3; 832 -0.0; 890 -0.3; 952 -0.6; 1019 0.3; 1090 0.3; 1167 0.1; 1248 -0.9; 1336 -1.7; 1429 -2.4; 1529 -2.9; 1636 -3.2; 1751 -3.1; 1873 -2.6; 2004 -1.8; 2145 -1.0; 2295 -0.4; 2455 0.6; 2627 1.4; 2811 2.4; 3008 3.9; 3219 4.9; 3444 4.9; 3685 3.6; 3943 2.6; 4219 1.8; 4514 1.5; 4830 2.4; 5168 4.2; 5530 5.7; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.8; 9502 -1.7; 10167 -0.4; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 250-250 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.19 | 4.6 dB  |
| Peaking | 32 Hz   | 1.48 | 2.5 dB  |
| Peaking | 87 Hz   | 0.67 | 3.4 dB  |
| Peaking | 3321 Hz | 4.49 | 5.2 dB  |
| Peaking | 5870 Hz | 3.65 | 6.6 dB  |
| Peaking | 100 Hz  | 1.85 | 3.1 dB  |
| Peaking | 105 Hz  | 0.89 | -3.4 dB |
| Peaking | 329 Hz  | 0.07 | 1.0 dB  |
| Peaking | 1658 Hz | 2.01 | -4.4 dB |
| Peaking | 9324 Hz | 4.49 | -2.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%20250-250/Beyerdynamic%20DT%20250-250.png)