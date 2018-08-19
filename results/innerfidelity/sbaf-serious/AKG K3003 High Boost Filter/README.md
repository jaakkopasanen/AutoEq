# AKG K3003 High Boost Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.4dB
GraphicEQ: 10 -84; 20 4.3; 22 3.8; 23 3.5; 25 3.0; 26 2.8; 28 2.5; 30 2.1; 32 1.8; 35 1.4; 37 1.2; 40 0.8; 42 0.6; 45 0.3; 49 -0.1; 52 -0.3; 56 -0.7; 59 -0.9; 64 -1.3; 68 -1.6; 73 -1.9; 78 -2.2; 83 -2.5; 89 -2.9; 95 -3.2; 102 -3.5; 109 -3.6; 117 -3.8; 125 -4.0; 134 -4.2; 143 -4.3; 153 -4.5; 164 -4.5; 175 -4.5; 188 -4.5; 201 -4.5; 215 -4.3; 230 -4.2; 246 -4.1; 263 -4.0; 282 -3.7; 301 -3.5; 323 -3.3; 345 -3.0; 369 -2.7; 395 -2.5; 423 -2.1; 452 -1.8; 484 -1.6; 518 -1.4; 554 -1.0; 593 -0.5; 635 -0.3; 679 -0.2; 726 0.1; 777 0.3; 832 0.3; 890 0.2; 952 0.1; 1019 -0.1; 1090 -0.3; 1167 -0.4; 1248 -0.5; 1336 -0.7; 1429 -0.9; 1529 -1.2; 1636 -1.6; 1751 -1.8; 1873 -1.7; 2004 -1.6; 2145 -1.6; 2295 -1.6; 2455 -1.5; 2627 -1.5; 2811 -1.7; 3008 -1.3; 3219 -0.2; 3444 2.3; 3685 3.7; 3943 3.3; 4219 0.2; 4514 -4.6; 4830 -6.6; 5168 -6.0; 5530 -6.4; 5917 -4.9; 6331 -1.4; 6775 0.8; 7249 1.2; 7756 0.0; 8299 -2.8; 8880 -6.6; 9502 -9.4; 10167 -9.3; 10879 -5.9; 11640 -0.9; 12455 0.0; 13327 0.0; 14260 0.0; 15258 -0.1; 16326 -0.5; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.439059597351554dB` and instead set Global volume in the UI for both channels to **-44**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K3003 High Boost Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.3dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 17 Hz    | 0.75 | 4.6 dB   |
| Peaking | 165 Hz   | 0.56 | -4.8 dB  |
| Peaking | 5338 Hz  | 3.95 | -7.6 dB  |
| Peaking | 7175 Hz  | 3.59 | 3.8 dB   |
| Peaking | 9714 Hz  | 3.7  | -11.0 dB |
| Peaking | 817 Hz   | 2.03 | 1.3 dB   |
| Peaking | 2644 Hz  | 0.87 | -2.3 dB  |
| Peaking | 3810 Hz  | 3.44 | 6.9 dB   |
| Peaking | 4611 Hz  | 8.67 | -4.3 dB  |
| Peaking | 12294 Hz | 6.1  | 2.0 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K3003%20High%20Boost%20Filter/AKG%20K3003%20High%20Boost%20Filter.png)