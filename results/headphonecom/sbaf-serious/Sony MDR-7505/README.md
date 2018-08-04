# Sony MDR-7505

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 5.6; 68 5.1; 73 4.5; 78 4.1; 83 3.9; 89 4.8; 95 5.1; 102 4.2; 109 3.7; 117 3.2; 125 2.7; 134 2.4; 143 2.1; 153 1.8; 164 1.7; 175 1.6; 188 1.3; 201 1.2; 215 1.4; 230 2.0; 246 2.6; 263 2.6; 282 2.8; 301 2.4; 323 1.5; 345 0.7; 369 -0.1; 395 0.1; 423 0.5; 452 0.6; 484 0.4; 518 0.3; 554 0.3; 593 0.4; 635 0.1; 679 0.1; 726 0.9; 777 1.3; 832 1.1; 890 0.2; 952 -0.1; 1019 0.2; 1090 0.6; 1167 0.6; 1248 0.4; 1336 0.0; 1429 -0.4; 1529 -0.7; 1636 -0.3; 1751 0.0; 1873 0.4; 2004 0.7; 2145 0.8; 2295 1.1; 2455 1.3; 2627 1.9; 2811 1.6; 3008 1.2; 3219 0.7; 3444 0.5; 3685 0.6; 3943 0.8; 4219 -0.0; 4514 -0.2; 4830 0.7; 5168 2.2; 5530 2.8; 5917 1.3; 6331 0.7; 6775 3.0; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
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
| Peaking | 25 Hz   | 0.41 | 5.6 dB  |
| Peaking | 76 Hz   | 0.74 | 2.5 dB  |
| Peaking | 272 Hz  | 3.89 | 2.4 dB  |
| Peaking | 2643 Hz | 3.6  | 1.8 dB  |
| Peaking | 5884 Hz | 2.41 | 2.0 dB  |
| Peaking | 83 Hz   | 5.08 | -1.3 dB |
| Peaking | 94 Hz   | 5.83 | 1.4 dB  |
| Peaking | 789 Hz  | 8.88 | 1.4 dB  |
| Peaking | 1494 Hz | 4.8  | -1.6 dB |
| Peaking | 1360 Hz | 2.38 | 0.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-7505/Sony%20MDR-7505.png)