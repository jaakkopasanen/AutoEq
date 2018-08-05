# Etymotic mc3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 5.7; 95 5.2; 102 4.6; 109 4.1; 117 3.6; 125 2.9; 134 2.4; 143 2.1; 153 1.9; 164 1.7; 175 1.6; 188 1.5; 201 1.5; 215 1.6; 230 1.6; 246 1.6; 263 1.6; 282 1.7; 301 1.7; 323 1.8; 345 1.9; 369 1.9; 395 1.9; 423 2.0; 452 2.0; 484 2.0; 518 1.9; 554 2.1; 593 2.3; 635 2.2; 679 2.0; 726 1.8; 777 1.8; 832 1.4; 890 0.9; 952 0.4; 1019 -0.2; 1090 -0.8; 1167 -1.3; 1248 -1.9; 1336 -2.6; 1429 -3.4; 1529 -4.0; 1636 -4.3; 1751 -4.3; 1873 -3.6; 2004 -3.3; 2145 -2.9; 2295 -2.1; 2455 -0.9; 2627 0.1; 2811 1.2; 3008 2.8; 3219 4.0; 3444 5.2; 3685 5.7; 3943 5.5; 4219 4.3; 4514 3.6; 4830 3.9; 5168 5.2; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic mc3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 42 Hz   | 0.39 | 6.6 dB  |
| Peaking | 689 Hz  | 0.8  | 2.8 dB  |
| Peaking | 1703 Hz | 1.09 | -5.6 dB |
| Peaking | 5840 Hz | 3.33 | 5.9 dB  |
| Peaking | 3580 Hz | 2.06 | 6.5 dB  |
| Peaking | 15 Hz   | 0.98 | 1.8 dB  |
| Peaking | 40 Hz   | 1.03 | -1.1 dB |
| Peaking | 86 Hz   | 2.01 | 1.3 dB  |
| Peaking | 147 Hz  | 2.28 | -1.0 dB |
| Peaking | 8230 Hz | 4.74 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Etymotic%20mc3/Etymotic%20mc3.png)