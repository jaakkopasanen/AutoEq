# Sony MDR-G75

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 5.9; 42 5.7; 45 4.9; 49 3.8; 52 3.0; 56 2.0; 59 1.4; 64 0.5; 68 -0.2; 73 -0.9; 78 -1.6; 83 -2.1; 89 -2.5; 95 -2.9; 102 -3.3; 109 -3.5; 117 -3.8; 125 -3.9; 134 -3.9; 143 -4.1; 153 -4.0; 164 -4.0; 175 -3.8; 188 -3.6; 201 -3.4; 215 -3.1; 230 -2.8; 246 -2.5; 263 -2.3; 282 -2.0; 301 -1.4; 323 -0.9; 345 -0.6; 369 -0.1; 395 0.3; 423 -0.2; 452 -0.2; 484 -0.1; 518 0.0; 554 0.2; 593 0.3; 635 0.4; 679 0.4; 726 0.4; 777 0.4; 832 0.3; 890 0.2; 952 0.1; 1019 -0.1; 1090 -0.2; 1167 -0.3; 1248 -0.5; 1336 -0.9; 1429 -1.5; 1529 -2.3; 1636 -3.2; 1751 -3.6; 1873 -3.1; 2004 -1.7; 2145 -0.2; 2295 1.4; 2455 3.2; 2627 4.7; 2811 5.6; 3008 5.2; 3219 4.6; 3444 2.8; 3685 0.4; 3943 -2.1; 4219 -2.2; 4514 -0.3; 4830 3.2; 5168 5.9; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.1; 8880 -1.4; 9502 -1.4; 10167 -0.1; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-G75 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 0.71 | 7.2 dB  |
| Peaking | 123 Hz  | 0.78 | -5.2 dB |
| Peaking | 2950 Hz | 2.38 | 12.8 dB |
| Peaking | 3909 Hz | 0.72 | -9.5 dB |
| Peaking | 5613 Hz | 2    | 12.7 dB |
| Peaking | 639 Hz  | 1.39 | 0.7 dB  |
| Peaking | 1551 Hz | 0.65 | 1.2 dB  |
| Peaking | 1750 Hz | 2.86 | -3.8 dB |
| Peaking | 2396 Hz | 6.53 | 1.2 dB  |
| Peaking | 4166 Hz | 9.59 | -2.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-G75/Sony%20MDR-G75.png)