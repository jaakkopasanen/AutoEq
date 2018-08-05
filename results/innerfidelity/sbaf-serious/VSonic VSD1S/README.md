# VSonic VSD1S

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 2.6; 22 2.2; 23 2.0; 25 1.7; 26 1.6; 28 1.3; 30 1.1; 32 1.0; 35 0.8; 37 0.7; 40 0.5; 42 0.4; 45 0.3; 49 0.2; 52 0.2; 56 0.1; 59 0.0; 64 -0.1; 68 -0.2; 73 -0.3; 78 -0.5; 83 -0.8; 89 -1.1; 95 -1.4; 102 -2.0; 109 -2.4; 117 -2.9; 125 -3.4; 134 -3.8; 143 -4.0; 153 -4.1; 164 -4.2; 175 -4.1; 188 -4.0; 201 -3.8; 215 -3.6; 230 -3.3; 246 -3.1; 263 -2.9; 282 -2.5; 301 -2.3; 323 -2.0; 345 -1.6; 369 -1.3; 395 -1.1; 423 -0.7; 452 -0.4; 484 -0.3; 518 -0.1; 554 0.3; 593 0.6; 635 0.7; 679 0.7; 726 0.8; 777 0.9; 832 0.7; 890 0.4; 952 0.1; 1019 0.2; 1090 -0.0; 1167 -0.4; 1248 -0.7; 1336 -1.1; 1429 -1.4; 1529 -1.7; 1636 -1.8; 1751 -1.7; 1873 -1.3; 2004 -0.7; 2145 -0.2; 2295 0.7; 2455 2.1; 2627 3.4; 2811 4.8; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 4.6; 4514 2.2; 4830 0.8; 5168 1.2; 5530 3.2; 5917 5.5; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `VSonic VSD1S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 9 Hz    | 0.37 | 3.2 dB  |
| Peaking | 169 Hz  | 1.01 | -4.5 dB |
| Peaking | 1746 Hz | 2.4  | -2.8 dB |
| Peaking | 3326 Hz | 1.94 | 6.9 dB  |
| Peaking | 6220 Hz | 5.87 | 5.5 dB  |
| Peaking | 301 Hz  | 2.77 | -0.7 dB |
| Peaking | 680 Hz  | 2.19 | 1.2 dB  |
| Peaking | 4745 Hz | 2.44 | 2.1 dB  |
| Peaking | 4879 Hz | 5.71 | -4.0 dB |
| Peaking | 8358 Hz | 3.17 | -0.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/VSonic%20VSD1S/VSonic%20VSD1S.png)