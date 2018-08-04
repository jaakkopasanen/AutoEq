# Sennheiser HD 25-1 II

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 5.9; 64 5.5; 68 5.0; 73 4.5; 78 4.2; 83 4.0; 89 4.0; 95 3.9; 102 2.7; 109 1.6; 117 0.8; 125 -0.1; 134 -1.2; 143 -1.8; 153 -2.0; 164 -1.8; 175 -2.2; 188 -2.3; 201 -2.1; 215 -2.0; 230 -1.8; 246 -1.6; 263 -1.4; 282 -1.0; 301 -1.1; 323 -1.1; 345 -1.0; 369 -0.7; 395 -0.4; 423 -0.2; 452 -0.2; 484 -0.2; 518 -0.1; 554 0.1; 593 0.2; 635 0.3; 679 0.2; 726 0.3; 777 0.4; 832 0.2; 890 0.1; 952 0.0; 1019 0.0; 1090 -0.1; 1167 -0.3; 1248 -0.5; 1336 -0.9; 1429 -1.4; 1529 -1.9; 1636 -2.5; 1751 -3.0; 1873 -2.9; 2004 -2.9; 2145 -2.8; 2295 -2.3; 2455 -1.2; 2627 0.3; 2811 1.7; 3008 2.6; 3219 2.4; 3444 2.4; 3685 2.3; 3943 2.7; 4219 2.6; 4514 2.5; 4830 4.1; 5168 5.2; 5530 4.9; 5917 5.8; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -1.4; 8880 -3.3; 9502 -1.6; 10167 -0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 25-1 II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 53 Hz   | 0.23 | 7.1 dB  |
| Peaking | 168 Hz  | 0.83 | -7.2 dB |
| Peaking | 2044 Hz | 1.74 | -4.4 dB |
| Peaking | 3155 Hz | 1.63 | 3.5 dB  |
| Peaking | 5762 Hz | 3.2  | 5.9 dB  |
| Peaking | 93 Hz   | 6.18 | 1.2 dB  |
| Peaking | 79 Hz   | 2.66 | -0.3 dB |
| Peaking | 132 Hz  | 7.17 | -0.7 dB |
| Peaking | 6555 Hz | 7.27 | 1.6 dB  |
| Peaking | 8809 Hz | 5.77 | -4.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%2025-1%20II/Sennheiser%20HD%2025-1%20II.png)