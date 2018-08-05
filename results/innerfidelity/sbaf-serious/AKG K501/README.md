# AKG K501

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 5.9; 64 5.4; 68 5.2; 73 5.3; 78 5.2; 83 4.9; 89 4.1; 95 3.3; 102 2.7; 109 2.3; 117 1.9; 125 1.4; 134 1.1; 143 0.8; 153 0.6; 164 0.6; 175 0.6; 188 0.5; 201 0.5; 215 0.5; 230 0.5; 246 0.4; 263 0.4; 282 0.5; 301 0.6; 323 0.7; 345 0.8; 369 0.7; 395 0.8; 423 0.9; 452 0.9; 484 0.8; 518 0.8; 554 0.9; 593 1.1; 635 1.1; 679 1.1; 726 1.5; 777 2.1; 832 1.3; 890 0.6; 952 0.2; 1019 -0.2; 1090 -0.6; 1167 -0.9; 1248 -1.4; 1336 -1.9; 1429 -2.3; 1529 -2.6; 1636 -3.0; 1751 -3.2; 1873 -2.7; 2004 -1.8; 2145 -2.0; 2295 -1.9; 2455 -1.4; 2627 -1.6; 2811 -1.2; 3008 -1.9; 3219 -2.2; 3444 -1.9; 3685 -2.2; 3943 -1.4; 4219 -1.3; 4514 -0.7; 4830 -0.1; 5168 1.2; 5530 1.4; 5917 -1.7; 6331 -4.8; 6775 -1.9; 7249 -1.3; 7756 -1.7; 8299 -3.3; 8880 -4.0; 9502 -1.5; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -0.3; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K501 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 38 Hz   | 0.52 | 6.7 dB  |
| Peaking | 747 Hz  | 1.52 | 1.9 dB  |
| Peaking | 1638 Hz | 1.4  | -3.1 dB |
| Peaking | 3436 Hz | 3.19 | -1.8 dB |
| Peaking | 8499 Hz | 3.57 | -3.7 dB |
| Peaking | 38 Hz   | 2.81 | -0.7 dB |
| Peaking | 80 Hz   | 3.07 | 1.4 dB  |
| Peaking | 144 Hz  | 1.83 | -1.0 dB |
| Peaking | 5562 Hz | 5.32 | 2.9 dB  |
| Peaking | 6284 Hz | 8.93 | -5.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K501/AKG%20K501.png)