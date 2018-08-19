# Sony MDR-DS6000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 5.9; 52 5.4; 56 4.6; 59 4.1; 64 3.1; 68 2.1; 73 1.0; 78 0.2; 83 -0.5; 89 -1.2; 95 -1.7; 102 -2.1; 109 -2.5; 117 -2.7; 125 -2.8; 134 -2.8; 143 -2.7; 153 -2.7; 164 -2.4; 175 -2.0; 188 -2.3; 201 -2.0; 215 -1.2; 230 -1.6; 246 -1.5; 263 -1.3; 282 -1.1; 301 -0.8; 323 -0.7; 345 -0.5; 369 -0.4; 395 -0.3; 423 0.3; 452 0.3; 484 -0.0; 518 -0.2; 554 -0.5; 593 -0.6; 635 -0.8; 679 -1.2; 726 -1.4; 777 -1.6; 832 -1.4; 890 -0.8; 952 0.1; 1019 -0.2; 1090 -1.1; 1167 -1.8; 1248 -2.6; 1336 -2.8; 1429 -3.1; 1529 -3.7; 1636 -4.4; 1751 -4.8; 1873 -5.3; 2004 -5.7; 2145 -5.3; 2295 -4.3; 2455 -2.8; 2627 -1.1; 2811 0.4; 3008 1.6; 3219 3.0; 3444 4.2; 3685 5.9; 3943 6.0; 4219 5.1; 4514 3.8; 4830 5.5; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-DS6000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 44 Hz   | 0.41 | 8.5 dB  |
| Peaking | 106 Hz  | 0.72 | -7.5 dB |
| Peaking | 1989 Hz | 1.43 | -6.6 dB |
| Peaking | 3696 Hz | 1.94 | 6.6 dB  |
| Peaking | 5751 Hz | 3.03 | 5.6 dB  |
| Peaking | 444 Hz  | 4.83 | 0.9 dB  |
| Peaking | 795 Hz  | 2.81 | -1.3 dB |
| Peaking | 973 Hz  | 4.77 | 1.8 dB  |
| Peaking | 1249 Hz | 6.96 | -0.7 dB |
| Peaking | 8238 Hz | 4.66 | -1.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-DS6000/Sony%20MDR-DS6000.png)