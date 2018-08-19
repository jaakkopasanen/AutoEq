# Xiaomi Piston 2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.9dB
GraphicEQ: 10 -84; 20 -9.5; 22 -9.6; 23 -9.7; 25 -9.9; 26 -9.9; 28 -10.1; 30 -10.2; 32 -10.2; 35 -10.2; 37 -10.3; 40 -10.3; 42 -10.4; 45 -10.4; 49 -10.4; 52 -10.4; 56 -10.5; 59 -10.5; 64 -10.5; 68 -10.5; 73 -10.6; 78 -10.6; 83 -10.7; 89 -10.7; 95 -10.7; 102 -10.6; 109 -10.5; 117 -10.3; 125 -10.2; 134 -10.1; 143 -9.9; 153 -9.7; 164 -9.4; 175 -9.1; 188 -8.8; 201 -8.5; 215 -8.1; 230 -7.7; 246 -7.3; 263 -6.9; 282 -6.4; 301 -6.0; 323 -5.5; 345 -5.1; 369 -4.6; 395 -4.2; 423 -3.5; 452 -3.1; 484 -2.8; 518 -2.3; 554 -1.8; 593 -1.1; 635 -0.8; 679 -0.6; 726 -0.2; 777 0.2; 832 0.3; 890 0.2; 952 0.1; 1019 -0.1; 1090 -0.2; 1167 -0.3; 1248 -0.4; 1336 -0.8; 1429 -1.3; 1529 -1.6; 1636 -1.9; 1751 -2.0; 1873 -2.0; 2004 -1.9; 2145 -1.9; 2295 -1.9; 2455 -1.6; 2627 -1.5; 2811 -1.5; 3008 -0.9; 3219 -0.2; 3444 0.8; 3685 0.7; 3943 0.0; 4219 -1.7; 4514 -3.1; 4830 -4.0; 5168 -4.9; 5530 -5.8; 5917 -6.2; 6331 -5.3; 6775 -3.6; 7249 -2.5; 7756 -2.2; 8299 -2.9; 8880 -4.0; 9502 -4.6; 10167 -3.7; 10879 -1.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-0.9275059678049558dB` and instead set Global volume in the UI for both channels to **-9**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Xiaomi Piston 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -0.1dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 37 Hz    | 0.23 | -10.0 dB |
| Peaking | 180 Hz   | 0.65 | -4.7 dB  |
| Peaking | 1911 Hz  | 2.99 | -1.8 dB  |
| Peaking | 6098 Hz  | 1.58 | -5.6 dB  |
| Peaking | 24000 Hz | 2.11 | -2.6 dB  |
| Peaking | 820 Hz   | 2.4  | 1.5 dB   |
| Peaking | 3696 Hz  | 2.99 | 4.9 dB   |
| Peaking | 3927 Hz  | 1.14 | -2.6 dB  |
| Peaking | 7187 Hz  | 4.24 | 2.4 dB   |
| Peaking | 9493 Hz  | 5.38 | -3.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Xiaomi%20Piston%202/Xiaomi%20Piston%202.png)