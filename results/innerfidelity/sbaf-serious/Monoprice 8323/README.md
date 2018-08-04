# Monoprice 8323

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 5.3; 52 4.7; 56 4.0; 59 3.7; 64 3.3; 68 3.1; 73 3.0; 78 3.0; 83 2.9; 89 2.8; 95 2.7; 102 2.5; 109 2.5; 117 2.4; 125 2.1; 134 1.8; 143 1.6; 153 1.4; 164 1.8; 175 1.9; 188 1.6; 201 1.6; 215 1.7; 230 1.7; 246 1.8; 263 2.1; 282 2.4; 301 2.9; 323 3.2; 345 3.3; 369 3.2; 395 2.8; 423 2.5; 452 2.1; 484 1.6; 518 1.3; 554 1.2; 593 1.2; 635 1.0; 679 0.7; 726 0.5; 777 0.5; 832 0.3; 890 0.1; 952 -0.0; 1019 0.0; 1090 0.5; 1167 0.2; 1248 -0.2; 1336 -0.4; 1429 -0.5; 1529 -1.0; 1636 -1.1; 1751 -0.7; 1873 0.4; 2004 1.4; 2145 2.3; 2295 3.7; 2455 5.3; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.9; 8880 -2.1; 9502 -1.7; 10167 -0.1; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monoprice 8323 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.54 | 6.3 dB  |
| Peaking | 125 Hz  | 0.92 | 0.8 dB  |
| Peaking | 348 Hz  | 1.83 | 3.1 dB  |
| Peaking | 4385 Hz | 0.86 | 7.1 dB  |
| Peaking | 8832 Hz | 3.01 | -4.4 dB |
| Peaking | 2200 Hz | 4.7  | -1.0 dB |
| Peaking | 1671 Hz | 2.15 | -3.2 dB |
| Peaking | 2543 Hz | 1.9  | 4.1 dB  |
| Peaking | 4340 Hz | 0.86 | -1.6 dB |
| Peaking | 6121 Hz | 4.07 | 2.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monoprice%208323/Monoprice%208323.png)