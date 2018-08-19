# Shure SE420

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 5.4; 22 5.1; 23 5.0; 25 4.7; 26 4.6; 28 4.4; 30 4.2; 32 4.0; 35 3.7; 37 3.5; 40 3.3; 42 3.1; 45 2.9; 49 2.6; 52 2.3; 56 2.0; 59 1.8; 64 1.5; 68 1.2; 73 0.9; 78 0.6; 83 0.3; 89 0.1; 95 -0.1; 102 -0.4; 109 -0.7; 117 -0.9; 125 -1.1; 134 -1.3; 143 -1.5; 153 -1.7; 164 -1.8; 175 -1.9; 188 -2.0; 201 -2.1; 215 -2.1; 230 -2.1; 246 -2.1; 263 -2.1; 282 -1.9; 301 -1.8; 323 -1.7; 345 -1.6; 369 -1.3; 395 -1.2; 423 -1.1; 452 -1.0; 484 -0.8; 518 -0.7; 554 -0.4; 593 -0.1; 635 0.0; 679 0.2; 726 0.3; 777 0.4; 832 0.5; 890 0.4; 952 0.2; 1019 -0.0; 1090 -0.3; 1167 -0.5; 1248 -0.7; 1336 -1.1; 1429 -1.5; 1529 -1.9; 1636 -2.2; 1751 -2.3; 1873 -2.3; 2004 -2.5; 2145 -2.7; 2295 -2.5; 2455 -2.0; 2627 -1.2; 2811 0.0; 3008 1.4; 3219 2.8; 3444 4.1; 3685 4.8; 3943 4.9; 4219 4.7; 4514 4.9; 4830 5.8; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099245613600242dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE420 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.4dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 0.78 | 5.0 dB  |
| Peaking | 45 Hz   | 1.18 | 1.4 dB  |
| Peaking | 206 Hz  | 0.82 | -2.4 dB |
| Peaking | 2111 Hz | 1.74 | -4.0 dB |
| Peaking | 4695 Hz | 1.28 | 6.6 dB  |
| Peaking | 798 Hz  | 1.54 | 1.8 dB  |
| Peaking | 809 Hz  | 0.74 | -0.9 dB |
| Peaking | 3486 Hz | 5.2  | 2.1 dB  |
| Peaking | 6203 Hz | 2.94 | 6.0 dB  |
| Peaking | 6540 Hz | 1.21 | -4.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Shure%20SE420/Shure%20SE420.png)