# Beyerdynamic T1 sn3964

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.4dB
GraphicEQ: 10 -84; 20 4.0; 22 3.5; 23 3.3; 25 2.9; 26 2.8; 28 2.5; 30 2.2; 32 2.0; 35 1.8; 37 1.6; 40 1.4; 42 1.3; 45 1.1; 49 1.0; 52 1.0; 56 1.1; 59 1.4; 64 1.6; 68 1.2; 73 0.5; 78 0.1; 83 -0.1; 89 -0.5; 95 -0.8; 102 -1.3; 109 -1.6; 117 -1.9; 125 -2.4; 134 -2.7; 143 -2.9; 153 -3.0; 164 -3.1; 175 -3.1; 188 -3.2; 201 -3.2; 215 -3.0; 230 -3.0; 246 -2.9; 263 -2.8; 282 -2.7; 301 -2.6; 323 -2.4; 345 -2.3; 369 -2.1; 395 -1.9; 423 -1.7; 452 -1.6; 484 -1.4; 518 -1.3; 554 -1.1; 593 -0.7; 635 -0.4; 679 -0.2; 726 0.1; 777 0.1; 832 -0.2; 890 -0.4; 952 -0.3; 1019 0.1; 1090 0.4; 1167 1.1; 1248 0.4; 1336 -0.3; 1429 0.3; 1529 0.2; 1636 -0.3; 1751 -0.5; 1873 -1.4; 2004 -1.2; 2145 -0.9; 2295 -2.1; 2455 -1.5; 2627 -1.5; 2811 -1.6; 3008 -0.4; 3219 0.5; 3444 0.8; 3685 -0.2; 3943 -1.1; 4219 -2.0; 4514 -1.9; 4830 -0.0; 5168 4.4; 5530 2.7; 5917 -2.7; 6331 -4.6; 6775 0.1; 7249 -0.8; 7756 -5.0; 8299 -8.0; 8880 -7.9; 9502 -5.1; 10167 -1.5; 10879 -0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.4dB` and instead set Global volume in the UI for both channels to **-54**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T1 sn3964 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 9 Hz     |  0.13 | 3.0 dB  |
| Peaking | 185 Hz   |  0.65 | -3.8 dB |
| Peaking | 2384 Hz  |  3.11 | -1.8 dB |
| Peaking | 5257 Hz  | 13.93 | 6.0 dB  |
| Peaking | 8561 Hz  |  4.08 | -9.0 dB |
| Peaking | 1171 Hz  |  5.57 | 1.3 dB  |
| Peaking | 3370 Hz  |  6.92 | 1.7 dB  |
| Peaking | 4932 Hz  |  0.77 | -0.4 dB |
| Peaking | 4318 Hz  |  7.64 | -1.9 dB |
| Peaking | 11059 Hz |  4.86 | 1.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T1%20sn3964/Beyerdynamic%20T1%20sn3964.png)