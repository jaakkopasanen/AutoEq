# Sennheiser PXC150

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 5.3; 59 4.4; 64 3.1; 68 2.2; 73 1.4; 78 0.9; 83 0.7; 89 1.3; 95 1.5; 102 1.2; 109 0.8; 117 0.3; 125 0.1; 134 0.1; 143 0.1; 153 0.2; 164 0.7; 175 1.2; 188 1.1; 201 1.1; 215 1.1; 230 1.1; 246 1.1; 263 1.4; 282 1.6; 301 1.7; 323 2.0; 345 2.2; 369 2.3; 395 2.4; 423 2.5; 452 2.5; 484 2.6; 518 2.7; 554 2.8; 593 2.6; 635 2.4; 679 2.3; 726 2.1; 777 1.7; 832 1.3; 890 0.9; 952 0.4; 1019 -0.2; 1090 -0.7; 1167 -1.2; 1248 -1.9; 1336 -2.1; 1429 -3.0; 1529 -3.9; 1636 -4.6; 1751 -5.1; 1873 -5.4; 2004 -5.4; 2145 -4.1; 2295 -3.0; 2455 -1.6; 2627 -0.2; 2811 0.7; 3008 1.8; 3219 2.9; 3444 4.0; 3685 4.9; 3943 4.3; 4219 1.3; 4514 -0.3; 4830 -0.0; 5168 1.0; 5530 3.3; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.2; 8299 -2.8; 8880 -5.7; 9502 -6.9; 10167 -6.2; 10879 -3.7; 11640 -0.3; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PXC150 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 0.66 | 6.7 dB  |
| Peaking | 1852 Hz | 2.49 | -6.2 dB |
| Peaking | 3551 Hz | 3.86 | 5.4 dB  |
| Peaking | 6253 Hz | 4.21 | 6.9 dB  |
| Peaking | 9538 Hz | 3.49 | -8.0 dB |
| Peaking | 53 Hz   | 4.21 | 1.7 dB  |
| Peaking | 75 Hz   | 3.8  | -1.7 dB |
| Peaking | 130 Hz  | 4.06 | -1.1 dB |
| Peaking | 480 Hz  | 1.02 | 2.9 dB  |
| Peaking | 4637 Hz | 8.67 | -2.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20PXC150/Sennheiser%20PXC150.png)