# AKG K 550

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 2.3; 22 1.9; 23 1.6; 25 1.3; 26 1.1; 28 0.9; 30 0.7; 32 0.5; 35 0.3; 37 0.2; 40 0.1; 42 -0.0; 45 -0.1; 49 -0.1; 52 -0.1; 56 -0.1; 59 -0.1; 64 -0.3; 68 -0.3; 73 -0.0; 78 0.4; 83 1.0; 89 1.9; 95 2.1; 102 1.2; 109 0.2; 117 -0.7; 125 -1.4; 134 -1.7; 143 -1.7; 153 -1.6; 164 0.1; 175 -0.6; 188 -1.7; 201 -1.7; 215 -1.8; 230 -1.9; 246 -1.9; 263 -1.8; 282 -1.6; 301 -1.5; 323 -1.4; 345 -1.2; 369 -0.9; 395 -0.7; 423 -0.5; 452 -0.3; 484 -0.1; 518 0.0; 554 0.4; 593 0.8; 635 1.1; 679 1.3; 726 1.4; 777 1.5; 832 0.9; 890 0.4; 952 0.3; 1019 0.0; 1090 -0.2; 1167 -0.5; 1248 -0.8; 1336 -1.1; 1429 -1.4; 1529 -2.0; 1636 -1.8; 1751 -1.1; 1873 -0.6; 2004 -0.1; 2145 0.4; 2295 0.7; 2455 1.0; 2627 1.1; 2811 1.7; 3008 2.6; 3219 3.6; 3444 4.8; 3685 5.9; 3943 5.9; 4219 4.8; 4514 3.8; 4830 3.2; 5168 0.7; 5530 -0.9; 5917 -0.2; 6331 3.3; 6775 3.9; 7249 1.3; 7756 -0.0; 8299 -3.8; 8880 -6.8; 9502 -6.0; 10167 -1.7; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -0.1; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.09999957120612dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K 550 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 16 Hz    | 1.27 | 3.4 dB  |
| Peaking | 237 Hz   | 1.56 | -2.0 dB |
| Peaking | 3808 Hz  | 2.91 | 6.5 dB  |
| Peaking | 6710 Hz  | 8.13 | 4.7 dB  |
| Peaking | 9049 Hz  | 5.29 | -8.0 dB |
| Peaking | 95 Hz    | 5.27 | 2.6 dB  |
| Peaking | 132 Hz   | 4.73 | -1.6 dB |
| Peaking | 717 Hz   | 3.02 | 1.7 dB  |
| Peaking | 1540 Hz  | 3.26 | -2.2 dB |
| Peaking | 11143 Hz | 5.11 | 0.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K550/AKG%20K%20550.png)