# Audio Technica ATH-A700

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 5.9; 49 5.2; 52 4.6; 56 3.9; 59 3.6; 64 4.1; 68 4.4; 73 3.2; 78 2.0; 83 1.6; 89 1.6; 95 1.7; 102 1.5; 109 1.4; 117 1.2; 125 1.2; 134 1.3; 143 1.3; 153 1.4; 164 1.8; 175 2.0; 188 2.2; 201 2.6; 215 3.1; 230 3.4; 246 3.2; 263 3.6; 282 4.2; 301 4.7; 323 5.0; 345 4.3; 369 2.5; 395 0.8; 423 -0.3; 452 -0.7; 484 -0.9; 518 -0.7; 554 -0.4; 593 0.1; 635 0.4; 679 -0.0; 726 -0.4; 777 1.2; 832 0.9; 890 0.3; 952 0.0; 1019 -0.0; 1090 0.3; 1167 0.5; 1248 0.6; 1336 0.3; 1429 -0.4; 1529 0.0; 1636 0.9; 1751 0.9; 1873 -0.5; 2004 -0.7; 2145 0.8; 2295 2.6; 2455 4.3; 2627 5.9; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 5.9; 4219 1.9; 4514 1.0; 4830 3.6; 5168 5.9; 5530 6.0; 5917 5.0; 6331 4.0; 6775 3.9; 7249 1.1; 7756 -3.1; 8299 -5.7; 8880 -5.9; 9502 -4.0; 10167 -0.6; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 -2.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-A700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 0.57 | 6.4 dB  |
| Peaking | 288 Hz  | 2.3  | 4.7 dB  |
| Peaking | 3098 Hz | 2.28 | 6.5 dB  |
| Peaking | 5962 Hz | 2.13 | 5.9 dB  |
| Peaking | 8524 Hz | 3.74 | -8.3 dB |
| Peaking | 346 Hz  | 5.87 | 2.7 dB  |
| Peaking | 390 Hz  | 0.61 | 1.1 dB  |
| Peaking | 423 Hz  | 1.47 | -3.1 dB |
| Peaking | 1990 Hz | 6.45 | -2.4 dB |
| Peaking | 2552 Hz | 8.34 | 1.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audio%20Technica%20ATH-A700/Audio%20Technica%20ATH-A700.png)