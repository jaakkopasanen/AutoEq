# RBH EP1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.6dB
GraphicEQ: 10 -84; 20 -10.2; 22 -10.0; 23 -9.8; 25 -9.5; 26 -9.4; 28 -9.1; 30 -8.8; 32 -8.6; 35 -8.3; 37 -8.1; 40 -7.6; 42 -7.3; 45 -7.0; 49 -6.7; 52 -6.4; 56 -6.1; 59 -5.9; 64 -5.6; 68 -5.3; 73 -5.1; 78 -4.9; 83 -4.9; 89 -4.9; 95 -5.0; 102 -5.4; 109 -5.4; 117 -5.4; 125 -6.0; 134 -5.9; 143 -6.1; 153 -5.6; 164 -5.6; 175 -5.5; 188 -5.0; 201 -4.9; 215 -4.4; 230 -4.1; 246 -3.8; 263 -3.5; 282 -3.1; 301 -2.7; 323 -2.6; 345 -2.1; 369 -1.8; 395 -1.5; 423 -1.1; 452 -0.8; 484 -0.6; 518 -0.4; 554 0.1; 593 0.3; 635 1.1; 679 1.0; 726 1.0; 777 1.1; 832 0.8; 890 0.6; 952 0.3; 1019 -0.1; 1090 -0.4; 1167 -0.7; 1248 -1.0; 1336 -1.6; 1429 -2.4; 1529 -3.1; 1636 -3.8; 1751 -4.3; 1873 -4.4; 2004 -4.4; 2145 -4.5; 2295 -4.3; 2455 -3.6; 2627 -3.2; 2811 -2.3; 3008 -0.8; 3219 0.3; 3444 1.1; 3685 0.7; 3943 -0.8; 4219 -3.7; 4514 -5.7; 4830 -6.7; 5168 -4.5; 5530 -1.8; 5917 0.8; 6331 3.1; 6775 3.7; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.3; 10167 -0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.6dB` and instead set Global volume in the UI for both channels to **-46**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RBH EP1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 10 Hz   | 0.58 | -9.3 dB |
| Peaking | 31 Hz   | 0.45 | -5.7 dB |
| Peaking | 162 Hz  | 0.93 | -4.8 dB |
| Peaking | 1979 Hz | 2.22 | -5.1 dB |
| Peaking | 4717 Hz | 6.79 | -7.3 dB |
| Peaking | 730 Hz  | 2.4  | 1.9 dB  |
| Peaking | 3137 Hz | 1.42 | -1.6 dB |
| Peaking | 3446 Hz | 3.87 | 4.0 dB  |
| Peaking | 5549 Hz | 2.04 | -1.8 dB |
| Peaking | 6502 Hz | 4.61 | 5.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/RBH%20EP1/RBH%20EP1.png)