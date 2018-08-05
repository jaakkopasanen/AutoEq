# Sennheiser IE 800

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 0.4; 22 0.1; 23 -0.0; 25 -0.3; 26 -0.4; 28 -0.5; 30 -0.7; 32 -0.8; 35 -0.9; 37 -1.0; 40 -1.1; 42 -1.2; 45 -1.2; 49 -1.3; 52 -1.3; 56 -1.3; 59 -1.3; 64 -1.4; 68 -1.4; 73 -1.5; 78 -1.6; 83 -1.7; 89 -2.0; 95 -2.3; 102 -2.7; 109 -3.1; 117 -3.5; 125 -3.9; 134 -4.2; 143 -4.4; 153 -4.5; 164 -4.4; 175 -4.3; 188 -4.1; 201 -4.0; 215 -3.7; 230 -3.4; 246 -3.2; 263 -3.0; 282 -2.7; 301 -2.4; 323 -2.2; 345 -1.9; 369 -1.7; 395 -1.4; 423 -1.0; 452 -0.8; 484 -0.7; 518 -0.5; 554 -0.1; 593 0.3; 635 0.4; 679 0.4; 726 0.5; 777 0.7; 832 0.6; 890 0.4; 952 0.2; 1019 -0.0; 1090 -0.2; 1167 -0.3; 1248 -0.5; 1336 -0.6; 1429 -0.7; 1529 -0.9; 1636 -0.8; 1751 -0.3; 1873 0.4; 2004 1.3; 2145 2.4; 2295 3.6; 2455 5.2; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 5.4; 4830 4.2; 5168 3.4; 5530 2.2; 5917 2.2; 6331 4.8; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -1.5; 9502 -3.5; 10167 -4.5; 10879 -4.0; 11640 -1.9; 12455 -0.1; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE 800 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 41 Hz    | 1.75 | -0.8 dB |
| Peaking | 165 Hz   | 0.82 | -4.5 dB |
| Peaking | 2703 Hz  | 3.7  | 4.0 dB  |
| Peaking | 4098 Hz  | 1.27 | 5.7 dB  |
| Peaking | 10220 Hz | 3.69 | -5.7 dB |
| Peaking | 743 Hz   | 2.28 | 1.1 dB  |
| Peaking | 1649 Hz  | 1.65 | -2.9 dB |
| Peaking | 2085 Hz  | 1.27 | 1.7 dB  |
| Peaking | 5960 Hz  | 2.86 | -2.2 dB |
| Peaking | 6448 Hz  | 6.82 | 5.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20IE%20800/Sennheiser%20IE%20800.png)