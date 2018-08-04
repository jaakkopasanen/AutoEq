# Sennheiser HD 439

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 2.1; 22 1.8; 23 1.6; 25 1.3; 26 1.2; 28 0.9; 30 0.7; 32 0.5; 35 0.2; 37 0.1; 40 -0.1; 42 -0.2; 45 -0.3; 49 -0.5; 52 -0.5; 56 -0.6; 59 -0.6; 64 -0.6; 68 -0.4; 73 -0.3; 78 -0.6; 83 -0.9; 89 -0.8; 95 0.1; 102 1.4; 109 0.7; 117 -1.0; 125 -2.2; 134 -2.7; 143 -3.0; 153 -3.3; 164 -2.9; 175 -3.3; 188 -3.3; 201 -3.3; 215 -3.4; 230 -3.4; 246 -3.3; 263 -3.2; 282 -2.5; 301 -1.7; 323 -1.0; 345 -0.6; 369 -0.3; 395 -0.3; 423 -0.2; 452 0.2; 484 0.3; 518 0.3; 554 0.3; 593 0.5; 635 0.4; 679 0.3; 726 0.3; 777 0.3; 832 0.0; 890 -0.2; 952 -0.0; 1019 0.2; 1090 0.3; 1167 0.4; 1248 0.3; 1336 -0.7; 1429 -1.5; 1529 -1.6; 1636 -1.7; 1751 -1.2; 1873 -0.3; 2004 0.4; 2145 1.3; 2295 2.6; 2455 3.9; 2627 4.5; 2811 4.4; 3008 4.9; 3219 4.9; 3444 5.0; 3685 4.9; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 439 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.92 | 2.2 dB  |
| Peaking | 51 Hz   | 2.25 | -0.8 dB |
| Peaking | 196 Hz  | 1.4  | -3.9 dB |
| Peaking | 1626 Hz | 3.27 | -3.3 dB |
| Peaking | 4119 Hz | 0.93 | 6.5 dB  |
| Peaking | 105 Hz  | 7.91 | 2.7 dB  |
| Peaking | 132 Hz  | 4.76 | -1.2 dB |
| Peaking | 2570 Hz | 6.52 | 1.7 dB  |
| Peaking | 6192 Hz | 2.51 | 6.3 dB  |
| Peaking | 6839 Hz | 1.22 | -4.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20439/Sennheiser%20HD%20439.png)