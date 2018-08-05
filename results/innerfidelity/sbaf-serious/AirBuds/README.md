# AirBuds

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 -0.6; 22 -1.4; 23 -1.7; 25 -2.2; 26 -2.3; 28 -2.3; 30 -2.4; 32 -2.5; 35 -3.0; 37 -3.3; 40 -3.5; 42 -3.7; 45 -3.9; 49 -4.2; 52 -4.3; 56 -4.5; 59 -4.7; 64 -5.0; 68 -5.2; 73 -5.4; 78 -5.7; 83 -6.0; 89 -6.4; 95 -6.9; 102 -7.6; 109 -8.1; 117 -8.6; 125 -9.3; 134 -9.7; 143 -10.1; 153 -10.3; 164 -10.4; 175 -10.4; 188 -10.4; 201 -10.3; 215 -10.1; 230 -9.9; 246 -9.8; 263 -9.6; 282 -9.3; 301 -9.0; 323 -8.7; 345 -8.3; 369 -7.9; 395 -7.6; 423 -7.0; 452 -6.6; 484 -6.2; 518 -5.7; 554 -5.0; 593 -4.3; 635 -3.8; 679 -3.3; 726 -2.7; 777 -1.9; 832 -1.3; 890 -0.7; 952 -0.4; 1019 0.0; 1090 1.1; 1167 3.2; 1248 3.3; 1336 4.3; 1429 5.9; 1529 6.0; 1636 6.0; 1751 4.8; 1873 2.7; 2004 1.9; 2145 2.4; 2295 3.7; 2455 5.5; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 5.8; 4219 3.2; 4514 0.3; 4830 -2.0; 5168 -4.1; 5530 -5.2; 5917 -3.3; 6331 -0.9; 6775 2.1; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AirBuds ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 88 Hz   | 0.16 | -1.5 dB |
| Peaking | 204 Hz  | 0.44 | -9.1 dB |
| Peaking | 1432 Hz | 2.23 | 6.1 dB  |
| Peaking | 3426 Hz | 1.19 | 7.2 dB  |
| Peaking | 5284 Hz | 3.58 | -8.5 dB |
| Peaking | 81 Hz   | 4.56 | 0.4 dB  |
| Peaking | 1675 Hz | 7.77 | 1.9 dB  |
| Peaking | 2028 Hz | 3.64 | -2.4 dB |
| Peaking | 2524 Hz | 4.21 | 2.0 dB  |
| Peaking | 3159 Hz | 5.08 | -0.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AirBuds/AirBuds.png)