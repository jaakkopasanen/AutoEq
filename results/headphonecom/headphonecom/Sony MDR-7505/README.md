# Sony MDR-7505

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 5.8; 64 5.0; 68 4.5; 73 3.9; 78 3.4; 83 3.2; 89 4.0; 95 4.2; 102 3.2; 109 2.6; 117 1.9; 125 1.5; 134 1.1; 143 0.8; 153 0.5; 164 0.4; 175 0.2; 188 -0.1; 201 -0.1; 215 -0.0; 230 0.6; 246 1.2; 263 1.3; 282 1.4; 301 1.0; 323 0.2; 345 -0.7; 369 -1.5; 395 -1.2; 423 -0.8; 452 -0.5; 484 -0.3; 518 -0.2; 554 -0.1; 593 -0.1; 635 -0.2; 679 0.0; 726 0.9; 777 1.2; 832 1.0; 890 0.2; 952 -0.2; 1019 0.2; 1090 0.7; 1167 0.9; 1248 1.0; 1336 1.4; 1429 1.7; 1529 2.0; 1636 2.7; 1751 3.1; 1873 3.3; 2004 3.6; 2145 3.9; 2295 4.1; 2455 4.2; 2627 4.9; 2811 4.6; 3008 3.7; 3219 3.0; 3444 2.6; 3685 2.7; 3943 3.1; 4219 3.6; 4514 4.6; 4830 5.9; 5168 6.0; 5530 6.0; 5917 4.8; 6331 3.0; 6775 3.7; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-7505 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.61 | 5.3 dB  |
| Peaking | 57 Hz   | 0.91 | 3.7 dB  |
| Peaking | 12 Hz   | 1.9  | 0.2 dB  |
| Peaking | 2376 Hz | 1.3  | 4.3 dB  |
| Peaking | 5270 Hz | 2.6  | 5.9 dB  |
| Peaking | 96 Hz   | 6.51 | 1.7 dB  |
| Peaking | 213 Hz  | 1.48 | -1.7 dB |
| Peaking | 275 Hz  | 1.98 | 2.7 dB  |
| Peaking | 370 Hz  | 2.86 | -2.3 dB |
| Peaking | 8525 Hz | 4.29 | -0.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Sony%20MDR-7505/Sony%20MDR-7505.png)