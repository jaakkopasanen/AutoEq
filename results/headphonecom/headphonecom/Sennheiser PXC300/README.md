# Sennheiser PXC300

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 5.9; 45 5.5; 49 4.5; 52 3.8; 56 2.9; 59 2.4; 64 1.6; 68 1.1; 73 0.9; 78 1.4; 83 1.6; 89 0.9; 95 0.3; 102 -0.1; 109 -0.3; 117 -0.3; 125 -0.3; 134 -0.3; 143 -0.5; 153 -0.5; 164 -0.3; 175 -0.2; 188 0.1; 201 0.5; 215 0.6; 230 0.7; 246 0.7; 263 0.6; 282 0.6; 301 0.7; 323 0.9; 345 1.1; 369 1.4; 395 1.6; 423 1.6; 452 1.8; 484 2.0; 518 2.3; 554 2.5; 593 2.5; 635 2.7; 679 2.5; 726 2.3; 777 1.9; 832 1.4; 890 1.0; 952 0.4; 1019 -0.2; 1090 -0.7; 1167 -1.0; 1248 -1.1; 1336 -0.8; 1429 -0.3; 1529 0.2; 1636 0.4; 1751 0.5; 1873 1.3; 2004 1.2; 2145 0.6; 2295 0.4; 2455 0.5; 2627 1.2; 2811 2.0; 3008 2.6; 3219 2.9; 3444 3.0; 3685 3.3; 3943 4.0; 4219 4.7; 4514 3.7; 4830 3.0; 5168 4.3; 5530 5.3; 5917 4.5; 6331 1.7; 6775 -1.8; 7249 -2.3; 7756 -1.4; 8299 -1.0; 8880 -2.2; 9502 -4.2; 10167 -4.5; 10879 -1.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser PXC300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 0.98 | 6.9 dB  |
| Peaking | 570 Hz  | 1.7  | 2.8 dB  |
| Peaking | 5566 Hz | 6.44 | 4.8 dB  |
| Peaking | 3964 Hz | 2.04 | 4.2 dB  |
| Peaking | 9480 Hz | 3.05 | -4.5 dB |
| Peaking | 124 Hz  | 1.54 | -1.3 dB |
| Peaking | 769 Hz  | 5.91 | 0.6 dB  |
| Peaking | 1189 Hz | 3.02 | -1.9 dB |
| Peaking | 1549 Hz | 0    | 0.3 dB  |
| Peaking | 7095 Hz | 8.64 | -3.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Sennheiser%20PXC300/Sennheiser%20PXC300.png)