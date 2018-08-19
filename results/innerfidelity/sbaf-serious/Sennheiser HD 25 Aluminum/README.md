# Sennheiser HD 25 Aluminum

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -3.3; 22 -3.6; 23 -3.8; 25 -4.0; 26 -4.1; 28 -4.3; 30 -4.4; 32 -4.6; 35 -4.7; 37 -4.7; 40 -4.8; 42 -4.8; 45 -4.8; 49 -4.8; 52 -4.8; 56 -4.8; 59 -4.7; 64 -4.7; 68 -4.7; 73 -4.5; 78 -4.2; 83 -3.9; 89 -4.2; 95 -5.1; 102 -6.2; 109 -6.8; 117 -7.3; 125 -7.3; 134 -6.9; 143 -6.6; 153 -6.0; 164 -5.3; 175 -5.4; 188 -4.5; 201 -3.8; 215 -3.2; 230 -2.4; 246 -1.6; 263 -0.5; 282 0.4; 301 1.0; 323 1.5; 345 2.0; 369 2.3; 395 2.4; 423 2.6; 452 2.4; 484 2.0; 518 1.8; 554 1.7; 593 1.7; 635 1.5; 679 1.2; 726 1.0; 777 1.0; 832 0.7; 890 0.4; 952 0.1; 1019 -0.1; 1090 -0.3; 1167 -0.5; 1248 -0.8; 1336 -1.4; 1429 -2.1; 1529 -2.9; 1636 -3.6; 1751 -4.1; 1873 -4.4; 2004 -4.5; 2145 -4.2; 2295 -3.5; 2455 -2.4; 2627 -1.3; 2811 -0.4; 3008 0.5; 3219 0.7; 3444 0.6; 3685 0.4; 3943 0.5; 4219 1.0; 4514 3.6; 4830 5.7; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 -2.3; 8299 -5.7; 8880 -6.4; 9502 -4.1; 10167 -0.4; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.098686844670457dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 25 Aluminum ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 39 Hz   | 0.62 | -4.8 dB |
| Peaking | 131 Hz  | 1.69 | -6.6 dB |
| Peaking | 1958 Hz | 2.3  | -5.3 dB |
| Peaking | 5784 Hz | 1.82 | 7.4 dB  |
| Peaking | 8599 Hz | 3.91 | -9.0 dB |
| Peaking | 208 Hz  | 2.15 | -2.7 dB |
| Peaking | 390 Hz  | 0.91 | 3.2 dB  |
| Peaking | 1496 Hz | 4.56 | -1.1 dB |
| Peaking | 4110 Hz | 6.78 | -1.9 dB |
| Peaking | 4794 Hz | 9.17 | 1.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%2025%20Aluminum/Sennheiser%20HD%2025%20Aluminum.png)