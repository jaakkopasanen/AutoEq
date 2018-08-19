# Sennheiser HD 565 Ovation

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 5.9; 78 5.5; 83 5.0; 89 4.3; 95 3.7; 102 3.2; 109 2.9; 117 2.5; 125 2.1; 134 1.7; 143 1.4; 153 1.2; 164 1.0; 175 0.8; 188 0.6; 201 0.5; 215 0.5; 230 0.4; 246 0.3; 263 0.3; 282 0.3; 301 0.3; 323 0.3; 345 0.3; 369 0.4; 395 0.4; 423 0.4; 452 0.5; 484 0.4; 518 0.3; 554 0.4; 593 0.5; 635 0.5; 679 0.3; 726 0.3; 777 0.3; 832 0.1; 890 -0.2; 952 -0.1; 1019 -0.1; 1090 -0.4; 1167 -0.8; 1248 -1.1; 1336 -1.3; 1429 -1.5; 1529 -1.7; 1636 -2.0; 1751 -1.8; 1873 -1.4; 2004 -1.4; 2145 -1.7; 2295 -1.8; 2455 -1.3; 2627 -0.6; 2811 0.3; 3008 1.2; 3219 1.4; 3444 1.1; 3685 0.3; 3943 -0.2; 4219 -0.8; 4514 0.4; 4830 2.4; 5168 5.1; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 565 Ovation ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 45 Hz    | 0.34 | 7.1 dB  |
| Peaking | 635 Hz   | 0.45 | 4.6 dB  |
| Peaking | 789 Hz   | 0.13 | -4.5 dB |
| Peaking | 3107 Hz  | 3.38 | 3.6 dB  |
| Peaking | 5797 Hz  | 2.55 | 8.6 dB  |
| Peaking | 20 Hz    | 1.15 | 1.6 dB  |
| Peaking | 39 Hz    | 0.65 | -0.8 dB |
| Peaking | 73 Hz    | 2.94 | 1.3 dB  |
| Peaking | 1967 Hz  | 5.77 | 0.3 dB  |
| Peaking | 12654 Hz | 2.02 | 0.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20565%20Ovation/Sennheiser%20HD%20565%20Ovation.png)