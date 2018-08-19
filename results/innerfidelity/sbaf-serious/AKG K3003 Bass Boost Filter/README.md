# AKG K3003 Bass Boost Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.3dB
GraphicEQ: 10 -84; 20 -0.4; 22 -0.9; 23 -1.2; 25 -1.6; 26 -1.8; 28 -2.2; 30 -2.5; 32 -2.9; 35 -3.3; 37 -3.5; 40 -3.9; 42 -4.1; 45 -4.4; 49 -4.7; 52 -5.0; 56 -5.3; 59 -5.5; 64 -5.9; 68 -6.2; 73 -6.5; 78 -6.8; 83 -7.1; 89 -7.5; 95 -7.8; 102 -8.0; 109 -8.1; 117 -8.2; 125 -8.4; 134 -8.5; 143 -8.6; 153 -8.7; 164 -8.7; 175 -8.6; 188 -8.5; 201 -8.4; 215 -8.2; 230 -8.0; 246 -7.8; 263 -7.6; 282 -7.2; 301 -6.9; 323 -6.5; 345 -6.1; 369 -5.6; 395 -5.2; 423 -4.5; 452 -4.1; 484 -3.8; 518 -3.3; 554 -2.6; 593 -2.0; 635 -1.5; 679 -1.2; 726 -0.8; 777 -0.3; 832 -0.2; 890 -0.1; 952 -0.1; 1019 0.0; 1090 -0.1; 1167 -0.1; 1248 -0.2; 1336 -0.3; 1429 -0.1; 1529 -0.4; 1636 -1.0; 1751 -1.6; 1873 -1.8; 2004 -2.0; 2145 -2.2; 2295 -2.3; 2455 -1.7; 2627 -0.7; 2811 0.7; 3008 2.7; 3219 4.2; 3444 5.2; 3685 4.9; 3943 3.7; 4219 1.2; 4514 -1.3; 4830 -3.2; 5168 -4.6; 5530 -3.7; 5917 -0.9; 6331 1.5; 6775 2.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.7; 9502 -2.4; 10167 -1.6; 10879 -0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.339318794564122dB` and instead set Global volume in the UI for both channels to **-53**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K3003 Bass Boost Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 110 Hz  | 0.45 | -7.3 dB |
| Peaking | 268 Hz  | 0.9  | -3.8 dB |
| Peaking | 2421 Hz | 1.7  | -7.6 dB |
| Peaking | 3325 Hz | 1.09 | 9.0 dB  |
| Peaking | 5019 Hz | 3.47 | -8.5 dB |
| Peaking | 483 Hz  | 2.42 | -0.8 dB |
| Peaking | 807 Hz  | 1.38 | 0.9 dB  |
| Peaking | 1762 Hz | 6.55 | -0.9 dB |
| Peaking | 6749 Hz | 8.85 | 2.9 dB  |
| Peaking | 9621 Hz | 5.53 | -3.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K3003%20Bass%20Boost%20Filter/AKG%20K3003%20Bass%20Boost%20Filter.png)