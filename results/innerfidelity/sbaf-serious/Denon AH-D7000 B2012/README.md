# Denon AH-D7000 B2012

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.9dB
GraphicEQ: 10 -84; 20 2.3; 22 1.3; 23 0.9; 25 0.2; 26 -0.1; 28 -0.6; 30 -0.9; 32 -1.2; 35 -1.4; 37 -1.5; 40 -1.5; 42 -1.5; 45 -1.5; 49 -1.3; 52 -1.2; 56 -1.2; 59 -1.1; 64 -0.7; 68 -0.6; 73 -0.7; 78 -0.9; 83 -1.1; 89 -1.4; 95 -1.7; 102 -1.9; 109 -2.2; 117 -2.5; 125 -2.8; 134 -3.1; 143 -3.2; 153 -3.3; 164 -3.1; 175 -3.1; 188 -3.2; 201 -3.1; 215 -3.0; 230 -2.8; 246 -2.6; 263 -2.5; 282 -2.2; 301 -2.1; 323 -1.8; 345 -1.7; 369 -1.5; 395 -1.3; 423 -0.9; 452 -0.7; 484 -0.5; 518 -0.3; 554 -0.0; 593 0.2; 635 0.2; 679 0.0; 726 -0.3; 777 -0.5; 832 -0.8; 890 -0.2; 952 0.4; 1019 -0.1; 1090 -0.1; 1167 0.1; 1248 0.4; 1336 0.3; 1429 -0.1; 1529 -0.4; 1636 -0.6; 1751 -0.7; 1873 -0.7; 2004 -0.6; 2145 -0.2; 2295 0.9; 2455 2.1; 2627 1.6; 2811 0.9; 3008 1.1; 3219 0.9; 3444 0.2; 3685 -0.3; 3943 -0.0; 4219 0.0; 4514 -0.2; 4830 0.2; 5168 1.5; 5530 1.4; 5917 0.7; 6331 0.1; 6775 -0.4; 7249 -0.2; 7756 0.2; 8299 0.0; 8880 -0.3; 9502 -1.7; 10167 -1.2; 10879 -0.0; 11640 0.0; 12455 0.0; 13327 -0.1; 14260 -0.1; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -0.0; 20000 -2.8
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.9dB` and instead set Global volume in the UI for both channels to **-29**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D7000 B2012 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 1.35 | 3.9 dB  |
| Peaking | 35 Hz   | 1.46 | -2.0 dB |
| Peaking | 176 Hz  | 0.81 | -3.4 dB |
| Peaking | 2554 Hz | 6.15 | 2.1 dB  |
| Peaking | 5372 Hz | 7.6  | 1.7 dB  |
| Peaking | 15 Hz   | 0.19 | 0.1 dB  |
| Peaking | 1357 Hz | 1.91 | 0.7 dB  |
| Peaking | 1730 Hz | 2.53 | -1.2 dB |
| Peaking | 3100 Hz | 8.75 | 0.8 dB  |
| Peaking | 9713 Hz | 8.18 | -2.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-D7000%20B2012/Denon%20AH-D7000%20B2012.png)