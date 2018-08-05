# Torque t096z Warm Tilt Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.4dB
GraphicEQ: 10 -84; 20 -4.3; 22 -4.6; 23 -4.7; 25 -4.9; 26 -5.0; 28 -5.2; 30 -5.3; 32 -5.4; 35 -5.5; 37 -5.6; 40 -5.7; 42 -5.7; 45 -5.7; 49 -5.7; 52 -5.7; 56 -5.7; 59 -5.7; 64 -5.7; 68 -5.7; 73 -5.7; 78 -5.8; 83 -6.0; 89 -6.2; 95 -6.5; 102 -6.9; 109 -7.2; 117 -7.6; 125 -7.9; 134 -8.2; 143 -8.2; 153 -8.2; 164 -8.1; 175 -7.9; 188 -7.6; 201 -7.3; 215 -6.9; 230 -6.6; 246 -6.2; 263 -5.8; 282 -5.3; 301 -4.9; 323 -4.5; 345 -4.0; 369 -3.5; 395 -3.1; 423 -2.5; 452 -2.1; 484 -1.8; 518 -1.5; 554 -0.9; 593 -0.3; 635 -0.0; 679 0.2; 726 0.4; 777 0.7; 832 0.6; 890 0.4; 952 0.2; 1019 -0.1; 1090 -0.4; 1167 -0.8; 1248 -1.2; 1336 -1.9; 1429 -2.6; 1529 -3.4; 1636 -4.1; 1751 -4.9; 1873 -5.6; 2004 -6.2; 2145 -6.9; 2295 -7.3; 2455 -6.4; 2627 -5.0; 2811 -2.8; 3008 -0.3; 3219 1.1; 3444 2.1; 3685 1.7; 3943 -0.0; 4219 -3.4; 4514 -6.0; 4830 -5.1; 5168 -1.5; 5530 2.5; 5917 5.6; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.3; 10167 -0.4; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.4dB` and instead set Global volume in the UI for both channels to **-64**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t096z Warm Tilt Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.28 | -5.0 dB |
| Peaking | 176 Hz  | 0.81 | -6.3 dB |
| Peaking | 2123 Hz | 2.53 | -7.7 dB |
| Peaking | 4684 Hz | 6.92 | -7.5 dB |
| Peaking | 6124 Hz | 4.08 | 6.9 dB  |
| Peaking | 349 Hz  | 2.27 | -0.9 dB |
| Peaking | 779 Hz  | 1.59 | 1.7 dB  |
| Peaking | 1515 Hz | 5.09 | -1.4 dB |
| Peaking | 3394 Hz | 1.45 | -3.1 dB |
| Peaking | 3402 Hz | 3.48 | 6.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t096z%20Warm%20Tilt%20Filter/Torque%20t096z%20Warm%20Tilt%20Filter.png)