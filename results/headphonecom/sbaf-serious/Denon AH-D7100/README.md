# Denon AH-D7100

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 -10.7; 22 -10.8; 23 -10.8; 25 -10.8; 26 -10.7; 28 -10.7; 30 -10.6; 32 -10.5; 35 -10.3; 37 -10.2; 40 -10.0; 42 -9.8; 45 -9.6; 49 -9.3; 52 -9.1; 56 -8.4; 59 -7.8; 64 -7.4; 68 -7.5; 73 -7.8; 78 -7.9; 83 -8.2; 89 -8.8; 95 -9.3; 102 -9.3; 109 -9.0; 117 -8.7; 125 -8.5; 134 -8.1; 143 -7.7; 153 -7.2; 164 -5.6; 175 -5.4; 188 -4.9; 201 -3.5; 215 -2.0; 230 0.1; 246 2.3; 263 4.4; 282 5.9; 301 6.0; 323 6.0; 345 6.0; 369 6.0; 395 6.0; 423 5.8; 452 5.3; 484 4.5; 518 3.9; 554 3.4; 593 2.9; 635 2.1; 679 1.5; 726 1.2; 777 1.2; 832 0.9; 890 0.6; 952 0.2; 1019 0.0; 1090 -0.3; 1167 -0.5; 1248 -0.8; 1336 -1.3; 1429 -2.0; 1529 -2.8; 1636 -3.4; 1751 -3.4; 1873 -3.2; 2004 -2.7; 2145 -1.9; 2295 -0.6; 2455 1.2; 2627 2.3; 2811 2.6; 3008 2.9; 3219 3.3; 3444 5.1; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 5.9; 5917 4.1; 6331 3.4; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.8; 8880 -4.8; 9502 -3.9; 10167 -0.2; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.7; 17469 -6.0; 18692 -6.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D7100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 25 Hz    | 0.54 | -10.3 dB |
| Peaking | 136 Hz   | 0.66 | -8.9 dB  |
| Peaking | 322 Hz   | 1.18 | 10.6 dB  |
| Peaking | 4512 Hz  | 1.89 | 7.2 dB   |
| Peaking | 18237 Hz | 3.11 | -8.0 dB  |
| Peaking | 510 Hz   | 2.94 | 1.3 dB   |
| Peaking | 1841 Hz  | 1.67 | -4.9 dB  |
| Peaking | 2725 Hz  | 2.12 | 2.7 dB   |
| Peaking | 8134 Hz  | 1.14 | 1.9 dB   |
| Peaking | 9014 Hz  | 4.67 | -7.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-D7100/Denon%20AH-D7100.png)