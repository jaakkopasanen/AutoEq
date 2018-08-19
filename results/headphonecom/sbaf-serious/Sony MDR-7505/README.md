# Sony MDR-7505

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 6.0; 95 6.0; 102 5.9; 109 5.3; 117 4.5; 125 3.9; 134 3.3; 143 2.9; 153 2.4; 164 2.2; 175 2.0; 188 1.6; 201 1.5; 215 1.6; 230 2.2; 246 2.7; 263 2.7; 282 2.8; 301 2.4; 323 1.6; 345 0.7; 369 -0.1; 395 0.1; 423 0.4; 452 0.5; 484 0.5; 518 0.4; 554 0.4; 593 0.3; 635 0.1; 679 0.2; 726 1.0; 777 1.3; 832 1.1; 890 0.3; 952 -0.1; 1019 0.1; 1090 0.6; 1167 0.6; 1248 0.4; 1336 0.1; 1429 -0.4; 1529 -0.7; 1636 -0.3; 1751 0.1; 1873 0.4; 2004 0.7; 2145 0.9; 2295 1.1; 2455 1.2; 2627 1.9; 2811 1.7; 3008 1.1; 3219 0.7; 3444 0.6; 3685 0.7; 3943 0.6; 4219 -0.0; 4514 -0.1; 4830 0.8; 5168 2.1; 5530 2.7; 5917 1.4; 6331 0.8; 6775 3.0; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-7505 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.4dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.25 | 6.1 dB  |
| Peaking | 94 Hz   | 2.62 | 1.8 dB  |
| Peaking | 792 Hz  | 6.86 | 1.1 dB  |
| Peaking | 2656 Hz | 3.98 | 1.8 dB  |
| Peaking | 5851 Hz | 2.47 | 2.1 dB  |
| Peaking | 197 Hz  | 2.17 | -1.3 dB |
| Peaking | 242 Hz  | 2.36 | 0.5 dB  |
| Peaking | 282 Hz  | 2.54 | 1.8 dB  |
| Peaking | 370 Hz  | 4.47 | -1.4 dB |
| Peaking | 9032 Hz | 3.79 | -0.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-7505/Sony%20MDR-7505.png)