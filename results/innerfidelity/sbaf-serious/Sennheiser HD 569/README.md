# Sennheiser HD 569

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.7dB
GraphicEQ: 10 -84; 20 6.2; 22 5.2; 23 4.8; 25 4.0; 26 3.7; 28 3.0; 30 2.5; 32 1.9; 35 1.3; 37 0.9; 40 0.4; 42 0.1; 45 -0.3; 49 -0.6; 52 -0.8; 56 -1.1; 59 -1.2; 64 -1.3; 68 -1.3; 73 -1.3; 78 -1.3; 83 -1.3; 89 -1.3; 95 -1.4; 102 -1.6; 109 -1.9; 117 -2.3; 125 -3.1; 134 -3.8; 143 -4.2; 153 -3.9; 164 -1.9; 175 -1.8; 188 -1.9; 201 -1.5; 215 -0.8; 230 0.0; 246 0.9; 263 1.5; 282 2.1; 301 2.3; 323 2.3; 345 2.1; 369 1.8; 395 1.4; 423 0.9; 452 0.4; 484 -0.2; 518 -0.5; 554 -0.3; 593 -0.1; 635 0.1; 679 0.0; 726 0.0; 777 0.1; 832 -0.0; 890 -0.1; 952 -0.0; 1019 0.0; 1090 0.3; 1167 0.6; 1248 0.9; 1336 1.0; 1429 0.8; 1529 0.6; 1636 0.6; 1751 0.5; 1873 0.5; 2004 0.6; 2145 0.6; 2295 0.9; 2455 2.0; 2627 2.7; 2811 3.0; 3008 2.6; 3219 0.7; 3444 0.2; 3685 1.3; 3943 2.7; 4219 3.1; 4514 3.5; 4830 4.7; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -1.0; 9502 -1.2; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -1.1; 20000 -3.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.7dB` and instead set Global volume in the UI for both channels to **-67**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 569 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 1.95 | 5.8 dB  |
| Peaking | 142 Hz  | 1.09 | -3.6 dB |
| Peaking | 299 Hz  | 1.99 | 3.4 dB  |
| Peaking | 2709 Hz | 4.43 | 2.7 dB  |
| Peaking | 5509 Hz | 2.5  | 6.7 dB  |
| Peaking | 58 Hz   | 3.31 | -1.1 dB |
| Peaking | 520 Hz  | 6.9  | -0.9 dB |
| Peaking | 1334 Hz | 4.34 | 1.0 dB  |
| Peaking | 6477 Hz | 9.2  | 2.0 dB  |
| Peaking | 8838 Hz | 2.73 | -1.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20569/Sennheiser%20HD%20569.png)