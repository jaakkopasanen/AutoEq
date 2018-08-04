# Sennheiser PXC300

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 5.8; 49 5.1; 52 4.3; 56 3.5; 59 2.9; 64 2.2; 68 1.6; 73 1.5; 78 2.1; 83 2.3; 89 1.7; 95 1.2; 102 0.9; 109 0.9; 117 1.0; 125 1.0; 134 1.0; 143 0.9; 153 0.9; 164 1.0; 175 1.2; 188 1.4; 201 1.8; 215 2.0; 230 2.1; 246 2.1; 263 1.9; 282 2.0; 301 2.1; 323 2.3; 345 2.5; 369 2.8; 395 2.8; 423 2.8; 452 2.8; 484 2.8; 518 2.8; 554 3.0; 593 3.0; 635 3.0; 679 2.6; 726 2.3; 777 2.0; 832 1.5; 890 1.0; 952 0.4; 1019 -0.2; 1090 -0.8; 1167 -1.3; 1248 -1.7; 1336 -2.2; 1429 -2.4; 1529 -2.5; 1636 -2.6; 1751 -2.6; 1873 -1.6; 2004 -1.7; 2145 -2.5; 2295 -2.7; 2455 -2.5; 2627 -1.8; 2811 -1.0; 3008 0.0; 3219 0.5; 3444 0.9; 3685 1.2; 3943 1.7; 4219 1.1; 4514 -1.1; 4830 -2.4; 5168 -1.1; 5530 0.6; 5917 1.0; 6331 -0.6; 6775 -3.2; 7249 -3.3; 7756 -2.4; 8299 -2.4; 8880 -4.1; 9502 -6.8; 10167 -8.0; 10879 -5.0; 11640 -0.2; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PXC300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 31 Hz    | 0.79 | 6.7 dB  |
| Peaking | 879 Hz   | 0.37 | 4.7 dB  |
| Peaking | 1369 Hz  | 1.01 | -6.5 dB |
| Peaking | 2373 Hz  | 4.13 | -2.7 dB |
| Peaking | 9862 Hz  | 3.32 | -8.2 dB |
| Peaking | 115 Hz   | 2.25 | -0.5 dB |
| Peaking | 4921 Hz  | 2.01 | 3.9 dB  |
| Peaking | 6992 Hz  | 5.92 | -3.8 dB |
| Peaking | 4840 Hz  | 5.31 | -6.6 dB |
| Peaking | 11996 Hz | 6.61 | 2.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20PXC300/Sennheiser%20PXC300.png)