# Sony MDR-ZX700

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 5.5; 42 5.0; 45 4.2; 49 3.2; 52 2.5; 56 1.5; 59 0.8; 64 -0.1; 68 -0.5; 73 -0.5; 78 -0.1; 83 0.2; 89 0.3; 95 -0.7; 102 -1.9; 109 -2.3; 117 -2.6; 125 -2.7; 134 -2.8; 143 -2.8; 153 -2.7; 164 -1.5; 175 -1.8; 188 -2.4; 201 -2.5; 215 -2.6; 230 -2.7; 246 -2.7; 263 -2.6; 282 -2.6; 301 -3.1; 323 -3.4; 345 -4.5; 369 -3.9; 395 -3.6; 423 -3.4; 452 -3.3; 484 -3.1; 518 -2.8; 554 -2.1; 593 -1.3; 635 -0.7; 679 -0.3; 726 -0.1; 777 -0.1; 832 0.1; 890 0.1; 952 0.2; 1019 0.0; 1090 -0.1; 1167 -0.1; 1248 -0.3; 1336 -0.8; 1429 -1.5; 1529 -2.5; 1636 -3.6; 1751 -5.1; 1873 -6.0; 2004 -7.2; 2145 -7.5; 2295 -7.0; 2455 -6.0; 2627 -5.3; 2811 -4.6; 3008 -3.4; 3219 -1.8; 3444 -0.2; 3685 2.3; 3943 5.4; 4219 6.0; 4514 6.0; 4830 6.0; 5168 4.1; 5530 3.0; 5917 4.2; 6331 3.9; 6775 3.6; 7249 1.0; 7756 -4.7; 8299 -10.0; 8880 -11.3; 9502 -8.2; 10167 -3.2; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-ZX700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 29 Hz   | 1.54 | 7.3 dB   |
| Peaking | 2280 Hz | 1.54 | -8.2 dB  |
| Peaking | 6703 Hz | 1.17 | 6.9 dB   |
| Peaking | 4230 Hz | 3.34 | 6.2 dB   |
| Peaking | 8625 Hz | 3.42 | -17.1 dB |
| Peaking | 43 Hz   | 3.92 | 2.2 dB   |
| Peaking | 125 Hz  | 2.02 | -2.7 dB  |
| Peaking | 218 Hz  | 2.39 | -1.1 dB  |
| Peaking | 387 Hz  | 1.27 | -3.9 dB  |
| Peaking | 947 Hz  | 1.36 | 1.7 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-ZX700/Sony%20MDR-ZX700.png)