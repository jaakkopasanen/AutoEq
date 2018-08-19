# Beyerdynamic Custom One Pro linear bass position

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -0.2; 22 -0.6; 23 -0.8; 25 -1.2; 26 -1.4; 28 -1.7; 30 -1.9; 32 -2.1; 35 -2.4; 37 -2.4; 40 -2.5; 42 -2.5; 45 -2.4; 49 -1.9; 52 -1.4; 56 -0.8; 59 -0.2; 64 1.5; 68 1.7; 73 -0.4; 78 1.4; 83 4.8; 89 4.7; 95 2.3; 102 0.3; 109 -0.4; 117 -0.8; 125 -1.2; 134 -1.4; 143 -1.5; 153 -1.4; 164 -1.4; 175 -3.6; 188 -4.4; 201 -4.4; 215 -4.4; 230 -4.2; 246 -4.4; 263 -4.4; 282 -4.2; 301 -3.9; 323 -3.6; 345 -3.3; 369 -3.1; 395 -2.8; 423 -2.7; 452 -2.5; 484 -2.3; 518 -2.0; 554 -1.9; 593 -1.5; 635 -1.3; 679 -1.4; 726 -1.1; 777 -0.3; 832 -0.1; 890 -0.3; 952 -0.1; 1019 0.0; 1090 -0.1; 1167 0.0; 1248 -0.2; 1336 -0.6; 1429 -1.1; 1529 -2.0; 1636 -2.7; 1751 -3.4; 1873 -4.0; 2004 -4.8; 2145 -5.1; 2295 -4.7; 2455 -3.6; 2627 -2.2; 2811 -0.9; 3008 0.1; 3219 0.9; 3444 1.4; 3685 1.8; 3943 2.0; 4219 3.6; 4514 5.2; 4830 5.9; 5168 6.0; 5530 6.0; 5917 5.8; 6331 3.7; 6775 3.4; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.8; 9502 -0.8; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099566618642662dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic Custom One Pro linear bass position ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 38 Hz   |  1.84 | -2.7 dB |
| Peaking | 87 Hz   |  5.19 | 6.3 dB  |
| Peaking | 256 Hz  |  0.9  | -4.6 dB |
| Peaking | 2113 Hz |  2.5  | -5.7 dB |
| Peaking | 5134 Hz |  2.09 | 6.9 dB  |
| Peaking | 159 Hz  | 10.98 | 1.2 dB  |
| Peaking | 928 Hz  |  0.88 | -1.4 dB |
| Peaking | 988 Hz  |  1.55 | 2.1 dB  |
| Peaking | 6235 Hz |  4.8  | 1.1 dB  |
| Peaking | 8827 Hz |  2.8  | -1.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Beyerdynamic%20Custom%20One%20Pro%20linear%20bass%20position/Beyerdynamic%20Custom%20One%20Pro%20linear%20bass%20position.png)