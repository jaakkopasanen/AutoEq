# Audeo PFE 121 Black Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 0.5; 22 0.4; 23 0.3; 25 0.2; 26 0.1; 28 0.1; 30 -0.0; 32 -0.1; 35 -0.2; 37 -0.3; 40 -0.4; 42 -0.5; 45 -0.6; 49 -0.8; 52 -1.0; 56 -1.2; 59 -1.3; 64 -1.6; 68 -1.8; 73 -2.1; 78 -2.3; 83 -2.6; 89 -2.9; 95 -3.1; 102 -3.3; 109 -3.4; 117 -3.6; 125 -3.8; 134 -3.9; 143 -4.1; 153 -4.1; 164 -4.2; 175 -4.2; 188 -4.2; 201 -4.2; 215 -4.1; 230 -3.9; 246 -3.9; 263 -3.7; 282 -3.6; 301 -3.4; 323 -3.2; 345 -3.0; 369 -2.8; 395 -2.6; 423 -2.2; 452 -2.0; 484 -1.8; 518 -1.6; 554 -1.1; 593 -0.6; 635 -0.3; 679 -0.2; 726 -0.1; 777 0.3; 832 0.3; 890 0.2; 952 0.0; 1019 0.0; 1090 -0.2; 1167 -0.1; 1248 -0.1; 1336 -0.2; 1429 -0.4; 1529 -0.6; 1636 -0.6; 1751 -0.2; 1873 0.4; 2004 0.9; 2145 1.7; 2295 2.7; 2455 3.5; 2627 3.2; 2811 2.9; 3008 3.5; 3219 4.1; 3444 4.9; 3685 5.5; 3943 5.5; 4219 5.0; 4514 5.1; 4830 5.9; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 -1.2; 8299 -3.8; 8880 -4.2; 9502 -3.3; 10167 -2.2; 10879 -0.4; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.0994290242552625dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeo PFE 121 Black Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.3dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 133 Hz  | 0.74 | -3.3 dB |
| Peaking | 282 Hz  | 0.96 | -2.4 dB |
| Peaking | 3532 Hz | 1.43 | 3.8 dB  |
| Peaking | 6030 Hz | 1.48 | 6.4 dB  |
| Peaking | 8582 Hz | 2.53 | -7.3 dB |
| Peaking | 21 Hz   | 1.13 | 0.6 dB  |
| Peaking | 794 Hz  | 3.38 | 0.8 dB  |
| Peaking | 1621 Hz | 2.62 | -1.2 dB |
| Peaking | 2387 Hz | 7.1  | 1.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeo%20PFE%20121%20Black%20Filter/Audeo%20PFE%20121%20Black%20Filter.png)