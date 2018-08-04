# AKG K 601

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.0dB
GraphicEQ: 10 -84; 20 2.5; 22 2.0; 23 1.8; 25 1.4; 26 1.2; 28 0.9; 30 0.6; 32 0.4; 35 0.1; 37 -0.1; 40 -0.3; 42 -0.5; 45 -0.7; 49 -0.9; 52 -1.0; 56 -1.1; 59 -1.2; 64 -1.4; 68 -1.2; 73 0.2; 78 0.1; 83 -1.0; 89 -0.9; 95 -0.5; 102 -0.7; 109 -0.9; 117 -0.8; 125 -1.0; 134 -1.0; 143 -1.1; 153 -1.2; 164 -0.9; 175 -1.0; 188 -1.1; 201 -1.0; 215 -1.0; 230 -0.9; 246 -0.8; 263 -0.8; 282 -0.7; 301 -0.6; 323 -0.3; 345 -0.3; 369 -0.2; 395 -0.1; 423 0.0; 452 0.1; 484 -0.0; 518 -0.1; 554 0.1; 593 0.5; 635 0.8; 679 0.7; 726 0.7; 777 0.9; 832 0.8; 890 0.6; 952 0.2; 1019 -0.1; 1090 -0.3; 1167 -0.6; 1248 -1.0; 1336 -1.5; 1429 -2.0; 1529 -2.2; 1636 -2.1; 1751 -2.3; 1873 -2.2; 2004 -1.7; 2145 -1.6; 2295 -1.3; 2455 -1.4; 2627 -1.5; 2811 -1.5; 3008 -0.9; 3219 -0.7; 3444 -0.2; 3685 -1.2; 3943 -1.3; 4219 -1.8; 4514 -2.0; 4830 -1.2; 5168 0.2; 5530 -0.2; 5917 -2.9; 6331 -2.7; 6775 -0.1; 7249 0.1; 7756 -0.1; 8299 -0.3; 8880 -0.4; 9502 -0.4; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.0dB` and instead set Global volume in the UI for both channels to **-30**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K 601 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 1.56 | 2.7 dB  |
| Peaking | 88 Hz   | 0.41 | -1.0 dB |
| Peaking | 1619 Hz | 2.92 | -2.1 dB |
| Peaking | 4982 Hz | 1.24 | -1.3 dB |
| Peaking | 2348 Hz | 2.38 | -1.0 dB |
| Peaking | 216 Hz  | 2.09 | -0.4 dB |
| Peaking | 736 Hz  | 2.33 | 1.1 dB  |
| Peaking | 5356 Hz | 6.73 | 3.9 dB  |
| Peaking | 6057 Hz | 3.25 | -4.5 dB |
| Peaking | 6931 Hz | 4.22 | 3.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K%20601/AKG%20K%20601.png)