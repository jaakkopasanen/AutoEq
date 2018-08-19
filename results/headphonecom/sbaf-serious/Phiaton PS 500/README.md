# Phiaton PS 500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 5.9; 30 5.4; 32 4.8; 35 4.0; 37 3.8; 40 3.7; 42 3.4; 45 2.6; 49 1.6; 52 1.6; 56 2.0; 59 2.1; 64 1.3; 68 0.4; 73 -0.4; 78 -1.0; 83 -1.4; 89 -1.8; 95 -2.2; 102 -2.4; 109 -2.6; 117 -2.9; 125 -3.1; 134 -3.2; 143 -3.4; 153 -3.5; 164 -3.1; 175 -3.4; 188 -3.3; 201 -3.1; 215 -3.0; 230 -2.7; 246 -2.1; 263 -1.4; 282 -0.3; 301 0.9; 323 1.8; 345 2.5; 369 2.8; 395 2.9; 423 2.7; 452 2.5; 484 2.3; 518 2.2; 554 2.1; 593 2.1; 635 1.9; 679 1.6; 726 1.3; 777 0.9; 832 1.4; 890 1.3; 952 0.4; 1019 -0.1; 1090 -0.4; 1167 -0.6; 1248 -0.7; 1336 -0.7; 1429 -0.5; 1529 -0.5; 1636 -0.9; 1751 -1.7; 1873 -2.2; 2004 -1.2; 2145 0.2; 2295 2.2; 2455 4.6; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 4.8; 4514 5.7; 4830 6.0; 5168 6.0; 5530 5.9; 5917 4.5; 6331 3.0; 6775 2.5; 7249 1.3; 7756 0.2; 8299 -0.6; 8880 -1.1; 9502 -0.5; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 -0.9
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton PS 500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 29 Hz   | 0.41 | 7.7 dB   |
| Peaking | 528 Hz  | 0.47 | 12.5 dB  |
| Peaking | 535 Hz  | 0.1  | -10.0 dB |
| Peaking | 2955 Hz | 1.4  | 10.4 dB  |
| Peaking | 5144 Hz | 1.57 | 7.7 dB   |
| Peaking | 62 Hz   | 6.41 | 1.3 dB   |
| Peaking | 227 Hz  | 1.23 | -3.5 dB  |
| Peaking | 434 Hz  | 0.61 | 6.6 dB   |
| Peaking | 540 Hz  | 1.09 | -6.4 dB  |
| Peaking | 1921 Hz | 7.09 | -2.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Phiaton%20PS%20500/Phiaton%20PS%20500.png)