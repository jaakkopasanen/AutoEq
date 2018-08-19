# Audio Technical ATH-ES55

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 6.0; 95 6.0; 102 6.0; 109 6.0; 117 6.0; 125 6.0; 134 5.5; 143 5.1; 153 4.9; 164 4.6; 175 4.3; 188 3.9; 201 3.6; 215 3.4; 230 3.3; 246 3.2; 263 3.3; 282 3.7; 301 3.8; 323 3.8; 345 3.6; 369 3.1; 395 3.1; 423 3.5; 452 3.5; 484 3.4; 518 3.4; 554 3.5; 593 3.4; 635 3.0; 679 2.4; 726 1.8; 777 1.4; 832 0.8; 890 0.4; 952 0.1; 1019 -0.1; 1090 -0.4; 1167 -0.5; 1248 -0.8; 1336 -1.2; 1429 -1.7; 1529 -2.1; 1636 -2.3; 1751 -2.2; 1873 -1.9; 2004 -1.2; 2145 -0.2; 2295 0.7; 2455 2.2; 2627 3.4; 2811 4.2; 3008 5.1; 3219 5.1; 3444 5.2; 3685 5.5; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 -0.1; 16326 -0.2; 17469 -0.2; 18692 -1.2; 20000 -3.3
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technical ATH-ES55 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 12 Hz   | 0.1  | 6.0 dB  |
| Peaking | 119 Hz  | 0.78 | 2.7 dB  |
| Peaking | 467 Hz  | 0.94 | 3.1 dB  |
| Peaking | 1660 Hz | 1.53 | -4.1 dB |
| Peaking | 4097 Hz | 0.98 | 7.0 dB  |
| Peaking | 924 Hz  | 6.07 | -0.5 dB |
| Peaking | 2900 Hz | 3.37 | 2.2 dB  |
| Peaking | 3456 Hz | 1.51 | -1.3 dB |
| Peaking | 6300 Hz | 2.56 | 5.3 dB  |
| Peaking | 7264 Hz | 1.46 | -3.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technical%20ATH-ES55/Audio%20Technical%20ATH-ES55.png)