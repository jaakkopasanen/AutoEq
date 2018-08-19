# Skullcandy Navigator

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -2.4; 22 -2.4; 23 -2.4; 25 -2.5; 26 -2.5; 28 -2.5; 30 -2.5; 32 -2.5; 35 -2.5; 37 -2.5; 40 -2.5; 42 -2.5; 45 -2.5; 49 -2.5; 52 -2.6; 56 -2.7; 59 -2.7; 64 -2.8; 68 -2.9; 73 -3.0; 78 -3.2; 83 -3.4; 89 -3.6; 95 -3.7; 102 -3.9; 109 -3.9; 117 -4.1; 125 -4.3; 134 -4.4; 143 -4.4; 153 -4.3; 164 -4.4; 175 -4.0; 188 -3.9; 201 -4.2; 215 -4.4; 230 -4.3; 246 -4.2; 263 -4.1; 282 -3.6; 301 -3.3; 323 -3.1; 345 -2.8; 369 -2.5; 395 -2.2; 423 -1.5; 452 -1.1; 484 -0.8; 518 -0.3; 554 0.2; 593 0.7; 635 0.9; 679 1.0; 726 1.3; 777 1.6; 832 1.1; 890 0.7; 952 0.3; 1019 0.1; 1090 0.2; 1167 0.1; 1248 -0.1; 1336 -0.1; 1429 -0.1; 1529 -0.3; 1636 0.3; 1751 0.6; 1873 1.0; 2004 1.5; 2145 2.1; 2295 2.7; 2455 3.4; 2627 3.9; 2811 4.0; 3008 4.4; 3219 4.8; 3444 5.2; 3685 5.5; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.0999994318308834dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Skullcandy Navigator ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.36 | -2.2 dB |
| Peaking | 119 Hz  | 0.8  | -2.7 dB |
| Peaking | 255 Hz  | 0.85 | -3.0 dB |
| Peaking | 674 Hz  | 2.24 | 2.0 dB  |
| Peaking | 4314 Hz | 1.09 | 6.7 dB  |
| Peaking | 1514 Hz | 2.71 | -1.0 dB |
| Peaking | 2568 Hz | 2.93 | 1.2 dB  |
| Peaking | 4311 Hz | 3.53 | -0.8 dB |
| Peaking | 6271 Hz | 2.9  | 4.5 dB  |
| Peaking | 7475 Hz | 1.61 | -3.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Skullcandy%20Navigator/Skullcandy%20Navigator.png)