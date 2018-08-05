# JAYS u-JAYS

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 3.8; 22 3.4; 23 3.2; 25 2.9; 26 2.8; 28 2.6; 30 2.4; 32 2.2; 35 2.1; 37 2.0; 40 1.8; 42 1.8; 45 1.7; 49 1.8; 52 1.8; 56 1.7; 59 1.6; 64 1.5; 68 1.4; 73 1.4; 78 1.4; 83 1.4; 89 1.2; 95 1.1; 102 1.0; 109 1.0; 117 0.8; 125 0.6; 134 0.2; 143 -0.1; 153 -0.1; 164 0.2; 175 0.4; 188 0.2; 201 0.4; 215 0.6; 230 0.9; 246 1.2; 263 1.7; 282 2.5; 301 3.1; 323 3.6; 345 3.8; 369 3.6; 395 3.4; 423 3.2; 452 2.9; 484 2.5; 518 2.2; 554 2.1; 593 2.1; 635 1.8; 679 1.4; 726 1.1; 777 1.0; 832 0.7; 890 0.4; 952 0.2; 1019 0.0; 1090 -0.0; 1167 0.1; 1248 0.1; 1336 0.1; 1429 -0.1; 1529 -0.2; 1636 -0.3; 1751 0.1; 1873 0.6; 2004 1.2; 2145 1.8; 2295 2.5; 2455 3.4; 2627 4.0; 2811 4.1; 3008 4.2; 3219 3.7; 3444 4.0; 3685 4.8; 3943 5.9; 4219 5.8; 4514 5.0; 4830 5.8; 5168 5.4; 5530 3.2; 5917 2.9; 6331 2.3; 6775 1.2; 7249 1.0; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JAYS u-JAYS ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 17 Hz   | 0.67 | 3.6 dB  |
| Peaking | 66 Hz   | 1.49 | 1.0 dB  |
| Peaking | 381 Hz  | 1.47 | 3.8 dB  |
| Peaking | 2716 Hz | 3.16 | 3.1 dB  |
| Peaking | 4419 Hz | 1.86 | 5.9 dB  |
| Peaking | 308 Hz  | 1.06 | -1.5 dB |
| Peaking | 306 Hz  | 2.52 | 2.1 dB  |
| Peaking | 604 Hz  | 3.15 | 1.0 dB  |
| Peaking | 1559 Hz | 3.84 | -0.9 dB |
| Peaking | 8603 Hz | 3.21 | -0.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/JAYS%20u-JAYS/JAYS%20u-JAYS.png)