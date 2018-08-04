# Sennheiser HD 575

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 5.8; 35 5.3; 37 4.9; 40 4.4; 42 4.1; 45 3.7; 49 3.4; 52 3.2; 56 3.0; 59 2.7; 64 2.2; 68 1.9; 73 1.4; 78 1.0; 83 0.5; 89 -0.1; 95 -0.7; 102 -1.3; 109 -1.8; 117 -2.2; 125 -2.8; 134 -3.1; 143 -3.5; 153 -3.7; 164 -3.7; 175 -3.7; 188 -3.8; 201 -3.8; 215 -3.8; 230 -3.5; 246 -3.2; 263 -3.2; 282 -3.1; 301 -2.9; 323 -2.7; 345 -2.5; 369 -2.3; 395 -2.1; 423 -1.7; 452 -1.5; 484 -1.4; 518 -1.1; 554 -0.8; 593 -0.4; 635 -0.4; 679 -0.4; 726 -0.1; 777 0.2; 832 0.0; 890 -0.1; 952 -0.1; 1019 -0.1; 1090 0.1; 1167 0.0; 1248 -0.2; 1336 -0.2; 1429 -0.4; 1529 -0.6; 1636 -0.3; 1751 0.2; 1873 1.3; 2004 1.0; 2145 0.4; 2295 -0.3; 2455 -1.4; 2627 -2.9; 2811 -4.2; 3008 -4.5; 3219 -4.6; 3444 -3.9; 3685 -2.7; 3943 -1.5; 4219 -1.0; 4514 -0.5; 4830 0.0; 5168 1.4; 5530 1.1; 5917 -0.1; 6331 1.4; 6775 3.4; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 575 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.32 | 6.3 dB  |
| Peaking | 170 Hz  | 0.65 | -4.8 dB |
| Peaking | 1993 Hz | 4.36 | 2.0 dB  |
| Peaking | 3078 Hz | 2.85 | -5.2 dB |
| Peaking | 6793 Hz | 6.51 | 3.5 dB  |
| Peaking | 371 Hz  | 3.28 | -0.5 dB |
| Peaking | 768 Hz  | 2.26 | 0.6 dB  |
| Peaking | 5540 Hz | 2.29 | -0.8 dB |
| Peaking | 5245 Hz | 6.42 | 2.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20575/Sennheiser%20HD%20575.png)