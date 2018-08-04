# Creative Fatal1ty

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 1.7; 22 0.9; 23 0.6; 25 -0.0; 26 -0.3; 28 -0.8; 30 -1.2; 32 -1.5; 35 -2.0; 37 -2.3; 40 -2.7; 42 -2.8; 45 -3.0; 49 -3.2; 52 -3.3; 56 -3.4; 59 -3.5; 64 -3.5; 68 -3.5; 73 -3.6; 78 -3.6; 83 -3.7; 89 -3.8; 95 -3.8; 102 -3.8; 109 -3.9; 117 -4.1; 125 -4.4; 134 -4.4; 143 -4.5; 153 -4.4; 164 -4.1; 175 -3.8; 188 -3.6; 201 -3.3; 215 -2.9; 230 -2.4; 246 -2.0; 263 -1.7; 282 -1.1; 301 -0.5; 323 -0.0; 345 0.6; 369 1.1; 395 1.4; 423 1.9; 452 2.2; 484 2.2; 518 1.9; 554 1.7; 593 1.3; 635 0.9; 679 0.2; 726 0.1; 777 0.4; 832 0.1; 890 -0.0; 952 -0.1; 1019 0.0; 1090 0.3; 1167 0.4; 1248 0.5; 1336 0.3; 1429 0.3; 1529 0.6; 1636 0.9; 1751 1.5; 1873 2.4; 2004 3.5; 2145 4.5; 2295 5.4; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Creative Fatal1ty ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 17 Hz   | 1.24 | 2.9 dB  |
| Peaking | 50 Hz   | 0.7  | -2.9 dB |
| Peaking | 149 Hz  | 0.8  | -3.9 dB |
| Peaking | 436 Hz  | 2.05 | 3.0 dB  |
| Peaking | 3738 Hz | 0.87 | 7.0 dB  |
| Peaking | 1632 Hz | 1.27 | -1.6 dB |
| Peaking | 2332 Hz | 2.35 | 2.8 dB  |
| Peaking | 3657 Hz | 2.51 | -1.3 dB |
| Peaking | 6236 Hz | 2.39 | 5.2 dB  |
| Peaking | 7458 Hz | 1.54 | -4.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Creative%20Fatal1ty/Creative%20Fatal1ty.png)