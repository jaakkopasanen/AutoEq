# AKG K601

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.5; 22 6.0; 23 5.7; 25 5.3; 26 5.2; 28 4.9; 30 4.6; 32 4.3; 35 4.0; 37 3.8; 40 3.5; 42 3.4; 45 3.2; 49 2.9; 52 2.7; 56 2.5; 59 2.3; 64 1.9; 68 2.1; 73 3.2; 78 2.9; 83 1.7; 89 1.5; 95 1.7; 102 1.2; 109 0.7; 117 0.5; 125 0.1; 134 -0.0; 143 -0.3; 153 -0.5; 164 -0.4; 175 -0.6; 188 -0.7; 201 -0.8; 215 -0.8; 230 -0.7; 246 -0.7; 263 -0.7; 282 -0.7; 301 -0.6; 323 -0.3; 345 -0.3; 369 -0.2; 395 -0.1; 423 -0.0; 452 0.0; 484 0.1; 518 -0.0; 554 0.1; 593 0.4; 635 0.7; 679 0.8; 726 0.7; 777 0.8; 832 0.8; 890 0.6; 952 0.2; 1019 -0.1; 1090 -0.3; 1167 -0.6; 1248 -1.0; 1336 -1.5; 1429 -1.9; 1529 -2.2; 1636 -2.1; 1751 -2.2; 1873 -2.2; 2004 -1.7; 2145 -1.6; 2295 -1.3; 2455 -1.4; 2627 -1.4; 2811 -1.4; 3008 -1.0; 3219 -0.6; 3444 -0.1; 3685 -1.2; 3943 -1.6; 4219 -1.8; 4514 -1.9; 4830 -1.2; 5168 0.2; 5530 -0.2; 5917 -2.8; 6331 -2.7; 6775 -0.2; 7249 0.0; 7756 -0.1; 8299 -0.1; 8880 -0.3; 9502 -0.6; 10167 -0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.603145735052058dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K601 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.69 | 5.9 dB  |
| Peaking | 76 Hz   | 4.31 | 2.1 dB  |
| Peaking | 1590 Hz | 2.93 | -2.0 dB |
| Peaking | 2232 Hz | 2.2  | -1.0 dB |
| Peaking | 4928 Hz | 1.2  | -1.3 dB |
| Peaking | 212 Hz  | 1.38 | -1.0 dB |
| Peaking | 745 Hz  | 2.54 | 1.1 dB  |
| Peaking | 5328 Hz | 7.71 | 3.1 dB  |
| Peaking | 6080 Hz | 4.12 | -3.8 dB |
| Peaking | 6961 Hz | 4.4  | 2.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K601/AKG%20K601.png)