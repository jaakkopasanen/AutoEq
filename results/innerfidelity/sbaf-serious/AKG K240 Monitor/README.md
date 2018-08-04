# AKG K240 Monitor

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 5.8; 35 5.2; 37 4.7; 40 3.9; 42 3.5; 45 2.9; 49 2.1; 52 1.7; 56 1.2; 59 0.9; 64 0.5; 68 0.3; 73 0.3; 78 0.1; 83 -0.2; 89 -0.7; 95 -1.0; 102 -1.4; 109 -1.9; 117 -2.5; 125 -3.0; 134 -3.4; 143 -3.6; 153 -3.7; 164 -3.5; 175 -3.6; 188 -3.7; 201 -3.7; 215 -3.6; 230 -3.4; 246 -3.3; 263 -3.2; 282 -3.1; 301 -3.0; 323 -3.0; 345 -3.2; 369 -3.1; 395 -2.9; 423 -2.6; 452 -2.4; 484 -2.4; 518 -2.2; 554 -1.8; 593 -1.3; 635 -1.0; 679 -0.9; 726 -0.6; 777 -0.4; 832 -0.4; 890 -0.2; 952 -0.0; 1019 0.0; 1090 0.1; 1167 0.4; 1248 0.5; 1336 0.2; 1429 -0.3; 1529 -0.8; 1636 -1.3; 1751 -1.4; 1873 -1.6; 2004 -1.4; 2145 -0.9; 2295 0.1; 2455 1.2; 2627 1.5; 2811 1.9; 3008 3.1; 3219 1.8; 3444 -1.8; 3685 -3.9; 3943 -2.6; 4219 -0.8; 4514 0.9; 4830 2.2; 5168 4.6; 5530 5.9; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -1.4; 8880 -3.2; 9502 -3.4; 10167 -2.1; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K240 Monitor ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.86 | 6.5 dB  |
| Peaking | 162 Hz  | 0.89 | -3.8 dB |
| Peaking | 386 Hz  | 1.25 | -2.1 dB |
| Peaking | 5926 Hz | 3.48 | 7.1 dB  |
| Peaking | 9025 Hz | 4.1  | -4.3 dB |
| Peaking | 1217 Hz | 2.28 | 1.0 dB  |
| Peaking | 1845 Hz | 2.28 | -2.2 dB |
| Peaking | 3131 Hz | 2.69 | 5.4 dB  |
| Peaking | 3640 Hz | 3.93 | -7.4 dB |
| Peaking | 5153 Hz | 7.52 | 1.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K240%20Monitor/AKG%20K240%20Monitor.png)