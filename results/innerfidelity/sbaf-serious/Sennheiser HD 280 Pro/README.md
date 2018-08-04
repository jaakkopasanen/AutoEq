# Sennheiser HD 280 Pro

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -7.1dB
GraphicEQ: 10 -84; 20 6.5; 22 6.0; 23 5.7; 25 5.3; 26 5.1; 28 4.7; 30 4.4; 32 4.2; 35 3.9; 37 3.7; 40 3.5; 42 3.4; 45 3.2; 49 3.2; 52 3.2; 56 3.5; 59 3.8; 64 4.6; 68 5.4; 73 6.0; 78 6.0; 83 6.0; 89 6.0; 95 6.0; 102 5.9; 109 5.5; 117 4.9; 125 4.4; 134 4.5; 143 3.8; 153 3.5; 164 4.4; 175 2.8; 188 1.9; 201 1.4; 215 1.0; 230 0.9; 246 0.8; 263 0.5; 282 0.5; 301 0.3; 323 0.2; 345 0.3; 369 0.3; 395 0.3; 423 0.4; 452 0.4; 484 0.3; 518 0.2; 554 0.3; 593 0.5; 635 0.4; 679 0.3; 726 0.3; 777 0.4; 832 0.2; 890 0.0; 952 0.0; 1019 -0.1; 1090 -0.3; 1167 -0.5; 1248 -0.5; 1336 -0.6; 1429 -0.9; 1529 -1.4; 1636 -2.1; 1751 -2.6; 1873 -2.4; 2004 -2.0; 2145 -1.6; 2295 -0.5; 2455 1.5; 2627 3.7; 2811 5.3; 3008 5.6; 3219 5.1; 3444 4.6; 3685 4.3; 3943 4.6; 4219 4.6; 4514 3.0; 4830 3.6; 5168 5.3; 5530 5.8; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.8; 8880 -3.2; 9502 -3.0; 10167 -0.5; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-7.1dB` and instead set Global volume in the UI for both channels to **-71**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 280 Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 12 Hz   | 1.32 | 6.2 dB  |
| Peaking | 22 Hz   | 0.98 | 3.8 dB  |
| Peaking | 93 Hz   | 0.94 | 5.9 dB  |
| Peaking | 3223 Hz | 3.05 | 5.6 dB  |
| Peaking | 5686 Hz | 3.13 | 6.3 dB  |
| Peaking | 282 Hz  | 2.9  | -0.6 dB |
| Peaking | 1897 Hz | 1.69 | -3.8 dB |
| Peaking | 2695 Hz | 7.08 | 2.7 dB  |
| Peaking | 3175 Hz | 0.28 | 0.8 dB  |
| Peaking | 9025 Hz | 4.76 | -4.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20280%20Pro/Sennheiser%20HD%20280%20Pro.png)