# Sony MDR-7505

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 5.7; 95 5.1; 102 4.5; 109 4.4; 117 4.4; 125 4.5; 134 4.1; 143 3.5; 153 2.9; 164 2.8; 175 2.8; 188 2.6; 201 2.6; 215 2.7; 230 2.6; 246 2.6; 263 2.8; 282 3.0; 301 2.7; 323 2.4; 345 2.1; 369 1.7; 395 1.6; 423 1.8; 452 1.6; 484 0.9; 518 0.5; 554 0.4; 593 0.2; 635 -0.1; 679 -0.6; 726 0.2; 777 1.5; 832 0.8; 890 0.2; 952 -0.0; 1019 -0.1; 1090 0.4; 1167 0.6; 1248 0.9; 1336 1.2; 1429 1.4; 1529 1.6; 1636 2.2; 1751 2.4; 1873 2.8; 2004 3.2; 2145 3.5; 2295 3.5; 2455 3.6; 2627 4.1; 2811 3.5; 3008 3.1; 3219 2.7; 3444 2.7; 3685 2.7; 3943 2.7; 4219 2.0; 4514 2.0; 4830 3.1; 5168 5.2; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-7505 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 0.16 | 5.8 dB  |
| Peaking | 86 Hz   | 0.74 | 2.4 dB  |
| Peaking | 291 Hz  | 1.78 | 1.9 dB  |
| Peaking | 2453 Hz | 1.28 | 3.8 dB  |
| Peaking | 5786 Hz | 3.24 | 6.2 dB  |
| Peaking | 679 Hz  | 4.25 | -2.6 dB |
| Peaking | 776 Hz  | 2.29 | 2.6 dB  |
| Peaking | 936 Hz  | 3.28 | -2.0 dB |
| Peaking | 8251 Hz | 4.59 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-7505/Sony%20MDR-7505.png)