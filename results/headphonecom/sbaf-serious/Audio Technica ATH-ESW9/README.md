# Audio Technica ATH-ESW9

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 5.9; 59 5.7; 64 5.6; 68 5.9; 73 5.9; 78 5.5; 83 5.3; 89 5.0; 95 4.8; 102 4.7; 109 4.5; 117 4.7; 125 5.3; 134 5.2; 143 4.8; 153 4.6; 164 4.6; 175 4.5; 188 4.7; 201 4.7; 215 4.4; 230 4.2; 246 4.0; 263 3.7; 282 3.3; 301 3.2; 323 3.6; 345 4.0; 369 4.1; 395 4.4; 423 4.6; 452 4.6; 484 4.7; 518 4.6; 554 4.6; 593 4.4; 635 3.8; 679 2.9; 726 2.0; 777 1.4; 832 1.0; 890 0.6; 952 0.2; 1019 -0.1; 1090 -0.6; 1167 -1.0; 1248 -1.2; 1336 -1.5; 1429 -1.9; 1529 -2.3; 1636 -2.4; 1751 -2.1; 1873 -1.5; 2004 -0.9; 2145 -0.0; 2295 1.0; 2455 2.0; 2627 3.4; 2811 5.0; 3008 5.9; 3219 6.0; 3444 6.0; 3685 6.0; 3943 5.7; 4219 4.7; 4514 4.3; 4830 5.8; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.0; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.10214761800253dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-ESW9 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.25 | 6.1 dB  |
| Peaking | 204 Hz  | 0.93 | 2.4 dB  |
| Peaking | 499 Hz  | 1.99 | 4.3 dB  |
| Peaking | 3333 Hz | 2.87 | 6.2 dB  |
| Peaking | 5485 Hz | 2.53 | 6.1 dB  |
| Peaking | 636 Hz  | 6.1  | 1.3 dB  |
| Peaking | 1185 Hz | 2.8  | -0.9 dB |
| Peaking | 1659 Hz | 2.34 | -3.0 dB |
| Peaking | 2760 Hz | 5.52 | 2.0 dB  |
| Peaking | 8283 Hz | 4.59 | -1.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Audio%20Technica%20ATH-ESW9/Audio%20Technica%20ATH-ESW9.png)