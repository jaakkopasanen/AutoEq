# Phiaton Bridge M500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 5.9; 26 5.8; 28 5.5; 30 5.1; 32 4.7; 35 4.2; 37 3.9; 40 3.5; 42 3.3; 45 3.0; 49 2.8; 52 2.8; 56 3.0; 59 2.8; 64 1.7; 68 1.2; 73 1.3; 78 1.7; 83 1.8; 89 1.9; 95 1.5; 102 1.2; 109 1.2; 117 1.2; 125 1.5; 134 1.7; 143 2.0; 153 2.3; 164 2.9; 175 3.1; 188 3.6; 201 4.1; 215 4.6; 230 5.1; 246 5.5; 263 5.9; 282 6.0; 301 5.6; 323 5.4; 345 5.2; 369 4.8; 395 4.3; 423 3.7; 452 3.3; 484 2.7; 518 2.3; 554 2.0; 593 1.9; 635 1.6; 679 1.1; 726 0.8; 777 0.8; 832 0.6; 890 0.4; 952 0.1; 1019 0.0; 1090 0.1; 1167 0.3; 1248 0.3; 1336 0.5; 1429 0.9; 1529 1.4; 1636 1.2; 1751 0.2; 1873 0.2; 2004 1.6; 2145 3.3; 2295 4.8; 2455 5.9; 2627 6.0; 2811 6.0; 3008 5.0; 3219 3.1; 3444 2.6; 3685 2.4; 3943 3.6; 4219 5.3; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
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
| Peaking | 23 Hz   | 0.87 | 6.0 dB  |
| Peaking | 53 Hz   | 2.2  | 0.9 dB  |
| Peaking | 284 Hz  | 1.05 | 6.0 dB  |
| Peaking | 2607 Hz | 3.18 | 5.9 dB  |
| Peaking | 5211 Hz | 1.98 | 6.6 dB  |
| Peaking | 1007 Hz | 3.18 | -0.7 dB |
| Peaking | 5381 Hz | 5.39 | -2.4 dB |
| Peaking | 8382 Hz | 1.3  | -1.4 dB |
| Peaking | 6447 Hz | 1.94 | 3.5 dB  |
| Peaking | 7488 Hz | 4.04 | -2.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Phiaton%20Bridge%20M500/Phiaton%20Bridge%20M500.png)