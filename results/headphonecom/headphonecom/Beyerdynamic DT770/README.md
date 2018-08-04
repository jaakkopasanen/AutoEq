# Beyerdynamic DT770

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -5.6; 22 -6.1; 23 -6.3; 25 -6.6; 26 -6.8; 28 -7.0; 30 -7.1; 32 -7.2; 35 -7.3; 37 -7.2; 40 -6.9; 42 -6.5; 45 -5.7; 49 -5.2; 52 -5.2; 56 -4.0; 59 -1.8; 64 0.4; 68 -1.5; 73 -4.6; 78 -6.1; 83 -6.9; 89 -7.3; 95 -7.5; 102 -7.6; 109 -7.5; 117 -7.2; 125 -6.7; 134 -5.8; 143 -4.8; 153 -3.5; 164 -2.8; 175 -2.6; 188 -1.6; 201 -1.0; 215 -0.7; 230 -0.8; 246 -0.9; 263 -1.3; 282 -1.5; 301 -1.6; 323 -1.7; 345 -1.7; 369 -1.8; 395 -1.8; 423 -1.7; 452 -1.6; 484 -1.4; 518 -1.4; 554 -1.3; 593 -1.2; 635 -1.1; 679 -1.1; 726 -1.0; 777 -1.0; 832 -0.7; 890 -0.5; 952 0.1; 1019 0.0; 1090 0.2; 1167 0.6; 1248 1.1; 1336 1.9; 1429 2.6; 1529 2.9; 1636 2.7; 1751 2.3; 1873 2.1; 2004 2.2; 2145 2.5; 2295 3.2; 2455 4.0; 2627 4.7; 2811 5.2; 3008 5.5; 3219 5.5; 3444 6.0; 3685 6.0; 3943 6.0; 4219 5.8; 4514 3.6; 4830 2.4; 5168 3.4; 5530 3.4; 5917 -0.4; 6331 -4.0; 6775 -3.5; 7249 -2.7; 7756 -3.5; 8299 -5.1; 8880 -6.0; 9502 -4.7; 10167 -1.7; 10879 -0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -0.7; 20000 -2.3
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT770 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 30 Hz    | 1.13 | -7.6 dB |
| Peaking | 107 Hz   | 1.45 | -7.4 dB |
| Peaking | 4070 Hz  | 1.93 | 3.1 dB  |
| Peaking | 3049 Hz  | 1.04 | 4.5 dB  |
| Peaking | 8132 Hz  | 1.87 | -6.1 dB |
| Peaking | 60 Hz    | 1.89 | -2.8 dB |
| Peaking | 63 Hz    | 5.9  | 8.0 dB  |
| Peaking | 529 Hz   | 1.03 | -1.6 dB |
| Peaking | 1470 Hz  | 5.11 | 2.0 dB  |
| Peaking | 11162 Hz | 5.93 | 1.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Beyerdynamic%20DT770/Beyerdynamic%20DT770.png)