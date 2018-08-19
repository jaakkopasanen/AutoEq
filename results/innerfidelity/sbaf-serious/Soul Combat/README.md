# Soul Combat

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 5.9; 22 4.5; 23 3.8; 25 2.6; 26 2.1; 28 1.1; 30 0.2; 32 -0.5; 35 -1.5; 37 -2.1; 40 -2.8; 42 -3.2; 45 -3.7; 49 -4.1; 52 -4.4; 56 -4.7; 59 -4.9; 64 -5.2; 68 -5.4; 73 -5.7; 78 -5.9; 83 -6.1; 89 -6.3; 95 -6.5; 102 -6.7; 109 -6.8; 117 -7.1; 125 -7.4; 134 -7.7; 143 -8.0; 153 -8.3; 164 -8.6; 175 -8.4; 188 -8.7; 201 -8.9; 215 -9.3; 230 -9.5; 246 -9.8; 263 -10.2; 282 -10.6; 301 -10.9; 323 -11.2; 345 -11.4; 369 -11.6; 395 -11.8; 423 -12.3; 452 -12.7; 484 -12.7; 518 -12.2; 554 -11.0; 593 -8.9; 635 -6.8; 679 -4.7; 726 -2.3; 777 -0.2; 832 1.3; 890 1.6; 952 1.0; 1019 -0.4; 1090 -1.9; 1167 -3.1; 1248 -3.4; 1336 -2.6; 1429 -2.0; 1529 -1.6; 1636 -2.3; 1751 -3.8; 1873 -3.8; 2004 -3.0; 2145 -1.3; 2295 0.6; 2455 2.8; 2627 4.2; 2811 5.1; 3008 5.7; 3219 5.4; 3444 5.4; 3685 5.6; 3943 5.8; 4219 4.2; 4514 5.7; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.9; 9502 -3.7; 10167 -4.3; 10879 -2.4; 11640 -0.1; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099917628730951dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Soul Combat ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 2.42 | 6.3 dB  |
| Peaking | 164 Hz  | 0.39 | -8.1 dB |
| Peaking | 443 Hz  | 1.71 | -9.0 dB |
| Peaking | 3250 Hz | 2.66 | 5.9 dB  |
| Peaking | 5359 Hz | 2.51 | 6.4 dB  |
| Peaking | 574 Hz  | 3.58 | -3.2 dB |
| Peaking | 866 Hz  | 2.21 | 5.7 dB  |
| Peaking | 1195 Hz | 3.3  | -3.6 dB |
| Peaking | 1851 Hz | 5.3  | -4.5 dB |
| Peaking | 9903 Hz | 4.96 | -5.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Soul%20Combat/Soul%20Combat.png)