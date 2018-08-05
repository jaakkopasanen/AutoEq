# Yutai BAS02

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -0.9; 22 -1.0; 23 -1.0; 25 -1.1; 26 -1.2; 28 -1.2; 30 -1.2; 32 -1.3; 35 -1.4; 37 -1.4; 40 -1.4; 42 -1.4; 45 -1.4; 49 -1.4; 52 -1.4; 56 -1.4; 59 -1.3; 64 -1.3; 68 -1.4; 73 -1.5; 78 -1.6; 83 -1.8; 89 -2.2; 95 -2.5; 102 -3.0; 109 -3.3; 117 -3.9; 125 -4.3; 134 -4.8; 143 -5.0; 153 -5.1; 164 -5.2; 175 -5.1; 188 -5.0; 201 -4.9; 215 -4.8; 230 -4.6; 246 -4.4; 263 -4.3; 282 -4.0; 301 -3.8; 323 -3.6; 345 -3.4; 369 -3.2; 395 -2.9; 423 -2.6; 452 -2.2; 484 -2.1; 518 -1.8; 554 -1.4; 593 -1.0; 635 -0.7; 679 -0.6; 726 -0.3; 777 0.1; 832 0.1; 890 0.1; 952 -0.0; 1019 -0.1; 1090 -0.2; 1167 -0.2; 1248 -0.3; 1336 -0.6; 1429 -0.8; 1529 -1.0; 1636 -1.1; 1751 -1.0; 1873 -0.7; 2004 -0.3; 2145 -0.2; 2295 -0.2; 2455 -0.1; 2627 -0.2; 2811 -0.4; 3008 0.4; 3219 2.4; 3444 5.1; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yutai BAS02 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 1.31 | -0.6 dB |
| Peaking | 36 Hz   | 1.79 | -0.7 dB |
| Peaking | 189 Hz  | 0.65 | -5.2 dB |
| Peaking | 2588 Hz | 1.35 | -2.8 dB |
| Peaking | 4390 Hz | 1.25 | 7.8 dB  |
| Peaking | 870 Hz  | 1.29 | 2.6 dB  |
| Peaking | 2222 Hz | 4.51 | 1.1 dB  |
| Peaking | 973 Hz  | 0.7  | -1.8 dB |
| Peaking | 6339 Hz | 3.59 | 4.4 dB  |
| Peaking | 7364 Hz | 1.6  | -2.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Yutai%20BAS02/Yutai%20BAS02.png)