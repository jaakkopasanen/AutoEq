# FLC Technologies FLC8 GGBl

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -1.8; 22 -1.9; 23 -1.9; 25 -2.0; 26 -2.1; 28 -2.1; 30 -2.2; 32 -2.2; 35 -2.1; 37 -2.1; 40 -2.1; 42 -2.1; 45 -2.1; 49 -2.1; 52 -2.1; 56 -2.1; 59 -2.2; 64 -2.2; 68 -2.3; 73 -2.3; 78 -2.4; 83 -2.5; 89 -2.6; 95 -2.7; 102 -2.7; 109 -2.7; 117 -2.7; 125 -2.7; 134 -2.8; 143 -2.8; 153 -2.8; 164 -2.7; 175 -2.6; 188 -2.5; 201 -2.5; 215 -2.3; 230 -2.2; 246 -2.0; 263 -1.9; 282 -1.7; 301 -1.6; 323 -1.4; 345 -1.2; 369 -0.9; 395 -0.8; 423 -0.4; 452 -0.2; 484 -0.1; 518 0.1; 554 0.4; 593 0.8; 635 0.9; 679 0.8; 726 0.8; 777 1.0; 832 1.2; 890 0.8; 952 0.4; 1019 -0.1; 1090 -0.5; 1167 -0.7; 1248 -0.8; 1336 -0.7; 1429 -0.4; 1529 0.2; 1636 0.8; 1751 1.8; 1873 2.8; 2004 3.9; 2145 4.6; 2295 5.3; 2455 5.9; 2627 5.9; 2811 5.6; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999678132dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FLC Technologies FLC8 GGBl ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 38 Hz   | 0.25 | -2.0 dB |
| Peaking | 178 Hz  | 0.73 | -1.9 dB |
| Peaking | 1470 Hz | 1.4  | -6.4 dB |
| Peaking | 2210 Hz | 0.63 | 7.7 dB  |
| Peaking | 5307 Hz | 2.28 | 4.0 dB  |
| Peaking | 780 Hz  | 1.9  | 0.6 dB  |
| Peaking | 1072 Hz | 4.81 | -1.0 dB |
| Peaking | 3982 Hz | 2.53 | 1.4 dB  |
| Peaking | 6388 Hz | 3.96 | 4.6 dB  |
| Peaking | 6850 Hz | 1.3  | -3.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/FLC%20Technologies%20FLC8%20GGBl/FLC%20Technologies%20FLC8%20GGBl.png)