# Stax SR-007

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 5.3; 52 4.0; 56 2.7; 59 3.1; 64 3.9; 68 4.2; 73 4.4; 78 4.5; 83 4.5; 89 4.3; 95 4.1; 102 3.8; 109 3.6; 117 3.4; 125 2.9; 134 2.6; 143 2.4; 153 2.2; 164 2.1; 175 2.1; 188 1.9; 201 1.8; 215 1.8; 230 1.8; 246 1.7; 263 1.6; 282 1.6; 301 1.4; 323 1.4; 345 1.3; 369 1.2; 395 1.2; 423 1.3; 452 1.5; 484 2.0; 518 2.6; 554 2.1; 593 1.5; 635 0.7; 679 0.3; 726 0.4; 777 0.6; 832 0.6; 890 0.4; 952 0.2; 1019 0.2; 1090 1.2; 1167 2.3; 1248 3.9; 1336 1.6; 1429 -0.7; 1529 -0.9; 1636 -0.6; 1751 0.6; 1873 2.2; 2004 3.5; 2145 4.7; 2295 5.1; 2455 5.9; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 5.7; 3685 5.1; 3943 4.6; 4219 3.7; 4514 2.6; 4830 2.0; 5168 2.9; 5530 4.8; 5917 5.0; 6331 5.3; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.3; 8880 -1.7; 9502 -0.9; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -0.0; 20000 -3.6
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-007 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.69 | 5.6 dB  |
| Peaking | 95 Hz   | 0.51 | 2.8 dB  |
| Peaking | 515 Hz  | 3.61 | 2.0 dB  |
| Peaking | 2926 Hz | 1.49 | 6.6 dB  |
| Peaking | 6076 Hz | 4.43 | 4.8 dB  |
| Peaking | 1248 Hz | 5.61 | 5.7 dB  |
| Peaking | 1474 Hz | 2.15 | -3.9 dB |
| Peaking | 2114 Hz | 3.64 | 2.1 dB  |
| Peaking | 6680 Hz | 9.45 | 1.2 dB  |
| Peaking | 8873 Hz | 4.69 | -2.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-007/Stax%20SR-007.png)