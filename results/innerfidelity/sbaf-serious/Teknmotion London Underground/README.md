# Teknmotion London Underground

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 5.8; 40 5.3; 42 4.9; 45 4.4; 49 3.9; 52 3.5; 56 3.1; 59 2.8; 64 2.5; 68 2.3; 73 2.1; 78 2.0; 83 1.9; 89 1.9; 95 1.7; 102 1.3; 109 1.2; 117 1.1; 125 1.0; 134 1.0; 143 1.0; 153 1.1; 164 1.4; 175 1.7; 188 2.0; 201 2.3; 215 2.7; 230 3.0; 246 3.4; 263 3.6; 282 4.0; 301 4.5; 323 5.0; 345 5.5; 369 5.9; 395 6.0; 423 6.0; 452 6.0; 484 6.0; 518 5.9; 554 5.4; 593 4.8; 635 3.6; 679 2.5; 726 1.5; 777 1.1; 832 0.6; 890 0.4; 952 0.3; 1019 0.0; 1090 0.1; 1167 0.8; 1248 0.7; 1336 -0.3; 1429 -0.5; 1529 -0.1; 1636 0.7; 1751 1.7; 1873 3.1; 2004 4.7; 2145 5.6; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Teknmotion London Underground ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.63 | 6.3 dB  |
| Peaking | 518 Hz  | 2.87 | 4.0 dB  |
| Peaking | 345 Hz  | 1.38 | 5.0 dB  |
| Peaking | 2621 Hz | 1.85 | 5.6 dB  |
| Peaking | 4939 Hz | 1.57 | 6.0 dB  |
| Peaking | 1547 Hz | 3.88 | -1.3 dB |
| Peaking | 1262 Hz | 1.19 | -0.7 dB |
| Peaking | 2092 Hz | 5.04 | 2.0 dB  |
| Peaking | 6407 Hz | 4.6  | 3.5 dB  |
| Peaking | 7552 Hz | 1.8  | -2.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Teknmotion%20London%20Underground/Teknmotion%20London%20Underground.png)