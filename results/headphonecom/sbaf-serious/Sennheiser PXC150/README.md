# Sennheiser PXC150

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 5.6; 59 4.8; 64 3.6; 68 2.8; 73 2.1; 78 1.6; 83 1.5; 89 2.1; 95 2.3; 102 1.8; 109 1.2; 117 0.6; 125 0.1; 134 -0.1; 143 -0.1; 153 0.0; 164 0.5; 175 1.0; 188 0.9; 201 0.9; 215 0.9; 230 1.0; 246 1.0; 263 1.3; 282 1.6; 301 1.7; 323 2.0; 345 2.2; 369 2.3; 395 2.4; 423 2.5; 452 2.6; 484 2.5; 518 2.6; 554 2.8; 593 2.7; 635 2.5; 679 2.2; 726 2.0; 777 1.8; 832 1.3; 890 0.9; 952 0.4; 1019 -0.2; 1090 -0.7; 1167 -1.3; 1248 -1.9; 1336 -2.2; 1429 -3.0; 1529 -3.9; 1636 -4.6; 1751 -5.2; 1873 -5.3; 2004 -5.4; 2145 -4.1; 2295 -3.0; 2455 -1.6; 2627 -0.3; 2811 0.7; 3008 1.9; 3219 2.9; 3444 3.9; 3685 4.9; 3943 4.5; 4219 1.3; 4514 -0.4; 4830 -0.1; 5168 1.1; 5530 3.3; 5917 5.8; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.2; 8299 -3.0; 8880 -5.8; 9502 -6.7; 10167 -6.1; 10879 -3.9; 11640 -0.4; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PXC150 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 0.58 | 6.6 dB  |
| Peaking | 1852 Hz | 2.49 | -6.2 dB |
| Peaking | 3559 Hz | 3.81 | 5.4 dB  |
| Peaking | 6258 Hz | 4.16 | 6.9 dB  |
| Peaking | 9514 Hz | 3.32 | -7.9 dB |
| Peaking | 569 Hz  | 0.76 | 1.7 dB  |
| Peaking | 136 Hz  | 2.46 | -1.6 dB |
| Peaking | 1039 Hz | 0.43 | 3.1 dB  |
| Peaking | 1267 Hz | 0.83 | -4.1 dB |
| Peaking | 4626 Hz | 7.78 | -2.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20PXC150/Sennheiser%20PXC150.png)