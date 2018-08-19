# Sennheiser MM 50 iP

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.2dB
GraphicEQ: 10 -84; 20 -0.0; 22 -0.6; 23 -0.9; 25 -1.5; 26 -1.7; 28 -2.2; 30 -2.6; 32 -3.0; 35 -3.5; 37 -3.8; 40 -4.2; 42 -4.4; 45 -4.8; 49 -5.3; 52 -5.6; 56 -6.0; 59 -6.2; 64 -6.7; 68 -7.0; 73 -7.3; 78 -7.6; 83 -7.9; 89 -8.1; 95 -8.3; 102 -8.5; 109 -8.7; 117 -8.8; 125 -8.9; 134 -9.0; 143 -9.0; 153 -9.1; 164 -9.0; 175 -9.0; 188 -8.8; 201 -8.6; 215 -8.3; 230 -8.0; 246 -7.7; 263 -7.4; 282 -7.6; 301 -7.3; 323 -6.9; 345 -6.5; 369 -5.9; 395 -5.4; 423 -4.9; 452 -4.5; 484 -4.0; 518 -3.5; 554 -2.9; 593 -2.4; 635 -1.9; 679 -1.4; 726 -1.0; 777 -0.6; 832 -0.4; 890 -0.1; 952 -0.1; 1019 0.0; 1090 0.2; 1167 0.3; 1248 0.2; 1336 0.2; 1429 0.0; 1529 -0.6; 1636 -1.0; 1751 -1.1; 1873 -0.9; 2004 -0.6; 2145 -0.2; 2295 0.2; 2455 0.7; 2627 1.1; 2811 1.4; 3008 1.9; 3219 2.5; 3444 3.1; 3685 2.9; 3943 1.8; 4219 -0.0; 4514 -1.7; 4830 -2.8; 5168 -4.0; 5530 -6.0; 5917 -9.0; 6331 -7.7; 6775 -4.5; 7249 -2.6; 7756 -1.9; 8299 -3.2; 8880 -5.6; 9502 -6.6; 10167 -3.5; 10879 -0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.2022696944585367dB` and instead set Global volume in the UI for both channels to **-32**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser MM 50 iP ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -3.4dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 113 Hz   | 0.46 | -8.5 dB |
| Peaking | 296 Hz   | 1.04 | -3.3 dB |
| Peaking | 3455 Hz  | 2.97 | 3.9 dB  |
| Peaking | 5954 Hz  | 3.49 | -9.1 dB |
| Peaking | 9329 Hz  | 5.79 | -6.8 dB |
| Peaking | 19 Hz    | 2.1  | 1.3 dB  |
| Peaking | 1052 Hz  | 1.62 | 1.1 dB  |
| Peaking | 1747 Hz  | 4.2  | -1.3 dB |
| Peaking | 9969 Hz  | 9.95 | -2.2 dB |
| Peaking | 10750 Hz | 3.83 | 1.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20MM%2050%20iP/Sennheiser%20MM%2050%20iP.png)