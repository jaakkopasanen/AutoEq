# Sennheiser HD 250 II

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.4dB
GraphicEQ: 10 -84; 20 0.5; 22 -0.2; 23 -0.5; 25 -1.1; 26 -1.3; 28 -1.8; 30 -2.1; 32 -2.4; 35 -2.8; 37 -2.9; 40 -3.1; 42 -3.1; 45 -3.2; 49 -3.3; 52 -3.3; 56 -3.1; 59 -2.9; 64 -2.4; 68 -2.1; 73 -1.7; 78 -1.1; 83 -0.6; 89 -0.9; 95 -1.9; 102 -3.6; 109 -4.7; 117 -5.2; 125 -4.7; 134 -4.1; 143 -4.5; 153 -4.1; 164 -2.4; 175 -3.1; 188 -1.9; 201 -1.1; 215 -0.7; 230 -0.8; 246 -0.6; 263 -0.2; 282 0.0; 301 0.2; 323 0.6; 345 1.0; 369 1.2; 395 1.2; 423 1.3; 452 1.1; 484 1.0; 518 0.9; 554 1.0; 593 1.1; 635 1.0; 679 0.8; 726 0.7; 777 0.8; 832 0.6; 890 0.4; 952 0.2; 1019 0.1; 1090 -0.1; 1167 0.0; 1248 0.6; 1336 0.1; 1429 -0.5; 1529 -1.0; 1636 -1.0; 1751 -0.5; 1873 -0.3; 2004 -0.5; 2145 -0.7; 2295 -0.9; 2455 -0.3; 2627 0.3; 2811 0.7; 3008 1.7; 3219 1.9; 3444 2.2; 3685 2.4; 3943 2.1; 4219 0.7; 4514 -0.1; 4830 -0.2; 5168 0.6; 5530 1.8; 5917 3.8; 6331 2.1; 6775 -0.4; 7249 -0.6; 7756 -0.8; 8299 -2.1; 8880 -3.4; 9502 -2.6; 10167 -0.3; 10879 0.0; 11640 -0.3; 12455 -0.8; 13327 -0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.4dB` and instead set Global volume in the UI for both channels to **-44**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 250 II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 44 Hz   | 1.42 | -3.4 dB |
| Peaking | 128 Hz  | 2.14 | -5.0 dB |
| Peaking | 3528 Hz | 4.08 | 2.7 dB  |
| Peaking | 5952 Hz | 8.34 | 4.2 dB  |
| Peaking | 8897 Hz | 4.56 | -3.7 dB |
| Peaking | 84 Hz   | 4.29 | 3.1 dB  |
| Peaking | 87 Hz   | 1.37 | -2.4 dB |
| Peaking | 203 Hz  | 1.15 | -2.3 dB |
| Peaking | 252 Hz  | 0.41 | 2.3 dB  |
| Peaking | 1709 Hz | 1.67 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20250%20II/Sennheiser%20HD%20250%20II.png)