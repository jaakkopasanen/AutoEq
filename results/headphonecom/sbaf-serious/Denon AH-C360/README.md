# Denon AH-C360

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.7dB
GraphicEQ: 10 -84; 20 -6.6; 22 -6.9; 23 -7.0; 25 -7.2; 26 -7.3; 28 -7.5; 30 -7.7; 32 -7.8; 35 -8.0; 37 -8.1; 40 -8.3; 42 -8.3; 45 -8.4; 49 -8.7; 52 -8.8; 56 -9.0; 59 -9.1; 64 -9.3; 68 -9.5; 73 -9.7; 78 -9.9; 83 -10.0; 89 -10.2; 95 -10.2; 102 -10.3; 109 -10.3; 117 -10.3; 125 -10.3; 134 -10.4; 143 -10.3; 153 -10.3; 164 -10.2; 175 -10.0; 188 -9.8; 201 -9.5; 215 -9.2; 230 -8.9; 246 -8.6; 263 -8.3; 282 -7.8; 301 -7.4; 323 -6.7; 345 -6.3; 369 -5.8; 395 -5.4; 423 -5.1; 452 -4.7; 484 -4.2; 518 -3.6; 554 -3.0; 593 -2.4; 635 -1.6; 679 -1.1; 726 -0.7; 777 -0.2; 832 0.1; 890 0.2; 952 0.0; 1019 0.1; 1090 0.2; 1167 0.3; 1248 0.5; 1336 0.5; 1429 0.1; 1529 -0.6; 1636 -0.8; 1751 0.2; 1873 0.4; 2004 -0.1; 2145 -0.3; 2295 -0.1; 2455 0.1; 2627 0.4; 2811 0.6; 3008 0.6; 3219 0.4; 3444 0.1; 3685 -0.6; 3943 -2.1; 4219 -3.7; 4514 -5.1; 4830 -6.0; 5168 -6.4; 5530 -7.0; 5917 -8.0; 6331 -7.5; 6775 -6.1; 7249 -5.6; 7756 -6.3; 8299 -7.7; 8880 -8.1; 9502 -5.9; 10167 -1.3; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -0.1; 15258 -1.3; 16326 -0.3; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-0.7363767439604646dB` and instead set Global volume in the UI for both channels to **-7**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-C360 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -0.1dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 45 Hz    | 0.3  | -7.8 dB |
| Peaking | 155 Hz   | 0.73 | -5.6 dB |
| Peaking | 318 Hz   | 1.24 | -3.2 dB |
| Peaking | 5759 Hz  | 2.19 | -7.8 dB |
| Peaking | 8641 Hz  | 4.16 | -7.4 dB |
| Peaking | 503 Hz   | 2.88 | -1.2 dB |
| Peaking | 875 Hz   | 1.28 | 1.2 dB  |
| Peaking | 3213 Hz  | 2.4  | 1.7 dB  |
| Peaking | 4456 Hz  | 5.51 | -2.2 dB |
| Peaking | 10854 Hz | 6.16 | 1.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-C360/Denon%20AH-C360.png)