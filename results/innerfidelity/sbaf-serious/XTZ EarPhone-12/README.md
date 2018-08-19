# XTZ EarPhone-12

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.9dB
GraphicEQ: 10 -84; 20 0.1; 22 -0.4; 23 -0.6; 25 -1.0; 26 -1.2; 28 -1.6; 30 -1.9; 32 -2.2; 35 -2.7; 37 -2.9; 40 -3.2; 42 -3.4; 45 -3.7; 49 -4.0; 52 -4.3; 56 -4.6; 59 -4.8; 64 -5.1; 68 -5.4; 73 -5.7; 78 -5.9; 83 -6.2; 89 -6.5; 95 -6.8; 102 -6.9; 109 -7.0; 117 -7.1; 125 -7.2; 134 -7.3; 143 -7.3; 153 -7.3; 164 -7.2; 175 -7.1; 188 -7.0; 201 -6.7; 215 -6.6; 230 -6.3; 246 -6.0; 263 -5.8; 282 -5.4; 301 -5.0; 323 -4.7; 345 -4.3; 369 -3.9; 395 -3.5; 423 -3.0; 452 -2.6; 484 -2.3; 518 -1.8; 554 -1.3; 593 -0.7; 635 -0.4; 679 -0.2; 726 0.1; 777 0.6; 832 0.6; 890 0.5; 952 0.2; 1019 -0.0; 1090 -0.2; 1167 -0.5; 1248 -0.7; 1336 -1.0; 1429 -1.4; 1529 -1.8; 1636 -2.3; 1751 -2.7; 1873 -3.0; 2004 -3.3; 2145 -3.4; 2295 -3.2; 2455 -2.7; 2627 -1.8; 2811 -0.8; 3008 0.8; 3219 2.1; 3444 3.4; 3685 3.6; 3943 3.0; 4219 1.4; 4514 0.4; 4830 0.5; 5168 1.1; 5530 1.9; 5917 2.7; 6331 3.5; 6775 3.6; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.9390929440544777dB` and instead set Global volume in the UI for both channels to **-39**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `XTZ EarPhone-12 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 102 Hz  | 0.53 | -6.4 dB |
| Peaking | 240 Hz  | 1.04 | -3.3 dB |
| Peaking | 2137 Hz | 2.05 | -3.9 dB |
| Peaking | 3557 Hz | 3.57 | 4.5 dB  |
| Peaking | 6409 Hz | 4.58 | 3.9 dB  |
| Peaking | 17 Hz   | 0.45 | 1.1 dB  |
| Peaking | 36 Hz   | 1.32 | -1.2 dB |
| Peaking | 413 Hz  | 2.56 | -0.7 dB |
| Peaking | 797 Hz  | 1.98 | 1.5 dB  |
| Peaking | 1576 Hz | 4.04 | -0.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/XTZ%20EarPhone-12/XTZ%20EarPhone-12.png)