# MrSpeakers Mad Dog 2014

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 3.7; 22 3.3; 23 3.1; 25 2.7; 26 2.6; 28 2.4; 30 2.2; 32 2.0; 35 1.7; 37 1.6; 40 1.4; 42 1.4; 45 1.3; 49 1.1; 52 1.0; 56 0.7; 59 0.6; 64 0.5; 68 0.4; 73 0.4; 78 0.3; 83 0.1; 89 -0.2; 95 -0.6; 102 -1.0; 109 -1.5; 117 -2.0; 125 -2.7; 134 -2.9; 143 -3.3; 153 -3.3; 164 -2.7; 175 -3.0; 188 -3.5; 201 -3.6; 215 -3.6; 230 -3.4; 246 -3.3; 263 -3.2; 282 -3.0; 301 -2.9; 323 -2.9; 345 -2.6; 369 -2.4; 395 -1.6; 423 -0.3; 452 -0.9; 484 -0.6; 518 1.4; 554 1.5; 593 1.4; 635 0.1; 679 -0.0; 726 0.1; 777 1.1; 832 0.9; 890 0.0; 952 0.3; 1019 0.2; 1090 0.7; 1167 0.1; 1248 0.6; 1336 0.5; 1429 -0.1; 1529 0.6; 1636 1.3; 1751 1.7; 1873 2.2; 2004 2.9; 2145 3.9; 2295 5.1; 2455 5.9; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 5.5; 4830 5.1; 5168 5.2; 5530 3.9; 5917 2.2; 6331 1.1; 6775 1.1; 7249 1.2; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999996125dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MrSpeakers Mad Dog 2014 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 13 Hz   | 0.31 | 3.8 dB  |
| Peaking | 81 Hz   | 1.38 | 2.1 dB  |
| Peaking | 189 Hz  | 0.34 | -4.0 dB |
| Peaking | 550 Hz  | 1.98 | 3.2 dB  |
| Peaking | 3326 Hz | 1    | 6.9 dB  |
| Peaking | 1460 Hz | 7.28 | -1.3 dB |
| Peaking | 2414 Hz | 5.65 | 1.6 dB  |
| Peaking | 3284 Hz | 4.49 | -0.8 dB |
| Peaking | 5057 Hz | 3.2  | 2.5 dB  |
| Peaking | 6804 Hz | 0.94 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/MrSpeakers%20Mad%20Dog%202014/MrSpeakers%20Mad%20Dog%202014.png)