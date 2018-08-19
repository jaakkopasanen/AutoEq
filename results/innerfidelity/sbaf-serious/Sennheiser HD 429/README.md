# Sennheiser HD 429

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 0.3; 22 0.1; 23 0.0; 25 -0.1; 26 -0.2; 28 -0.4; 30 -0.5; 32 -0.6; 35 -0.7; 37 -0.7; 40 -0.8; 42 -0.8; 45 -0.8; 49 -0.7; 52 -0.7; 56 -0.8; 59 -0.9; 64 -0.9; 68 -0.9; 73 -0.8; 78 -0.5; 83 -0.3; 89 0.4; 95 1.2; 102 1.2; 109 0.1; 117 -1.3; 125 -2.2; 134 -2.4; 143 -2.4; 153 -2.2; 164 -1.7; 175 -2.5; 188 -2.5; 201 -2.3; 215 -2.4; 230 -2.0; 246 -1.6; 263 -1.3; 282 -0.7; 301 -0.2; 323 0.4; 345 0.7; 369 0.4; 395 0.1; 423 -0.0; 452 -0.1; 484 -0.2; 518 -0.5; 554 -0.6; 593 -0.6; 635 -0.8; 679 -0.9; 726 -0.8; 777 -0.5; 832 -0.4; 890 -0.2; 952 -0.0; 1019 0.0; 1090 -0.1; 1167 -0.3; 1248 -0.1; 1336 -0.2; 1429 -0.6; 1529 -0.8; 1636 -0.7; 1751 -0.2; 1873 0.6; 2004 1.5; 2145 2.8; 2295 3.8; 2455 4.1; 2627 4.5; 2811 4.9; 3008 5.5; 3219 5.7; 3444 5.4; 3685 5.1; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999254591366dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 429 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 48 Hz   | 0.97 | -0.6 dB |
| Peaking | 99 Hz   | 4.6  | 3.0 dB  |
| Peaking | 157 Hz  | 1.07 | -2.7 dB |
| Peaking | 1549 Hz | 2.33 | -2.4 dB |
| Peaking | 3916 Hz | 0.87 | 6.7 dB  |
| Peaking | 343 Hz  | 5.4  | 1.4 dB  |
| Peaking | 681 Hz  | 2.8  | -1.0 dB |
| Peaking | 3669 Hz | 7.27 | -1.3 dB |
| Peaking | 6276 Hz | 2.53 | 4.7 dB  |
| Peaking | 7557 Hz | 1.65 | -3.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20429/Sennheiser%20HD%20429.png)