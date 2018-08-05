# Klipsch Reference ONE

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -7.5; 22 -7.8; 23 -7.9; 25 -8.1; 26 -8.2; 28 -8.3; 30 -8.4; 32 -8.5; 35 -8.5; 37 -8.5; 40 -8.5; 42 -8.5; 45 -8.4; 49 -8.3; 52 -8.3; 56 -8.3; 59 -8.2; 64 -8.1; 68 -8.0; 73 -7.8; 78 -7.7; 83 -7.6; 89 -7.7; 95 -7.7; 102 -7.6; 109 -7.5; 117 -7.2; 125 -7.1; 134 -7.4; 143 -7.7; 153 -7.8; 164 -7.4; 175 -7.0; 188 -6.9; 201 -6.3; 215 -6.2; 230 -6.1; 246 -5.8; 263 -5.5; 282 -5.0; 301 -4.4; 323 -3.7; 345 -2.9; 369 -2.1; 395 -1.2; 423 0.0; 452 1.0; 484 1.6; 518 1.9; 554 2.3; 593 2.7; 635 2.8; 679 2.7; 726 2.6; 777 2.5; 832 2.0; 890 1.2; 952 0.5; 1019 -0.2; 1090 -0.8; 1167 -0.8; 1248 -1.2; 1336 -2.4; 1429 -3.1; 1529 -4.1; 1636 -4.8; 1751 -5.2; 1873 -5.2; 2004 -5.1; 2145 -5.0; 2295 -5.0; 2455 -4.6; 2627 -4.6; 2811 -4.7; 3008 -4.3; 3219 -3.8; 3444 -2.8; 3685 -1.3; 3943 0.6; 4219 1.7; 4514 3.7; 4830 5.5; 5168 2.2; 5530 -0.3; 5917 -0.3; 6331 2.8; 6775 3.8; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.1; 10167 -0.2; 10879 -0.3; 11640 -0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch Reference ONE ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 0.28 | -8.0 dB |
| Peaking | 245 Hz  | 0.5  | -6.3 dB |
| Peaking | 586 Hz  | 0.79 | 7.1 dB  |
| Peaking | 2104 Hz | 0.82 | -6.3 dB |
| Peaking | 4706 Hz | 3.22 | 6.5 dB  |
| Peaking | 2468 Hz | 6.13 | 0.6 dB  |
| Peaking | 2154 Hz | 6.37 | 0.4 dB  |
| Peaking | 5717 Hz | 7.94 | -3.0 dB |
| Peaking | 3103 Hz | 4.72 | -1.0 dB |
| Peaking | 6659 Hz | 6.67 | 4.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Klipsch%20Reference%20ONE/Klipsch%20Reference%20ONE.png)