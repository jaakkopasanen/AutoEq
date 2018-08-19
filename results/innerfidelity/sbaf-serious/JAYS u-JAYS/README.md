# JAYS u-JAYS

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 3.8; 22 3.4; 23 3.2; 25 2.9; 26 2.8; 28 2.5; 30 2.4; 32 2.2; 35 2.0; 37 1.9; 40 1.7; 42 1.6; 45 1.6; 49 1.5; 52 1.5; 56 1.4; 59 1.2; 64 1.0; 68 0.8; 73 0.7; 78 0.6; 83 0.6; 89 0.4; 95 0.4; 102 0.4; 109 0.6; 117 0.6; 125 0.6; 134 0.3; 143 0.1; 153 0.2; 164 0.4; 175 0.6; 188 0.4; 201 0.5; 215 0.8; 230 1.0; 246 1.3; 263 1.8; 282 2.6; 301 3.2; 323 3.7; 345 3.8; 369 3.7; 395 3.5; 423 3.2; 452 2.9; 484 2.5; 518 2.2; 554 2.1; 593 2.1; 635 1.8; 679 1.4; 726 1.1; 777 1.0; 832 0.7; 890 0.4; 952 0.2; 1019 0.0; 1090 -0.0; 1167 0.1; 1248 0.1; 1336 0.1; 1429 -0.1; 1529 -0.2; 1636 -0.3; 1751 0.1; 1873 0.6; 2004 1.2; 2145 1.8; 2295 2.5; 2455 3.4; 2627 4.0; 2811 4.1; 3008 4.2; 3219 3.7; 3444 4.0; 3685 4.8; 3943 5.9; 4219 5.8; 4514 5.0; 4830 5.8; 5168 5.4; 5530 3.2; 5917 2.9; 6331 2.3; 6775 1.2; 7249 1.0; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.132356342558974dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JAYS u-JAYS ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.3dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.89 | 3.6 dB  |
| Peaking | 48 Hz   | 1.76 | 0.8 dB  |
| Peaking | 377 Hz  | 1.4  | 3.8 dB  |
| Peaking | 2719 Hz | 3.15 | 3.1 dB  |
| Peaking | 4421 Hz | 1.86 | 5.9 dB  |
| Peaking | 666 Hz  | 1.96 | 1.2 dB  |
| Peaking | 912 Hz  | 0.7  | -0.9 dB |
| Peaking | 1640 Hz | 3.24 | -1.3 dB |
| Peaking | 1768 Hz | 1    | 0.8 dB  |
| Peaking | 8618 Hz | 2.91 | -0.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/JAYS%20u-JAYS/JAYS%20u-JAYS.png)