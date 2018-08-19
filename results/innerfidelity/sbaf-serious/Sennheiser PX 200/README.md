# Sennheiser PX 200

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 6.0; 95 6.0; 102 6.0; 109 5.9; 117 5.6; 125 5.0; 134 4.7; 143 4.9; 153 5.3; 164 5.0; 175 4.9; 188 5.6; 201 5.6; 215 5.2; 230 4.7; 246 4.1; 263 3.6; 282 3.2; 301 2.9; 323 2.7; 345 2.8; 369 2.7; 395 2.6; 423 2.5; 452 2.1; 484 0.9; 518 -0.0; 554 -0.5; 593 -0.6; 635 -1.0; 679 -0.9; 726 -0.7; 777 -0.5; 832 -0.3; 890 -0.2; 952 -0.0; 1019 0.0; 1090 0.1; 1167 0.1; 1248 0.0; 1336 -0.3; 1429 -0.7; 1529 -1.1; 1636 -1.5; 1751 -1.7; 1873 -1.7; 2004 -1.2; 2145 -0.3; 2295 0.2; 2455 0.9; 2627 2.0; 2811 3.3; 3008 4.9; 3219 6.0; 3444 5.8; 3685 3.6; 3943 1.8; 4219 1.7; 4514 2.4; 4830 3.7; 5168 5.6; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PX 200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 38 Hz   | 0.19 | 6.1 dB  |
| Peaking | 241 Hz  | 0.73 | 2.8 dB  |
| Peaking | 1434 Hz | 0.13 | -1.4 dB |
| Peaking | 3205 Hz | 3.3  | 7.0 dB  |
| Peaking | 5754 Hz | 2.56 | 7.4 dB  |
| Peaking | 289 Hz  | 5.31 | -0.7 dB |
| Peaking | 429 Hz  | 3.47 | 1.7 dB  |
| Peaking | 589 Hz  | 1.58 | -1.8 dB |
| Peaking | 1166 Hz | 0.92 | 1.4 dB  |
| Peaking | 1742 Hz | 3.04 | -1.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20PX%20200/Sennheiser%20PX%20200.png)