# Westone UM3X RC

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 3.2; 22 2.8; 23 2.7; 25 2.4; 26 2.2; 28 2.0; 30 1.8; 32 1.6; 35 1.4; 37 1.2; 40 1.0; 42 0.9; 45 0.7; 49 0.4; 52 0.3; 56 0.0; 59 -0.2; 64 -0.5; 68 -0.7; 73 -1.0; 78 -1.3; 83 -1.6; 89 -1.9; 95 -2.2; 102 -2.5; 109 -2.6; 117 -2.8; 125 -3.1; 134 -3.2; 143 -3.3; 153 -3.5; 164 -3.6; 175 -3.5; 188 -3.7; 201 -3.6; 215 -3.6; 230 -3.5; 246 -3.5; 263 -3.4; 282 -3.2; 301 -3.1; 323 -3.0; 345 -2.7; 369 -2.6; 395 -2.4; 423 -2.0; 452 -1.7; 484 -1.5; 518 -1.3; 554 -0.9; 593 -0.4; 635 -0.2; 679 -0.1; 726 0.1; 777 0.4; 832 0.4; 890 0.3; 952 0.2; 1019 0.0; 1090 -0.1; 1167 -0.3; 1248 -0.5; 1336 -0.9; 1429 -1.2; 1529 -1.4; 1636 -1.4; 1751 -1.0; 1873 -0.2; 2004 1.0; 2145 2.3; 2295 3.7; 2455 5.5; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.6; 10167 -0.4; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999993319dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone UM3X RC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 12 Hz    | 0.31 | 3.4 dB  |
| Peaking | 196 Hz   | 0.45 | -4.0 dB |
| Peaking | 1625 Hz  | 1.46 | -6.9 dB |
| Peaking | 3478 Hz  | 0.38 | 8.1 dB  |
| Peaking | 9131 Hz  | 1.27 | -4.6 dB |
| Peaking | 2562 Hz  | 6.36 | 1.6 dB  |
| Peaking | 4675 Hz  | 0.98 | -1.7 dB |
| Peaking | 6691 Hz  | 1.52 | 4.0 dB  |
| Peaking | 7455 Hz  | 3.83 | -4.0 dB |
| Peaking | 14955 Hz | 1.14 | -0.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Westone%20UM3X%20RC/Westone%20UM3X%20RC.png)