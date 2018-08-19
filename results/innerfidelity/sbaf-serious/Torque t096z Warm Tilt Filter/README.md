# Torque t096z Warm Tilt Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.9dB
GraphicEQ: 10 -84; 20 -4.3; 22 -4.6; 23 -4.8; 25 -5.0; 26 -5.1; 28 -5.4; 30 -5.5; 32 -5.7; 35 -5.8; 37 -5.9; 40 -6.1; 42 -6.2; 45 -6.3; 49 -6.4; 52 -6.6; 56 -6.7; 59 -6.8; 64 -7.0; 68 -7.1; 73 -7.3; 78 -7.5; 83 -7.6; 89 -7.8; 95 -7.9; 102 -7.9; 109 -7.9; 117 -7.9; 125 -7.9; 134 -7.9; 143 -7.8; 153 -7.7; 164 -7.6; 175 -7.4; 188 -7.1; 201 -6.9; 215 -6.5; 230 -6.2; 246 -5.9; 263 -5.6; 282 -5.1; 301 -4.8; 323 -4.4; 345 -3.9; 369 -3.5; 395 -3.1; 423 -2.5; 452 -2.0; 484 -1.8; 518 -1.4; 554 -0.9; 593 -0.3; 635 0.0; 679 0.2; 726 0.4; 777 0.7; 832 0.6; 890 0.4; 952 0.2; 1019 -0.1; 1090 -0.4; 1167 -0.8; 1248 -1.2; 1336 -1.9; 1429 -2.6; 1529 -3.4; 1636 -4.1; 1751 -4.9; 1873 -5.6; 2004 -6.2; 2145 -6.9; 2295 -7.3; 2455 -6.4; 2627 -5.0; 2811 -2.8; 3008 -0.3; 3219 1.1; 3444 2.1; 3685 1.7; 3943 -0.0; 4219 -3.4; 4514 -6.0; 4830 -5.1; 5168 -1.5; 5530 2.5; 5917 5.6; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.3; 10167 -0.4; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.91766217295971dB` and instead set Global volume in the UI for both channels to **-59**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t096z Warm Tilt Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.3dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 55 Hz   | 0.33 | -6.2 dB |
| Peaking | 179 Hz  | 0.77 | -4.4 dB |
| Peaking | 2124 Hz | 2.54 | -7.7 dB |
| Peaking | 4680 Hz | 7    | -7.6 dB |
| Peaking | 6122 Hz | 4.11 | 6.9 dB  |
| Peaking | 787 Hz  | 2.27 | 1.7 dB  |
| Peaking | 1561 Hz | 4.74 | -1.6 dB |
| Peaking | 2569 Hz | 6.32 | -2.6 dB |
| Peaking | 3475 Hz | 3.04 | 3.9 dB  |
| Peaking | 4243 Hz | 6.07 | -2.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t096z%20Warm%20Tilt%20Filter/Torque%20t096z%20Warm%20Tilt%20Filter.png)