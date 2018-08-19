# Creative Fatal1ty

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 1.7; 22 0.9; 23 0.6; 25 -0.0; 26 -0.3; 28 -0.8; 30 -1.2; 32 -1.6; 35 -2.1; 37 -2.4; 40 -2.8; 42 -3.0; 45 -3.2; 49 -3.5; 52 -3.6; 56 -3.8; 59 -3.9; 64 -4.1; 68 -4.1; 73 -4.3; 78 -4.4; 83 -4.5; 89 -4.6; 95 -4.5; 102 -4.4; 109 -4.3; 117 -4.3; 125 -4.4; 134 -4.3; 143 -4.3; 153 -4.1; 164 -3.9; 175 -3.6; 188 -3.4; 201 -3.1; 215 -2.8; 230 -2.3; 246 -1.9; 263 -1.6; 282 -1.0; 301 -0.4; 323 0.0; 345 0.6; 369 1.1; 395 1.4; 423 1.9; 452 2.2; 484 2.2; 518 1.9; 554 1.7; 593 1.3; 635 0.9; 679 0.2; 726 0.2; 777 0.4; 832 0.1; 890 -0.0; 952 -0.1; 1019 0.1; 1090 0.3; 1167 0.4; 1248 0.5; 1336 0.3; 1429 0.3; 1529 0.6; 1636 0.9; 1751 1.5; 1873 2.4; 2004 3.5; 2145 4.5; 2295 5.4; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999998325dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Creative Fatal1ty ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 1.12 | 3.6 dB  |
| Peaking | 58 Hz   | 0.32 | -2.4 dB |
| Peaking | 301 Hz  | 0.19 | -3.7 dB |
| Peaking | 447 Hz  | 0.93 | 5.8 dB  |
| Peaking | 3453 Hz | 0.74 | 7.4 dB  |
| Peaking | 1667 Hz | 3.91 | -1.0 dB |
| Peaking | 2358 Hz | 2.81 | 1.7 dB  |
| Peaking | 3438 Hz | 2.35 | -1.2 dB |
| Peaking | 6193 Hz | 2.23 | 5.4 dB  |
| Peaking | 7494 Hz | 1.46 | -4.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Creative%20Fatal1ty/Creative%20Fatal1ty.png)