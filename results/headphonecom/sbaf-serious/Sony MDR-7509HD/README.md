# Sony MDR-7509HD

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 6.0; 95 6.0; 102 6.0; 109 6.0; 117 6.0; 125 6.0; 134 5.4; 143 4.9; 153 4.3; 164 4.1; 175 3.8; 188 3.3; 201 3.1; 215 2.9; 230 2.9; 246 3.6; 263 4.5; 282 4.2; 301 3.7; 323 3.3; 345 2.3; 369 0.6; 395 -0.9; 423 -2.1; 452 -2.4; 484 -2.3; 518 -2.6; 554 -2.8; 593 -2.1; 635 -1.0; 679 -0.4; 726 -0.5; 777 -1.0; 832 -1.4; 890 -1.1; 952 -0.4; 1019 0.2; 1090 0.3; 1167 0.3; 1248 0.3; 1336 -0.3; 1429 -2.0; 1529 -3.2; 1636 -4.7; 1751 -4.6; 1873 -5.1; 2004 -6.0; 2145 -5.4; 2295 -4.1; 2455 -2.1; 2627 0.6; 2811 2.0; 3008 3.1; 3219 4.2; 3444 5.4; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 2.0; 5917 5.5; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -3.3; 8880 -7.1; 9502 -6.8; 10167 -1.9; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-7509HD ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 52 Hz   | 0.28 | 6.6 dB  |
| Peaking | 2048 Hz | 1.6  | -8.8 dB |
| Peaking | 3751 Hz | 0.99 | 8.0 dB  |
| Peaking | 6369 Hz | 6.21 | 3.5 dB  |
| Peaking | 9091 Hz | 4.71 | -9.6 dB |
| Peaking | 20 Hz   | 2.71 | 0.7 dB  |
| Peaking | 305 Hz  | 2.29 | 3.8 dB  |
| Peaking | 460 Hz  | 1.51 | -4.4 dB |
| Peaking | 1236 Hz | 3.19 | 2.0 dB  |
| Peaking | 1580 Hz | 6.41 | -1.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sony%20MDR-7509HD/Sony%20MDR-7509HD.png)