# Westone UM3X RC

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 2.5; 22 2.1; 23 2.0; 25 1.7; 26 1.6; 28 1.4; 30 1.2; 32 1.0; 35 0.9; 37 0.8; 40 0.6; 42 0.6; 45 0.4; 49 0.3; 52 0.2; 56 0.1; 59 -0.0; 64 -0.1; 68 -0.2; 73 -0.2; 78 -0.5; 83 -0.8; 89 -1.1; 95 -1.5; 102 -2.0; 109 -2.5; 117 -3.0; 125 -3.6; 134 -3.9; 143 -4.2; 153 -4.5; 164 -4.6; 175 -4.7; 188 -4.6; 201 -4.6; 215 -4.4; 230 -4.3; 246 -4.2; 263 -4.0; 282 -3.9; 301 -3.7; 323 -3.4; 345 -3.0; 369 -2.8; 395 -2.5; 423 -2.1; 452 -1.9; 484 -1.7; 518 -1.4; 554 -1.0; 593 -0.5; 635 -0.3; 679 -0.2; 726 0.1; 777 0.5; 832 0.4; 890 0.3; 952 0.2; 1019 0.0; 1090 -0.2; 1167 -0.4; 1248 -0.6; 1336 -1.0; 1429 -1.3; 1529 -1.6; 1636 -1.7; 1751 -1.3; 1873 -0.4; 2004 0.6; 2145 1.8; 2295 3.3; 2455 5.1; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -1.0; 9502 -3.2; 10167 -2.3; 10879 -0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone UM3X RC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 0.11 | 1.8 dB  |
| Peaking | 190 Hz   | 0.58 | -5.7 dB |
| Peaking | 1648 Hz  | 1.47 | -6.9 dB |
| Peaking | 3403 Hz  | 0.41 | 7.9 dB  |
| Peaking | 9307 Hz  | 1.98 | -5.9 dB |
| Peaking | 15 Hz    | 1.84 | 0.8 dB  |
| Peaking | 2604 Hz  | 5.94 | 1.7 dB  |
| Peaking | 3810 Hz  | 0.86 | -0.7 dB |
| Peaking | 6068 Hz  | 4.96 | 1.8 dB  |
| Peaking | 15349 Hz | 1.89 | -0.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Westone%20UM3X%20RC/Westone%20UM3X%20RC.png)