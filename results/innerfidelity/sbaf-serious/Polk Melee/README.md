# Polk Melee

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -1.0; 22 -1.4; 23 -1.5; 25 -1.8; 26 -2.0; 28 -2.2; 30 -2.3; 32 -2.4; 35 -2.6; 37 -2.6; 40 -2.7; 42 -2.7; 45 -2.8; 49 -2.8; 52 -2.8; 56 -2.8; 59 -2.7; 64 -2.6; 68 -2.5; 73 -2.3; 78 -2.2; 83 -2.5; 89 -3.3; 95 -3.9; 102 -3.8; 109 -3.6; 117 -3.7; 125 -4.4; 134 -5.3; 143 -5.9; 153 -5.8; 164 -4.7; 175 -5.3; 188 -5.7; 201 -5.6; 215 -5.3; 230 -5.0; 246 -4.7; 263 -4.2; 282 -3.6; 301 -3.3; 323 -3.2; 345 -3.2; 369 -3.0; 395 -2.6; 423 -2.1; 452 -1.8; 484 -1.7; 518 -1.5; 554 -1.1; 593 -0.8; 635 -0.6; 679 -0.6; 726 -0.6; 777 -0.4; 832 -0.3; 890 -0.3; 952 -0.1; 1019 0.0; 1090 0.3; 1167 0.6; 1248 0.9; 1336 1.0; 1429 1.1; 1529 1.4; 1636 2.0; 1751 2.9; 1873 4.1; 2004 5.1; 2145 5.9; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 5.6; 3685 4.7; 3943 3.5; 4219 3.3; 4514 3.2; 4830 4.3; 5168 5.7; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Polk Melee ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 4 Hz    | 1.38 | -0.3 dB |
| Peaking | 37 Hz   | 0.97 | -2.2 dB |
| Peaking | 182 Hz  | 0.64 | -5.4 dB |
| Peaking | 2650 Hz | 1.25 | 6.6 dB  |
| Peaking | 5749 Hz | 3.23 | 5.6 dB  |
| Peaking | 2175 Hz | 1.39 | -2.1 dB |
| Peaking | 2076 Hz | 3.19 | 3.0 dB  |
| Peaking | 3390 Hz | 5.15 | 1.5 dB  |
| Peaking | 6634 Hz | 7.69 | 2.1 dB  |
| Peaking | 7877 Hz | 2.27 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Polk%20Melee/Polk%20Melee.png)