# Sennheiser EH350

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 5.9; 83 5.5; 89 4.7; 95 4.1; 102 3.3; 109 2.9; 117 2.6; 125 2.2; 134 2.2; 143 2.7; 153 2.6; 164 2.2; 175 2.0; 188 1.8; 201 1.7; 215 1.5; 230 1.5; 246 1.4; 263 1.2; 282 1.2; 301 1.1; 323 1.0; 345 0.9; 369 0.8; 395 0.8; 423 0.7; 452 0.5; 484 0.6; 518 0.8; 554 1.0; 593 0.8; 635 1.1; 679 1.4; 726 0.8; 777 0.3; 832 0.1; 890 0.1; 952 -0.1; 1019 0.0; 1090 0.4; 1167 0.1; 1248 -0.5; 1336 -0.8; 1429 -1.2; 1529 -1.5; 1636 -1.6; 1751 -1.0; 1873 0.1; 2004 0.5; 2145 1.0; 2295 1.3; 2455 1.5; 2627 1.3; 2811 1.4; 3008 1.1; 3219 0.8; 3444 1.4; 3685 3.8; 3943 6.0; 4219 4.5; 4514 -2.8; 4830 -0.3; 5168 1.8; 5530 2.5; 5917 4.9; 6331 5.5; 6775 2.7; 7249 -1.2; 7756 -3.0; 8299 -2.4; 8880 -0.3; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 -1.7; 13327 -6.6; 14260 -8.7; 15258 -7.7; 16326 -5.8; 17469 -4.8; 18692 -4.1; 20000 -2.9
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser EH350 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.3dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 27 Hz    | 0.24 | 6.0 dB   |
| Peaking | 72 Hz    | 3.01 | 1.6 dB   |
| Peaking | 5602 Hz  | 0.9  | 4.8 dB   |
| Peaking | 11750 Hz | 2.07 | 10.8 dB  |
| Peaking | 13145 Hz | 0.77 | -12.8 dB |
| Peaking | 1552 Hz  | 4.94 | -2.2 dB  |
| Peaking | 4091 Hz  | 5.96 | 7.2 dB   |
| Peaking | 4535 Hz  | 6.19 | -8.3 dB  |
| Peaking | 6284 Hz  | 5.93 | 4.5 dB   |
| Peaking | 7615 Hz  | 7.38 | -3.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20EH350/Sennheiser%20EH350.png)