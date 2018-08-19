# AKG K3003 High Boost Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.7dB
GraphicEQ: 10 -84; 20 3.2; 22 2.6; 23 2.4; 25 1.9; 26 1.7; 28 1.3; 30 1.0; 32 0.7; 35 0.3; 37 0.1; 40 -0.2; 42 -0.4; 45 -0.7; 49 -1.1; 52 -1.4; 56 -1.7; 59 -1.9; 64 -2.3; 68 -2.5; 73 -2.9; 78 -3.2; 83 -3.4; 89 -3.6; 95 -3.8; 102 -4.0; 109 -4.1; 117 -4.3; 125 -4.5; 134 -4.7; 143 -4.7; 153 -4.9; 164 -4.9; 175 -4.9; 188 -4.9; 201 -4.8; 215 -4.7; 230 -4.5; 246 -4.4; 263 -4.2; 282 -4.0; 301 -3.7; 323 -3.4; 345 -3.0; 369 -2.7; 395 -2.4; 423 -2.1; 452 -2.0; 484 -1.6; 518 -1.3; 554 -1.0; 593 -0.6; 635 -0.3; 679 -0.1; 726 0.1; 777 0.4; 832 0.3; 890 0.3; 952 0.2; 1019 -0.1; 1090 -0.4; 1167 -0.5; 1248 -0.6; 1336 -0.8; 1429 -0.8; 1529 -1.2; 1636 -1.6; 1751 -1.8; 1873 -1.8; 2004 -1.7; 2145 -1.7; 2295 -1.5; 2455 -1.5; 2627 -1.5; 2811 -1.5; 3008 -1.5; 3219 -0.3; 3444 2.5; 3685 4.5; 3943 4.0; 4219 0.9; 4514 -3.9; 4830 -6.3; 5168 -5.8; 5530 -5.6; 5917 -3.4; 6331 0.1; 6775 2.0; 7249 1.3; 7756 0.1; 8299 -3.1; 8880 -7.5; 9502 -10.8; 10167 -10.4; 10879 -5.9; 11640 -0.5; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.697351015208161dB` and instead set Global volume in the UI for both channels to **-46**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K3003 High Boost Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -2.7dB.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 19 Hz    |  1.19 | 3.2 dB   |
| Peaking | 158 Hz   |  0.51 | -5.1 dB  |
| Peaking | 5263 Hz  |  3.55 | -10.4 dB |
| Peaking | 6894 Hz  |  0.95 | 5.6 dB   |
| Peaking | 9638 Hz  |  3.26 | -15.2 dB |
| Peaking | 806 Hz   |  2.03 | 1.5 dB   |
| Peaking | 2618 Hz  |  0.9  | -2.7 dB  |
| Peaking | 3817 Hz  |  3.95 | 6.8 dB   |
| Peaking | 4615 Hz  | 10.01 | -3.5 dB  |
| Peaking | 11694 Hz |  6.31 | 2.0 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K3003%20High%20Boost%20Filter/AKG%20K3003%20High%20Boost%20Filter.png)