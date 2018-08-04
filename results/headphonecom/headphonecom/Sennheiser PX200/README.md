# Sennheiser PX200

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 6.0; 95 6.0; 102 6.0; 109 6.0; 117 6.0; 125 6.0; 134 6.0; 143 6.0; 153 6.0; 164 6.0; 175 5.8; 188 5.5; 201 5.2; 215 5.0; 230 5.2; 246 5.6; 263 5.5; 282 5.1; 301 4.9; 323 4.5; 345 4.2; 369 4.1; 395 3.7; 423 3.7; 452 3.5; 484 3.0; 518 2.6; 554 2.3; 593 1.9; 635 1.3; 679 0.8; 726 0.6; 777 -0.0; 832 -0.2; 890 -0.2; 952 -0.1; 1019 0.0; 1090 0.2; 1167 0.6; 1248 0.9; 1336 1.4; 1429 1.8; 1529 2.0; 1636 2.1; 1751 1.9; 1873 1.7; 2004 1.9; 2145 2.6; 2295 3.8; 2455 4.2; 2627 4.6; 2811 5.4; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PX200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.21 | 5.9 dB  |
| Peaking | 158 Hz  | 0.75 | 2.9 dB  |
| Peaking | 331 Hz  | 1.24 | 2.7 dB  |
| Peaking | 3322 Hz | 1.26 | 6.0 dB  |
| Peaking | 5607 Hz | 2.73 | 4.7 dB  |
| Peaking | 528 Hz  | 2.81 | 0.9 dB  |
| Peaking | 861 Hz  | 1.69 | -1.3 dB |
| Peaking | 1484 Hz | 4.1  | 1.1 dB  |
| Peaking | 6534 Hz | 7.08 | 2.3 dB  |
| Peaking | 7889 Hz | 2.2  | -1.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Sennheiser%20PX200/Sennheiser%20PX200.png)