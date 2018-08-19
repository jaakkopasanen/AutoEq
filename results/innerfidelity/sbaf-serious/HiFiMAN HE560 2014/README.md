# HiFiMAN HE560 2014

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.1dB
GraphicEQ: 10 -84; 20 2.0; 22 2.0; 23 2.0; 25 2.1; 26 2.1; 28 2.1; 30 2.2; 32 2.2; 35 2.2; 37 2.2; 40 2.2; 42 2.2; 45 2.3; 49 2.2; 52 2.2; 56 2.1; 59 2.0; 64 1.9; 68 1.7; 73 1.4; 78 1.2; 83 1.1; 89 0.9; 95 0.6; 102 0.4; 109 0.2; 117 -0.0; 125 -0.3; 134 -0.5; 143 -0.6; 153 -0.7; 164 -0.9; 175 -0.9; 188 -1.1; 201 -1.3; 215 -1.3; 230 -1.4; 246 -1.5; 263 -1.5; 282 -1.1; 301 -1.1; 323 -1.3; 345 -1.6; 369 -1.8; 395 -2.0; 423 -2.1; 452 -1.7; 484 -1.1; 518 0.2; 554 1.7; 593 1.6; 635 0.7; 679 0.3; 726 0.0; 777 -0.4; 832 -0.7; 890 -0.3; 952 -0.0; 1019 0.1; 1090 -0.1; 1167 -0.5; 1248 -0.4; 1336 -0.8; 1429 -0.0; 1529 0.2; 1636 0.9; 1751 2.2; 1873 2.5; 2004 2.8; 2145 2.8; 2295 1.9; 2455 1.8; 2627 1.2; 2811 0.7; 3008 -0.6; 3219 -1.6; 3444 -1.6; 3685 -2.5; 3943 -2.5; 4219 -4.0; 4514 -4.7; 4830 -3.3; 5168 0.5; 5530 0.5; 5917 -0.5; 6331 -2.4; 6775 -2.0; 7249 -1.3; 7756 -1.4; 8299 -2.8; 8880 -3.9; 9502 -1.9; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.1028930363394394dB` and instead set Global volume in the UI for both channels to **-31**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE560 2014 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -3.2dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 38 Hz   | 0.53 | 2.5 dB  |
| Peaking | 243 Hz  | 0.78 | -1.8 dB |
| Peaking | 2063 Hz | 3.04 | 3.3 dB  |
| Peaking | 4287 Hz | 3.5  | -4.6 dB |
| Peaking | 8703 Hz | 4.85 | -3.8 dB |
| Peaking | 432 Hz  | 3.96 | -1.6 dB |
| Peaking | 571 Hz  | 5.37 | 2.7 dB  |
| Peaking | 1319 Hz | 6.34 | -1.0 dB |
| Peaking | 5372 Hz | 9.05 | 2.5 dB  |
| Peaking | 6469 Hz | 7.79 | -2.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20HE560%202014/HiFiMAN%20HE560%202014.png)