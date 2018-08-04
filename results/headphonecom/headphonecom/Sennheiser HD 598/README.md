# Sennheiser HD 598

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.5dB
GraphicEQ: 10 -84; 20 4.6; 22 3.9; 23 3.6; 25 3.0; 26 2.7; 28 2.2; 30 1.8; 32 1.4; 35 0.8; 37 0.5; 40 0.0; 42 -0.2; 45 -0.6; 49 -0.9; 52 -1.2; 56 -1.5; 59 -1.7; 64 -1.4; 68 -1.6; 73 -2.1; 78 -1.8; 83 -1.2; 89 -1.8; 95 -2.4; 102 -2.8; 109 -3.0; 117 -3.1; 125 -3.3; 134 -3.5; 143 -3.4; 153 -3.6; 164 -3.5; 175 -3.5; 188 -3.6; 201 -3.5; 215 -3.4; 230 -3.3; 246 -3.4; 263 -3.5; 282 -3.5; 301 -3.4; 323 -3.2; 345 -3.1; 369 -3.0; 395 -2.8; 423 -2.6; 452 -2.3; 484 -2.1; 518 -1.7; 554 -1.2; 593 -1.3; 635 -1.3; 679 0.6; 726 0.0; 777 -0.3; 832 -0.4; 890 -0.2; 952 0.1; 1019 -0.0; 1090 0.0; 1167 0.4; 1248 0.5; 1336 1.2; 1429 2.1; 1529 2.9; 1636 4.1; 1751 4.3; 1873 4.1; 2004 3.9; 2145 3.6; 2295 4.3; 2455 4.9; 2627 4.0; 2811 2.9; 3008 2.9; 3219 2.0; 3444 1.6; 3685 1.9; 3943 2.5; 4219 1.3; 4514 0.8; 4830 2.2; 5168 4.0; 5530 4.2; 5917 3.5; 6331 2.1; 6775 1.5; 7249 1.2; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.5dB` and instead set Global volume in the UI for both channels to **-55**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 598 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 0.99 | 5.3 dB  |
| Peaking | 66 Hz   | 0.29 | -1.2 dB |
| Peaking | 237 Hz  | 0.5  | -3.0 dB |
| Peaking | 2110 Hz | 1.21 | 4.7 dB  |
| Peaking | 5550 Hz | 4.13 | 4.0 dB  |
| Peaking | 123 Hz  | 4.2  | -0.4 dB |
| Peaking | 698 Hz  | 9.48 | 1.6 dB  |
| Peaking | 1315 Hz | 1.58 | -0.7 dB |
| Peaking | 1622 Hz | 5.79 | 1.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Sennheiser%20HD%20598/Sennheiser%20HD%20598.png)