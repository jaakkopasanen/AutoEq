# VSonic VSD3S

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.1dB
GraphicEQ: 10 -84; 20 0.9; 22 0.5; 23 0.4; 25 0.1; 26 -0.1; 28 -0.3; 30 -0.5; 32 -0.7; 35 -0.9; 37 -1.1; 40 -1.3; 42 -1.4; 45 -1.6; 49 -1.8; 52 -2.0; 56 -2.2; 59 -2.3; 64 -2.6; 68 -2.9; 73 -3.1; 78 -3.3; 83 -3.6; 89 -3.8; 95 -4.0; 102 -4.3; 109 -4.4; 117 -4.5; 125 -4.6; 134 -4.8; 143 -4.9; 153 -4.9; 164 -4.9; 175 -4.9; 188 -4.9; 201 -4.8; 215 -4.7; 230 -4.5; 246 -4.4; 263 -4.3; 282 -4.0; 301 -3.9; 323 -3.7; 345 -3.4; 369 -3.2; 395 -3.0; 423 -2.6; 452 -2.4; 484 -2.2; 518 -2.0; 554 -1.6; 593 -1.1; 635 -0.9; 679 -0.7; 726 -0.5; 777 -0.1; 832 -0.0; 890 -0.0; 952 -0.0; 1019 0.0; 1090 0.0; 1167 0.2; 1248 0.2; 1336 0.1; 1429 -0.1; 1529 -0.3; 1636 -0.3; 1751 -0.1; 1873 0.3; 2004 0.7; 2145 1.1; 2295 1.6; 2455 2.3; 2627 2.7; 2811 3.1; 3008 3.9; 3219 4.4; 3444 5.0; 3685 4.8; 3943 4.0; 4219 2.0; 4514 0.6; 4830 -0.4; 5168 -1.3; 5530 -2.4; 5917 -2.1; 6331 -0.2; 6775 1.4; 7249 1.3; 7756 0.3; 8299 -0.1; 8880 -2.4; 9502 -4.4; 10167 -4.6; 10879 -3.0; 11640 -0.8; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.0747382372172805dB` and instead set Global volume in the UI for both channels to **-50**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `VSonic VSD3S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 130 Hz  | 0.57 | -4.3 dB |
| Peaking | 295 Hz  | 0.95 | -2.0 dB |
| Peaking | 3422 Hz | 1.82 | 5.2 dB  |
| Peaking | 5385 Hz | 4.5  | -3.6 dB |
| Peaking | 9950 Hz | 4.7  | -5.5 dB |
| Peaking | 18 Hz   | 1.94 | 1.2 dB  |
| Peaking | 867 Hz  | 2.61 | 0.5 dB  |
| Peaking | 1655 Hz | 5.52 | -0.8 dB |
| Peaking | 5988 Hz | 6.78 | -1.3 dB |
| Peaking | 6928 Hz | 5.49 | 2.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/VSonic%20VSD3S/VSonic%20VSD3S.png)