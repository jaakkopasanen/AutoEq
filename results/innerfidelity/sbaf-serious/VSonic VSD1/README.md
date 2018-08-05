# VSonic VSD1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -0.1; 22 -0.4; 23 -0.6; 25 -0.8; 26 -0.9; 28 -1.1; 30 -1.3; 32 -1.5; 35 -1.6; 37 -1.7; 40 -1.8; 42 -1.9; 45 -2.0; 49 -2.0; 52 -2.0; 56 -2.0; 59 -2.0; 64 -2.0; 68 -2.0; 73 -2.0; 78 -2.1; 83 -2.3; 89 -2.5; 95 -2.8; 102 -3.2; 109 -3.5; 117 -3.9; 125 -4.3; 134 -4.5; 143 -4.7; 153 -4.7; 164 -4.6; 175 -4.4; 188 -4.3; 201 -4.0; 215 -3.8; 230 -3.5; 246 -3.3; 263 -3.0; 282 -2.7; 301 -2.5; 323 -2.2; 345 -1.9; 369 -1.7; 395 -1.5; 423 -1.1; 452 -0.9; 484 -0.8; 518 -0.6; 554 -0.3; 593 0.1; 635 0.3; 679 0.2; 726 0.4; 777 0.6; 832 0.5; 890 0.4; 952 0.2; 1019 -0.0; 1090 -0.2; 1167 -0.4; 1248 -0.6; 1336 -1.1; 1429 -1.6; 1529 -2.0; 1636 -2.4; 1751 -2.3; 1873 -2.1; 2004 -2.2; 2145 -2.2; 2295 -1.7; 2455 -0.6; 2627 0.6; 2811 2.3; 3008 4.3; 3219 5.7; 3444 6.0; 3685 6.0; 3943 5.7; 4219 3.4; 4514 1.3; 4830 -0.5; 5168 -1.8; 5530 -1.6; 5917 0.7; 6331 3.3; 6775 3.8; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.2; 10167 -0.7; 10879 -0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `VSonic VSD1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 42 Hz    | 1.05 | -1.5 dB |
| Peaking | 162 Hz   | 0.84 | -4.7 dB |
| Peaking | 1972 Hz  | 1.87 | -3.2 dB |
| Peaking | 3446 Hz  | 2.76 | 7.4 dB  |
| Peaking | 23961 Hz | 2.15 | 1.2 dB  |
| Peaking | 788 Hz   | 2.11 | 1.1 dB  |
| Peaking | 1508 Hz  | 5.7  | -0.7 dB |
| Peaking | 4063 Hz  | 6.2  | 2.5 dB  |
| Peaking | 5395 Hz  | 2.36 | -3.8 dB |
| Peaking | 6508 Hz  | 5.23 | 5.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/VSonic%20VSD1/VSonic%20VSD1.png)