# PSB M4U 8 Wired Passive

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.0dB
GraphicEQ: 10 -84; 20 -5.5; 22 -5.5; 23 -5.5; 25 -5.5; 26 -5.5; 28 -5.4; 30 -5.4; 32 -5.3; 35 -5.2; 37 -5.1; 40 -5.0; 42 -4.8; 45 -4.7; 49 -4.5; 52 -4.5; 56 -4.7; 59 -4.9; 64 -5.0; 68 -4.9; 73 -4.8; 78 -4.6; 83 -4.4; 89 -4.3; 95 -4.3; 102 -5.1; 109 -5.7; 117 -5.9; 125 -6.3; 134 -7.0; 143 -7.0; 153 -6.5; 164 -5.3; 175 -5.9; 188 -6.1; 201 -5.6; 215 -5.1; 230 -4.5; 246 -3.9; 263 -3.4; 282 -2.9; 301 -2.9; 323 -2.4; 345 -1.8; 369 -1.2; 395 -0.6; 423 -0.0; 452 0.4; 484 0.5; 518 0.9; 554 1.3; 593 1.7; 635 1.9; 679 1.7; 726 1.6; 777 1.3; 832 0.7; 890 0.2; 952 0.1; 1019 -0.1; 1090 -0.3; 1167 -0.8; 1248 -1.0; 1336 -1.2; 1429 -1.3; 1529 -1.4; 1636 -1.4; 1751 -1.3; 1873 -0.8; 2004 -0.2; 2145 -0.5; 2295 -0.5; 2455 -0.4; 2627 -0.4; 2811 -0.7; 3008 -0.8; 3219 -1.3; 3444 -1.8; 3685 -2.2; 3943 -2.7; 4219 -2.8; 4514 -1.8; 4830 -0.8; 5168 -0.4; 5530 -0.5; 5917 0.4; 6331 0.2; 6775 0.2; 7249 -0.3; 7756 0.1; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-1.9769255444532858dB` and instead set Global volume in the UI for both channels to **-19**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `PSB M4U 8 Wired Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -2.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 12 Hz   | 1.05 | -5.2 dB |
| Peaking | 32 Hz   | 0.49 | -4.2 dB |
| Peaking | 158 Hz  | 0.81 | -5.9 dB |
| Peaking | 598 Hz  | 2.1  | 2.7 dB  |
| Peaking | 3905 Hz | 2.69 | -2.7 dB |
| Peaking | 86 Hz   | 1.67 | -1.0 dB |
| Peaking | 92 Hz   | 3.74 | 1.8 dB  |
| Peaking | 1343 Hz | 0.68 | 0.9 dB  |
| Peaking | 1450 Hz | 1.59 | -2.3 dB |
| Peaking | 6044 Hz | 5.82 | 0.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/PSB%20M4U%208%20Wired%20Passive/PSB%20M4U%208%20Wired%20Passive.png)