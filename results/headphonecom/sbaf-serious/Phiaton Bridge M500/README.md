# Phiaton Bridge M500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 5.5; 68 5.0; 73 5.1; 78 5.3; 83 5.3; 89 5.1; 95 4.4; 102 3.6; 109 3.2; 117 2.8; 125 2.6; 134 2.6; 143 2.6; 153 2.7; 164 3.2; 175 3.3; 188 3.7; 201 4.2; 215 4.6; 230 5.2; 246 5.6; 263 5.9; 282 6.0; 301 5.6; 323 5.4; 345 5.2; 369 4.8; 395 4.3; 423 3.7; 452 3.3; 484 2.7; 518 2.3; 554 2.0; 593 1.9; 635 1.6; 679 1.1; 726 0.8; 777 0.8; 832 0.6; 890 0.4; 952 0.1; 1019 0.0; 1090 0.1; 1167 0.3; 1248 0.3; 1336 0.5; 1429 0.9; 1529 1.4; 1636 1.2; 1751 0.2; 1873 0.2; 2004 1.6; 2145 3.3; 2295 4.8; 2455 5.9; 2627 6.0; 2811 6.0; 3008 5.0; 3219 3.1; 3444 2.6; 3685 2.4; 3943 3.6; 4219 5.3; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
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
| Peaking | 36 Hz   | 0.23 | 6.2 dB  |
| Peaking | 300 Hz  | 1.18 | 4.7 dB  |
| Peaking | 132 Hz  | 1.74 | -2.2 dB |
| Peaking | 2607 Hz | 3.17 | 5.9 dB  |
| Peaking | 5211 Hz | 1.98 | 6.6 dB  |
| Peaking | 1008 Hz | 3.21 | -0.7 dB |
| Peaking | 5394 Hz | 5.31 | -2.5 dB |
| Peaking | 8275 Hz | 1.26 | -1.4 dB |
| Peaking | 6432 Hz | 1.93 | 3.6 dB  |
| Peaking | 7480 Hz | 4.02 | -2.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Phiaton%20Bridge%20M500/Phiaton%20Bridge%20M500.png)