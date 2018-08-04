# Denon AH-D1001

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 5.9; 49 5.6; 52 5.4; 56 5.3; 59 5.3; 64 5.2; 68 4.9; 73 4.6; 78 4.2; 83 3.8; 89 3.3; 95 2.9; 102 2.5; 109 2.1; 117 1.8; 125 1.3; 134 1.0; 143 0.9; 153 0.8; 164 0.8; 175 0.9; 188 1.0; 201 1.1; 215 1.4; 230 1.6; 246 1.9; 263 2.2; 282 2.6; 301 2.9; 323 3.1; 345 3.4; 369 3.6; 395 3.7; 423 4.1; 452 4.2; 484 4.1; 518 3.9; 554 3.8; 593 3.4; 635 2.7; 679 1.7; 726 0.9; 777 0.5; 832 0.1; 890 -0.2; 952 0.0; 1019 0.1; 1090 0.5; 1167 0.8; 1248 1.2; 1336 1.3; 1429 1.4; 1529 1.6; 1636 1.9; 1751 2.5; 1873 3.3; 2004 4.0; 2145 4.2; 2295 4.1; 2455 3.6; 2627 2.7; 2811 2.3; 3008 4.3; 3219 4.8; 3444 2.9; 3685 1.4; 3943 0.9; 4219 -0.3; 4514 -0.5; 4830 0.8; 5168 3.0; 5530 4.1; 5917 4.7; 6331 3.5; 6775 3.8; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.9; 9502 -2.2; 10167 -1.7; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D1001 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 34 Hz   | 0.5  | 6.5 dB  |
| Peaking | 438 Hz  | 1.43 | 4.3 dB  |
| Peaking | 2118 Hz | 2.56 | 4.2 dB  |
| Peaking | 3183 Hz | 6.04 | 4.0 dB  |
| Peaking | 5941 Hz | 4.23 | 4.9 dB  |
| Peaking | 148 Hz  | 2.26 | -1.2 dB |
| Peaking | 856 Hz  | 0.05 | 0.3 dB  |
| Peaking | 888 Hz  | 3.19 | -1.6 dB |
| Peaking | 4406 Hz | 6.79 | -2.1 dB |
| Peaking | 9645 Hz | 5.07 | -2.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-D1001/Denon%20AH-D1001.png)