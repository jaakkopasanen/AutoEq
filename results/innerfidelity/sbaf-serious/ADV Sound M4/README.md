# ADV Sound M4

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -5.6; 22 -5.9; 23 -6.1; 25 -6.3; 26 -6.4; 28 -6.6; 30 -6.7; 32 -6.8; 35 -7.0; 37 -7.1; 40 -7.2; 42 -7.3; 45 -7.5; 49 -7.7; 52 -7.8; 56 -8.0; 59 -8.1; 64 -8.3; 68 -8.5; 73 -8.7; 78 -8.8; 83 -9.1; 89 -9.3; 95 -9.5; 102 -9.6; 109 -9.6; 117 -9.6; 125 -9.7; 134 -9.7; 143 -9.7; 153 -9.6; 164 -9.5; 175 -9.3; 188 -9.2; 201 -9.0; 215 -8.7; 230 -8.4; 246 -8.1; 263 -7.8; 282 -7.3; 301 -7.0; 323 -6.6; 345 -6.1; 369 -5.6; 395 -5.2; 423 -4.6; 452 -4.1; 484 -3.8; 518 -3.3; 554 -2.7; 593 -2.0; 635 -1.7; 679 -1.4; 726 -1.0; 777 -0.5; 832 -0.3; 890 -0.3; 952 -0.2; 1019 0.0; 1090 0.6; 1167 0.3; 1248 0.2; 1336 -0.0; 1429 -0.2; 1529 -0.4; 1636 -0.4; 1751 -0.2; 1873 0.2; 2004 0.5; 2145 0.9; 2295 1.0; 2455 0.6; 2627 0.3; 2811 1.3; 3008 3.3; 3219 4.7; 3444 5.9; 3685 6.0; 3943 5.8; 4219 4.4; 4514 3.4; 4830 3.2; 5168 3.4; 5530 3.0; 5917 1.6; 6331 -1.3; 6775 -4.7; 7249 -6.1; 7756 -5.0; 8299 -2.7; 8880 -0.3; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.0999999382105505dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `ADV Sound M4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 41 Hz   | 0.28 | -6.4 dB |
| Peaking | 147 Hz  | 0.67 | -5.4 dB |
| Peaking | 309 Hz  | 1.06 | -3.2 dB |
| Peaking | 3898 Hz | 1.71 | 6.1 dB  |
| Peaking | 7283 Hz | 4.62 | -7.7 dB |
| Peaking | 1013 Hz | 2.66 | 0.9 dB  |
| Peaking | 2693 Hz | 6.16 | -1.7 dB |
| Peaking | 3426 Hz | 2.61 | 3.2 dB  |
| Peaking | 4005 Hz | 1.26 | -2.6 dB |
| Peaking | 5450 Hz | 4.67 | 2.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/ADV%20Sound%20M4/ADV%20Sound%20M4.png)