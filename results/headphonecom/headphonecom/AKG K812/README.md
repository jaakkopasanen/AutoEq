# AKG K812

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -5.1; 22 -5.5; 23 -5.6; 25 -5.9; 26 -6.0; 28 -6.2; 30 -6.4; 32 -6.5; 35 -6.7; 37 -6.8; 40 -6.9; 42 -7.0; 45 -7.1; 49 -7.1; 52 -7.1; 56 -7.1; 59 -7.2; 64 -7.4; 68 -7.4; 73 -7.2; 78 -7.1; 83 -7.1; 89 -7.1; 95 -7.1; 102 -7.1; 109 -7.3; 117 -7.3; 125 -7.3; 134 -7.3; 143 -7.3; 153 -7.3; 164 -7.1; 175 -7.0; 188 -7.0; 201 -6.9; 215 -6.9; 230 -6.8; 246 -6.6; 263 -6.5; 282 -6.3; 301 -6.1; 323 -6.0; 345 -5.7; 369 -5.4; 395 -5.2; 423 -4.8; 452 -4.5; 484 -4.1; 518 -3.6; 554 -3.3; 593 -2.9; 635 -2.4; 679 -2.0; 726 -1.5; 777 -1.1; 832 -0.7; 890 -0.6; 952 -0.3; 1019 0.0; 1090 0.5; 1167 1.3; 1248 1.9; 1336 2.5; 1429 2.2; 1529 1.7; 1636 2.1; 1751 3.2; 1873 3.3; 2004 3.2; 2145 3.1; 2295 2.8; 2455 4.7; 2627 6.0; 2811 5.0; 3008 2.0; 3219 1.5; 3444 1.4; 3685 -0.4; 3943 -0.7; 4219 4.4; 4514 6.0; 4830 5.3; 5168 2.7; 5530 -0.6; 5917 -4.2; 6331 -4.8; 6775 0.0; 7249 1.2; 7756 0.3; 8299 -0.7; 8880 -2.5; 9502 -3.6; 10167 -2.2; 10879 -0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 -0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K812 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 62 Hz   |  0.21 | -7.0 dB  |
| Peaking | 335 Hz  |  0.66 | -2.8 dB  |
| Peaking | 2867 Hz |  0.81 | 12.3 dB  |
| Peaking | 4575 Hz |  4.05 | 12.6 dB  |
| Peaking | 4001 Hz |  0.91 | -13.7 dB |
| Peaking | 1311 Hz |  7.6  | 1.1 dB   |
| Peaking | 2234 Hz | 10.45 | -1.6 dB  |
| Peaking | 6176 Hz |  6.57 | -7.8 dB  |
| Peaking | 6858 Hz |  2.18 | 4.6 dB   |
| Peaking | 9352 Hz |  5.57 | -3.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/AKG%20K812/AKG%20K812.png)