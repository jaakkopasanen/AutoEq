# I-Mego Throne

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -3.2; 22 -3.3; 23 -3.4; 25 -3.5; 26 -3.5; 28 -3.6; 30 -3.6; 32 -3.6; 35 -3.6; 37 -3.6; 40 -3.7; 42 -3.8; 45 -3.9; 49 -4.0; 52 -4.2; 56 -4.3; 59 -4.3; 64 -4.5; 68 -4.5; 73 -4.7; 78 -4.8; 83 -5.0; 89 -5.1; 95 -5.2; 102 -5.3; 109 -5.2; 117 -5.3; 125 -5.4; 134 -5.7; 143 -5.8; 153 -5.7; 164 -5.3; 175 -5.1; 188 -4.8; 201 -4.5; 215 -4.0; 230 -3.4; 246 -2.9; 263 -2.3; 282 -1.6; 301 -1.1; 323 -0.8; 345 -0.8; 369 -1.6; 395 -1.6; 423 -2.1; 452 -2.6; 484 -3.2; 518 -3.5; 554 -3.4; 593 -3.2; 635 -2.9; 679 -2.7; 726 -2.2; 777 -1.6; 832 -1.1; 890 -0.6; 952 -0.2; 1019 0.2; 1090 0.5; 1167 0.8; 1248 1.4; 1336 1.8; 1429 2.0; 1529 2.3; 1636 2.8; 1751 3.5; 1873 4.3; 2004 5.5; 2145 6.0; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999999965dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `I-Mego Throne ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 0.4  | -3.3 dB |
| Peaking | 97 Hz   | 0.96 | -3.0 dB |
| Peaking | 168 Hz  | 1.59 | -3.5 dB |
| Peaking | 602 Hz  | 1.48 | -3.7 dB |
| Peaking | 3282 Hz | 0.66 | 6.9 dB  |
| Peaking | 220 Hz  | 5.31 | -0.4 dB |
| Peaking | 2154 Hz | 3.09 | 2.3 dB  |
| Peaking | 2661 Hz | 0.9  | -1.2 dB |
| Peaking | 6209 Hz | 2.03 | 5.6 dB  |
| Peaking | 7475 Hz | 1.45 | -4.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/I-Mego%20Throne/I-Mego%20Throne.png)