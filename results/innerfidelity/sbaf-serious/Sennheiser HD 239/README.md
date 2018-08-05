# Sennheiser HD 239

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.3dB
GraphicEQ: 10 -84; 20 3.1; 22 2.5; 23 2.2; 25 1.7; 26 1.5; 28 1.1; 30 0.9; 32 0.6; 35 0.2; 37 0.0; 40 -0.3; 42 -0.4; 45 -0.7; 49 -0.9; 52 -1.0; 56 -1.2; 59 -1.3; 64 -1.4; 68 -1.5; 73 -1.6; 78 -1.6; 83 -1.6; 89 -1.9; 95 -2.3; 102 -2.7; 109 -3.0; 117 -3.3; 125 -3.7; 134 -3.9; 143 -4.0; 153 -4.0; 164 -3.9; 175 -3.8; 188 -3.7; 201 -3.6; 215 -3.4; 230 -3.1; 246 -2.9; 263 -2.7; 282 -2.5; 301 -2.3; 323 -2.1; 345 -1.9; 369 -1.6; 395 -1.4; 423 -1.1; 452 -1.0; 484 -0.9; 518 -0.8; 554 -0.6; 593 -0.2; 635 -0.1; 679 -0.1; 726 -0.0; 777 0.2; 832 0.1; 890 0.1; 952 0.0; 1019 0.0; 1090 0.0; 1167 -0.2; 1248 -0.4; 1336 -0.8; 1429 -0.6; 1529 -1.3; 1636 -2.0; 1751 -2.1; 1873 -1.5; 2004 -0.3; 2145 0.8; 2295 2.2; 2455 3.0; 2627 3.0; 2811 1.3; 3008 0.1; 3219 -1.9; 3444 -0.9; 3685 3.2; 3943 4.6; 4219 0.4; 4514 -2.3; 4830 -1.8; 5168 -0.6; 5530 -0.1; 5917 0.6; 6331 1.1; 6775 1.0; 7249 0.7; 7756 0.3; 8299 -1.4; 8880 -3.9; 9502 -5.4; 10167 -4.1; 10879 -0.6; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.3dB` and instead set Global volume in the UI for both channels to **-53**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 239 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.77 | 3.1 dB  |
| Peaking | 161 Hz  | 0.67 | -4.0 dB |
| Peaking | 2520 Hz | 6.84 | 3.6 dB  |
| Peaking | 6958 Hz | 3.86 | 1.6 dB  |
| Peaking | 9481 Hz | 4.74 | -6.0 dB |
| Peaking | 1707 Hz | 4.72 | -2.5 dB |
| Peaking | 761 Hz  | 2.06 | 0.5 dB  |
| Peaking | 3343 Hz | 6.84 | -4.9 dB |
| Peaking | 3896 Hz | 3.6  | 7.2 dB  |
| Peaking | 4468 Hz | 4.76 | -5.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20239/Sennheiser%20HD%20239.png)