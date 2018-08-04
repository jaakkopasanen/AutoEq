# Sennheiser HD 660 S

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 5.9; 42 5.7; 45 5.3; 49 4.9; 52 4.7; 56 4.4; 59 4.2; 64 3.8; 68 3.8; 73 4.1; 78 4.2; 83 3.4; 89 2.5; 95 1.9; 102 1.3; 109 0.9; 117 0.4; 125 -0.1; 134 -0.5; 143 -0.8; 153 -1.0; 164 -1.0; 175 -1.1; 188 -1.2; 201 -1.1; 215 -1.1; 230 -1.1; 246 -1.0; 263 -1.0; 282 -0.9; 301 -0.9; 323 -0.7; 345 -0.6; 369 -0.5; 395 -0.4; 423 -0.2; 452 -0.2; 484 -0.2; 518 -0.1; 554 0.2; 593 0.5; 635 0.5; 679 0.5; 726 0.7; 777 0.9; 832 0.8; 890 0.7; 952 0.3; 1019 -0.1; 1090 -0.2; 1167 -0.5; 1248 -0.5; 1336 -0.6; 1429 -0.7; 1529 -0.7; 1636 -0.9; 1751 -0.9; 1873 -0.5; 2004 0.1; 2145 0.5; 2295 1.0; 2455 1.5; 2627 1.9; 2811 1.8; 3008 1.6; 3219 1.2; 3444 1.2; 3685 1.5; 3943 1.8; 4219 1.7; 4514 2.7; 4830 3.0; 5168 2.8; 5530 3.9; 5917 3.7; 6331 3.6; 6775 3.8; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 660 S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 32 Hz   |  0.21 | 6.4 dB  |
| Peaking | 157 Hz  |  0.66 | -4.2 dB |
| Peaking | 1585 Hz |  1.17 | -5.1 dB |
| Peaking | 1770 Hz |  0.61 | 4.1 dB  |
| Peaking | 5848 Hz |  2.7  | 3.6 dB  |
| Peaking | 127 Hz  |  4.84 | -0.2 dB |
| Peaking | 1856 Hz |  9.77 | -0.3 dB |
| Peaking | 785 Hz  |  7.35 | 0.4 dB  |
| Peaking | 6694 Hz | 11.42 | 2.2 dB  |
| Peaking | 7991 Hz |  2.29 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20660%20S/Sennheiser%20HD%20660%20S.png)