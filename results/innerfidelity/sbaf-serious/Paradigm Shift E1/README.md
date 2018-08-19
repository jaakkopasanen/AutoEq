# Paradigm Shift E1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -5.9; 22 -5.9; 23 -6.0; 25 -6.0; 26 -6.1; 28 -6.2; 30 -6.2; 32 -6.3; 35 -6.4; 37 -6.4; 40 -6.5; 42 -6.5; 45 -6.6; 49 -6.7; 52 -6.8; 56 -7.0; 59 -7.2; 64 -7.4; 68 -7.5; 73 -7.7; 78 -8.0; 83 -8.2; 89 -8.4; 95 -8.7; 102 -8.8; 109 -8.8; 117 -8.9; 125 -9.1; 134 -9.2; 143 -9.2; 153 -9.2; 164 -9.2; 175 -9.1; 188 -8.9; 201 -8.8; 215 -8.5; 230 -8.3; 246 -8.0; 263 -7.7; 282 -7.3; 301 -6.9; 323 -6.5; 345 -6.0; 369 -5.5; 395 -5.0; 423 -4.3; 452 -3.8; 484 -3.4; 518 -2.8; 554 -2.1; 593 -1.5; 635 -1.0; 679 -0.8; 726 -0.5; 777 0.0; 832 0.2; 890 0.1; 952 0.1; 1019 0.0; 1090 0.1; 1167 0.6; 1248 1.5; 1336 1.6; 1429 1.9; 1529 2.3; 1636 2.5; 1751 3.1; 1873 4.0; 2004 5.2; 2145 6.0; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 5.9; 4830 5.2; 5168 4.8; 5530 4.0; 5917 4.1; 6331 4.9; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.0999999999999375dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Paradigm Shift E1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 0.22 | -5.6 dB |
| Peaking | 133 Hz  | 0.68 | -4.6 dB |
| Peaking | 274 Hz  | 0.82 | -4.5 dB |
| Peaking | 3179 Hz | 0.72 | 6.8 dB  |
| Peaking | 2169 Hz | 4.03 | 1.9 dB  |
| Peaking | 4564 Hz | 0.57 | -1.7 dB |
| Peaking | 4726 Hz | 1.95 | 2.6 dB  |
| Peaking | 6500 Hz | 4.85 | 4.5 dB  |
| Peaking | 7235 Hz | 1.65 | -2.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Paradigm%20Shift%20E1/Paradigm%20Shift%20E1.png)