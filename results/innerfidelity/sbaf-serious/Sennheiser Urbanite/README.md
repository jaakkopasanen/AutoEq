# Sennheiser Urbanite

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -0.7; 22 -0.8; 23 -0.9; 25 -0.9; 26 -1.0; 28 -1.0; 30 -1.0; 32 -1.0; 35 -1.0; 37 -1.0; 40 -1.0; 42 -1.0; 45 -0.9; 49 -0.9; 52 -0.9; 56 -0.9; 59 -0.8; 64 -0.8; 68 -0.8; 73 -0.7; 78 -0.8; 83 -1.0; 89 -1.1; 95 -1.2; 102 -1.3; 109 -1.4; 117 -1.5; 125 -1.6; 134 -1.7; 143 -2.0; 153 -2.3; 164 -1.9; 175 -1.7; 188 -1.9; 201 -1.8; 215 -1.6; 230 -1.2; 246 -0.9; 263 -0.7; 282 -0.3; 301 -0.0; 323 0.3; 345 0.5; 369 0.6; 395 0.6; 423 0.8; 452 0.9; 484 0.9; 518 0.9; 554 1.0; 593 1.0; 635 0.7; 679 0.4; 726 0.3; 777 0.4; 832 0.3; 890 0.2; 952 0.1; 1019 0.0; 1090 0.0; 1167 0.2; 1248 0.3; 1336 0.3; 1429 0.0; 1529 -0.2; 1636 -0.2; 1751 0.3; 1873 1.3; 2004 2.7; 2145 4.0; 2295 5.4; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Urbanite ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 0.68 | -1.0 dB |
| Peaking | 165 Hz  | 0.98 | -2.0 dB |
| Peaking | 429 Hz  | 1.51 | 1.3 dB  |
| Peaking | 2831 Hz | 1.83 | 5.8 dB  |
| Peaking | 5114 Hz | 1.76 | 5.9 dB  |
| Peaking | 1642 Hz | 3.1  | -1.6 dB |
| Peaking | 2260 Hz | 5.72 | 1.7 dB  |
| Peaking | 6725 Hz | 3.9  | 0.6 dB  |
| Peaking | 6431 Hz | 5.13 | 2.8 dB  |
| Peaking | 7474 Hz | 1.89 | -2.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20Urbanite/Sennheiser%20Urbanite.png)