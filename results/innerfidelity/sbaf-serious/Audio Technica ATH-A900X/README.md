# Audio Technica ATH-A900X

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.4dB
GraphicEQ: 10 -84; 20 6.3; 22 5.6; 23 5.2; 25 4.6; 26 4.3; 28 3.7; 30 3.1; 32 2.7; 35 2.0; 37 1.7; 40 1.2; 42 0.9; 45 0.6; 49 0.2; 52 -0.0; 56 -0.3; 59 -0.6; 64 -1.2; 68 -1.4; 73 -1.5; 78 -1.6; 83 -2.0; 89 -2.8; 95 -3.0; 102 -3.0; 109 -3.3; 117 -3.7; 125 -4.2; 134 -4.5; 143 -4.6; 153 -4.4; 164 -3.7; 175 -4.2; 188 -4.3; 201 -4.1; 215 -3.8; 230 -3.2; 246 -2.8; 263 -2.2; 282 -1.5; 301 -1.1; 323 -0.7; 345 -0.8; 369 -0.9; 395 -1.0; 423 -1.0; 452 -1.0; 484 -1.2; 518 -1.3; 554 -1.2; 593 -1.0; 635 -0.7; 679 -0.0; 726 0.2; 777 0.3; 832 -0.1; 890 -0.1; 952 -0.1; 1019 0.1; 1090 0.2; 1167 0.3; 1248 0.7; 1336 1.3; 1429 1.4; 1529 1.2; 1636 1.2; 1751 -0.1; 1873 -0.8; 2004 -1.3; 2145 -1.0; 2295 0.1; 2455 1.8; 2627 3.2; 2811 3.9; 3008 4.8; 3219 4.8; 3444 5.1; 3685 5.9; 3943 6.0; 4219 3.9; 4514 3.6; 4830 5.9; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.1; 17469 -0.3; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.405572078140262dB` and instead set Global volume in the UI for both channels to **-64**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-A900X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.03 | 6.3 dB  |
| Peaking | 140 Hz  | 0.8  | -4.2 dB |
| Peaking | 206 Hz  | 3.07 | -1.2 dB |
| Peaking | 3482 Hz | 2.22 | 5.3 dB  |
| Peaking | 5640 Hz | 2.77 | 5.9 dB  |
| Peaking | 533 Hz  | 5.14 | -1.0 dB |
| Peaking | 1530 Hz | 2.54 | 2.0 dB  |
| Peaking | 2029 Hz | 2.67 | -3.0 dB |
| Peaking | 2664 Hz | 4.59 | 1.9 dB  |
| Peaking | 8283 Hz | 4.54 | -1.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-A900X/Audio%20Technica%20ATH-A900X.png)