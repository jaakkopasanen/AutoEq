# Phiaton Bridge M500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 5.1; 68 4.4; 73 4.4; 78 4.5; 83 4.5; 89 4.2; 95 3.7; 102 3.1; 109 2.8; 117 2.6; 125 2.6; 134 2.7; 143 2.8; 153 3.0; 164 3.4; 175 3.5; 188 3.9; 201 4.4; 215 4.8; 230 5.2; 246 5.7; 263 6.0; 282 6.0; 301 5.7; 323 5.5; 345 5.2; 369 4.9; 395 4.3; 423 3.7; 452 3.2; 484 2.8; 518 2.4; 554 2.1; 593 1.8; 635 1.5; 679 1.2; 726 0.9; 777 0.7; 832 0.6; 890 0.4; 952 0.1; 1019 0.0; 1090 0.1; 1167 0.3; 1248 0.3; 1336 0.5; 1429 0.9; 1529 1.4; 1636 1.2; 1751 0.2; 1873 0.2; 2004 1.6; 2145 3.3; 2295 4.8; 2455 5.9; 2627 6.0; 2811 6.0; 3008 4.9; 3219 3.1; 3444 2.7; 3685 2.5; 3943 3.4; 4219 5.3; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.3; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton Bridge M500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 0.29 | 6.2 dB  |
| Peaking | 121 Hz  | 1.87 | -1.5 dB |
| Peaking | 294 Hz  | 1.11 | 5.3 dB  |
| Peaking | 2607 Hz | 3.16 | 5.9 dB  |
| Peaking | 5216 Hz | 2    | 6.6 dB  |
| Peaking | 1008 Hz | 3.32 | -0.7 dB |
| Peaking | 5380 Hz | 5.47 | -2.4 dB |
| Peaking | 6496 Hz | 1.95 | 3.5 dB  |
| Peaking | 7439 Hz | 4.52 | -2.3 dB |
| Peaking | 8412 Hz | 1.47 | -1.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Phiaton%20Bridge%20M500/Phiaton%20Bridge%20M500.png)