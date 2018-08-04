# AKG K272HD

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 5.8; 52 5.5; 56 4.7; 59 4.0; 64 2.9; 68 2.3; 73 2.0; 78 2.1; 83 2.4; 89 3.2; 95 3.7; 102 3.1; 109 1.9; 117 0.5; 125 -0.6; 134 -1.3; 143 -1.8; 153 -2.2; 164 -2.0; 175 -1.6; 188 -1.1; 201 -0.7; 215 -0.7; 230 -0.8; 246 -0.8; 263 -0.9; 282 -0.9; 301 -0.8; 323 -0.8; 345 -0.9; 369 -1.2; 395 -1.4; 423 -1.4; 452 -1.5; 484 -1.6; 518 -1.8; 554 -1.8; 593 -2.1; 635 -3.1; 679 -3.1; 726 -0.4; 777 0.3; 832 0.5; 890 0.5; 952 0.3; 1019 -0.1; 1090 -0.6; 1167 -1.1; 1248 -1.5; 1336 -1.8; 1429 -2.6; 1529 -3.5; 1636 -4.1; 1751 -4.1; 1873 -3.1; 2004 -0.5; 2145 3.0; 2295 3.0; 2455 3.8; 2627 2.9; 2811 2.9; 3008 2.8; 3219 2.7; 3444 3.4; 3685 4.5; 3943 5.1; 4219 4.2; 4514 3.9; 4830 4.8; 5168 5.9; 5530 6.0; 5917 5.7; 6331 3.4; 6775 3.1; 7249 1.3; 7756 0.3; 8299 -1.4; 8880 -5.6; 9502 -6.5; 10167 -4.1; 10879 -0.8; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K272HD ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.8  | 6.9 dB  |
| Peaking | 1849 Hz | 1.74 | -9.3 dB |
| Peaking | 2192 Hz | 2.28 | 8.5 dB  |
| Peaking | 5189 Hz | 0.96 | 5.9 dB  |
| Peaking | 9348 Hz | 3.58 | -9.1 dB |
| Peaking | 99 Hz   | 4.23 | 3.2 dB  |
| Peaking | 147 Hz  | 2.11 | -2.8 dB |
| Peaking | 549 Hz  | 0.93 | -2.3 dB |
| Peaking | 659 Hz  | 5.4  | -3.8 dB |
| Peaking | 765 Hz  | 1.62 | 3.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K272HD/AKG%20K272HD.png)