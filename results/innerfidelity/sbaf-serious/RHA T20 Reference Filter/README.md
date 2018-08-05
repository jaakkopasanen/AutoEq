# RHA T20 Reference Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.6dB
GraphicEQ: 10 -84; 20 -4.9; 22 -5.1; 23 -5.3; 25 -5.5; 26 -5.5; 28 -5.6; 30 -5.7; 32 -5.8; 35 -5.8; 37 -5.8; 40 -5.7; 42 -5.7; 45 -5.6; 49 -5.5; 52 -5.4; 56 -5.3; 59 -5.2; 64 -5.0; 68 -4.9; 73 -4.8; 78 -4.7; 83 -4.7; 89 -4.8; 95 -5.0; 102 -5.2; 109 -5.4; 117 -5.6; 125 -5.8; 134 -6.0; 143 -5.9; 153 -5.9; 164 -5.6; 175 -5.4; 188 -5.1; 201 -4.8; 215 -4.3; 230 -3.9; 246 -3.6; 263 -3.3; 282 -2.8; 301 -2.5; 323 -2.1; 345 -1.7; 369 -1.4; 395 -1.1; 423 -0.7; 452 -0.3; 484 -0.2; 518 0.0; 554 0.4; 593 0.8; 635 1.0; 679 1.0; 726 1.1; 777 1.1; 832 1.0; 890 0.7; 952 0.4; 1019 -0.1; 1090 -0.5; 1167 -1.0; 1248 -1.6; 1336 -2.6; 1429 -3.6; 1529 -4.3; 1636 -3.9; 1751 -2.0; 1873 -0.2; 2004 -2.2; 2145 -3.2; 2295 -3.7; 2455 -4.4; 2627 -4.8; 2811 -4.5; 3008 -3.4; 3219 -2.4; 3444 -1.7; 3685 -2.2; 3943 -3.8; 4219 -6.8; 4514 -9.4; 4830 -8.5; 5168 -4.2; 5530 0.1; 5917 3.2; 6331 4.9; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.6dB` and instead set Global volume in the UI for both channels to **-56**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RHA T20 Reference Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 33 Hz   | 0.39 | -5.6 dB  |
| Peaking | 158 Hz  | 1.04 | -4.7 dB  |
| Peaking | 2406 Hz | 1.32 | -3.8 dB  |
| Peaking | 4620 Hz | 4.58 | -10.2 dB |
| Peaking | 6231 Hz | 4.03 | 6.7 dB   |
| Peaking | 749 Hz  | 1.7  | 2.0 dB   |
| Peaking | 1568 Hz | 3.14 | -3.9 dB  |
| Peaking | 1863 Hz | 4.84 | 4.2 dB   |
| Peaking | 3178 Hz | 1.63 | -1.7 dB  |
| Peaking | 3437 Hz | 3.95 | 3.0 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/RHA%20T20%20Reference%20Filter/RHA%20T20%20Reference%20Filter.png)