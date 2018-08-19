# Blue Lola

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -0.1; 22 -0.3; 23 -0.4; 25 -0.6; 26 -0.7; 28 -0.8; 30 -0.9; 32 -0.9; 35 -1.0; 37 -1.1; 40 -1.2; 42 -1.3; 45 -1.4; 49 -1.4; 52 -1.5; 56 -1.6; 59 -1.7; 64 -1.8; 68 -1.9; 73 -2.0; 78 -2.1; 83 -2.2; 89 -2.5; 95 -2.8; 102 -2.8; 109 -2.5; 117 -2.4; 125 -2.5; 134 -2.8; 143 -3.1; 153 -3.5; 164 -2.7; 175 -2.3; 188 -2.7; 201 -2.5; 215 -2.1; 230 -1.6; 246 -0.9; 263 -0.3; 282 0.4; 301 0.7; 323 0.9; 345 0.9; 369 0.8; 395 0.6; 423 0.6; 452 1.1; 484 1.6; 518 2.9; 554 2.5; 593 2.0; 635 1.7; 679 1.3; 726 1.0; 777 1.1; 832 0.9; 890 0.5; 952 0.1; 1019 -0.1; 1090 -0.2; 1167 -0.3; 1248 -0.4; 1336 -0.4; 1429 -0.7; 1529 -1.0; 1636 -1.1; 1751 -1.0; 1873 -0.4; 2004 0.1; 2145 0.5; 2295 1.0; 2455 1.9; 2627 2.3; 2811 2.6; 3008 3.0; 3219 3.3; 3444 5.0; 3685 5.8; 3943 6.0; 4219 3.8; 4514 1.0; 4830 2.1; 5168 4.8; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.084225018767814dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Blue Lola ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 82 Hz   | 0.71 | -2.1 dB |
| Peaking | 162 Hz  | 1.77 | -2.2 dB |
| Peaking | 535 Hz  | 2.02 | 2.6 dB  |
| Peaking | 3630 Hz | 3.1  | 5.6 dB  |
| Peaking | 5904 Hz | 3.78 | 6.3 dB  |
| Peaking | 310 Hz  | 5.63 | 1.2 dB  |
| Peaking | 1649 Hz | 2.24 | -1.6 dB |
| Peaking | 2642 Hz | 2.57 | 1.5 dB  |
| Peaking | 3299 Hz | 7.12 | -1.1 dB |
| Peaking | 8307 Hz | 4.67 | -0.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Blue%20Lola/Blue%20Lola.png)