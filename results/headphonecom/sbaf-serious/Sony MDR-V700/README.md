# Sony MDR-V700

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 5.7; 68 4.7; 73 3.6; 78 2.6; 83 1.8; 89 1.0; 95 0.5; 102 0.4; 109 0.4; 117 0.3; 125 0.4; 134 0.5; 143 0.6; 153 0.8; 164 1.2; 175 1.5; 188 1.7; 201 1.9; 215 2.1; 230 2.4; 246 2.9; 263 3.3; 282 3.6; 301 3.8; 323 3.9; 345 3.8; 369 3.7; 395 4.8; 423 5.0; 452 4.0; 484 2.8; 518 1.2; 554 -0.1; 593 -0.7; 635 -0.7; 679 -0.4; 726 0.1; 777 1.1; 832 -0.4; 890 -0.8; 952 -0.5; 1019 0.2; 1090 0.9; 1167 1.2; 1248 0.7; 1336 -0.2; 1429 -1.5; 1529 -2.4; 1636 -3.2; 1751 -3.7; 1873 -3.4; 2004 -4.0; 2145 -4.7; 2295 -5.0; 2455 -4.6; 2627 -4.2; 2811 -3.4; 3008 -2.1; 3219 -1.0; 3444 0.0; 3685 1.3; 3943 2.9; 4219 4.1; 4514 5.7; 4830 6.0; 5168 6.0; 5530 5.2; 5917 4.8; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.4; 8880 -3.2; 9502 -4.3; 10167 -1.4; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-V700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.74 | 7.0 dB  |
| Peaking | 351 Hz  | 1.56 | 4.6 dB  |
| Peaking | 2400 Hz | 1.38 | -6.4 dB |
| Peaking | 5065 Hz | 1.29 | 7.4 dB  |
| Peaking | 9218 Hz | 4.15 | -5.8 dB |
| Peaking | 63 Hz   | 2.17 | 4.1 dB  |
| Peaking | 88 Hz   | 0.71 | -2.7 dB |
| Peaking | 187 Hz  | 0.92 | 1.3 dB  |
| Peaking | 603 Hz  | 5.51 | -2.0 dB |
| Peaking | 1173 Hz | 6.68 | 2.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-V700/Sony%20MDR-V700.png)