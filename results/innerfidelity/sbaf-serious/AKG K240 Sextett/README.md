# AKG K240 Sextett

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 5.9; 35 5.5; 37 4.9; 40 3.9; 42 3.3; 45 2.5; 49 1.6; 52 1.0; 56 0.4; 59 0.3; 64 0.6; 68 0.4; 73 -1.1; 78 -3.0; 83 -4.4; 89 -5.4; 95 -6.1; 102 -6.5; 109 -6.7; 117 -6.9; 125 -6.9; 134 -6.7; 143 -6.7; 153 -6.4; 164 -5.4; 175 -4.5; 188 -5.0; 201 -5.5; 215 -5.3; 230 -5.0; 246 -4.8; 263 -4.5; 282 -4.1; 301 -3.9; 323 -3.6; 345 -3.1; 369 -2.8; 395 -2.7; 423 -2.4; 452 -2.0; 484 -1.5; 518 -1.8; 554 -2.0; 593 -1.8; 635 -1.5; 679 -1.3; 726 -1.1; 777 -0.7; 832 -0.4; 890 -0.2; 952 0.0; 1019 -0.1; 1090 -0.3; 1167 -0.4; 1248 -0.6; 1336 -1.1; 1429 -1.7; 1529 -2.3; 1636 -2.8; 1751 -3.2; 1873 -3.4; 2004 -3.7; 2145 -3.7; 2295 -2.6; 2455 -2.5; 2627 -1.1; 2811 1.5; 3008 3.3; 3219 2.1; 3444 2.4; 3685 0.8; 3943 -1.1; 4219 -5.2; 4514 -7.2; 4830 -4.2; 5168 -0.2; 5530 1.6; 5917 1.9; 6331 0.6; 6775 -2.0; 7249 -4.1; 7756 -6.2; 8299 -8.6; 8880 -10.2; 9502 -9.8; 10167 -6.6; 10879 -2.0; 11640 -0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K240 Sextett ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.4dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 26 Hz    | 0.65 | 6.6 dB   |
| Peaking | 109 Hz   | 1.29 | -6.4 dB  |
| Peaking | 232 Hz   | 0.74 | -3.9 dB  |
| Peaking | 1919 Hz  | 3.01 | -3.9 dB  |
| Peaking | 8956 Hz  | 3.31 | -11.4 dB |
| Peaking | 2492 Hz  | 3.38 | -3.4 dB  |
| Peaking | 3080 Hz  | 2.35 | 5.3 dB   |
| Peaking | 4496 Hz  | 4.83 | -8.3 dB  |
| Peaking | 5689 Hz  | 5.12 | 4.3 dB   |
| Peaking | 11734 Hz | 6.17 | 2.1 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K240%20Sextett/AKG%20K240%20Sextett.png)