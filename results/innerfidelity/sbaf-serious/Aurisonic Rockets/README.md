# Aurisonic Rockets

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 2.0; 22 1.8; 23 1.7; 25 1.6; 26 1.6; 28 1.5; 30 1.4; 32 1.3; 35 1.2; 37 1.1; 40 0.9; 42 0.9; 45 0.8; 49 0.6; 52 0.5; 56 0.3; 59 0.2; 64 -0.1; 68 -0.3; 73 -0.6; 78 -0.8; 83 -1.1; 89 -1.4; 95 -1.7; 102 -2.0; 109 -2.0; 117 -2.2; 125 -2.5; 134 -2.7; 143 -2.8; 153 -3.0; 164 -3.1; 175 -3.0; 188 -3.2; 201 -3.2; 215 -3.2; 230 -3.0; 246 -3.1; 263 -3.0; 282 -2.8; 301 -2.8; 323 -2.6; 345 -2.4; 369 -2.2; 395 -2.0; 423 -1.8; 452 -1.5; 484 -1.3; 518 -1.1; 554 -0.8; 593 -0.3; 635 -0.1; 679 -0.0; 726 0.1; 777 0.5; 832 0.4; 890 0.3; 952 0.1; 1019 -0.1; 1090 -0.2; 1167 -0.4; 1248 -0.6; 1336 -0.6; 1429 -1.0; 1529 -1.4; 1636 -1.7; 1751 -1.7; 1873 -1.5; 2004 -1.1; 2145 -0.7; 2295 0.0; 2455 1.2; 2627 2.4; 2811 3.9; 3008 5.7; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999998308316dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Aurisonic Rockets ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.22 | 2.0 dB  |
| Peaking | 181 Hz  | 0.43 | -3.7 dB |
| Peaking | 742 Hz  | 1.58 | 1.3 dB  |
| Peaking | 1878 Hz | 1.66 | -3.7 dB |
| Peaking | 3989 Hz | 0.98 | 7.3 dB  |
| Peaking | 3069 Hz | 7.02 | 1.8 dB  |
| Peaking | 4102 Hz | 3.66 | -0.9 dB |
| Peaking | 6353 Hz | 2.27 | 5.0 dB  |
| Peaking | 7166 Hz | 0.72 | -1.5 dB |
| Peaking | 7477 Hz | 2.82 | -2.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Aurisonic%20Rockets/Aurisonic%20Rockets.png)