# Torque t103z Reference

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 5.9; 52 5.7; 56 5.2; 59 4.9; 64 4.5; 68 4.1; 73 3.7; 78 3.2; 83 2.6; 89 1.9; 95 1.1; 102 0.2; 109 -0.6; 117 -1.5; 125 -2.4; 134 -3.2; 143 -3.9; 153 -4.5; 164 -5.1; 175 -5.6; 188 -6.1; 201 -6.5; 215 -6.8; 230 -7.2; 246 -7.5; 263 -7.7; 282 -7.8; 301 -7.8; 323 -7.7; 345 -7.4; 369 -7.1; 395 -6.6; 423 -5.8; 452 -5.2; 484 -4.6; 518 -4.0; 554 -3.2; 593 -2.4; 635 -2.0; 679 -1.0; 726 -0.2; 777 -0.0; 832 0.3; 890 0.0; 952 0.1; 1019 0.0; 1090 -0.1; 1167 -0.3; 1248 -0.4; 1336 -0.8; 1429 -1.2; 1529 -1.7; 1636 -2.1; 1751 -2.4; 1873 -2.5; 2004 -2.4; 2145 -2.0; 2295 -0.9; 2455 1.0; 2627 3.0; 2811 5.1; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t103z Reference ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 38 Hz   | 0.44 | 7.0 dB   |
| Peaking | 251 Hz  | 0.67 | -9.0 dB  |
| Peaking | 2043 Hz | 1.52 | -10.3 dB |
| Peaking | 2935 Hz | 0.66 | 10.0 dB  |
| Peaking | 408 Hz  | 3.01 | -1.0 dB  |
| Peaking | 773 Hz  | 2.85 | 1.6 dB   |
| Peaking | 1455 Hz | 5.09 | -0.9 dB  |
| Peaking | 6167 Hz | 2.24 | 5.9 dB   |
| Peaking | 7349 Hz | 1.31 | -4.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t103z%20Reference/Torque%20t103z%20Reference.png)