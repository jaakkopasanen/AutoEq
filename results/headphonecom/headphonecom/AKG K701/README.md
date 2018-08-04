# AKG K701

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 6.0; 22 5.8; 23 5.6; 25 5.1; 26 4.9; 28 4.2; 30 3.6; 32 3.1; 35 2.4; 37 2.0; 40 1.4; 42 1.0; 45 0.5; 49 -0.0; 52 -0.4; 56 -0.8; 59 -0.6; 64 0.6; 68 0.3; 73 -1.1; 78 -1.6; 83 -2.0; 89 -2.1; 95 -2.3; 102 -2.4; 109 -2.5; 117 -2.7; 125 -3.0; 134 -3.0; 143 -3.0; 153 -2.9; 164 -2.9; 175 -3.0; 188 -3.1; 201 -2.9; 215 -2.9; 230 -3.0; 246 -2.9; 263 -2.7; 282 -2.5; 301 -2.4; 323 -2.3; 345 -2.2; 369 -2.0; 395 -1.9; 423 -1.6; 452 -1.2; 484 -0.9; 518 -0.7; 554 0.7; 593 1.3; 635 0.7; 679 0.9; 726 0.9; 777 0.6; 832 0.4; 890 0.2; 952 -0.0; 1019 -0.0; 1090 -0.2; 1167 -0.2; 1248 -0.0; 1336 0.8; 1429 1.0; 1529 1.1; 1636 1.1; 1751 0.5; 1873 -0.5; 2004 -1.3; 2145 -1.7; 2295 -1.5; 2455 -1.0; 2627 -0.2; 2811 0.2; 3008 0.1; 3219 0.2; 3444 -0.1; 3685 0.1; 3943 0.2; 4219 0.7; 4514 1.8; 4830 3.6; 5168 3.4; 5530 0.7; 5917 -2.2; 6331 -3.0; 6775 -2.4; 7249 -3.0; 7756 -3.4; 8299 -2.8; 8880 -1.4; 9502 -0.1; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K701 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 21 Hz    | 1.25 | 6.2 dB  |
| Peaking | 161 Hz   | 0.64 | -3.4 dB |
| Peaking | 2201 Hz  | 7.36 | -1.9 dB |
| Peaking | 5004 Hz  | 4.69 | 5.4 dB  |
| Peaking | 6806 Hz  | 2    | -3.9 dB |
| Peaking | 428 Hz   | 1.47 | -1.2 dB |
| Peaking | 611 Hz   | 2.19 | 2.2 dB  |
| Peaking | 1643 Hz  | 3.34 | 2.2 dB  |
| Peaking | 1826 Hz  | 3.21 | -1.4 dB |
| Peaking | 10140 Hz | 5.78 | 0.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/AKG%20K701/AKG%20K701.png)