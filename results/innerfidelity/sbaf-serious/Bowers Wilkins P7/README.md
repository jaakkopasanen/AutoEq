# Bowers Wilkins P7

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.8dB
GraphicEQ: 10 -84; 20 0.9; 22 0.5; 23 0.4; 25 0.0; 26 -0.1; 28 -0.3; 30 -0.6; 32 -0.8; 35 -1.0; 37 -1.1; 40 -1.1; 42 -1.2; 45 -1.3; 49 -1.4; 52 -1.3; 56 -1.0; 59 -1.0; 64 -1.5; 68 -1.6; 73 -1.8; 78 -1.7; 83 -1.6; 89 -1.7; 95 -1.5; 102 -0.8; 109 -0.5; 117 -0.4; 125 -1.0; 134 -1.6; 143 -2.3; 153 -2.4; 164 -1.2; 175 -1.4; 188 -1.6; 201 -1.1; 215 -0.8; 230 -0.2; 246 0.3; 263 0.8; 282 1.3; 301 1.6; 323 1.8; 345 1.9; 369 2.1; 395 2.0; 423 2.1; 452 2.2; 484 2.1; 518 2.0; 554 2.1; 593 2.2; 635 2.0; 679 1.6; 726 1.2; 777 0.7; 832 0.1; 890 0.0; 952 0.2; 1019 -0.1; 1090 -0.4; 1167 -0.9; 1248 -1.4; 1336 -2.2; 1429 -3.0; 1529 -3.7; 1636 -4.2; 1751 -4.3; 1873 -4.3; 2004 -4.0; 2145 -3.5; 2295 -2.9; 2455 -1.3; 2627 1.1; 2811 3.0; 3008 4.1; 3219 4.0; 3444 2.8; 3685 1.0; 3943 0.1; 4219 0.0; 4514 0.4; 4830 1.4; 5168 2.5; 5530 2.2; 5917 2.0; 6331 5.1; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.8dB` and instead set Global volume in the UI for both channels to **-58**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bowers Wilkins P7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 184 Hz  | 0.37 | -2.7 dB |
| Peaking | 416 Hz  | 0.67 | 4.3 dB  |
| Peaking | 1882 Hz | 1.32 | -5.4 dB |
| Peaking | 3016 Hz | 3.19 | 6.3 dB  |
| Peaking | 6392 Hz | 4.71 | 5.0 dB  |
| Peaking | 70 Hz   | 0.75 | -0.4 dB |
| Peaking | 113 Hz  | 3.67 | 1.7 dB  |
| Peaking | 145 Hz  | 5.58 | -1.2 dB |
| Peaking | 5158 Hz | 2.11 | -1.4 dB |
| Peaking | 5145 Hz | 6.02 | 3.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bowers%20Wilkins%20P7/Bowers%20Wilkins%20P7.png)