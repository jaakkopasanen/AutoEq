# Audio Technica ATH-A2000Z

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.9dB
GraphicEQ: 10 -84; 20 6.4; 22 5.5; 23 5.2; 25 4.5; 26 4.2; 28 3.7; 30 3.2; 32 2.7; 35 2.1; 37 1.8; 40 1.4; 42 1.1; 45 0.8; 49 0.5; 52 0.4; 56 0.2; 59 0.1; 64 0.0; 68 -0.0; 73 -0.0; 78 -0.1; 83 -0.1; 89 -0.5; 95 -1.1; 102 -1.8; 109 -2.2; 117 -2.4; 125 -2.6; 134 -2.7; 143 -2.8; 153 -2.7; 164 -1.9; 175 -2.0; 188 -2.0; 201 -1.7; 215 -1.3; 230 -0.9; 246 -0.5; 263 -0.2; 282 0.0; 301 0.1; 323 0.2; 345 0.1; 369 0.1; 395 -0.1; 423 -0.1; 452 -0.1; 484 -0.2; 518 -0.2; 554 -0.2; 593 0.1; 635 0.1; 679 -0.0; 726 -0.1; 777 0.1; 832 0.4; 890 0.1; 952 -0.1; 1019 0.2; 1090 0.4; 1167 0.1; 1248 0.0; 1336 -0.4; 1429 -1.2; 1529 -2.4; 1636 -3.6; 1751 -4.3; 1873 -4.8; 2004 -5.1; 2145 -5.2; 2295 -4.6; 2455 -2.7; 2627 -0.8; 2811 0.6; 3008 1.6; 3219 1.6; 3444 0.0; 3685 -2.3; 3943 -3.4; 4219 -3.8; 4514 -2.0; 4830 1.3; 5168 5.7; 5530 6.0; 5917 4.6; 6331 4.9; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -2.6; 9502 -5.2; 10167 -4.2; 10879 -0.8; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 -0.4; 16326 -3.7; 17469 -3.6; 18692 -1.1; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.9dB` and instead set Global volume in the UI for both channels to **-69**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audio Technica ATH-A2000Z ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 1.94 | 5.9 dB   |
| Peaking | 2014 Hz  | 2.47 | -6.7 dB  |
| Peaking | 4248 Hz  | 3.28 | -12.1 dB |
| Peaking | 4973 Hz  | 1.19 | 9.7 dB   |
| Peaking | 9520 Hz  | 3.25 | -6.9 dB  |
| Peaking | 32 Hz    | 0.05 | 0.6 dB   |
| Peaking | 141 Hz   | 1.1  | -3.4 dB  |
| Peaking | 291 Hz   | 4.11 | 0.5 dB   |
| Peaking | 16270 Hz | 5    | -1.8 dB  |
| Peaking | 17319 Hz | 3.37 | -3.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audio%20Technica%20ATH-A2000Z/Audio%20Technica%20ATH-A2000Z.png)