# Etymotic EK5

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 5.8; 83 5.5; 89 5.1; 95 4.6; 102 4.1; 109 3.7; 117 3.1; 125 2.5; 134 2.0; 143 1.6; 153 1.3; 164 1.2; 175 1.2; 188 1.2; 201 1.1; 215 1.1; 230 1.2; 246 1.2; 263 1.2; 282 1.3; 301 1.4; 323 1.5; 345 1.6; 369 1.6; 395 1.7; 423 1.8; 452 1.8; 484 1.7; 518 1.7; 554 1.9; 593 2.1; 635 2.1; 679 1.8; 726 1.8; 777 1.8; 832 1.5; 890 1.0; 952 0.5; 1019 -0.1; 1090 -0.8; 1167 -1.4; 1248 -2.2; 1336 -2.7; 1429 -2.9; 1529 -3.8; 1636 -4.6; 1751 -5.3; 1873 -5.8; 2004 -6.2; 2145 -6.3; 2295 -5.3; 2455 -3.1; 2627 -2.6; 2811 -1.8; 3008 -0.3; 3219 0.7; 3444 1.8; 3685 2.1; 3943 2.2; 4219 1.5; 4514 1.3; 4830 1.3; 5168 1.8; 5530 2.0; 5917 2.9; 6331 3.8; 6775 3.8; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic EK5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 41 Hz   | 0.43 | 6.7 dB  |
| Peaking | 670 Hz  | 0.96 | 2.6 dB  |
| Peaking | 2021 Hz | 1.19 | -7.4 dB |
| Peaking | 3530 Hz | 1.55 | 4.2 dB  |
| Peaking | 6414 Hz | 4.76 | 4.1 dB  |
| Peaking | 17 Hz   | 1.1  | 1.8 dB  |
| Peaking | 41 Hz   | 1.24 | -1.2 dB |
| Peaking | 81 Hz   | 1.7  | 1.3 dB  |
| Peaking | 148 Hz  | 2.37 | -1.1 dB |
| Peaking | 8077 Hz | 5.71 | -0.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Etymotic%20EK5/Etymotic%20EK5.png)