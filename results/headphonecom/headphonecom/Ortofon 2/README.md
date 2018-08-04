# Ortofon 2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 5.8; 35 5.1; 37 4.5; 40 3.9; 42 3.5; 45 3.0; 49 2.4; 52 2.0; 56 1.7; 59 1.6; 64 2.1; 68 2.7; 73 2.9; 78 2.6; 83 2.2; 89 2.0; 95 2.2; 102 2.3; 109 2.6; 117 2.9; 125 3.0; 134 3.0; 143 3.1; 153 3.2; 164 3.5; 175 3.7; 188 3.6; 201 3.2; 215 3.3; 230 2.8; 246 1.8; 263 1.2; 282 0.1; 301 -1.1; 323 -2.2; 345 -3.0; 369 -3.2; 395 -2.9; 423 -2.4; 452 -2.1; 484 -1.6; 518 -1.3; 554 -1.0; 593 -0.7; 635 -0.2; 679 0.0; 726 0.2; 777 0.4; 832 0.3; 890 0.2; 952 0.1; 1019 -0.0; 1090 -0.0; 1167 0.4; 1248 1.3; 1336 1.8; 1429 2.7; 1529 3.1; 1636 2.8; 1751 1.9; 1873 2.0; 2004 2.5; 2145 3.2; 2295 4.1; 2455 5.1; 2627 5.9; 2811 6.0; 3008 5.7; 3219 5.0; 3444 5.7; 3685 5.9; 3943 5.6; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.0; 9502 -1.1; 10167 -0.5; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Ortofon 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 25 Hz   | 0.93 | 6.3 dB  |
| Peaking | 223 Hz  | 0.69 | 5.5 dB  |
| Peaking | 357 Hz  | 1.29 | -7.0 dB |
| Peaking | 3078 Hz | 1.06 | 5.6 dB  |
| Peaking | 5464 Hz | 2.54 | 4.7 dB  |
| Peaking | 1122 Hz | 2.94 | -1.8 dB |
| Peaking | 1554 Hz | 1.54 | 2.7 dB  |
| Peaking | 1857 Hz | 3.28 | -2.6 dB |
| Peaking | 6439 Hz | 7.18 | 2.5 dB  |
| Peaking | 8445 Hz | 1.55 | -1.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Ortofon%202/Ortofon%202.png)