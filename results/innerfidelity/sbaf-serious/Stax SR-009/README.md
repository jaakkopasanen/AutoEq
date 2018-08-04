# Stax SR-009

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 5.3; 68 5.0; 73 5.3; 78 5.5; 83 5.5; 89 5.3; 95 5.1; 102 4.8; 109 4.5; 117 4.2; 125 3.8; 134 3.6; 143 3.4; 153 3.2; 164 3.0; 175 2.9; 188 2.8; 201 2.8; 215 2.8; 230 2.8; 246 2.7; 263 2.7; 282 2.7; 301 2.7; 323 2.6; 345 2.5; 369 2.5; 395 2.4; 423 2.4; 452 2.3; 484 1.9; 518 1.8; 554 1.9; 593 1.9; 635 1.8; 679 1.6; 726 1.6; 777 1.9; 832 1.7; 890 1.1; 952 0.5; 1019 -0.0; 1090 -0.1; 1167 -0.7; 1248 -0.5; 1336 -0.1; 1429 0.2; 1529 -0.1; 1636 -0.3; 1751 0.6; 1873 2.0; 2004 2.9; 2145 3.1; 2295 4.1; 2455 4.9; 2627 4.4; 2811 4.0; 3008 4.0; 3219 3.5; 3444 4.0; 3685 3.3; 3943 2.0; 4219 1.3; 4514 -0.1; 4830 -1.2; 5168 -0.4; 5530 3.7; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-009 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.24 | 6.1 dB  |
| Peaking | 413 Hz  | 0.99 | 1.7 dB  |
| Peaking | 2782 Hz | 1.73 | 4.7 dB  |
| Peaking | 4975 Hz | 5.22 | -4.0 dB |
| Peaking | 6020 Hz | 4.13 | 6.8 dB  |
| Peaking | 795 Hz  | 2.87 | 1.5 dB  |
| Peaking | 1323 Hz | 1.14 | -1.6 dB |
| Peaking | 2139 Hz | 3.35 | 1.5 dB  |
| Peaking | 6762 Hz | 7.85 | 1.3 dB  |
| Peaking | 7793 Hz | 3.07 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-009/Stax%20SR-009.png)