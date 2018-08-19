# Sennheiser HD 428

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 5.0; 95 3.8; 102 2.7; 109 2.1; 117 1.4; 125 1.0; 134 0.9; 143 0.7; 153 0.6; 164 0.9; 175 1.1; 188 1.4; 201 1.5; 215 1.6; 230 2.3; 246 2.3; 263 1.6; 282 1.7; 301 1.9; 323 1.7; 345 1.6; 369 1.6; 395 1.7; 423 1.8; 452 1.7; 484 1.8; 518 2.0; 554 2.2; 593 2.3; 635 2.0; 679 1.4; 726 0.9; 777 0.5; 832 0.1; 890 -0.0; 952 -0.1; 1019 0.0; 1090 1.7; 1167 1.6; 1248 0.1; 1336 -0.6; 1429 -0.8; 1529 -1.2; 1636 -1.8; 1751 -2.1; 1873 -1.8; 2004 -1.2; 2145 -0.0; 2295 1.8; 2455 2.6; 2627 2.5; 2811 2.9; 3008 3.1; 3219 3.2; 3444 3.0; 3685 2.5; 3943 3.4; 4219 6.0; 4514 6.0; 4830 6.0; 5168 4.4; 5530 3.4; 5917 4.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 428 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 40 Hz    | 0.5  | 6.8 dB  |
| Peaking | 461 Hz   | 1.28 | 1.9 dB  |
| Peaking | 2868 Hz  | 4.11 | 2.0 dB  |
| Peaking | 4884 Hz  | 1.75 | 5.9 dB  |
| Peaking | 24000 Hz | 2.34 | 3.0 dB  |
| Peaking | 15 Hz    | 2.63 | 1.5 dB  |
| Peaking | 82 Hz    | 3.95 | 2.1 dB  |
| Peaking | 127 Hz   | 2.23 | -1.9 dB |
| Peaking | 747 Hz   | 0.16 | 0.3 dB  |
| Peaking | 1736 Hz  | 3.44 | -3.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20428/Sennheiser%20HD%20428.png)