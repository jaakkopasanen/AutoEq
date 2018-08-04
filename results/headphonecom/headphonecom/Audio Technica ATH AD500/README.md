# Audio Technica ATH AD500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 5.8; 59 5.8; 64 4.7; 68 3.5; 73 2.6; 78 1.7; 83 1.1; 89 0.8; 95 0.6; 102 0.0; 109 -0.2; 117 -0.3; 125 -0.5; 134 -0.5; 143 -0.5; 153 -0.4; 164 -0.4; 175 -0.4; 188 -0.4; 201 -0.3; 215 -0.2; 230 -0.2; 246 -0.4; 263 -0.4; 282 -0.3; 301 -0.2; 323 -0.2; 345 -0.0; 369 0.2; 395 0.4; 423 0.6; 452 0.6; 484 0.7; 518 0.9; 554 1.0; 593 1.2; 635 1.3; 679 1.4; 726 1.5; 777 1.2; 832 0.9; 890 0.6; 952 0.3; 1019 -0.1; 1090 -0.3; 1167 -0.3; 1248 -0.1; 1336 0.4; 1429 1.2; 1529 2.1; 1636 3.5; 1751 4.5; 1873 5.1; 2004 5.2; 2145 4.9; 2295 4.8; 2455 4.4; 2627 4.2; 2811 4.6; 3008 5.2; 3219 5.0; 3444 5.0; 3685 3.6; 3943 -0.7; 4219 -1.0; 4514 1.0; 4830 2.6; 5168 3.3; 5530 5.3; 5917 5.9; 6331 5.5; 6775 2.5; 7249 -1.3; 7756 -3.5; 8299 -5.4; 8880 -6.2; 9502 -5.0; 10167 -2.3; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH AD500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 34 Hz   |  0.86 | 7.1 dB  |
| Peaking | 2018 Hz |  2.31 | 5.2 dB  |
| Peaking | 3119 Hz |  3.76 | 4.6 dB  |
| Peaking | 6025 Hz |  3.8  | 7.4 dB  |
| Peaking | 8632 Hz |  3.05 | -7.3 dB |
| Peaking | 59 Hz   |  2.86 | 3.3 dB  |
| Peaking | 107 Hz  |  0.45 | -1.4 dB |
| Peaking | 970 Hz  |  0.76 | 3.2 dB  |
| Peaking | 1122 Hz |  1.49 | -4.1 dB |
| Peaking | 4105 Hz | 11.66 | -3.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Audio%20Technica%20ATH%20AD500/Audio%20Technica%20ATH%20AD500.png)