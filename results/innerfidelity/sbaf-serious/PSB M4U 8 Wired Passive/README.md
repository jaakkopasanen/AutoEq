# PSB M4U 8 Wired Passive

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.4dB
GraphicEQ: 10 -84; 20 -5.5; 22 -5.5; 23 -5.5; 25 -5.5; 26 -5.5; 28 -5.4; 30 -5.3; 32 -5.3; 35 -5.1; 37 -5.0; 40 -4.8; 42 -4.7; 45 -4.5; 49 -4.3; 52 -4.2; 56 -4.3; 59 -4.5; 64 -4.5; 68 -4.3; 73 -4.1; 78 -3.8; 83 -3.6; 89 -3.5; 95 -3.6; 102 -4.5; 109 -5.3; 117 -5.7; 125 -6.3; 134 -7.2; 143 -7.2; 153 -6.8; 164 -5.5; 175 -6.2; 188 -6.3; 201 -5.8; 215 -5.3; 230 -4.6; 246 -4.0; 263 -3.5; 282 -3.0; 301 -3.0; 323 -2.4; 345 -1.8; 369 -1.2; 395 -0.7; 423 -0.0; 452 0.4; 484 0.4; 518 0.9; 554 1.3; 593 1.7; 635 1.9; 679 1.7; 726 1.6; 777 1.3; 832 0.7; 890 0.2; 952 0.1; 1019 -0.1; 1090 -0.3; 1167 -0.8; 1248 -1.0; 1336 -1.2; 1429 -1.3; 1529 -1.4; 1636 -1.4; 1751 -1.3; 1873 -0.8; 2004 -0.2; 2145 -0.5; 2295 -0.5; 2455 -0.4; 2627 -0.4; 2811 -0.7; 3008 -0.8; 3219 -1.3; 3444 -1.8; 3685 -2.2; 3943 -2.7; 4219 -2.8; 4514 -1.8; 4830 -0.8; 5168 -0.4; 5530 -0.5; 5917 0.4; 6331 0.2; 6775 0.2; 7249 -0.3; 7756 0.1; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.4dB` and instead set Global volume in the UI for both channels to **-24**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `PSB M4U 8 Wired Passive ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 0.87 | -4.8 dB |
| Peaking | 38 Hz   | 0.76 | -3.4 dB |
| Peaking | 160 Hz  | 0.89 | -6.4 dB |
| Peaking | 601 Hz  | 2.18 | 2.7 dB  |
| Peaking | 3905 Hz | 2.68 | -2.7 dB |
| Peaking | 92 Hz   | 3.5  | 2.3 dB  |
| Peaking | 90 Hz   | 1.57 | -1.4 dB |
| Peaking | 1301 Hz | 0.68 | 0.8 dB  |
| Peaking | 1448 Hz | 1.61 | -2.2 dB |
| Peaking | 6114 Hz | 5.79 | 0.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/PSB%20M4U%208%20Wired%20Passive/PSB%20M4U%208%20Wired%20Passive.png)