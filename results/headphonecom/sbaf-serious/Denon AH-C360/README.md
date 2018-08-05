# Denon AH-C360

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.3dB
GraphicEQ: 10 -84; 20 -6.5; 22 -6.8; 23 -6.9; 25 -7.1; 26 -7.2; 28 -7.4; 30 -7.5; 32 -7.6; 35 -7.7; 37 -7.8; 40 -7.8; 42 -7.9; 45 -7.9; 49 -8.0; 52 -8.0; 56 -8.0; 59 -8.0; 64 -8.1; 68 -8.1; 73 -8.2; 78 -8.3; 83 -8.3; 89 -8.6; 95 -8.8; 102 -9.2; 109 -9.5; 117 -9.9; 125 -10.4; 134 -10.6; 143 -10.7; 153 -10.8; 164 -10.7; 175 -10.5; 188 -10.2; 201 -10.0; 215 -9.6; 230 -9.2; 246 -8.8; 263 -8.6; 282 -8.0; 301 -7.5; 323 -6.8; 345 -6.4; 369 -5.9; 395 -5.5; 423 -5.1; 452 -4.7; 484 -4.3; 518 -3.7; 554 -3.0; 593 -2.3; 635 -1.6; 679 -1.2; 726 -0.8; 777 -0.2; 832 0.1; 890 0.2; 952 -0.0; 1019 0.1; 1090 0.2; 1167 0.3; 1248 0.5; 1336 0.4; 1429 0.1; 1529 -0.5; 1636 -0.8; 1751 0.1; 1873 0.4; 2004 -0.1; 2145 -0.3; 2295 -0.1; 2455 0.2; 2627 0.3; 2811 0.5; 3008 0.7; 3219 0.4; 3444 0.0; 3685 -0.7; 3943 -1.8; 4219 -3.7; 4514 -5.3; 4830 -6.0; 5168 -6.4; 5530 -7.0; 5917 -8.1; 6331 -7.5; 6775 -6.0; 7249 -5.5; 7756 -6.3; 8299 -7.9; 8880 -8.2; 9502 -5.7; 10167 -1.1; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -0.1; 15258 -1.6; 16326 -0.4; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-1.3dB` and instead set Global volume in the UI for both channels to **-13**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-C360 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 5 Hz    | 1.77 | -5.9 dB |
| Peaking | 38 Hz   | 0.19 | -7.0 dB |
| Peaking | 198 Hz  | 0.69 | -6.8 dB |
| Peaking | 5767 Hz | 2.23 | -7.8 dB |
| Peaking | 8530 Hz | 4.22 | -7.5 dB |
| Peaking | 473 Hz  | 2.05 | -1.4 dB |
| Peaking | 835 Hz  | 1.14 | 1.5 dB  |
| Peaking | 3303 Hz | 2.11 | 1.9 dB  |
| Peaking | 4540 Hz | 3.58 | -2.6 dB |
| Peaking | 5442 Hz | 8.02 | 1.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Denon%20AH-C360/Denon%20AH-C360.png)