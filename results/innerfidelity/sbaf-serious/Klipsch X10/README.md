# Klipsch X10

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -0.9; 22 -0.9; 23 -0.9; 25 -0.9; 26 -0.9; 28 -0.9; 30 -0.9; 32 -0.9; 35 -0.9; 37 -0.9; 40 -0.9; 42 -0.9; 45 -0.9; 49 -0.9; 52 -1.0; 56 -1.0; 59 -1.0; 64 -1.1; 68 -1.2; 73 -1.3; 78 -1.5; 83 -1.6; 89 -1.9; 95 -2.4; 102 -2.9; 109 -3.2; 117 -3.8; 125 -4.3; 134 -4.7; 143 -4.9; 153 -5.2; 164 -5.2; 175 -5.1; 188 -5.1; 201 -5.0; 215 -4.8; 230 -4.6; 246 -4.5; 263 -4.3; 282 -4.0; 301 -3.8; 323 -3.6; 345 -3.3; 369 -3.1; 395 -2.8; 423 -2.5; 452 -2.1; 484 -2.0; 518 -1.7; 554 -1.3; 593 -0.8; 635 -0.6; 679 -0.5; 726 -0.3; 777 0.1; 832 0.1; 890 0.1; 952 0.0; 1019 -0.1; 1090 -0.2; 1167 -0.2; 1248 -0.3; 1336 -0.5; 1429 -0.7; 1529 -0.8; 1636 -1.0; 1751 -0.8; 1873 -0.6; 2004 -0.3; 2145 -0.2; 2295 0.0; 2455 0.3; 2627 0.0; 2811 -0.3; 3008 0.2; 3219 1.9; 3444 4.5; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 -0.8; 8299 -3.8; 8880 -4.0; 9502 -0.9; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch X10 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 1.47 | -0.8 dB |
| Peaking | 190 Hz   | 0.68 | -5.3 dB |
| Peaking | 2695 Hz  | 1.08 | -4.7 dB |
| Peaking | 4452 Hz  | 0.82 | 8.9 dB  |
| Peaking | 8551 Hz  | 3.74 | -7.5 dB |
| Peaking | 1490 Hz  | 2.02 | -2.0 dB |
| Peaking | 1429 Hz  | 0.98 | 1.3 dB  |
| Peaking | 4793 Hz  | 6    | -1.0 dB |
| Peaking | 6286 Hz  | 7.37 | 1.3 dB  |
| Peaking | 13217 Hz | 1.67 | -0.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Klipsch%20X10/Klipsch%20X10.png)