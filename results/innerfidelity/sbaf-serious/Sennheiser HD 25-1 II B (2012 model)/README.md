# Sennheiser HD 25-1 II B (2012 model)

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 2.4; 22 1.9; 23 1.7; 25 1.2; 26 1.0; 28 0.7; 30 0.4; 32 0.1; 35 -0.2; 37 -0.4; 40 -0.6; 42 -0.6; 45 -0.7; 49 -0.7; 52 -0.7; 56 -0.7; 59 -0.7; 64 -0.7; 68 -0.8; 73 -1.1; 78 -1.4; 83 -1.4; 89 -1.2; 95 -1.1; 102 -1.0; 109 -1.1; 117 -1.6; 125 -2.8; 134 -3.7; 143 -3.9; 153 -3.6; 164 -2.9; 175 -3.2; 188 -2.9; 201 -2.3; 215 -1.6; 230 -1.0; 246 -0.5; 263 -0.0; 282 0.4; 301 0.6; 323 0.6; 345 0.9; 369 1.0; 395 1.0; 423 1.0; 452 0.8; 484 0.7; 518 0.6; 554 0.7; 593 0.9; 635 0.7; 679 0.7; 726 0.6; 777 0.6; 832 0.5; 890 0.3; 952 0.2; 1019 0.0; 1090 -0.0; 1167 -0.1; 1248 -0.3; 1336 -0.7; 1429 -1.2; 1529 -1.5; 1636 -1.8; 1751 -2.1; 1873 -2.3; 2004 -2.3; 2145 -1.8; 2295 -0.9; 2455 0.5; 2627 1.6; 2811 2.5; 3008 3.2; 3219 2.6; 3444 2.8; 3685 3.0; 3943 3.4; 4219 3.9; 4514 4.8; 4830 4.7; 5168 5.9; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -1.7; 8880 -4.3; 9502 -3.5; 10167 -0.5; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 25-1 II B (2012 model) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 2.82 | 2.1 dB  |
| Peaking | 148 Hz  | 1.97 | -4.0 dB |
| Peaking | 3077 Hz | 5.31 | 2.2 dB  |
| Peaking | 5536 Hz | 1.78 | 6.7 dB  |
| Peaking | 8952 Hz | 4.44 | -6.0 dB |
| Peaking | 17 Hz   | 1.89 | -1.7 dB |
| Peaking | 59 Hz   | 1.02 | -0.7 dB |
| Peaking | 465 Hz  | 0.95 | 1.2 dB  |
| Peaking | 2540 Hz | 1.4  | 2.2 dB  |
| Peaking | 1980 Hz | 1.76 | -4.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%2025-1%20II%20B%20(2012%20model)/Sennheiser%20HD%2025-1%20II%20B%20(2012%20model).png)