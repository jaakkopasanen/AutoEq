# Sennheiser RS 170

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 2.1; 22 1.1; 23 0.6; 25 -0.2; 26 -0.6; 28 -1.4; 30 -2.0; 32 -2.6; 35 -3.3; 37 -3.8; 40 -4.4; 42 -4.8; 45 -5.3; 49 -5.8; 52 -6.1; 56 -6.4; 59 -6.6; 64 -6.8; 68 -7.0; 73 -7.4; 78 -7.5; 83 -7.2; 89 -7.0; 95 -6.5; 102 -6.2; 109 -6.5; 117 -7.1; 125 -7.6; 134 -7.9; 143 -8.0; 153 -8.0; 164 -7.6; 175 -7.3; 188 -7.7; 201 -7.4; 215 -6.7; 230 -5.9; 246 -5.4; 263 -5.0; 282 -4.7; 301 -4.1; 323 -3.5; 345 -3.1; 369 -2.7; 395 -2.8; 423 -2.9; 452 -2.8; 484 -2.5; 518 -1.8; 554 -1.1; 593 -0.5; 635 0.1; 679 0.5; 726 0.7; 777 1.4; 832 2.5; 890 1.6; 952 0.3; 1019 -0.0; 1090 1.0; 1167 0.2; 1248 -0.7; 1336 -0.8; 1429 -1.1; 1529 -1.5; 1636 -2.5; 1751 -1.2; 1873 1.6; 2004 -0.2; 2145 -1.0; 2295 -1.3; 2455 -1.4; 2627 -1.2; 2811 -1.3; 3008 -1.1; 3219 -1.3; 3444 -1.4; 3685 -1.0; 3943 0.9; 4219 3.9; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.6; 6331 2.5; 6775 0.4; 7249 1.3; 7756 0.3; 8299 -0.2; 8880 -1.9; 9502 -2.2; 10167 -0.4; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser RS 170 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 1.46 | 3.7 dB  |
| Peaking | 62 Hz   | 0.64 | -6.2 dB |
| Peaking | 180 Hz  | 1    | -6.1 dB |
| Peaking | 438 Hz  | 4.3  | -1.4 dB |
| Peaking | 5155 Hz | 3.39 | 7.3 dB  |
| Peaking | 819 Hz  | 4.06 | 2.8 dB  |
| Peaking | 1613 Hz | 8.37 | -2.4 dB |
| Peaking | 3318 Hz | 1.9  | -2.4 dB |
| Peaking | 4375 Hz | 7.71 | 3.8 dB  |
| Peaking | 9241 Hz | 6.85 | -2.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Sennheiser%20RS%20170/Sennheiser%20RS%20170.png)