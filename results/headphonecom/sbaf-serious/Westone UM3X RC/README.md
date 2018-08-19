# Westone UM3X RC

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 2.4; 22 2.1; 23 1.9; 25 1.6; 26 1.5; 28 1.2; 30 1.0; 32 0.8; 35 0.6; 37 0.4; 40 0.2; 42 0.1; 45 -0.1; 49 -0.4; 52 -0.6; 56 -0.9; 59 -1.1; 64 -1.4; 68 -1.6; 73 -1.8; 78 -2.1; 83 -2.4; 89 -2.7; 95 -2.9; 102 -3.1; 109 -3.2; 117 -3.4; 125 -3.6; 134 -3.7; 143 -3.8; 153 -4.0; 164 -4.1; 175 -4.2; 188 -4.1; 201 -4.1; 215 -4.0; 230 -4.0; 246 -4.0; 263 -3.8; 282 -3.7; 301 -3.5; 323 -3.2; 345 -2.9; 369 -2.7; 395 -2.4; 423 -2.1; 452 -1.9; 484 -1.6; 518 -1.3; 554 -0.9; 593 -0.6; 635 -0.3; 679 -0.1; 726 0.2; 777 0.4; 832 0.4; 890 0.3; 952 0.2; 1019 0.0; 1090 -0.2; 1167 -0.4; 1248 -0.6; 1336 -0.9; 1429 -1.3; 1529 -1.6; 1636 -1.7; 1751 -1.2; 1873 -0.5; 2004 0.6; 2145 1.8; 2295 3.4; 2455 5.1; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.9; 9502 -3.4; 10167 -2.5; 10879 -0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999984679dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone UM3X RC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 15 Hz    | 0.53 | 2.8 dB  |
| Peaking | 193 Hz   | 0.43 | -4.4 dB |
| Peaking | 1648 Hz  | 1.32 | -7.9 dB |
| Peaking | 3075 Hz  | 0.38 | 8.4 dB  |
| Peaking | 9479 Hz  | 2.04 | -6.0 dB |
| Peaking | 2610 Hz  | 6.57 | 1.5 dB  |
| Peaking | 5906 Hz  | 0.69 | -1.1 dB |
| Peaking | 5916 Hz  | 3.58 | 2.4 dB  |
| Peaking | 10956 Hz | 6.38 | 1.7 dB  |
| Peaking | 15417 Hz | 1.26 | -0.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Westone%20UM3X%20RC/Westone%20UM3X%20RC.png)