# Sony MDR-V500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 5.6; 89 5.1; 95 4.6; 102 4.1; 109 3.8; 117 3.4; 125 2.9; 134 2.5; 143 2.5; 153 3.0; 164 3.0; 175 2.6; 188 2.5; 201 2.4; 215 3.1; 230 3.6; 246 3.4; 263 3.1; 282 2.8; 301 2.1; 323 2.0; 345 2.0; 369 2.0; 395 1.9; 423 1.9; 452 1.7; 484 1.4; 518 1.1; 554 1.1; 593 1.3; 635 1.5; 679 1.0; 726 0.6; 777 0.7; 832 1.2; 890 0.6; 952 0.1; 1019 -0.1; 1090 -0.2; 1167 0.1; 1248 -0.7; 1336 -1.9; 1429 -2.4; 1529 -2.6; 1636 -2.7; 1751 -2.9; 1873 -2.8; 2004 -2.9; 2145 -2.9; 2295 -3.1; 2455 -3.0; 2627 -3.1; 2811 -3.5; 3008 -4.2; 3219 -4.4; 3444 -4.1; 3685 -3.7; 3943 -3.1; 4219 -3.0; 4514 -2.2; 4830 -1.1; 5168 0.4; 5530 1.4; 5917 0.4; 6331 -1.1; 6775 -0.1; 7249 1.1; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.3; 10167 -1.9; 10879 -1.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-V500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.29 | 5.9 dB  |
| Peaking | 75 Hz   | 1.44 | 2.2 dB  |
| Peaking | 241 Hz  | 2.13 | 2.1 dB  |
| Peaking | 535 Hz  | 0.74 | 1.4 dB  |
| Peaking | 2567 Hz | 0.89 | -4.0 dB |
| Peaking | 1498 Hz | 5.61 | -1.2 dB |
| Peaking | 2536 Hz | 2.74 | 1.6 dB  |
| Peaking | 3479 Hz | 1.78 | -1.6 dB |
| Peaking | 5480 Hz | 4.59 | 1.6 dB  |
| Peaking | 5475 Hz | 5.17 | 1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-V500/Sony%20MDR-V500.png)