# ZMF Eikon

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.7dB
GraphicEQ: 10 -84; 20 -3.4; 22 -3.5; 23 -3.5; 25 -3.6; 26 -3.6; 28 -3.6; 30 -3.6; 32 -3.6; 35 -3.6; 37 -3.6; 40 -3.5; 42 -3.5; 45 -3.5; 49 -3.7; 52 -3.6; 56 -3.4; 59 -3.3; 64 -3.6; 68 -4.1; 73 -4.8; 78 -5.2; 83 -5.6; 89 -5.9; 95 -6.2; 102 -6.3; 109 -6.3; 117 -6.3; 125 -6.3; 134 -6.2; 143 -6.1; 153 -5.5; 164 -4.9; 175 -5.3; 188 -5.0; 201 -4.8; 215 -4.4; 230 -4.2; 246 -4.1; 263 -3.9; 282 -3.9; 301 -3.9; 323 -3.9; 345 -3.7; 369 -3.4; 395 -3.0; 423 -2.4; 452 -2.2; 484 -2.1; 518 -1.8; 554 -1.3; 593 -0.7; 635 -0.5; 679 -0.5; 726 -0.3; 777 -0.3; 832 -0.6; 890 -0.5; 952 -0.3; 1019 0.1; 1090 0.3; 1167 0.3; 1248 0.2; 1336 0.1; 1429 1.1; 1529 4.7; 1636 4.9; 1751 2.5; 1873 1.1; 2004 0.3; 2145 -0.1; 2295 1.0; 2455 1.4; 2627 0.8; 2811 0.6; 3008 0.7; 3219 0.9; 3444 1.5; 3685 0.9; 3943 -1.0; 4219 -1.1; 4514 -0.7; 4830 0.2; 5168 0.5; 5530 -1.5; 5917 -3.2; 6331 4.1; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -1.5; 9502 -1.3; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.740886441264028dB` and instead set Global volume in the UI for both channels to **-57**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `ZMF Eikon ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 1.22 | -2.8 dB |
| Peaking | 129 Hz  | 0.44 | -6.0 dB |
| Peaking | 1585 Hz | 6.16 | 5.9 dB  |
| Peaking | 5911 Hz | 8.45 | -5.6 dB |
| Peaking | 6488 Hz | 7.07 | 6.7 dB  |
| Peaking | 360 Hz  | 3.96 | -0.9 dB |
| Peaking | 662 Hz  | 3.77 | 0.7 dB  |
| Peaking | 3744 Hz | 2.08 | 2.4 dB  |
| Peaking | 4097 Hz | 4.75 | -3.5 dB |
| Peaking | 9094 Hz | 8.57 | -2.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/ZMF%20Eikon/ZMF%20Eikon.png)