# Phiaton Bridge M500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 5.9; 25 5.6; 26 5.4; 28 5.0; 30 4.6; 32 4.2; 35 3.6; 37 3.3; 40 2.9; 42 2.7; 45 2.4; 49 2.2; 52 2.2; 56 2.4; 59 2.2; 64 1.1; 68 0.6; 73 0.7; 78 1.0; 83 1.1; 89 1.1; 95 0.7; 102 0.2; 109 0.0; 117 -0.0; 125 0.2; 134 0.4; 143 0.7; 153 1.0; 164 1.6; 175 1.8; 188 2.2; 201 2.7; 215 3.2; 230 3.7; 246 4.1; 263 4.6; 282 4.6; 301 4.3; 323 4.0; 345 3.8; 369 3.5; 395 3.0; 423 2.5; 452 2.3; 484 2.0; 518 1.8; 554 1.6; 593 1.4; 635 1.2; 679 1.0; 726 0.8; 777 0.7; 832 0.5; 890 0.4; 952 0.1; 1019 0.0; 1090 0.2; 1167 0.6; 1248 0.9; 1336 1.9; 1429 3.1; 1529 4.1; 1636 4.2; 1751 3.3; 1873 3.1; 2004 4.5; 2145 5.9; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 5.3; 3444 4.7; 3685 4.5; 3943 5.6; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton Bridge M500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.88 | 6.0 dB  |
| Peaking | 290 Hz  | 1.33 | 4.6 dB  |
| Peaking | 1558 Hz | 5.07 | 2.3 dB  |
| Peaking | 2576 Hz | 1.53 | 5.7 dB  |
| Peaking | 5157 Hz | 1.84 | 5.9 dB  |
| Peaking | 117 Hz  | 3.69 | -1.0 dB |
| Peaking | 1044 Hz | 2.64 | -1.2 dB |
| Peaking | 1442 Hz | 0.2  | 0.3 dB  |
| Peaking | 6470 Hz | 4.85 | 3.6 dB  |
| Peaking | 7292 Hz | 1.59 | -2.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Phiaton%20Bridge%20M500/Phiaton%20Bridge%20M500.png)