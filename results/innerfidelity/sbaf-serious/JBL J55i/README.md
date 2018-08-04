# JBL J55i

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -4.2; 22 -4.2; 23 -4.2; 25 -4.2; 26 -4.2; 28 -4.2; 30 -4.2; 32 -4.1; 35 -4.1; 37 -4.1; 40 -4.0; 42 -4.0; 45 -4.0; 49 -4.0; 52 -4.0; 56 -4.0; 59 -4.0; 64 -4.1; 68 -4.1; 73 -4.2; 78 -4.3; 83 -4.4; 89 -4.7; 95 -5.0; 102 -5.3; 109 -5.5; 117 -6.0; 125 -6.4; 134 -6.8; 143 -7.1; 153 -7.2; 164 -7.2; 175 -6.9; 188 -7.0; 201 -7.2; 215 -7.2; 230 -7.0; 246 -6.7; 263 -6.3; 282 -5.8; 301 -5.4; 323 -5.1; 345 -4.7; 369 -4.2; 395 -3.6; 423 -2.7; 452 -1.9; 484 -1.2; 518 -0.2; 554 0.9; 593 1.8; 635 2.0; 679 1.7; 726 1.1; 777 0.7; 832 -0.0; 890 -0.4; 952 -0.4; 1019 0.2; 1090 0.8; 1167 1.6; 1248 1.9; 1336 1.4; 1429 -0.2; 1529 -1.7; 1636 -1.3; 1751 3.0; 1873 6.0; 2004 4.0; 2145 0.2; 2295 1.3; 2455 3.7; 2627 5.7; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JBL J55i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.5  | -3.8 dB |
| Peaking | 194 Hz  | 0.54 | -7.2 dB |
| Peaking | 610 Hz  | 2.31 | 4.1 dB  |
| Peaking | 3319 Hz | 1.21 | 6.2 dB  |
| Peaking | 5632 Hz | 2.85 | 4.5 dB  |
| Peaking | 1258 Hz | 5.66 | 2.2 dB  |
| Peaking | 1608 Hz | 4    | -6.8 dB |
| Peaking | 1878 Hz | 3.44 | 8.4 dB  |
| Peaking | 2165 Hz | 6.56 | -6.1 dB |
| Peaking | 8425 Hz | 3.65 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/JBL%20J55i/JBL%20J55i.png)