# Xiaomi Piston 2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.4dB
GraphicEQ: 10 -84; 20 -9.4; 22 -9.6; 23 -9.6; 25 -9.8; 26 -9.8; 28 -9.9; 30 -10.0; 32 -10.0; 35 -9.9; 37 -9.9; 40 -9.9; 42 -9.9; 45 -9.8; 49 -9.7; 52 -9.6; 56 -9.5; 59 -9.4; 64 -9.2; 68 -9.1; 73 -9.0; 78 -9.0; 83 -9.1; 89 -9.1; 95 -9.3; 102 -9.6; 109 -9.7; 117 -10.0; 125 -10.2; 134 -10.4; 143 -10.3; 153 -10.2; 164 -10.0; 175 -9.6; 188 -9.3; 201 -9.0; 215 -8.5; 230 -8.0; 246 -7.6; 263 -7.2; 282 -6.6; 301 -6.1; 323 -5.7; 345 -5.2; 369 -4.7; 395 -4.2; 423 -3.6; 452 -3.1; 484 -2.8; 518 -2.3; 554 -1.8; 593 -1.2; 635 -0.8; 679 -0.6; 726 -0.2; 777 0.2; 832 0.3; 890 0.2; 952 0.1; 1019 -0.1; 1090 -0.2; 1167 -0.3; 1248 -0.4; 1336 -0.8; 1429 -1.3; 1529 -1.6; 1636 -1.9; 1751 -2.0; 1873 -2.0; 2004 -1.9; 2145 -1.9; 2295 -1.9; 2455 -1.6; 2627 -1.5; 2811 -1.5; 3008 -0.9; 3219 -0.2; 3444 0.8; 3685 0.7; 3943 0.0; 4219 -1.7; 4514 -3.1; 4830 -4.0; 5168 -4.9; 5530 -5.8; 5917 -6.2; 6331 -5.3; 6775 -3.6; 7249 -2.5; 7756 -2.2; 8299 -2.9; 8880 -4.0; 9502 -4.6; 10167 -3.7; 10879 -1.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-1.4dB` and instead set Global volume in the UI for both channels to **-14**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Xiaomi Piston 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 0.24 | -9.5 dB |
| Peaking | 180 Hz   | 0.71 | -7.0 dB |
| Peaking | 1907 Hz  | 2.95 | -1.9 dB |
| Peaking | 6098 Hz  | 1.58 | -5.6 dB |
| Peaking | 24000 Hz | 2.11 | -2.6 dB |
| Peaking | 825 Hz   | 2.53 | 1.5 dB  |
| Peaking | 3689 Hz  | 2.98 | 5.0 dB  |
| Peaking | 3935 Hz  | 1.16 | -2.6 dB |
| Peaking | 7200 Hz  | 4.26 | 2.4 dB  |
| Peaking | 9502 Hz  | 5.38 | -3.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Xiaomi%20Piston%202/Xiaomi%20Piston%202.png)