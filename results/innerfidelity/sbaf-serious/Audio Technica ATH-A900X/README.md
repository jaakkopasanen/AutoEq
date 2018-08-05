# Audio Technica ATH-A900X

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.9dB
GraphicEQ: 10 -84; 20 6.3; 22 5.6; 23 5.2; 25 4.6; 26 4.3; 28 3.7; 30 3.2; 32 2.7; 35 2.1; 37 1.8; 40 1.3; 42 1.1; 45 0.7; 49 0.4; 52 0.3; 56 0.1; 59 -0.2; 64 -0.7; 68 -0.8; 73 -0.8; 78 -0.8; 83 -1.2; 89 -2.1; 95 -2.3; 102 -2.4; 109 -2.9; 117 -3.5; 125 -4.2; 134 -4.6; 143 -4.8; 153 -4.7; 164 -3.9; 175 -4.4; 188 -4.5; 201 -4.2; 215 -3.9; 230 -3.3; 246 -2.9; 263 -2.3; 282 -1.5; 301 -1.1; 323 -0.8; 345 -0.8; 369 -1.0; 395 -1.0; 423 -1.0; 452 -1.1; 484 -1.2; 518 -1.3; 554 -1.2; 593 -1.0; 635 -0.7; 679 -0.0; 726 0.2; 777 0.3; 832 -0.1; 890 -0.1; 952 -0.1; 1019 0.1; 1090 0.2; 1167 0.3; 1248 0.7; 1336 1.3; 1429 1.4; 1529 1.2; 1636 1.2; 1751 -0.1; 1873 -0.8; 2004 -1.3; 2145 -1.0; 2295 0.1; 2455 1.8; 2627 3.2; 2811 3.9; 3008 4.8; 3219 4.8; 3444 5.1; 3685 5.9; 3943 6.0; 4219 3.9; 4514 3.6; 4830 5.9; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.1; 17469 -0.3; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.9dB` and instead set Global volume in the UI for both channels to **-69**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-A900X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.15 | 6.1 dB  |
| Peaking | 159 Hz  | 1.18 | -6.2 dB |
| Peaking | 163 Hz  | 4.03 | 2.0 dB  |
| Peaking | 3483 Hz | 2.22 | 5.3 dB  |
| Peaking | 5641 Hz | 2.77 | 5.9 dB  |
| Peaking | 532 Hz  | 4.84 | -1.0 dB |
| Peaking | 1523 Hz | 2.6  | 2.0 dB  |
| Peaking | 2023 Hz | 2.66 | -3.0 dB |
| Peaking | 2655 Hz | 4.57 | 1.9 dB  |
| Peaking | 8281 Hz | 4.54 | -1.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-A900X/Audio%20Technica%20ATH-A900X.png)