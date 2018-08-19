# NarMoo B2M

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -7.5; 22 -7.4; 23 -7.4; 25 -7.3; 26 -7.3; 28 -7.2; 30 -7.1; 32 -7.0; 35 -6.8; 37 -6.7; 40 -6.5; 42 -6.5; 45 -6.3; 49 -6.2; 52 -6.1; 56 -5.9; 59 -5.9; 64 -5.8; 68 -5.7; 73 -5.6; 78 -5.6; 83 -5.6; 89 -5.6; 95 -5.5; 102 -5.4; 109 -5.3; 117 -5.2; 125 -5.1; 134 -5.0; 143 -4.9; 153 -4.8; 164 -4.6; 175 -4.4; 188 -4.2; 201 -4.1; 215 -3.9; 230 -3.6; 246 -3.5; 263 -3.3; 282 -3.1; 301 -2.9; 323 -2.7; 345 -2.4; 369 -2.2; 395 -2.0; 423 -1.7; 452 -1.5; 484 -1.4; 518 -1.2; 554 -0.9; 593 -0.5; 635 -0.3; 679 -0.3; 726 -0.1; 777 0.2; 832 0.3; 890 0.2; 952 0.1; 1019 -0.1; 1090 -0.2; 1167 -0.2; 1248 -0.3; 1336 -0.6; 1429 -0.8; 1529 -1.1; 1636 -1.5; 1751 -0.5; 1873 0.2; 2004 0.4; 2145 0.4; 2295 0.5; 2455 0.9; 2627 1.5; 2811 2.3; 3008 4.0; 3219 5.8; 3444 6.0; 3685 6.0; 3943 6.0; 4219 5.5; 4514 3.3; 4830 2.3; 5168 3.9; 5530 5.9; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999991048582dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NarMoo B2M ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.28 | -7.1 dB |
| Peaking | 149 Hz  | 0.49 | -3.7 dB |
| Peaking | 3592 Hz | 2.68 | 6.4 dB  |
| Peaking | 6084 Hz | 2.95 | 6.5 dB  |
| Peaking | 7708 Hz | 2.08 | -1.6 dB |
| Peaking | 796 Hz  | 2.8  | 0.8 dB  |
| Peaking | 1584 Hz | 4.74 | -1.6 dB |
| Peaking | 3081 Hz | 2.9  | -0.7 dB |
| Peaking | 3129 Hz | 8.1  | 1.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NarMoo%20B2M/NarMoo%20B2M.png)