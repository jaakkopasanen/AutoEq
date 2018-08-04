# Bose AE2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -3.8; 22 -3.9; 23 -3.9; 25 -3.9; 26 -3.9; 28 -3.9; 30 -3.9; 32 -3.8; 35 -3.6; 37 -3.5; 40 -3.3; 42 -3.2; 45 -3.0; 49 -2.6; 52 -2.3; 56 -1.9; 59 -1.6; 64 -1.2; 68 -0.9; 73 -0.4; 78 -0.1; 83 0.1; 89 0.4; 95 0.4; 102 0.5; 109 0.6; 117 0.5; 125 0.1; 134 -0.6; 143 -1.5; 153 -2.1; 164 -0.3; 175 -0.2; 188 -1.0; 201 -0.7; 215 -0.7; 230 0.1; 246 1.1; 263 2.2; 282 2.3; 301 2.3; 323 2.8; 345 3.3; 369 3.7; 395 3.9; 423 4.2; 452 4.2; 484 3.9; 518 3.7; 554 3.5; 593 3.3; 635 2.9; 679 2.2; 726 1.7; 777 1.1; 832 0.5; 890 0.1; 952 0.0; 1019 0.3; 1090 0.7; 1167 1.2; 1248 1.8; 1336 2.1; 1429 2.4; 1529 2.6; 1636 2.9; 1751 3.2; 1873 3.4; 2004 3.5; 2145 4.3; 2295 4.2; 2455 3.8; 2627 3.4; 2811 2.0; 3008 1.3; 3219 1.0; 3444 1.0; 3685 1.3; 3943 1.0; 4219 0.7; 4514 1.8; 4830 4.3; 5168 6.0; 5530 6.0; 5917 3.7; 6331 2.2; 6775 0.4; 7249 -0.5; 7756 0.1; 8299 -0.2; 8880 -1.3; 9502 -0.9; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose AE2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.96 | -4.4 dB |
| Peaking | 187 Hz  | 2.32 | -1.7 dB |
| Peaking | 420 Hz  | 1.16 | 4.4 dB  |
| Peaking | 2112 Hz | 1.79 | 4.1 dB  |
| Peaking | 5336 Hz | 4.87 | 6.5 dB  |
| Peaking | 107 Hz  | 2.13 | 1.1 dB  |
| Peaking | 148 Hz  | 9.24 | -2.0 dB |
| Peaking | 934 Hz  | 4.58 | -1.4 dB |
| Peaking | 1386 Hz | 4.27 | 0.9 dB  |
| Peaking | 8974 Hz | 5.63 | -1.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bose%20AE2/Bose%20AE2.png)