# VSonic VSD1S

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 2.5; 22 2.1; 23 1.9; 25 1.6; 26 1.5; 28 1.2; 30 1.0; 32 0.8; 35 0.5; 37 0.3; 40 0.1; 42 -0.0; 45 -0.2; 49 -0.5; 52 -0.6; 56 -0.9; 59 -1.1; 64 -1.4; 68 -1.6; 73 -1.9; 78 -2.1; 83 -2.4; 89 -2.6; 95 -2.8; 102 -3.1; 109 -3.2; 117 -3.2; 125 -3.4; 134 -3.5; 143 -3.6; 153 -3.6; 164 -3.7; 175 -3.5; 188 -3.5; 201 -3.4; 215 -3.2; 230 -3.0; 246 -2.9; 263 -2.7; 282 -2.3; 301 -2.1; 323 -1.8; 345 -1.5; 369 -1.2; 395 -1.0; 423 -0.7; 452 -0.4; 484 -0.2; 518 -0.1; 554 0.3; 593 0.7; 635 0.8; 679 0.7; 726 0.8; 777 0.9; 832 0.7; 890 0.4; 952 0.1; 1019 0.2; 1090 -0.0; 1167 -0.4; 1248 -0.7; 1336 -1.1; 1429 -1.4; 1529 -1.7; 1636 -1.8; 1751 -1.7; 1873 -1.3; 2004 -0.7; 2145 -0.2; 2295 0.7; 2455 2.1; 2627 3.4; 2811 4.8; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 4.6; 4514 2.2; 4830 0.8; 5168 1.2; 5530 3.2; 5917 5.5; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999259689dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `VSonic VSD1S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 1.2  | 2.5 dB  |
| Peaking | 147 Hz  | 0.72 | -3.9 dB |
| Peaking | 1751 Hz | 2.44 | -2.8 dB |
| Peaking | 3326 Hz | 1.94 | 6.9 dB  |
| Peaking | 6212 Hz | 5.88 | 5.5 dB  |
| Peaking | 275 Hz  | 2.55 | -0.6 dB |
| Peaking | 672 Hz  | 2.08 | 1.3 dB  |
| Peaking | 4732 Hz | 2.52 | 2.2 dB  |
| Peaking | 4851 Hz | 5.76 | -4.0 dB |
| Peaking | 8380 Hz | 3.37 | -0.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/VSonic%20VSD1S/VSonic%20VSD1S.png)