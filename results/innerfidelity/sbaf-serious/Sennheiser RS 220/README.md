# Sennheiser RS 220

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 5.7; 30 5.4; 32 5.0; 35 4.5; 37 4.2; 40 3.8; 42 3.6; 45 3.4; 49 3.1; 52 2.9; 56 2.6; 59 2.4; 64 2.6; 68 2.8; 73 2.8; 78 2.0; 83 1.4; 89 0.9; 95 0.4; 102 -0.1; 109 -0.5; 117 -0.9; 125 -1.3; 134 -1.5; 143 -1.7; 153 -1.8; 164 -1.7; 175 -1.6; 188 -1.7; 201 -1.7; 215 -1.5; 230 -1.2; 246 -1.1; 263 -0.9; 282 -0.8; 301 -0.8; 323 -0.8; 345 -0.7; 369 -0.5; 395 -0.5; 423 -0.3; 452 -0.2; 484 -0.2; 518 0.0; 554 0.3; 593 0.5; 635 0.7; 679 0.5; 726 0.5; 777 1.0; 832 0.7; 890 0.4; 952 0.2; 1019 0.1; 1090 0.1; 1167 -0.1; 1248 -0.0; 1336 0.5; 1429 2.3; 1529 4.2; 1636 4.3; 1751 4.9; 1873 4.7; 2004 2.4; 2145 -0.5; 2295 -3.0; 2455 -4.1; 2627 -3.1; 2811 -1.8; 3008 -0.3; 3219 0.4; 3444 1.3; 3685 2.5; 3943 4.4; 4219 5.9; 4514 6.0; 4830 6.0; 5168 5.1; 5530 1.8; 5917 1.7; 6331 3.8; 6775 1.6; 7249 -0.9; 7756 -1.0; 8299 -0.9; 8880 -1.3; 9502 -2.2; 10167 -2.4; 10879 -1.2; 11640 -0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser RS 220 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 26 Hz   |  1.12 | 6.4 dB  |
| Peaking | 68 Hz   |  4.48 | 2.2 dB  |
| Peaking | 1787 Hz |  2.97 | 6.5 dB  |
| Peaking | 2428 Hz |  3.04 | -6.0 dB |
| Peaking | 4509 Hz |  2.75 | 6.9 dB  |
| Peaking | 175 Hz  |  1.2  | -2.1 dB |
| Peaking | 720 Hz  |  2.57 | 0.8 dB  |
| Peaking | 1211 Hz |  6.44 | -1.1 dB |
| Peaking | 6397 Hz | 13.39 | 3.5 dB  |
| Peaking | 9343 Hz |  2.21 | -2.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20RS%20220/Sennheiser%20RS%20220.png)