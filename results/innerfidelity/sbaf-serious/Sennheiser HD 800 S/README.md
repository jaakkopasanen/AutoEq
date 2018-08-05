# Sennheiser HD 800 S

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.5dB
GraphicEQ: 10 -84; 20 4.9; 22 4.4; 23 4.1; 25 3.7; 26 3.5; 28 3.2; 30 2.9; 32 2.6; 35 2.3; 37 2.2; 40 1.9; 42 1.8; 45 1.7; 49 1.6; 52 1.5; 56 1.4; 59 1.4; 64 1.5; 68 1.5; 73 1.4; 78 1.0; 83 0.5; 89 0.1; 95 -0.3; 102 -0.9; 109 -1.3; 117 -1.7; 125 -2.2; 134 -2.5; 143 -2.8; 153 -2.9; 164 -2.9; 175 -3.0; 188 -3.1; 201 -3.2; 215 -3.1; 230 -3.1; 246 -3.1; 263 -3.1; 282 -2.9; 301 -2.8; 323 -2.7; 345 -2.6; 369 -2.5; 395 -2.4; 423 -2.2; 452 -2.0; 484 -2.0; 518 -1.9; 554 -1.6; 593 -1.3; 635 -1.2; 679 -1.2; 726 -1.0; 777 -0.6; 832 -0.5; 890 -0.4; 952 -0.1; 1019 0.1; 1090 0.5; 1167 0.5; 1248 0.9; 1336 1.3; 1429 1.5; 1529 1.8; 1636 1.7; 1751 1.6; 1873 1.5; 2004 1.7; 2145 1.7; 2295 1.6; 2455 2.1; 2627 2.5; 2811 2.1; 3008 1.9; 3219 2.1; 3444 2.3; 3685 1.1; 3943 0.3; 4219 -0.2; 4514 -0.0; 4830 0.1; 5168 -0.4; 5530 -1.3; 5917 -1.2; 6331 -3.6; 6775 -4.2; 7249 -3.0; 7756 -1.9; 8299 -1.1; 8880 -0.5; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 -0.3
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.5dB` and instead set Global volume in the UI for both channels to **-55**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 800 S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 0.5  | 5.4 dB  |
| Peaking | 74 Hz   | 1.22 | 3.1 dB  |
| Peaking | 168 Hz  | 0.32 | -3.7 dB |
| Peaking | 2194 Hz | 0.7  | 2.3 dB  |
| Peaking | 6712 Hz | 3.23 | -4.6 dB |
| Peaking | 1495 Hz | 3.21 | 1.0 dB  |
| Peaking | 1796 Hz | 1.56 | -0.8 dB |
| Peaking | 3487 Hz | 2.33 | 1.2 dB  |
| Peaking | 4095 Hz | 4.36 | -1.6 dB |
| Peaking | 9874 Hz | 5.02 | 0.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20800%20S/Sennheiser%20HD%20800%20S.png)