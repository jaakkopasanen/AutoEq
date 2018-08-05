# AKG K550

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.5dB
GraphicEQ: 10 -84; 20 -0.7; 22 -1.0; 23 -1.0; 25 -1.2; 26 -1.3; 28 -1.4; 30 -1.4; 32 -1.5; 35 -1.5; 37 -1.5; 40 -1.3; 42 -1.2; 45 -1.0; 49 -0.8; 52 -0.7; 56 -0.5; 59 -0.3; 64 0.2; 68 0.8; 73 1.3; 78 1.6; 83 1.6; 89 1.1; 95 0.1; 102 -1.0; 109 -1.8; 117 -2.4; 125 -2.8; 134 -2.8; 143 -2.7; 153 -2.2; 164 -0.5; 175 -1.4; 188 -2.0; 201 -1.7; 215 -1.5; 230 -1.3; 246 -1.2; 263 -1.2; 282 -0.9; 301 -0.9; 323 -0.9; 345 -0.8; 369 -0.6; 395 -0.5; 423 -0.2; 452 0.1; 484 0.1; 518 0.3; 554 0.7; 593 1.0; 635 1.2; 679 1.3; 726 1.5; 777 1.7; 832 1.2; 890 0.6; 952 0.3; 1019 -0.1; 1090 -0.6; 1167 -1.0; 1248 -1.4; 1336 -1.7; 1429 -1.8; 1529 -1.9; 1636 -1.8; 1751 -1.3; 1873 -0.7; 2004 -0.3; 2145 -0.1; 2295 -0.0; 2455 0.3; 2627 0.6; 2811 1.0; 3008 1.8; 3219 2.6; 3444 3.3; 3685 3.8; 3943 3.8; 4219 3.6; 4514 3.5; 4830 3.3; 5168 1.1; 5530 -0.5; 5917 -0.7; 6331 -0.2; 6775 1.4; 7249 1.5; 7756 -1.3; 8299 -4.9; 8880 -7.1; 9502 -5.8; 10167 -1.8; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -0.4; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.5dB` and instead set Global volume in the UI for both channels to **-45**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K550 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 130 Hz  | 3.88 | -3.0 dB |
| Peaking | 214 Hz  | 2.1  | -1.5 dB |
| Peaking | 1527 Hz | 2.94 | -2.3 dB |
| Peaking | 3940 Hz | 2.08 | 4.3 dB  |
| Peaking | 8968 Hz | 5.28 | -8.2 dB |
| Peaking | 36 Hz   | 0.42 | -1.4 dB |
| Peaking | 78 Hz   | 2.71 | 3.0 dB  |
| Peaking | 720 Hz  | 2.9  | 1.8 dB  |
| Peaking | 5774 Hz | 7.4  | -1.9 dB |
| Peaking | 7088 Hz | 9.49 | 2.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K550/AKG%20K550.png)