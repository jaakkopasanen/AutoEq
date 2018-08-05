# Grado SR325

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 5.8; 49 5.1; 52 4.4; 56 3.6; 59 3.2; 64 2.6; 68 2.1; 73 1.7; 78 1.3; 83 1.0; 89 0.7; 95 0.3; 102 -0.0; 109 -0.2; 117 -0.4; 125 -0.6; 134 -0.8; 143 -0.8; 153 -1.0; 164 -0.9; 175 -0.7; 188 -0.7; 201 -0.7; 215 -0.7; 230 -0.5; 246 -0.4; 263 -0.4; 282 -0.3; 301 -0.2; 323 -0.0; 345 0.1; 369 0.2; 395 0.3; 423 0.5; 452 0.5; 484 0.3; 518 0.3; 554 0.5; 593 0.7; 635 0.7; 679 0.5; 726 0.5; 777 0.6; 832 0.5; 890 0.3; 952 0.2; 1019 -0.1; 1090 -0.3; 1167 -0.5; 1248 -0.9; 1336 -1.5; 1429 -2.2; 1529 -3.1; 1636 -3.9; 1751 -4.7; 1873 -6.4; 2004 -8.1; 2145 -8.2; 2295 -7.0; 2455 -5.9; 2627 -4.9; 2811 -3.9; 3008 -2.6; 3219 -1.6; 3444 -0.9; 3685 -0.9; 3943 -3.1; 4219 -9.2; 4514 -13.4; 4830 -10.5; 5168 -7.0; 5530 -5.0; 5917 -4.1; 6331 -5.0; 6775 -6.0; 7249 -6.4; 7756 -7.2; 8299 -9.2; 8880 -11.5; 9502 -12.3; 10167 -11.3; 10879 -9.6; 11640 -7.5; 12455 -3.9; 13327 -0.2; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR325 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 31 Hz    | 0.52 | 6.6 dB   |
| Peaking | 117 Hz   | 0.94 | -2.1 dB  |
| Peaking | 2090 Hz  | 2.67 | -8.4 dB  |
| Peaking | 4589 Hz  | 5.72 | -12.4 dB |
| Peaking | 9442 Hz  | 1.87 | -12.8 dB |
| Peaking | 694 Hz   | 0.71 | 1.6 dB   |
| Peaking | 1568 Hz  | 0.11 | -0.6 dB  |
| Peaking | 3617 Hz  | 5.7  | 3.4 dB   |
| Peaking | 3251 Hz  | 0.21 | -0.2 dB  |
| Peaking | 14010 Hz | 3.24 | 3.0 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20SR325/Grado%20SR325.png)