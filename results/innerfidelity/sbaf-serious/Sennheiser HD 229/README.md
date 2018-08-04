# Sennheiser HD 229

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -7.0dB
GraphicEQ: 10 -84; 20 6.5; 22 5.8; 23 5.4; 25 4.8; 26 4.5; 28 3.9; 30 3.3; 32 2.8; 35 2.2; 37 1.8; 40 1.2; 42 0.9; 45 0.5; 49 -0.0; 52 -0.4; 56 -0.8; 59 -1.0; 64 -1.4; 68 -1.6; 73 -1.9; 78 -2.1; 83 -2.4; 89 -2.8; 95 -3.2; 102 -3.5; 109 -3.7; 117 -3.8; 125 -3.9; 134 -4.0; 143 -4.0; 153 -4.4; 164 -4.4; 175 -3.8; 188 -3.6; 201 -3.1; 215 -2.7; 230 -2.6; 246 -2.8; 263 -2.4; 282 -1.6; 301 -0.7; 323 0.0; 345 0.4; 369 0.6; 395 0.8; 423 1.3; 452 1.3; 484 0.9; 518 0.9; 554 1.1; 593 1.3; 635 1.2; 679 0.9; 726 0.7; 777 0.7; 832 0.5; 890 0.4; 952 0.2; 1019 -0.0; 1090 -0.1; 1167 -0.0; 1248 0.1; 1336 0.2; 1429 0.5; 1529 1.0; 1636 -0.6; 1751 -1.5; 1873 -1.1; 2004 -0.7; 2145 -0.2; 2295 0.3; 2455 0.8; 2627 0.4; 2811 0.2; 3008 0.3; 3219 0.3; 3444 0.6; 3685 1.0; 3943 0.2; 4219 -1.0; 4514 -1.7; 4830 -0.7; 5168 1.4; 5530 3.0; 5917 4.1; 6331 4.8; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -1.8; 8880 -4.0; 9502 -3.4; 10167 -0.5; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-7.0dB` and instead set Global volume in the UI for both channels to **-70**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 229 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.79 | 6.8 dB  |
| Peaking | 165 Hz  | 0.47 | -4.9 dB |
| Peaking | 410 Hz  | 0.91 | 3.6 dB  |
| Peaking | 6311 Hz | 4.26 | 5.6 dB  |
| Peaking | 9000 Hz | 5.47 | -4.9 dB |
| Peaking | 1547 Hz | 6.92 | 1.9 dB  |
| Peaking | 1729 Hz | 4.65 | -2.2 dB |
| Peaking | 5368 Hz | 6.57 | 1.5 dB  |
| Peaking | 4509 Hz | 3.94 | -3.4 dB |
| Peaking | 3879 Hz | 1.94 | 1.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20229/Sennheiser%20HD%20229.png)