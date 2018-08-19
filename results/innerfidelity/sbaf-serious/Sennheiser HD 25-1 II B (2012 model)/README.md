# Sennheiser HD 25-1 II B (2012 model)

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 2.4; 22 1.9; 23 1.6; 25 1.2; 26 1.0; 28 0.6; 30 0.3; 32 0.0; 35 -0.3; 37 -0.5; 40 -0.7; 42 -0.8; 45 -0.9; 49 -0.9; 52 -1.0; 56 -1.0; 59 -1.1; 64 -1.2; 68 -1.4; 73 -1.8; 78 -2.1; 83 -2.2; 89 -2.0; 95 -1.8; 102 -1.6; 109 -1.5; 117 -1.8; 125 -2.9; 134 -3.6; 143 -3.7; 153 -3.4; 164 -2.7; 175 -3.0; 188 -2.7; 201 -2.2; 215 -1.5; 230 -0.9; 246 -0.4; 263 0.1; 282 0.5; 301 0.6; 323 0.7; 345 0.9; 369 1.0; 395 1.0; 423 1.1; 452 0.9; 484 0.7; 518 0.6; 554 0.7; 593 0.9; 635 0.7; 679 0.7; 726 0.6; 777 0.6; 832 0.5; 890 0.3; 952 0.2; 1019 0.0; 1090 -0.0; 1167 -0.1; 1248 -0.3; 1336 -0.7; 1429 -1.2; 1529 -1.5; 1636 -1.8; 1751 -2.1; 1873 -2.3; 2004 -2.3; 2145 -1.8; 2295 -0.9; 2455 0.5; 2627 1.6; 2811 2.5; 3008 3.2; 3219 2.6; 3444 2.8; 3685 3.0; 3943 3.4; 4219 3.9; 4514 4.8; 4830 4.7; 5168 5.9; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -1.7; 8880 -4.3; 9502 -3.5; 10167 -0.5; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.096025095977881dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 25-1 II B (2012 model) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 2.62 | 2.2 dB  |
| Peaking | 141 Hz  | 1.5  | -3.5 dB |
| Peaking | 3084 Hz | 5.16 | 2.2 dB  |
| Peaking | 5539 Hz | 1.78 | 6.7 dB  |
| Peaking | 8959 Hz | 4.44 | -6.0 dB |
| Peaking | 21 Hz   | 1.62 | 0.7 dB  |
| Peaking | 63 Hz   | 1.24 | -1.2 dB |
| Peaking | 442 Hz  | 0.93 | 1.3 dB  |
| Peaking | 1977 Hz | 1.77 | -4.3 dB |
| Peaking | 2549 Hz | 1.42 | 2.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%2025-1%20II%20B%20(2012%20model)/Sennheiser%20HD%2025-1%20II%20B%20(2012%20model).png)