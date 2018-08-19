# Alpha Design Labs H128

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 0.6; 22 0.0; 23 -0.3; 25 -0.8; 26 -1.0; 28 -1.4; 30 -1.8; 32 -2.1; 35 -2.4; 37 -2.6; 40 -2.9; 42 -3.0; 45 -3.2; 49 -3.4; 52 -3.6; 56 -3.7; 59 -3.8; 64 -4.0; 68 -4.0; 73 -4.2; 78 -4.4; 83 -4.6; 89 -4.7; 95 -4.8; 102 -4.8; 109 -4.6; 117 -4.5; 125 -4.4; 134 -4.6; 143 -5.0; 153 -5.2; 164 -5.0; 175 -4.5; 188 -4.4; 201 -4.2; 215 -4.0; 230 -4.0; 246 -3.7; 263 -3.5; 282 -3.2; 301 -3.0; 323 -2.7; 345 -2.5; 369 -2.3; 395 -2.1; 423 -2.0; 452 -2.0; 484 -2.0; 518 -2.1; 554 -1.9; 593 -1.6; 635 -1.6; 679 -1.6; 726 -1.6; 777 -1.4; 832 -1.2; 890 -0.7; 952 0.0; 1019 -0.1; 1090 -0.7; 1167 -0.6; 1248 -0.3; 1336 -0.3; 1429 -0.2; 1529 -0.1; 1636 -0.1; 1751 0.2; 1873 0.5; 2004 0.9; 2145 0.8; 2295 0.7; 2455 1.5; 2627 2.2; 2811 2.9; 3008 3.3; 3219 3.7; 3444 4.9; 3685 5.9; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.3; 9502 -0.5; 10167 -0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999674948805dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Alpha Design Labs H128 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 1.44 | 2.2 dB  |
| Peaking | 67 Hz   | 0.47 | -3.4 dB |
| Peaking | 178 Hz  | 0.73 | -2.9 dB |
| Peaking | 602 Hz  | 0.68 | -1.1 dB |
| Peaking | 4523 Hz | 1.28 | 6.9 dB  |
| Peaking | 1649 Hz | 3.74 | -0.4 dB |
| Peaking | 3675 Hz | 2.98 | 1.2 dB  |
| Peaking | 4444 Hz | 3.46 | -1.4 dB |
| Peaking | 6295 Hz | 3.29 | 3.9 dB  |
| Peaking | 7699 Hz | 1.57 | -2.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Alpha%20Design%20Labs%20H128/Alpha%20Design%20Labs%20H128.png)