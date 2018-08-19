# Syun ME1 Gold

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.3dB
GraphicEQ: 10 -84; 20 6.2; 22 5.7; 23 5.4; 25 5.0; 26 4.7; 28 4.3; 30 3.8; 32 3.3; 35 2.7; 37 2.4; 40 2.0; 42 1.8; 45 1.4; 49 0.9; 52 0.6; 56 0.2; 59 -0.1; 64 -0.5; 68 -0.9; 73 -1.3; 78 -1.7; 83 -2.1; 89 -2.5; 95 -2.8; 102 -3.3; 109 -3.5; 117 -3.7; 125 -4.0; 134 -4.4; 143 -4.6; 153 -4.9; 164 -5.1; 175 -5.2; 188 -5.3; 201 -5.5; 215 -5.5; 230 -5.5; 246 -5.5; 263 -5.5; 282 -5.4; 301 -5.3; 323 -5.2; 345 -5.0; 369 -4.7; 395 -4.5; 423 -4.0; 452 -3.6; 484 -3.4; 518 -3.0; 554 -2.5; 593 -1.9; 635 -1.6; 679 -1.4; 726 -1.2; 777 -0.9; 832 -0.5; 890 0.0; 952 0.2; 1019 -0.0; 1090 -0.2; 1167 -0.4; 1248 -0.7; 1336 -1.0; 1429 -1.4; 1529 -1.8; 1636 -2.0; 1751 -2.1; 1873 -2.0; 2004 -1.8; 2145 -1.6; 2295 -1.2; 2455 -0.6; 2627 0.0; 2811 0.8; 3008 1.8; 3219 2.6; 3444 3.1; 3685 2.5; 3943 1.1; 4219 -1.7; 4514 -4.1; 4830 -5.5; 5168 -3.6; 5530 -0.7; 5917 2.9; 6331 4.7; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.2900447304597815dB` and instead set Global volume in the UI for both channels to **-62**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Syun ME1 Gold ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.2dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.68 | 6.4 dB  |
| Peaking | 214 Hz  | 0.51 | -5.8 dB |
| Peaking | 3581 Hz | 3.59 | 5.3 dB  |
| Peaking | 4851 Hz | 2.47 | -7.1 dB |
| Peaking | 6295 Hz | 3.98 | 7.1 dB  |
| Peaking | 389 Hz  | 2.81 | -0.6 dB |
| Peaking | 952 Hz  | 1.71 | 1.5 dB  |
| Peaking | 1779 Hz | 1.66 | -2.1 dB |
| Peaking | 3020 Hz | 5.09 | 1.2 dB  |
| Peaking | 7810 Hz | 7.72 | -0.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Syun%20ME1%20Gold/Syun%20ME1%20Gold.png)