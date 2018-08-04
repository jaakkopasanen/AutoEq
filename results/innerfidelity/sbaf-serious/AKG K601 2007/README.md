# AKG K601 2007

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 5.8; 40 5.5; 42 5.3; 45 5.0; 49 4.6; 52 4.4; 56 4.4; 59 4.7; 64 5.6; 68 5.4; 73 4.2; 78 3.6; 83 3.4; 89 3.0; 95 2.4; 102 1.8; 109 1.4; 117 0.8; 125 0.3; 134 -0.1; 143 -0.4; 153 -0.6; 164 -0.8; 175 -0.9; 188 -1.0; 201 -1.1; 215 -1.1; 230 -1.1; 246 -1.1; 263 -1.1; 282 -1.0; 301 -0.9; 323 -0.8; 345 -0.7; 369 -0.6; 395 -0.4; 423 -0.3; 452 -0.2; 484 -0.1; 518 -0.0; 554 0.3; 593 0.5; 635 0.6; 679 0.5; 726 0.6; 777 0.3; 832 0.0; 890 -0.1; 952 -0.1; 1019 -0.0; 1090 -0.1; 1167 0.1; 1248 0.2; 1336 0.0; 1429 -0.3; 1529 -0.9; 1636 -1.3; 1751 -2.1; 1873 -3.0; 2004 -3.6; 2145 -3.8; 2295 -3.1; 2455 -3.2; 2627 -3.1; 2811 -2.5; 3008 -2.0; 3219 -0.6; 3444 -0.2; 3685 -1.3; 3943 -1.6; 4219 -2.1; 4514 -2.9; 4830 -2.8; 5168 -1.5; 5530 -2.0; 5917 -4.8; 6331 -5.3; 6775 -2.6; 7249 -1.8; 7756 -2.6; 8299 -4.0; 8880 -4.8; 9502 -4.2; 10167 -3.2; 10879 -1.9; 11640 -0.2; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 -0.1
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K601 2007 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.91 | 6.5 dB  |
| Peaking | 67 Hz   | 2.34 | 3.9 dB  |
| Peaking | 2248 Hz | 1.97 | -3.7 dB |
| Peaking | 6062 Hz | 4.16 | -4.6 dB |
| Peaking | 9152 Hz | 3.21 | -4.7 dB |
| Peaking | 96 Hz   | 2.68 | 1.3 dB  |
| Peaking | 209 Hz  | 0.76 | -1.5 dB |
| Peaking | 655 Hz  | 2.03 | 0.8 dB  |
| Peaking | 3767 Hz | 0.07 | 0.2 dB  |
| Peaking | 4521 Hz | 6.92 | -2.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K601%202007/AKG%20K601%202007.png)