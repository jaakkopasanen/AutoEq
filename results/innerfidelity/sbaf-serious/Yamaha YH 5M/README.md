# Yamaha YH 5M

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 6.0; 95 5.9; 102 5.3; 109 4.7; 117 4.2; 125 3.6; 134 2.9; 143 2.3; 153 2.1; 164 2.0; 175 1.7; 188 1.5; 201 1.5; 215 1.5; 230 1.5; 246 1.4; 263 1.3; 282 1.2; 301 1.2; 323 1.1; 345 1.0; 369 0.9; 395 0.8; 423 0.7; 452 0.6; 484 0.3; 518 -0.0; 554 -0.1; 593 -0.1; 635 -0.4; 679 -0.9; 726 -1.2; 777 -1.4; 832 -1.5; 890 -0.9; 952 -0.2; 1019 0.1; 1090 1.5; 1167 3.1; 1248 4.6; 1336 5.8; 1429 6.0; 1529 6.0; 1636 6.0; 1751 6.0; 1873 6.0; 2004 6.0; 2145 6.0; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 4.9; 4830 4.8; 5168 3.8; 5530 4.4; 5917 4.5; 6331 2.0; 6775 3.4; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yamaha YH 5M ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 43 Hz   | 0.35 | 6.6 dB  |
| Peaking | 877 Hz  | 1.61 | -3.3 dB |
| Peaking | 1390 Hz | 1.83 | 4.8 dB  |
| Peaking | 2369 Hz | 1.04 | 4.4 dB  |
| Peaking | 4297 Hz | 1.34 | 4.2 dB  |
| Peaking | 15 Hz   | 2.16 | 0.8 dB  |
| Peaking | 94 Hz   | 3.48 | 1.3 dB  |
| Peaking | 154 Hz  | 2.42 | -0.9 dB |
| Peaking | 6695 Hz | 2.5  | 2.6 dB  |
| Peaking | 7464 Hz | 1.57 | -2.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Yamaha%20YH%205M/Yamaha%20YH%205M.png)