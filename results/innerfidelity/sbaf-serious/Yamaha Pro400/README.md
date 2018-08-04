# Yamaha Pro400

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 2.3; 22 1.7; 23 1.4; 25 0.9; 26 0.7; 28 0.3; 30 0.1; 32 -0.1; 35 -0.4; 37 -0.5; 40 -0.6; 42 -0.7; 45 -0.7; 49 -0.8; 52 -0.9; 56 -1.0; 59 -1.0; 64 -0.5; 68 0.9; 73 2.9; 78 1.6; 83 -0.8; 89 -2.1; 95 -2.5; 102 -0.1; 109 0.0; 117 -2.5; 125 -3.9; 134 -4.6; 143 -5.0; 153 -5.0; 164 -3.2; 175 -3.7; 188 -3.5; 201 -2.1; 215 -0.3; 230 2.2; 246 4.5; 263 5.9; 282 6.0; 301 6.0; 323 6.0; 345 6.0; 369 6.0; 395 5.9; 423 5.3; 452 4.8; 484 3.7; 518 3.1; 554 2.6; 593 2.0; 635 1.3; 679 0.6; 726 0.0; 777 -0.2; 832 -0.4; 890 -0.5; 952 -0.3; 1019 0.1; 1090 0.4; 1167 0.8; 1248 1.1; 1336 1.1; 1429 1.0; 1529 0.6; 1636 0.6; 1751 1.0; 1873 1.8; 2004 2.6; 2145 3.3; 2295 4.0; 2455 4.9; 2627 5.9; 2811 6.0; 3008 6.0; 3219 6.0; 3444 5.5; 3685 4.7; 3943 4.8; 4219 5.4; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yamaha Pro400 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 2.29 | 2.3 dB  |
| Peaking | 163 Hz  | 1.55 | -7.0 dB |
| Peaking | 309 Hz  | 1.25 | 8.2 dB  |
| Peaking | 2895 Hz | 1.83 | 5.7 dB  |
| Peaking | 5308 Hz | 2.06 | 5.9 dB  |
| Peaking | 56 Hz   | 0.89 | -1.1 dB |
| Peaking | 73 Hz   | 7.46 | 4.5 dB  |
| Peaking | 447 Hz  | 4.45 | 1.3 dB  |
| Peaking | 824 Hz  | 2.8  | -1.6 dB |
| Peaking | 8355 Hz | 4.33 | -1.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Yamaha%20Pro400/Yamaha%20Pro400.png)