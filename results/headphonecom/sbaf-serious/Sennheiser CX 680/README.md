# Sennheiser CX 680

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.2dB
GraphicEQ: 10 -84; 20 2.5; 22 2.0; 23 1.9; 25 1.5; 26 1.3; 28 1.0; 30 0.7; 32 0.5; 35 0.2; 37 -0.0; 40 -0.3; 42 -0.5; 45 -0.7; 49 -1.0; 52 -1.3; 56 -1.6; 59 -1.8; 64 -2.2; 68 -2.5; 73 -2.9; 78 -3.2; 83 -3.5; 89 -3.8; 95 -4.1; 102 -4.4; 109 -4.6; 117 -4.9; 125 -5.2; 134 -5.5; 143 -5.8; 153 -6.0; 164 -6.3; 175 -6.5; 188 -6.6; 201 -6.6; 215 -6.7; 230 -6.7; 246 -6.7; 263 -6.5; 282 -6.4; 301 -6.1; 323 -5.8; 345 -5.3; 369 -5.0; 395 -4.6; 423 -4.1; 452 -3.8; 484 -3.3; 518 -2.8; 554 -2.2; 593 -1.9; 635 -1.3; 679 -0.3; 726 0.3; 777 0.4; 832 0.5; 890 0.4; 952 0.2; 1019 -0.1; 1090 -0.4; 1167 -0.7; 1248 -1.1; 1336 -1.7; 1429 -2.2; 1529 -2.9; 1636 -3.4; 1751 -3.7; 1873 -4.0; 2004 -4.3; 2145 -4.5; 2295 -4.4; 2455 -4.2; 2627 -3.5; 2811 -2.3; 3008 -0.6; 3219 1.2; 3444 2.6; 3685 3.0; 3943 1.9; 4219 -0.3; 4514 -2.8; 4830 -5.3; 5168 -6.3; 5530 -3.7; 5917 0.4; 6331 3.2; 6775 3.7; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.0; 9502 -1.5; 10167 -0.9; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.166856533993883dB` and instead set Global volume in the UI for both channels to **-41**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser CX 680 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.2dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 198 Hz  | 0.61 | -7.1 dB |
| Peaking | 2206 Hz | 1.77 | -5.1 dB |
| Peaking | 3660 Hz | 3.19 | 5.4 dB  |
| Peaking | 5100 Hz | 3.48 | -7.7 dB |
| Peaking | 6482 Hz | 4.84 | 5.9 dB  |
| Peaking | 21 Hz   | 1.75 | 2.6 dB  |
| Peaking | 419 Hz  | 1.59 | -1.1 dB |
| Peaking | 801 Hz  | 1.88 | 2.2 dB  |
| Peaking | 1566 Hz | 4.48 | -1.2 dB |
| Peaking | 9791 Hz | 9.21 | -1.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20CX%20680/Sennheiser%20CX%20680.png)