# Audio Technica ATH-AD900

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 5.8; 95 5.1; 102 4.4; 109 4.1; 117 3.4; 125 2.6; 134 2.0; 143 1.5; 153 1.1; 164 0.9; 175 1.0; 188 1.2; 201 1.3; 215 1.3; 230 1.2; 246 1.1; 263 1.0; 282 1.0; 301 0.9; 323 0.9; 345 0.9; 369 0.9; 395 0.9; 423 1.0; 452 0.9; 484 0.8; 518 0.8; 554 0.8; 593 0.9; 635 0.9; 679 0.7; 726 0.7; 777 0.9; 832 0.6; 890 0.3; 952 0.2; 1019 -0.0; 1090 -0.2; 1167 -0.5; 1248 -0.9; 1336 -1.5; 1429 -2.3; 1529 -2.8; 1636 -2.9; 1751 -2.3; 1873 -0.9; 2004 0.1; 2145 1.0; 2295 1.4; 2455 2.2; 2627 2.2; 2811 1.4; 3008 1.2; 3219 1.8; 3444 1.4; 3685 -1.7; 3943 -3.6; 4219 -4.9; 4514 -5.2; 4830 -3.5; 5168 -1.2; 5530 0.2; 5917 0.9; 6331 1.9; 6775 3.3; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-AD900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 42 Hz   | 0.42 | 6.7 dB  |
| Peaking | 1613 Hz | 1.53 | -7.8 dB |
| Peaking | 2046 Hz | 0.65 | 5.5 dB  |
| Peaking | 4326 Hz | 3.24 | -7.6 dB |
| Peaking | 6642 Hz | 6.26 | 3.1 dB  |
| Peaking | 16 Hz   | 1.03 | 2.1 dB  |
| Peaking | 39 Hz   | 1.1  | -1.2 dB |
| Peaking | 86 Hz   | 2.29 | 1.5 dB  |
| Peaking | 153 Hz  | 3.02 | -1.4 dB |
| Peaking | 8674 Hz | 3.38 | -0.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-AD900/Audio%20Technica%20ATH-AD900.png)