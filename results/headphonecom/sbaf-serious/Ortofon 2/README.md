# Ortofon 2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 5.6; 37 5.1; 40 4.5; 42 4.1; 45 3.6; 49 2.9; 52 2.6; 56 2.3; 59 2.2; 64 2.7; 68 3.3; 73 3.5; 78 3.2; 83 2.9; 89 2.8; 95 3.0; 102 3.3; 109 3.8; 117 4.2; 125 4.3; 134 4.3; 143 4.4; 153 4.5; 164 4.9; 175 5.1; 188 5.0; 201 4.6; 215 4.7; 230 4.2; 246 3.2; 263 2.6; 282 1.4; 301 0.3; 323 -0.8; 345 -1.6; 369 -1.8; 395 -1.7; 423 -1.2; 452 -1.0; 484 -0.9; 518 -0.8; 554 -0.5; 593 -0.2; 635 0.1; 679 0.1; 726 0.2; 777 0.5; 832 0.4; 890 0.2; 952 0.1; 1019 -0.0; 1090 -0.1; 1167 0.1; 1248 0.6; 1336 0.4; 1429 0.5; 1529 0.4; 1636 -0.2; 1751 -1.2; 1873 -0.9; 2004 -0.5; 2145 0.2; 2295 1.0; 2455 2.1; 2627 3.0; 2811 3.6; 3008 3.3; 3219 2.6; 3444 3.6; 3685 4.1; 3943 3.3; 4219 4.8; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -1.2; 9502 -3.7; 10167 -4.0; 10879 -2.4; 11640 -0.2; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ortofon 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 14 Hz   | 0.3  | 6.6 dB  |
| Peaking | 167 Hz  | 1.53 | 4.9 dB  |
| Peaking | 6001 Hz | 3.47 | 3.4 dB  |
| Peaking | 4505 Hz | 1.29 | 5.0 dB  |
| Peaking | 9842 Hz | 3.62 | -5.2 dB |
| Peaking | 54 Hz   | 5.23 | -1.0 dB |
| Peaking | 239 Hz  | 3.21 | 2.0 dB  |
| Peaking | 366 Hz  | 2.12 | -2.8 dB |
| Peaking | 1862 Hz | 4.78 | -1.9 dB |
| Peaking | 2727 Hz | 5.96 | 2.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Ortofon%202/Ortofon%202.png)