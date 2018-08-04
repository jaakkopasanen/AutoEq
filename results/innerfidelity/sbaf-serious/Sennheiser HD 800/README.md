# Sennheiser HD 800

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.1dB
GraphicEQ: 10 -84; 20 3.6; 22 3.2; 23 3.1; 25 2.8; 26 2.7; 28 2.4; 30 2.2; 32 2.1; 35 1.9; 37 1.8; 40 1.7; 42 1.7; 45 1.7; 49 1.8; 52 2.0; 56 2.3; 59 2.3; 64 1.9; 68 1.4; 73 0.8; 78 0.4; 83 0.1; 89 -0.2; 95 -0.6; 102 -1.0; 109 -1.3; 117 -1.7; 125 -2.2; 134 -2.4; 143 -2.6; 153 -2.9; 164 -2.8; 175 -3.0; 188 -3.0; 201 -3.1; 215 -3.0; 230 -2.9; 246 -3.0; 263 -2.9; 282 -2.7; 301 -2.7; 323 -2.6; 345 -2.4; 369 -2.3; 395 -2.2; 423 -2.0; 452 -1.8; 484 -1.8; 518 -1.7; 554 -1.5; 593 -1.2; 635 -1.1; 679 -1.1; 726 -1.0; 777 -0.5; 832 -0.5; 890 -0.4; 952 -0.1; 1019 0.1; 1090 0.5; 1167 0.9; 1248 1.4; 1336 1.5; 1429 1.5; 1529 1.6; 1636 1.4; 1751 1.2; 1873 1.2; 2004 1.6; 2145 1.6; 2295 1.5; 2455 2.1; 2627 2.6; 2811 2.2; 3008 2.0; 3219 2.2; 3444 2.0; 3685 0.9; 3943 -0.1; 4219 -1.7; 4514 -2.6; 4830 -2.6; 5168 -2.9; 5530 -3.9; 5917 -4.0; 6331 -4.9; 6775 -4.3; 7249 -3.0; 7756 -1.3; 8299 -0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 -0.7
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.1dB` and instead set Global volume in the UI for both channels to **-41**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 800 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 19 Hz    | 0.94 | 3.5 dB  |
| Peaking | 62 Hz    | 1.02 | 3.4 dB  |
| Peaking | 181 Hz   | 0.35 | -3.4 dB |
| Peaking | 4061 Hz  | 0.43 | 4.2 dB  |
| Peaking | 5731 Hz  | 1.26 | -8.4 dB |
| Peaking | 1989 Hz  | 2.4  | -1.9 dB |
| Peaking | 2033 Hz  | 1.29 | 1.3 dB  |
| Peaking | 6764 Hz  | 7.08 | -1.3 dB |
| Peaking | 13479 Hz | 0.86 | -0.3 dB |
| Peaking | 8325 Hz  | 3.93 | 1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20800/Sennheiser%20HD%20800.png)