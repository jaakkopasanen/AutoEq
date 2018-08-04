# Sennheiser HD 25-1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 3.6; 22 3.1; 23 2.8; 25 2.5; 26 2.3; 28 2.0; 30 1.9; 32 1.7; 35 1.6; 37 1.6; 40 1.6; 42 1.6; 45 1.6; 49 1.6; 52 1.8; 56 1.8; 59 1.7; 64 1.4; 68 1.5; 73 1.5; 78 1.1; 83 0.3; 89 -0.9; 95 -2.2; 102 -2.9; 109 -3.2; 117 -3.2; 125 -3.0; 134 -2.7; 143 -2.4; 153 -1.9; 164 -1.7; 175 -1.7; 188 -1.2; 201 -0.9; 215 -0.4; 230 0.2; 246 0.8; 263 1.1; 282 1.4; 301 1.7; 323 2.1; 345 2.6; 369 2.8; 395 2.7; 423 2.7; 452 2.5; 484 2.2; 518 2.0; 554 2.0; 593 2.0; 635 1.8; 679 1.5; 726 1.4; 777 1.2; 832 0.8; 890 0.5; 952 0.3; 1019 -0.0; 1090 -0.3; 1167 -0.6; 1248 -0.9; 1336 -1.5; 1429 -2.1; 1529 -2.6; 1636 -3.2; 1751 -3.5; 1873 -3.5; 2004 -3.3; 2145 -2.7; 2295 -1.7; 2455 -0.3; 2627 0.9; 2811 1.9; 3008 2.8; 3219 2.7; 3444 3.1; 3685 3.6; 3943 4.7; 4219 5.2; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 -0.5; 8299 -3.6; 8880 -4.9; 9502 -3.2; 10167 -0.2; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 25-1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 130 Hz  | 0.21 | 5.2 dB  |
| Peaking | 129 Hz  | 0.8  | -8.3 dB |
| Peaking | 1810 Hz | 1.45 | -5.4 dB |
| Peaking | 5307 Hz | 0.83 | 7.3 dB  |
| Peaking | 8633 Hz | 2.93 | -8.6 dB |
| Peaking | 40 Hz   | 2.73 | -0.7 dB |
| Peaking | 77 Hz   | 3.2  | 1.9 dB  |
| Peaking | 115 Hz  | 1.19 | -1.7 dB |
| Peaking | 138 Hz  | 2.74 | 1.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%2025-1/Sennheiser%20HD%2025-1.png)