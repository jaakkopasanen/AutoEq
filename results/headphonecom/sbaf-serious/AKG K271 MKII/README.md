# AKG K271 MKII

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 5.9; 83 5.3; 89 4.4; 95 3.8; 102 3.2; 109 2.7; 117 2.1; 125 1.6; 134 1.0; 143 0.5; 153 0.1; 164 0.4; 175 0.4; 188 0.0; 201 -0.3; 215 -0.1; 230 0.1; 246 -0.1; 263 0.1; 282 0.3; 301 -0.2; 323 -0.6; 345 -0.6; 369 -0.6; 395 -0.7; 423 -1.0; 452 -1.3; 484 -1.5; 518 -1.4; 554 -1.7; 593 -2.1; 635 -3.0; 679 -3.0; 726 0.7; 777 1.2; 832 0.8; 890 1.0; 952 0.5; 1019 -0.2; 1090 -0.7; 1167 -1.1; 1248 -1.4; 1336 -2.1; 1429 -2.7; 1529 -3.0; 1636 -3.2; 1751 -3.0; 1873 -2.5; 2004 -0.8; 2145 2.2; 2295 1.4; 2455 0.3; 2627 -0.3; 2811 -0.3; 3008 0.5; 3219 2.3; 3444 3.4; 3685 3.0; 3943 2.3; 4219 0.8; 4514 0.8; 4830 2.4; 5168 4.2; 5530 5.4; 5917 5.5; 6331 4.6; 6775 3.6; 7249 0.1; 7756 -4.1; 8299 -7.3; 8880 -8.7; 9502 -7.9; 10167 -5.3; 10879 -1.6; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K271 MKII ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.1dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 40 Hz   | 0.58 | 7.0 dB   |
| Peaking | 1566 Hz | 3    | -3.6 dB  |
| Peaking | 3497 Hz | 5.61 | 3.2 dB   |
| Peaking | 6051 Hz | 2.42 | 7.3 dB   |
| Peaking | 8816 Hz | 3    | -10.9 dB |
| Peaking | 21 Hz   | 2.82 | 1.8 dB   |
| Peaking | 78 Hz   | 4.86 | 1.9 dB   |
| Peaking | 710 Hz  | 1.54 | -5.2 dB  |
| Peaking | 748 Hz  | 8.88 | 3.6 dB   |
| Peaking | 856 Hz  | 2.4  | 4.5 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K271%20MKII/AKG%20K271%20MKII.png)