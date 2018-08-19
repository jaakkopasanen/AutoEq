# Paradigm Shift E3m

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -7.6; 22 -7.6; 23 -7.6; 25 -7.6; 26 -7.7; 28 -7.7; 30 -7.8; 32 -7.8; 35 -7.9; 37 -8.0; 40 -8.1; 42 -8.1; 45 -8.3; 49 -8.5; 52 -8.6; 56 -8.7; 59 -8.9; 64 -9.1; 68 -9.3; 73 -9.5; 78 -9.8; 83 -10.1; 89 -10.4; 95 -10.6; 102 -10.8; 109 -10.9; 117 -11.1; 125 -11.3; 134 -11.4; 143 -11.5; 153 -11.6; 164 -11.6; 175 -11.6; 188 -11.5; 201 -11.5; 215 -11.4; 230 -11.2; 246 -11.1; 263 -10.8; 282 -10.5; 301 -10.2; 323 -9.9; 345 -9.5; 369 -9.0; 395 -8.6; 423 -7.9; 452 -7.4; 484 -6.9; 518 -6.3; 554 -5.5; 593 -4.6; 635 -3.9; 679 -3.3; 726 -2.5; 777 -1.6; 832 -1.1; 890 -0.7; 952 -0.3; 1019 0.2; 1090 0.6; 1167 0.7; 1248 0.8; 1336 0.6; 1429 0.0; 1529 -0.5; 1636 0.5; 1751 1.5; 1873 1.1; 2004 1.8; 2145 2.9; 2295 4.3; 2455 5.8; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 4.8; 4830 3.8; 5168 3.4; 5530 2.5; 5917 1.6; 6331 1.7; 6775 3.0; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999996125dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Paradigm Shift E3m ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.4dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.18 | -7.4 dB |
| Peaking | 180 Hz  | 0.63 | -6.8 dB |
| Peaking | 382 Hz  | 1.21 | -4.3 dB |
| Peaking | 2519 Hz | 4.23 | 2.9 dB  |
| Peaking | 3585 Hz | 1.21 | 6.2 dB  |
| Peaking | 403 Hz  | 2.55 | 1.6 dB  |
| Peaking | 454 Hz  | 1.25 | -1.5 dB |
| Peaking | 1065 Hz | 1.72 | 1.5 dB  |
| Peaking | 1534 Hz | 7.05 | -1.6 dB |
| Peaking | 8995 Hz | 3.08 | -0.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Paradigm%20Shift%20E3m/Paradigm%20Shift%20E3m.png)