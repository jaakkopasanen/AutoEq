# AKG K3003 Reference Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 4.4; 22 3.9; 23 3.7; 25 3.2; 26 3.0; 28 2.6; 30 2.3; 32 2.0; 35 1.5; 37 1.3; 40 1.0; 42 0.7; 45 0.4; 49 0.1; 52 -0.2; 56 -0.6; 59 -0.8; 64 -1.2; 68 -1.5; 73 -1.8; 78 -2.2; 83 -2.4; 89 -2.8; 95 -3.2; 102 -3.4; 109 -3.5; 117 -3.6; 125 -3.9; 134 -4.2; 143 -4.3; 153 -4.3; 164 -4.4; 175 -4.4; 188 -4.4; 201 -4.3; 215 -4.2; 230 -4.1; 246 -4.0; 263 -3.9; 282 -3.6; 301 -3.4; 323 -3.2; 345 -2.9; 369 -2.6; 395 -2.4; 423 -1.9; 452 -1.7; 484 -1.5; 518 -1.3; 554 -0.9; 593 -0.4; 635 -0.1; 679 -0.1; 726 0.1; 777 0.4; 832 0.4; 890 0.2; 952 0.1; 1019 -0.1; 1090 -0.3; 1167 -0.5; 1248 -0.6; 1336 -0.9; 1429 -1.2; 1529 -1.5; 1636 -2.0; 1751 -2.3; 1873 -2.2; 2004 -2.1; 2145 -1.9; 2295 -1.6; 2455 -0.6; 2627 0.4; 2811 1.6; 3008 3.0; 3219 4.2; 3444 5.9; 3685 6.0; 3943 5.9; 4219 2.8; 4514 -1.5; 4830 -3.7; 5168 -3.1; 5530 -1.5; 5917 1.3; 6331 3.6; 6775 3.8; 7249 1.3; 7756 0.3; 8299 -0.9; 8880 -3.7; 9502 -6.1; 10167 -6.5; 10879 -3.4; 11640 -0.1; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999952996727dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K3003 Reference Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.2dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 0.87 | 4.4 dB   |
| Peaking | 165 Hz   | 0.62 | -4.7 dB  |
| Peaking | 3699 Hz  | 2.11 | 15.0 dB  |
| Peaking | 5212 Hz  | 0.74 | -12.2 dB |
| Peaking | 6505 Hz  | 2.85 | 12.8 dB  |
| Peaking | 825 Hz   | 2.13 | 1.4 dB   |
| Peaking | 1835 Hz  | 3.32 | -1.4 dB  |
| Peaking | 8117 Hz  | 6.7  | 2.5 dB   |
| Peaking | 10030 Hz | 3.02 | -7.6 dB  |
| Peaking | 11463 Hz | 1.6  | 4.7 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K3003%20Reference%20Filter/AKG%20K3003%20Reference%20Filter.png)