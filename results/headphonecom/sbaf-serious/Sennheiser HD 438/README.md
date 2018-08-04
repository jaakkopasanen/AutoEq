# Sennheiser HD 438

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -7.0dB
GraphicEQ: 10 -84; 20 6.5; 22 5.7; 23 5.3; 25 4.7; 26 4.4; 28 3.8; 30 3.4; 32 2.9; 35 2.4; 37 2.1; 40 1.7; 42 1.5; 45 1.1; 49 0.9; 52 0.9; 56 1.1; 59 1.1; 64 0.6; 68 0.1; 73 0.2; 78 1.6; 83 3.6; 89 3.6; 95 2.2; 102 1.7; 109 1.6; 117 1.5; 125 1.5; 134 1.5; 143 1.6; 153 2.0; 164 2.4; 175 2.2; 188 3.2; 201 3.7; 215 3.5; 230 4.4; 246 4.6; 263 4.2; 282 4.4; 301 4.7; 323 4.8; 345 4.1; 369 3.9; 395 3.6; 423 3.5; 452 3.5; 484 2.9; 518 2.5; 554 2.3; 593 2.2; 635 2.2; 679 2.1; 726 2.1; 777 1.9; 832 1.3; 890 0.4; 952 0.0; 1019 0.3; 1090 0.4; 1167 1.1; 1248 0.8; 1336 -0.4; 1429 0.1; 1529 1.0; 1636 1.7; 1751 2.4; 1873 3.3; 2004 4.3; 2145 4.9; 2295 5.8; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-7.0dB` and instead set Global volume in the UI for both channels to **-70**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 438 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.78 | 7.8 dB  |
| Peaking | 4 Hz    | 1.49 | 1.8 dB  |
| Peaking | 266 Hz  | 0.87 | 4.3 dB  |
| Peaking | 454 Hz  | 1.88 | 1.0 dB  |
| Peaking | 3676 Hz | 0.83 | 6.9 dB  |
| Peaking | 87 Hz   | 8.96 | 2.9 dB  |
| Peaking | 1383 Hz | 3.36 | -1.9 dB |
| Peaking | 2279 Hz | 3.09 | 2.2 dB  |
| Peaking | 6036 Hz | 2.17 | 7.5 dB  |
| Peaking | 6490 Hz | 1.04 | -5.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20438/Sennheiser%20HD%20438.png)