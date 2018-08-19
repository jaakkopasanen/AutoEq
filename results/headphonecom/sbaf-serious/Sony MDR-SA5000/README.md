# Sony MDR-SA5000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 5.7; 83 5.0; 89 4.5; 95 4.3; 102 4.0; 109 4.0; 117 4.0; 125 4.0; 134 4.1; 143 4.1; 153 4.2; 164 4.5; 175 4.6; 188 4.7; 201 4.8; 215 5.0; 230 4.9; 246 5.1; 263 5.2; 282 5.4; 301 5.6; 323 5.6; 345 4.5; 369 4.6; 395 4.7; 423 4.6; 452 4.4; 484 4.1; 518 3.6; 554 3.1; 593 2.6; 635 2.2; 679 1.8; 726 1.4; 777 0.9; 832 0.4; 890 -0.0; 952 -0.3; 1019 0.2; 1090 1.4; 1167 2.8; 1248 3.8; 1336 4.3; 1429 4.4; 1529 4.1; 1636 3.8; 1751 2.9; 1873 2.1; 2004 1.2; 2145 0.6; 2295 -0.4; 2455 -3.0; 2627 -5.8; 2811 -6.9; 3008 -5.0; 3219 -3.2; 3444 -1.3; 3685 2.1; 3943 1.5; 4219 -1.9; 4514 -1.6; 4830 1.7; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 2.5; 7249 -1.0; 7756 -3.2; 8299 -4.0; 8880 -4.5; 9502 -4.4; 10167 -1.9; 10879 -0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 -2.6
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-SA5000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 27 Hz   |  0.08 | 5.3 dB  |
| Peaking | 1135 Hz |  0.22 | 2.0 dB  |
| Peaking | 2804 Hz |  4    | -9.2 dB |
| Peaking | 5914 Hz |  3.53 | 7.3 dB  |
| Peaking | 8535 Hz |  2.6  | -6.1 dB |
| Peaking | 124 Hz  |  2.05 | -1.5 dB |
| Peaking | 356 Hz  |  1.06 | 1.3 dB  |
| Peaking | 969 Hz  |  1.55 | -4.4 dB |
| Peaking | 1335 Hz |  1.97 | 4.5 dB  |
| Peaking | 4445 Hz | 10.64 | -3.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-SA5000/Sony%20MDR-SA5000.png)