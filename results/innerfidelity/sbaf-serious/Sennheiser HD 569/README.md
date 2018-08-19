# Sennheiser HD 569

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.3dB
GraphicEQ: 10 -84; 20 6.2; 22 5.2; 23 4.8; 25 4.0; 26 3.7; 28 3.0; 30 2.4; 32 1.9; 35 1.2; 37 0.8; 40 0.3; 42 -0.0; 45 -0.4; 49 -0.9; 52 -1.1; 56 -1.4; 59 -1.6; 64 -1.8; 68 -1.9; 73 -2.0; 78 -2.0; 83 -2.1; 89 -2.1; 95 -2.1; 102 -2.1; 109 -2.3; 117 -2.5; 125 -3.1; 134 -3.6; 143 -4.0; 153 -3.7; 164 -1.7; 175 -1.5; 188 -1.7; 201 -1.3; 215 -0.6; 230 0.2; 246 1.0; 263 1.6; 282 2.2; 301 2.3; 323 2.4; 345 2.2; 369 1.8; 395 1.4; 423 1.0; 452 0.4; 484 -0.2; 518 -0.5; 554 -0.3; 593 -0.1; 635 0.1; 679 0.0; 726 0.0; 777 0.1; 832 -0.0; 890 -0.1; 952 -0.0; 1019 0.0; 1090 0.3; 1167 0.6; 1248 0.9; 1336 1.0; 1429 0.8; 1529 0.6; 1636 0.6; 1751 0.5; 1873 0.5; 2004 0.6; 2145 0.6; 2295 0.9; 2455 2.0; 2627 2.7; 2811 3.0; 3008 2.6; 3219 0.7; 3444 0.2; 3685 1.3; 3943 2.7; 4219 3.1; 4514 3.5; 4830 4.7; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -1.0; 9502 -1.2; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -1.1; 20000 -3.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.2512003630109dB` and instead set Global volume in the UI for both channels to **-62**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 569 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 1.45 | 6.1 dB  |
| Peaking | 150 Hz   | 0.51 | -3.7 dB |
| Peaking | 294 Hz   | 1.47 | 4.8 dB  |
| Peaking | 2705 Hz  | 4.22 | 2.7 dB  |
| Peaking | 5510 Hz  | 2.5  | 6.7 dB  |
| Peaking | 1326 Hz  | 3.98 | 1.0 dB  |
| Peaking | 6491 Hz  | 8.83 | 2.1 dB  |
| Peaking | 9351 Hz  | 2.19 | -2.5 dB |
| Peaking | 10326 Hz | 3.67 | 1.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20569/Sennheiser%20HD%20569.png)