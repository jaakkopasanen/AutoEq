# Skullcandy Grind

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.0dB
GraphicEQ: 10 -84; 20 1.2; 22 0.6; 23 0.3; 25 -0.2; 26 -0.4; 28 -0.7; 30 -1.0; 32 -1.2; 35 -1.5; 37 -1.6; 40 -1.7; 42 -1.7; 45 -1.8; 49 -1.8; 52 -1.8; 56 -1.7; 59 -1.7; 64 -1.6; 68 -1.6; 73 -1.6; 78 -1.5; 83 -1.5; 89 -1.4; 95 -1.3; 102 -1.3; 109 -1.2; 117 -1.0; 125 -0.9; 134 -1.1; 143 -1.3; 153 -1.5; 164 -1.3; 175 -1.1; 188 -1.2; 201 -1.2; 215 -1.1; 230 -0.9; 246 -0.6; 263 -0.4; 282 0.0; 301 0.1; 323 0.1; 345 0.2; 369 0.5; 395 0.8; 423 1.5; 452 1.9; 484 2.1; 518 2.4; 554 3.0; 593 3.7; 635 4.2; 679 4.6; 726 4.9; 777 4.7; 832 3.0; 890 0.7; 952 -0.3; 1019 0.4; 1090 1.5; 1167 1.9; 1248 1.8; 1336 0.6; 1429 -0.5; 1529 -1.4; 1636 -2.2; 1751 -3.1; 1873 -4.3; 2004 -4.8; 2145 -4.3; 2295 -4.0; 2455 -3.3; 2627 -1.8; 2811 -0.7; 3008 0.8; 3219 1.8; 3444 3.6; 3685 2.3; 3943 -1.7; 4219 -2.4; 4514 -2.5; 4830 -1.1; 5168 1.5; 5530 2.7; 5917 3.9; 6331 3.0; 6775 2.0; 7249 0.2; 7756 -1.5; 8299 -3.4; 8880 -4.3; 9502 -2.9; 10167 -0.1; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.027486260445207dB` and instead set Global volume in the UI for both channels to **-50**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Grind ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 683 Hz  | 2.09 | 5.1 dB  |
| Peaking | 2065 Hz | 2.45 | -5.2 dB |
| Peaking | 3388 Hz | 8.54 | 4.6 dB  |
| Peaking | 6060 Hz | 5.22 | 4.6 dB  |
| Peaking | 8753 Hz | 4.88 | -4.9 dB |
| Peaking | 16 Hz   | 1.28 | 2.4 dB  |
| Peaking | 43 Hz   | 0.52 | -2.1 dB |
| Peaking | 184 Hz  | 1.86 | -1.1 dB |
| Peaking | 4324 Hz | 1.6  | 2.2 dB  |
| Peaking | 4377 Hz | 4.14 | -5.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Skullcandy%20Grind/Skullcandy%20Grind.png)