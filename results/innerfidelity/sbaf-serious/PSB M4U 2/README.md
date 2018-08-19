# PSB M4U 2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.4dB
GraphicEQ: 10 -84; 20 3.1; 22 0.9; 23 0.0; 25 -1.1; 26 -1.4; 28 -1.6; 30 -1.3; 32 -0.9; 35 -0.2; 37 0.2; 40 0.7; 42 0.9; 45 1.2; 49 1.5; 52 1.7; 56 1.8; 59 1.9; 64 2.0; 68 2.1; 73 2.3; 78 2.4; 83 2.3; 89 1.9; 95 1.1; 102 0.4; 109 0.1; 117 0.1; 125 0.1; 134 0.1; 143 -0.0; 153 0.0; 164 0.5; 175 0.1; 188 0.0; 201 0.2; 215 0.4; 230 0.7; 246 0.9; 263 1.2; 282 1.7; 301 2.0; 323 2.3; 345 2.8; 369 2.8; 395 3.1; 423 3.7; 452 3.9; 484 3.6; 518 3.5; 554 3.5; 593 3.4; 635 3.3; 679 3.1; 726 2.7; 777 2.3; 832 1.9; 890 1.2; 952 0.6; 1019 -0.1; 1090 -0.5; 1167 -0.9; 1248 -1.4; 1336 -2.1; 1429 -2.9; 1529 -3.6; 1636 -3.7; 1751 -3.5; 1873 -2.8; 2004 -2.2; 2145 -1.6; 2295 -1.2; 2455 -0.3; 2627 0.4; 2811 0.9; 3008 1.0; 3219 0.5; 3444 0.2; 3685 -0.4; 3943 -0.0; 4219 0.8; 4514 1.0; 4830 1.9; 5168 3.1; 5530 4.5; 5917 5.2; 6331 4.3; 6775 3.6; 7249 1.3; 7756 0.3; 8299 -0.1; 8880 -0.7; 9502 -0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.40903803459118dB` and instead set Global volume in the UI for both channels to **-54**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `PSB M4U 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 69 Hz   | 2.06 | 2.5 dB  |
| Peaking | 526 Hz  | 0.99 | 4.1 dB  |
| Peaking | 1615 Hz | 1.68 | -4.3 dB |
| Peaking | 2813 Hz | 4.69 | 1.6 dB  |
| Peaking | 5889 Hz | 3.47 | 5.6 dB  |
| Peaking | 17 Hz   | 0.68 | 4.1 dB  |
| Peaking | 28 Hz   | 2.08 | -4.5 dB |
| Peaking | 143 Hz  | 1.44 | -0.7 dB |
| Peaking | 794 Hz  | 6.07 | 0.4 dB  |
| Peaking | 8712 Hz | 5.66 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/PSB%20M4U%202/PSB%20M4U%202.png)