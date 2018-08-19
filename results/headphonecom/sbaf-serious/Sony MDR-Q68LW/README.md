# Sony MDR-Q68LW

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 5.8; 64 4.7; 68 3.8; 73 2.9; 78 2.1; 83 1.5; 89 1.0; 95 0.5; 102 0.2; 109 -0.0; 117 -0.2; 125 -0.3; 134 -0.5; 143 -0.7; 153 -0.7; 164 -0.6; 175 -0.7; 188 -0.6; 201 -0.5; 215 -0.5; 230 -0.5; 246 -0.3; 263 -0.1; 282 0.2; 301 0.3; 323 0.5; 345 0.6; 369 0.7; 395 0.8; 423 0.9; 452 0.9; 484 1.0; 518 1.1; 554 1.2; 593 1.2; 635 1.2; 679 1.1; 726 1.0; 777 0.9; 832 0.8; 890 0.5; 952 0.2; 1019 -0.0; 1090 -0.3; 1167 -0.5; 1248 -1.0; 1336 -1.8; 1429 -2.6; 1529 -3.7; 1636 -4.4; 1751 -5.0; 1873 -5.5; 2004 -5.5; 2145 -5.2; 2295 -5.3; 2455 -5.1; 2627 -4.9; 2811 -4.3; 3008 -3.2; 3219 -1.9; 3444 -1.3; 3685 -2.2; 3943 -3.8; 4219 -3.5; 4514 -1.7; 4830 1.0; 5168 3.5; 5530 5.6; 5917 5.9; 6331 4.9; 6775 2.7; 7249 -0.4; 7756 -1.7; 8299 -0.5; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 -1.1
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-Q68LW ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.2dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.86 | 7.1 dB  |
| Peaking | 760 Hz  | 1.05 | 1.8 dB  |
| Peaking | 2075 Hz | 1.2  | -6.1 dB |
| Peaking | 4159 Hz | 6.52 | -3.7 dB |
| Peaking | 5752 Hz | 3.92 | 7.4 dB  |
| Peaking | 37 Hz   | 3.17 | -1.1 dB |
| Peaking | 57 Hz   | 2.78 | 2.5 dB  |
| Peaking | 126 Hz  | 1.08 | -1.5 dB |
| Peaking | 6530 Hz | 8.88 | 1.9 dB  |
| Peaking | 7594 Hz | 6.15 | -2.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-Q68LW/Sony%20MDR-Q68LW.png)