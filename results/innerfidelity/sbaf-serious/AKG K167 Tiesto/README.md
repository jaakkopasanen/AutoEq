# AKG K167 Tiesto

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 5.9; 25 5.7; 26 5.5; 28 5.2; 30 4.9; 32 4.7; 35 4.5; 37 4.5; 40 4.4; 42 4.4; 45 4.5; 49 4.6; 52 4.8; 56 5.1; 59 5.4; 64 5.9; 68 6.0; 73 6.0; 78 6.0; 83 5.8; 89 5.6; 95 5.5; 102 5.2; 109 4.9; 117 4.7; 125 4.3; 134 4.1; 143 4.0; 153 4.1; 164 4.7; 175 4.3; 188 3.7; 201 3.6; 215 3.8; 230 3.9; 246 3.9; 263 4.0; 282 4.0; 301 3.5; 323 3.0; 345 2.8; 369 2.5; 395 2.3; 423 2.2; 452 2.2; 484 1.9; 518 1.6; 554 1.6; 593 1.6; 635 1.4; 679 1.1; 726 1.0; 777 0.9; 832 0.5; 890 0.3; 952 0.2; 1019 -0.1; 1090 -0.4; 1167 -0.9; 1248 -0.9; 1336 -0.7; 1429 -1.8; 1529 -2.3; 1636 -3.1; 1751 -3.2; 1873 -3.1; 2004 -2.0; 2145 -0.0; 2295 0.9; 2455 1.6; 2627 2.3; 2811 2.9; 3008 3.7; 3219 3.7; 3444 3.6; 3685 3.2; 3943 3.1; 4219 2.9; 4514 3.1; 4830 4.9; 5168 6.0; 5530 5.6; 5917 3.1; 6331 2.6; 6775 3.5; 7249 1.3; 7756 0.3; 8299 -0.4; 8880 -2.5; 9502 -2.6; 10167 -1.0; 10879 -0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K167 Tiesto ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 12 Hz    | 1.72 | 5.8 dB  |
| Peaking | 22 Hz    | 1.04 | 4.1 dB  |
| Peaking | 76 Hz    | 0.7  | 5.2 dB  |
| Peaking | 264 Hz   | 0.93 | 3.0 dB  |
| Peaking | 4915 Hz  | 1.79 | 5.3 dB  |
| Peaking | 1772 Hz  | 1.7  | -6.6 dB |
| Peaking | 2708 Hz  | 0.7  | 4.1 dB  |
| Peaking | 4328 Hz  | 3.75 | -3.7 dB |
| Peaking | 24002 Hz | 0.45 | 0.3 dB  |
| Peaking | 9151 Hz  | 3.93 | -4.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K167%20Tiesto/AKG%20K167%20Tiesto.png)