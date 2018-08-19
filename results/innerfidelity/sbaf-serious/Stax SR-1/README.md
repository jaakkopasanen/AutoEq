# Stax SR-1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 5.0; 95 3.6; 102 2.0; 109 1.1; 117 0.5; 125 -0.1; 134 -0.2; 143 -0.4; 153 -0.4; 164 -0.5; 175 -0.9; 188 -0.9; 201 -0.6; 215 -0.4; 230 -0.1; 246 0.2; 263 0.3; 282 0.6; 301 0.7; 323 0.9; 345 1.0; 369 1.1; 395 1.1; 423 1.4; 452 1.5; 484 1.4; 518 1.4; 554 1.5; 593 1.7; 635 1.8; 679 1.6; 726 1.6; 777 1.5; 832 1.1; 890 0.8; 952 0.5; 1019 0.2; 1090 0.5; 1167 1.1; 1248 1.6; 1336 1.6; 1429 1.2; 1529 0.5; 1636 0.2; 1751 0.7; 1873 0.7; 2004 1.3; 2145 1.5; 2295 1.7; 2455 1.6; 2627 1.5; 2811 1.7; 3008 2.6; 3219 3.4; 3444 4.8; 3685 5.7; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -1.5; 9502 -4.2; 10167 -2.6; 10879 -0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.2dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 40 Hz   | 0.66 | 7.1 dB  |
| Peaking | 616 Hz  | 1.47 | 1.7 dB  |
| Peaking | 4187 Hz | 1.55 | 5.9 dB  |
| Peaking | 5990 Hz | 3.46 | 4.1 dB  |
| Peaking | 9579 Hz | 5.3  | -5.2 dB |
| Peaking | 16 Hz   | 1.17 | 3.0 dB  |
| Peaking | 38 Hz   | 1.65 | -1.8 dB |
| Peaking | 82 Hz   | 2.4  | 3.6 dB  |
| Peaking | 132 Hz  | 1.28 | -2.5 dB |
| Peaking | 1303 Hz | 7.04 | 1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-1/Stax%20SR-1.png)