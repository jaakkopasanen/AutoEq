# Blue Lola

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -0.1; 22 -0.3; 23 -0.4; 25 -0.6; 26 -0.6; 28 -0.8; 30 -0.8; 32 -0.9; 35 -1.0; 37 -1.0; 40 -1.1; 42 -1.2; 45 -1.2; 49 -1.2; 52 -1.2; 56 -1.2; 59 -1.3; 64 -1.3; 68 -1.3; 73 -1.3; 78 -1.3; 83 -1.4; 89 -1.7; 95 -2.1; 102 -2.2; 109 -2.1; 117 -2.2; 125 -2.5; 134 -3.0; 143 -3.3; 153 -3.7; 164 -3.0; 175 -2.5; 188 -2.9; 201 -2.7; 215 -2.3; 230 -1.7; 246 -1.0; 263 -0.4; 282 0.3; 301 0.6; 323 0.8; 345 0.8; 369 0.8; 395 0.5; 423 0.6; 452 1.1; 484 1.6; 518 2.9; 554 2.5; 593 2.0; 635 1.7; 679 1.3; 726 1.0; 777 1.1; 832 0.9; 890 0.5; 952 0.1; 1019 -0.1; 1090 -0.2; 1167 -0.3; 1248 -0.4; 1336 -0.4; 1429 -0.7; 1529 -1.0; 1636 -1.1; 1751 -1.0; 1873 -0.4; 2004 0.1; 2145 0.5; 2295 1.0; 2455 1.9; 2627 2.3; 2811 2.6; 3008 3.0; 3219 3.3; 3444 5.0; 3685 5.8; 3943 6.0; 4219 3.8; 4514 1.0; 4830 2.1; 5168 4.8; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Blue Lola ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 58 Hz   | 0.55 | -1.1 dB |
| Peaking | 157 Hz  | 1.55 | -3.1 dB |
| Peaking | 536 Hz  | 2.05 | 2.6 dB  |
| Peaking | 3630 Hz | 3.1  | 5.6 dB  |
| Peaking | 5904 Hz | 3.78 | 6.3 dB  |
| Peaking | 213 Hz  | 6    | -0.8 dB |
| Peaking | 306 Hz  | 4.36 | 1.2 dB  |
| Peaking | 1624 Hz | 2.43 | -1.5 dB |
| Peaking | 2568 Hz | 4.65 | 1.5 dB  |
| Peaking | 8259 Hz | 4.83 | -0.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Blue%20Lola/Blue%20Lola.png)