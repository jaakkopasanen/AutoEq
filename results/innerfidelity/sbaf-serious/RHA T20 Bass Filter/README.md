# RHA T20 Bass Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -4.9; 22 -5.2; 23 -5.3; 25 -5.5; 26 -5.6; 28 -5.7; 30 -5.8; 32 -5.8; 35 -5.9; 37 -5.9; 40 -5.9; 42 -5.8; 45 -5.7; 49 -5.6; 52 -5.5; 56 -5.3; 59 -5.2; 64 -5.0; 68 -4.9; 73 -4.8; 78 -4.8; 83 -4.7; 89 -4.8; 95 -5.0; 102 -5.2; 109 -5.4; 117 -5.6; 125 -5.9; 134 -6.0; 143 -6.0; 153 -5.9; 164 -5.7; 175 -5.4; 188 -5.1; 201 -4.7; 215 -4.4; 230 -4.0; 246 -3.6; 263 -3.3; 282 -2.9; 301 -2.5; 323 -2.2; 345 -1.7; 369 -1.4; 395 -1.1; 423 -0.7; 452 -0.4; 484 -0.2; 518 -0.0; 554 0.4; 593 0.8; 635 1.0; 679 1.0; 726 1.1; 777 1.2; 832 1.0; 890 0.7; 952 0.4; 1019 -0.1; 1090 -0.5; 1167 -1.0; 1248 -1.6; 1336 -2.6; 1429 -3.5; 1529 -4.1; 1636 -3.7; 1751 -1.6; 1873 0.0; 2004 -1.7; 2145 -2.4; 2295 -2.5; 2455 -2.5; 2627 -2.4; 2811 -1.9; 3008 -0.9; 3219 -0.3; 3444 0.0; 3685 -0.9; 3943 -2.9; 4219 -5.9; 4514 -7.6; 4830 -5.8; 5168 -1.8; 5530 2.0; 5917 4.7; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -0.5; 15258 -0.7; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RHA T20 Bass Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.4  | -5.7 dB |
| Peaking | 159 Hz  | 1.03 | -4.7 dB |
| Peaking | 1531 Hz | 3.62 | -4.1 dB |
| Peaking | 4561 Hz | 4.18 | -8.8 dB |
| Peaking | 6143 Hz | 4.08 | 7.1 dB  |
| Peaking | 290 Hz  | 2.48 | -0.7 dB |
| Peaking | 718 Hz  | 1.55 | 1.8 dB  |
| Peaking | 1836 Hz | 7.7  | 3.0 dB  |
| Peaking | 2390 Hz | 1.48 | -2.6 dB |
| Peaking | 3408 Hz | 4    | 2.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/RHA%20T20%20Bass%20Filter/RHA%20T20%20Bass%20Filter.png)