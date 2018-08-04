# Sennheiser HD 419

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -4.7; 22 -5.0; 23 -5.1; 25 -5.3; 26 -5.4; 28 -5.5; 30 -5.7; 32 -5.8; 35 -5.9; 37 -6.0; 40 -6.0; 42 -6.1; 45 -6.1; 49 -6.1; 52 -6.1; 56 -6.1; 59 -6.1; 64 -6.0; 68 -5.8; 73 -5.9; 78 -6.1; 83 -5.9; 89 -4.9; 95 -3.9; 102 -5.3; 109 -7.1; 117 -8.1; 125 -8.8; 134 -9.1; 143 -9.4; 153 -9.5; 164 -9.0; 175 -9.3; 188 -9.3; 201 -9.2; 215 -9.1; 230 -8.6; 246 -8.1; 263 -7.4; 282 -6.7; 301 -5.9; 323 -4.8; 345 -3.8; 369 -3.2; 395 -3.0; 423 -2.5; 452 -2.0; 484 -2.0; 518 -2.4; 554 -2.7; 593 -2.6; 635 -2.1; 679 -1.2; 726 -0.8; 777 -0.9; 832 -0.6; 890 0.0; 952 0.1; 1019 0.1; 1090 -0.2; 1167 -0.4; 1248 -0.2; 1336 -0.6; 1429 -1.2; 1529 -1.5; 1636 -1.6; 1751 -1.6; 1873 -1.4; 2004 -0.6; 2145 0.6; 2295 1.8; 2455 2.5; 2627 1.9; 2811 2.7; 3008 3.2; 3219 3.3; 3444 3.5; 3685 4.4; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 5.7; 5530 5.7; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 419 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.85 | -4.8 dB |
| Peaking | 53 Hz   | 1.59 | -2.7 dB |
| Peaking | 171 Hz  | 0.77 | -9.2 dB |
| Peaking | 251 Hz  | 3.28 | -1.3 dB |
| Peaking | 4698 Hz | 1.42 | 6.8 dB  |
| Peaking | 99 Hz   | 2.24 | -2.2 dB |
| Peaking | 96 Hz   | 5.87 | 4.5 dB  |
| Peaking | 1786 Hz | 2.26 | -4.3 dB |
| Peaking | 2102 Hz | 1.32 | 2.5 dB  |
| Peaking | 8547 Hz | 3.74 | -1.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20419/Sennheiser%20HD%20419.png)