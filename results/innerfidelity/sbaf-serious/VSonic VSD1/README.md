# VSonic VSD1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -0.2; 22 -0.5; 23 -0.6; 25 -0.9; 26 -1.1; 28 -1.3; 30 -1.5; 32 -1.7; 35 -1.9; 37 -2.1; 40 -2.2; 42 -2.3; 45 -2.5; 49 -2.7; 52 -2.8; 56 -2.9; 59 -3.1; 64 -3.3; 68 -3.4; 73 -3.6; 78 -3.8; 83 -3.9; 89 -4.0; 95 -4.2; 102 -4.3; 109 -4.3; 117 -4.2; 125 -4.3; 134 -4.3; 143 -4.3; 153 -4.2; 164 -4.1; 175 -3.9; 188 -3.8; 201 -3.6; 215 -3.4; 230 -3.2; 246 -3.0; 263 -2.8; 282 -2.5; 301 -2.3; 323 -2.1; 345 -1.8; 369 -1.6; 395 -1.4; 423 -1.0; 452 -0.8; 484 -0.7; 518 -0.6; 554 -0.2; 593 0.1; 635 0.3; 679 0.2; 726 0.4; 777 0.6; 832 0.5; 890 0.4; 952 0.2; 1019 0.0; 1090 -0.2; 1167 -0.4; 1248 -0.6; 1336 -1.1; 1429 -1.5; 1529 -2.0; 1636 -2.4; 1751 -2.3; 1873 -2.1; 2004 -2.2; 2145 -2.2; 2295 -1.7; 2455 -0.6; 2627 0.6; 2811 2.3; 3008 4.3; 3219 5.7; 3444 6.0; 3685 6.0; 3943 5.7; 4219 3.4; 4514 1.3; 4830 -0.5; 5168 -1.8; 5530 -1.6; 5917 0.7; 6331 3.3; 6775 3.8; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.2; 10167 -0.7; 10879 -0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999988230119dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `VSonic VSD1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 87 Hz    | 0.55 | -3.6 dB |
| Peaking | 196 Hz   | 1.02 | -2.0 dB |
| Peaking | 1975 Hz  | 1.86 | -3.2 dB |
| Peaking | 3445 Hz  | 2.75 | 7.4 dB  |
| Peaking | 23900 Hz | 2.23 | 0.9 dB  |
| Peaking | 789 Hz   | 2.14 | 1.0 dB  |
| Peaking | 1511 Hz  | 6.01 | -0.7 dB |
| Peaking | 4060 Hz  | 6.11 | 2.5 dB  |
| Peaking | 5395 Hz  | 2.32 | -3.8 dB |
| Peaking | 6481 Hz  | 5.13 | 5.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/VSonic%20VSD1/VSonic%20VSD1.png)