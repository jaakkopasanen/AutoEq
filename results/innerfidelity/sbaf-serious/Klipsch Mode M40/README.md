# Klipsch Mode M40

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 4.5; 22 3.6; 23 3.3; 25 2.6; 26 2.3; 28 1.9; 30 1.5; 32 1.2; 35 0.8; 37 0.6; 40 0.4; 42 0.3; 45 0.1; 49 0.1; 52 0.1; 56 0.1; 59 0.2; 64 0.3; 68 0.4; 73 0.4; 78 0.5; 83 0.5; 89 0.4; 95 0.3; 102 0.2; 109 0.1; 117 -0.0; 125 -0.3; 134 -0.5; 143 -0.6; 153 -0.6; 164 -0.6; 175 -0.4; 188 -0.4; 201 -0.3; 215 -0.2; 230 0.0; 246 0.4; 263 0.4; 282 0.3; 301 0.6; 323 1.0; 345 1.1; 369 0.9; 395 0.9; 423 1.0; 452 1.0; 484 1.1; 518 1.1; 554 1.2; 593 1.4; 635 1.4; 679 1.2; 726 1.2; 777 1.2; 832 1.0; 890 0.7; 952 0.3; 1019 -0.0; 1090 -0.5; 1167 -1.1; 1248 -1.9; 1336 -3.0; 1429 -4.4; 1529 -5.3; 1636 -5.3; 1751 -3.8; 1873 -2.7; 2004 -0.1; 2145 2.2; 2295 3.7; 2455 5.4; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch Mode M40 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.61 | 4.3 dB  |
| Peaking | 166 Hz  | 2.12 | -0.9 dB |
| Peaking | 571 Hz  | 0.67 | 1.2 dB  |
| Peaking | 1601 Hz | 2.05 | -9.5 dB |
| Peaking | 3248 Hz | 0.7  | 7.7 dB  |
| Peaking | 85 Hz   | 3.76 | 0.5 dB  |
| Peaking | 2537 Hz | 4.24 | 2.0 dB  |
| Peaking | 3133 Hz | 1.39 | -1.3 dB |
| Peaking | 6246 Hz | 2.01 | 6.0 dB  |
| Peaking | 7404 Hz | 1.47 | -4.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Klipsch%20Mode%20M40/Klipsch%20Mode%20M40.png)