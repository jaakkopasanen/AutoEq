# Westone UM3X RC

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 3.2; 22 2.9; 23 2.7; 25 2.5; 26 2.4; 28 2.2; 30 2.0; 32 1.9; 35 1.7; 37 1.6; 40 1.4; 42 1.4; 45 1.3; 49 1.2; 52 1.1; 56 1.0; 59 0.9; 64 0.8; 68 0.7; 73 0.5; 78 0.3; 83 0.0; 89 -0.4; 95 -0.8; 102 -1.4; 109 -1.9; 117 -2.5; 125 -3.1; 134 -3.4; 143 -3.7; 153 -4.0; 164 -4.2; 175 -4.1; 188 -4.2; 201 -4.1; 215 -4.0; 230 -3.8; 246 -3.8; 263 -3.6; 282 -3.4; 301 -3.3; 323 -3.1; 345 -2.8; 369 -2.7; 395 -2.4; 423 -2.0; 452 -1.7; 484 -1.6; 518 -1.3; 554 -0.9; 593 -0.4; 635 -0.2; 679 -0.1; 726 0.1; 777 0.4; 832 0.4; 890 0.3; 952 0.2; 1019 0.0; 1090 -0.1; 1167 -0.3; 1248 -0.5; 1336 -0.9; 1429 -1.2; 1529 -1.4; 1636 -1.4; 1751 -1.0; 1873 -0.2; 2004 1.0; 2145 2.3; 2295 3.7; 2455 5.5; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.6; 10167 -0.4; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone UM3X RC ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 13 Hz   | 0.42 | 3.5 dB  |
| Peaking | 78 Hz   | 1.22 | 1.9 dB  |
| Peaking | 180 Hz  | 0.6  | -4.7 dB |
| Peaking | 1654 Hz | 2.27 | -4.4 dB |
| Peaking | 3473 Hz | 0.75 | 7.1 dB  |
| Peaking | 757 Hz  | 3.37 | 0.8 dB  |
| Peaking | 2578 Hz | 4.69 | 2.1 dB  |
| Peaking | 3142 Hz | 1.15 | -1.1 dB |
| Peaking | 6149 Hz | 2.12 | 5.4 dB  |
| Peaking | 7593 Hz | 1.35 | -4.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Westone%20UM3X%20RC/Westone%20UM3X%20RC.png)