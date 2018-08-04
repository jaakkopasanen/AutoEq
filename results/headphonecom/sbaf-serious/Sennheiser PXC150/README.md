# Sennheiser PXC150

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 5.5; 49 4.1; 52 3.0; 56 1.7; 59 0.9; 64 -0.2; 68 -1.0; 73 -1.6; 78 -2.0; 83 -2.0; 89 -1.1; 95 -0.6; 102 -0.7; 109 -0.8; 117 -1.0; 125 -1.1; 134 -0.9; 143 -0.7; 153 -0.4; 164 0.2; 175 0.8; 188 0.8; 201 0.8; 215 0.9; 230 0.9; 246 1.0; 263 1.3; 282 1.6; 301 1.7; 323 2.0; 345 2.2; 369 2.3; 395 2.4; 423 2.5; 452 2.6; 484 2.5; 518 2.6; 554 2.8; 593 2.7; 635 2.5; 679 2.2; 726 2.0; 777 1.8; 832 1.3; 890 0.9; 952 0.4; 1019 -0.2; 1090 -0.7; 1167 -1.3; 1248 -1.9; 1336 -2.2; 1429 -3.0; 1529 -3.9; 1636 -4.6; 1751 -5.2; 1873 -5.3; 2004 -5.4; 2145 -4.1; 2295 -3.0; 2455 -1.6; 2627 -0.3; 2811 0.7; 3008 1.9; 3219 2.9; 3444 3.9; 3685 4.9; 3943 4.5; 4219 1.3; 4514 -0.4; 4830 -0.1; 5168 1.1; 5530 3.3; 5917 5.8; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.2; 8299 -3.0; 8880 -5.8; 9502 -6.7; 10167 -6.1; 10879 -3.9; 11640 -0.4; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PXC150 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 1.35 | 7.3 dB  |
| Peaking | 1852 Hz | 2.5  | -6.2 dB |
| Peaking | 3559 Hz | 3.82 | 5.4 dB  |
| Peaking | 6258 Hz | 4.16 | 6.9 dB  |
| Peaking | 9514 Hz | 3.32 | -7.9 dB |
| Peaking | 45 Hz   | 3.59 | 2.8 dB  |
| Peaking | 77 Hz   | 2.52 | -3.0 dB |
| Peaking | 128 Hz  | 3.7  | -1.3 dB |
| Peaking | 471 Hz  | 0.98 | 3.0 dB  |
| Peaking | 4641 Hz | 9.02 | -2.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20PXC150/Sennheiser%20PXC150.png)