# Fender FXA6

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -5.3; 22 -5.2; 23 -5.2; 25 -5.1; 26 -5.1; 28 -5.1; 30 -5.0; 32 -5.0; 35 -4.9; 37 -4.9; 40 -4.9; 42 -4.9; 45 -4.9; 49 -4.9; 52 -4.9; 56 -5.0; 59 -5.0; 64 -5.1; 68 -5.2; 73 -5.4; 78 -5.5; 83 -5.7; 89 -5.8; 95 -6.0; 102 -6.1; 109 -6.0; 117 -6.1; 125 -6.2; 134 -6.2; 143 -6.2; 153 -6.2; 164 -6.1; 175 -5.9; 188 -5.8; 201 -5.7; 215 -5.4; 230 -5.2; 246 -5.0; 263 -4.8; 282 -4.4; 301 -4.1; 323 -3.7; 345 -3.4; 369 -3.0; 395 -2.7; 423 -2.2; 452 -1.8; 484 -1.6; 518 -1.3; 554 -0.8; 593 -0.3; 635 -0.1; 679 0.1; 726 0.3; 777 0.6; 832 0.5; 890 0.4; 952 0.2; 1019 -0.1; 1090 -0.3; 1167 -0.4; 1248 -0.8; 1336 -1.5; 1429 -2.2; 1529 -3.1; 1636 -4.1; 1751 -5.2; 1873 -6.1; 2004 -6.8; 2145 -6.4; 2295 -4.7; 2455 -2.2; 2627 -0.0; 2811 1.7; 3008 3.5; 3219 4.3; 3444 3.8; 3685 2.2; 3943 1.2; 4219 1.5; 4514 2.8; 4830 4.5; 5168 5.9; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.094765865819561dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fender FXA6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.15 | -4.9 dB |
| Peaking | 182 Hz  | 0.74 | -4.1 dB |
| Peaking | 2012 Hz | 2.58 | -7.8 dB |
| Peaking | 3127 Hz | 3.55 | 5.2 dB  |
| Peaking | 5642 Hz | 2.78 | 6.8 dB  |
| Peaking | 359 Hz  | 1.88 | -0.8 dB |
| Peaking | 788 Hz  | 1.41 | 1.4 dB  |
| Peaking | 1567 Hz | 5.04 | -1.0 dB |
| Peaking | 6632 Hz | 7.46 | 2.3 dB  |
| Peaking | 7609 Hz | 2.19 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fender%20FXA6/Fender%20FXA6.png)