# Yamaha Pro500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 5.9; 26 5.8; 28 5.5; 30 5.1; 32 4.8; 35 4.4; 37 4.2; 40 4.0; 42 3.8; 45 3.5; 49 3.2; 52 3.0; 56 2.8; 59 2.7; 64 2.6; 68 2.9; 73 3.5; 78 2.9; 83 2.1; 89 1.5; 95 1.7; 102 1.5; 109 0.4; 117 -0.3; 125 -0.9; 134 -1.4; 143 -1.8; 153 -2.0; 164 -1.8; 175 -1.9; 188 -2.2; 201 -2.3; 215 -2.2; 230 -1.9; 246 -1.4; 263 -0.9; 282 -0.3; 301 0.2; 323 1.3; 345 2.3; 369 3.1; 395 3.7; 423 4.6; 452 4.7; 484 4.2; 518 4.1; 554 3.9; 593 3.3; 635 2.9; 679 2.3; 726 1.8; 777 1.4; 832 0.8; 890 0.5; 952 0.7; 1019 0.0; 1090 -0.2; 1167 -0.3; 1248 -0.4; 1336 -0.9; 1429 -1.4; 1529 -1.6; 1636 -1.6; 1751 -1.1; 1873 -0.1; 2004 0.9; 2145 1.7; 2295 2.8; 2455 4.0; 2627 5.2; 2811 5.9; 3008 6.0; 3219 5.2; 3444 3.6; 3685 3.5; 3943 4.4; 4219 4.9; 4514 5.9; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yamaha Pro500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 1.01 | 6.1 dB  |
| Peaking | 72 Hz   | 3.99 | 2.6 dB  |
| Peaking | 481 Hz  | 2.38 | 5.1 dB  |
| Peaking | 2867 Hz | 3.41 | 5.7 dB  |
| Peaking | 5205 Hz | 1.96 | 6.6 dB  |
| Peaking | 196 Hz  | 1.53 | -2.9 dB |
| Peaking | 367 Hz  | 4.52 | 1.8 dB  |
| Peaking | 661 Hz  | 4.52 | 1.2 dB  |
| Peaking | 1543 Hz | 3.55 | -2.5 dB |
| Peaking | 8352 Hz | 4.61 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Yamaha%20Pro500/Yamaha%20Pro500.png)