# Torque t096z Flat Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 2.8; 22 2.4; 23 2.2; 25 1.8; 26 1.7; 28 1.3; 30 1.1; 32 0.9; 35 0.6; 37 0.5; 40 0.2; 42 0.1; 45 -0.1; 49 -0.4; 52 -0.6; 56 -0.9; 59 -1.1; 64 -1.5; 68 -1.7; 73 -2.1; 78 -2.3; 83 -2.6; 89 -3.0; 95 -3.3; 102 -3.6; 109 -3.7; 117 -4.0; 125 -4.3; 134 -4.5; 143 -4.7; 153 -4.9; 164 -5.0; 175 -5.1; 188 -5.1; 201 -5.2; 215 -5.1; 230 -5.0; 246 -5.0; 263 -4.9; 282 -4.7; 301 -4.5; 323 -4.2; 345 -3.9; 369 -3.6; 395 -3.2; 423 -2.7; 452 -2.3; 484 -2.0; 518 -1.5; 554 -1.0; 593 -0.4; 635 -0.0; 679 0.2; 726 0.4; 777 0.7; 832 0.7; 890 0.5; 952 0.3; 1019 -0.1; 1090 -0.5; 1167 -1.0; 1248 -1.5; 1336 -2.2; 1429 -3.1; 1529 -4.1; 1636 -5.1; 1751 -6.0; 1873 -6.5; 2004 -6.5; 2145 -6.2; 2295 -4.6; 2455 -2.1; 2627 0.1; 2811 2.3; 3008 4.5; 3219 5.8; 3444 6.0; 3685 5.6; 3943 3.7; 4219 0.2; 4514 -1.6; 4830 0.3; 5168 4.6; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999988230117dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t096z Flat Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.2  | 2.8 dB  |
| Peaking | 183 Hz  | 0.65 | -5.5 dB |
| Peaking | 1957 Hz | 2.29 | -7.8 dB |
| Peaking | 3276 Hz | 3.38 | 7.7 dB  |
| Peaking | 5947 Hz | 4.23 | 6.7 dB  |
| Peaking | 362 Hz  | 2.16 | -1.1 dB |
| Peaking | 785 Hz  | 1.59 | 1.8 dB  |
| Peaking | 1510 Hz | 4.08 | -1.2 dB |
| Peaking | 4469 Hz | 6.61 | -7.0 dB |
| Peaking | 4575 Hz | 2.55 | 3.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t096z%20Flat%20Filter/Torque%20t096z%20Flat%20Filter.png)