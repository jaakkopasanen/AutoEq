# Torque t096z Flat Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 2.9; 22 2.5; 23 2.3; 25 1.9; 26 1.8; 28 1.5; 30 1.3; 32 1.1; 35 0.9; 37 0.8; 40 0.7; 42 0.6; 45 0.4; 49 0.3; 52 0.2; 56 0.1; 59 0.0; 64 -0.2; 68 -0.3; 73 -0.5; 78 -0.7; 83 -1.0; 89 -1.5; 95 -1.9; 102 -2.5; 109 -3.0; 117 -3.6; 125 -4.3; 134 -4.8; 143 -5.1; 153 -5.4; 164 -5.5; 175 -5.6; 188 -5.6; 201 -5.6; 215 -5.5; 230 -5.3; 246 -5.2; 263 -5.2; 282 -4.9; 301 -4.6; 323 -4.4; 345 -4.0; 369 -3.7; 395 -3.3; 423 -2.8; 452 -2.3; 484 -2.0; 518 -1.5; 554 -1.0; 593 -0.4; 635 -0.0; 679 0.1; 726 0.4; 777 0.7; 832 0.7; 890 0.5; 952 0.3; 1019 -0.1; 1090 -0.5; 1167 -1.0; 1248 -1.5; 1336 -2.2; 1429 -3.2; 1529 -4.1; 1636 -5.1; 1751 -6.0; 1873 -6.5; 2004 -6.5; 2145 -6.2; 2295 -4.6; 2455 -2.1; 2627 0.1; 2811 2.3; 3008 4.5; 3219 5.8; 3444 6.0; 3685 5.6; 3943 3.7; 4219 0.2; 4514 -1.6; 4830 0.3; 5168 4.6; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t096z Flat Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 10 Hz   | 0.24 | 2.6 dB  |
| Peaking | 195 Hz  | 0.78 | -6.2 dB |
| Peaking | 1957 Hz | 2.26 | -7.8 dB |
| Peaking | 3274 Hz | 3.37 | 7.7 dB  |
| Peaking | 5947 Hz | 4.23 | 6.7 dB  |
| Peaking | 379 Hz  | 2.4  | -1.1 dB |
| Peaking | 790 Hz  | 1.62 | 1.8 dB  |
| Peaking | 1499 Hz | 4.14 | -1.2 dB |
| Peaking | 4504 Hz | 6.61 | -7.0 dB |
| Peaking | 4525 Hz | 2.56 | 3.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t096z%20Flat%20Filter/Torque%20t096z%20Flat%20Filter.png)