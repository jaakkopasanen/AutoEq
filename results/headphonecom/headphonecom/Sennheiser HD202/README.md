# Sennheiser HD202

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 4.9; 22 4.0; 23 3.5; 25 2.6; 26 2.2; 28 1.4; 30 0.7; 32 -0.0; 35 -1.0; 37 -1.5; 40 -2.2; 42 -2.6; 45 -3.2; 49 -3.7; 52 -3.8; 56 -4.0; 59 -4.3; 64 -4.8; 68 -4.8; 73 -4.7; 78 -4.9; 83 -5.1; 89 -4.9; 95 -4.8; 102 -4.7; 109 -4.5; 117 -4.2; 125 -3.9; 134 -3.6; 143 -3.3; 153 -2.8; 164 -2.1; 175 -1.5; 188 -0.1; 201 1.8; 215 3.3; 230 3.5; 246 3.1; 263 3.0; 282 2.9; 301 2.8; 323 2.6; 345 1.8; 369 1.5; 395 1.6; 423 1.7; 452 1.6; 484 1.4; 518 1.2; 554 1.1; 593 0.9; 635 0.8; 679 0.7; 726 0.5; 777 0.4; 832 0.3; 890 0.1; 952 0.1; 1019 0.0; 1090 -0.1; 1167 -0.0; 1248 0.5; 1336 1.3; 1429 1.5; 1529 2.1; 1636 2.5; 1751 3.3; 1873 4.1; 2004 5.2; 2145 6.0; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 5.9; 4514 4.4; 4830 5.9; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD202 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 2.07 | 4.9 dB  |
| Peaking | 63 Hz   | 1.38 | -4.8 dB |
| Peaking | 111 Hz  | 2.42 | -3.8 dB |
| Peaking | 2823 Hz | 1.01 | 6.4 dB  |
| Peaking | 5592 Hz | 2.76 | 4.7 dB  |
| Peaking | 22 Hz   | 1.99 | 0.7 dB  |
| Peaking | 166 Hz  | 1.74 | -5.4 dB |
| Peaking | 218 Hz  | 1.17 | 6.3 dB  |
| Peaking | 1102 Hz | 3    | -1.5 dB |
| Peaking | 8418 Hz | 3.76 | -1.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Sennheiser%20HD202/Sennheiser%20HD202.png)