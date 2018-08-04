# Sennheiser HD205

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 2.1; 22 1.6; 23 1.4; 25 1.1; 26 0.9; 28 0.6; 30 0.4; 32 0.1; 35 -0.3; 37 -0.6; 40 -0.8; 42 -0.9; 45 -0.9; 49 -1.2; 52 -1.7; 56 -2.1; 59 -2.2; 64 -2.1; 68 -1.9; 73 -1.9; 78 -2.4; 83 -2.7; 89 -2.9; 95 -3.1; 102 -3.3; 109 -3.2; 117 -3.2; 125 -3.2; 134 -2.9; 143 -2.0; 153 -1.3; 164 -1.5; 175 -1.9; 188 -1.8; 201 -1.5; 215 -0.7; 230 -0.6; 246 -0.8; 263 -0.8; 282 -0.5; 301 -0.2; 323 0.2; 345 0.8; 369 1.6; 395 2.5; 423 3.1; 452 2.8; 484 1.8; 518 0.6; 554 0.0; 593 0.3; 635 1.5; 679 3.4; 726 4.4; 777 3.8; 832 2.5; 890 1.3; 952 0.4; 1019 -0.2; 1090 -0.6; 1167 -0.7; 1248 -0.6; 1336 -0.3; 1429 0.2; 1529 0.5; 1636 0.7; 1751 0.9; 1873 1.3; 2004 1.7; 2145 2.4; 2295 3.2; 2455 4.2; 2627 5.5; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 5.4; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD205 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 1.51 | 2.2 dB  |
| Peaking | 133 Hz  | 0.57 | -4.2 dB |
| Peaking | 159 Hz  | 2.14 | 1.9 dB  |
| Peaking | 438 Hz  | 0.97 | 3.0 dB  |
| Peaking | 4004 Hz | 1    | 6.9 dB  |
| Peaking | 574 Hz  | 5.33 | -2.9 dB |
| Peaking | 735 Hz  | 3.52 | 3.9 dB  |
| Peaking | 1148 Hz | 2.23 | -2.1 dB |
| Peaking | 6288 Hz | 3.35 | 4.7 dB  |
| Peaking | 7410 Hz | 1.53 | -3.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Sennheiser%20HD205/Sennheiser%20HD205.png)