# Sennheiser PXC300

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 5.5; 68 4.9; 73 4.6; 78 4.9; 83 5.0; 89 4.1; 95 3.4; 102 2.8; 109 2.5; 117 2.4; 125 2.2; 134 2.0; 143 1.6; 153 1.5; 164 1.6; 175 1.6; 188 1.7; 201 2.1; 215 2.2; 230 2.2; 246 2.2; 263 2.0; 282 2.1; 301 2.2; 323 2.3; 345 2.5; 369 2.8; 395 2.9; 423 2.7; 452 2.8; 484 2.8; 518 3.0; 554 3.0; 593 2.9; 635 2.9; 679 2.7; 726 2.3; 777 2.0; 832 1.4; 890 1.0; 952 0.4; 1019 -0.2; 1090 -0.8; 1167 -1.3; 1248 -1.7; 1336 -2.1; 1429 -2.4; 1529 -2.6; 1636 -2.6; 1751 -2.5; 1873 -1.7; 2004 -1.7; 2145 -2.5; 2295 -2.7; 2455 -2.5; 2627 -1.8; 2811 -0.9; 3008 -0.1; 3219 0.5; 3444 1.0; 3685 1.3; 3943 1.5; 4219 1.1; 4514 -1.0; 4830 -2.4; 5168 -1.2; 5530 0.5; 5917 1.0; 6331 -0.6; 6775 -3.3; 7249 -3.4; 7756 -2.4; 8299 -2.2; 8880 -4.0; 9502 -7.0; 10167 -8.2; 10879 -4.8; 11640 -0.2; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PXC300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 36 Hz    | 0.45 | 6.5 dB  |
| Peaking | 547 Hz   | 0.69 | 3.1 dB  |
| Peaking | 1410 Hz  | 1.6  | -3.5 dB |
| Peaking | 2330 Hz  | 4.73 | -2.3 dB |
| Peaking | 9861 Hz  | 3.75 | -8.5 dB |
| Peaking | 82 Hz    | 7.96 | 0.8 dB  |
| Peaking | 4831 Hz  | 4.99 | -7.3 dB |
| Peaking | 4876 Hz  | 1.97 | 5.0 dB  |
| Peaking | 7012 Hz  | 5.76 | -4.0 dB |
| Peaking | 11948 Hz | 7.2  | 1.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20PXC300/Sennheiser%20PXC300.png)