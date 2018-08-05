# Thinksound Rain2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.2dB
GraphicEQ: 10 -84; 20 -8.6; 22 -8.7; 23 -8.7; 25 -8.8; 26 -8.8; 28 -8.8; 30 -8.9; 32 -8.9; 35 -8.9; 37 -8.9; 40 -8.9; 42 -8.9; 45 -9.0; 49 -9.0; 52 -9.0; 56 -9.0; 59 -8.9; 64 -8.9; 68 -9.0; 73 -9.0; 78 -9.1; 83 -9.2; 89 -9.5; 95 -9.9; 102 -10.3; 109 -10.6; 117 -11.0; 125 -11.4; 134 -11.7; 143 -11.7; 153 -11.8; 164 -11.7; 175 -11.4; 188 -11.1; 201 -10.9; 215 -10.5; 230 -10.1; 246 -9.7; 263 -9.4; 282 -8.8; 301 -8.4; 323 -7.9; 345 -7.4; 369 -6.9; 395 -6.4; 423 -5.7; 452 -5.2; 484 -4.8; 518 -4.3; 554 -3.6; 593 -2.9; 635 -2.3; 679 -1.9; 726 -1.5; 777 -0.9; 832 -0.6; 890 -0.4; 952 -0.1; 1019 0.1; 1090 0.3; 1167 0.5; 1248 0.6; 1336 0.4; 1429 0.0; 1529 -0.6; 1636 -1.0; 1751 -1.2; 1873 -1.0; 2004 -0.6; 2145 -0.2; 2295 0.3; 2455 1.1; 2627 1.5; 2811 1.8; 3008 2.3; 3219 2.5; 3444 2.5; 3685 1.9; 3943 0.8; 4219 -1.3; 4514 -2.8; 4830 -4.0; 5168 -5.5; 5530 -8.7; 5917 -10.9; 6331 -8.3; 6775 -4.5; 7249 -1.6; 7756 0.1; 8299 0.0; 8880 0.0; 9502 -0.9; 10167 -2.4; 10879 -1.7; 11640 -0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 -0.2; 16326 -2.3; 17469 -1.8; 18692 -0.1; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.2dB` and instead set Global volume in the UI for both channels to **-32**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Thinksound Rain2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 8 Hz     | 1.14 | -8.2 dB  |
| Peaking | 31 Hz    | 0.14 | -7.7 dB  |
| Peaking | 200 Hz   | 0.63 | -7.0 dB  |
| Peaking | 3246 Hz  | 2.64 | 3.5 dB   |
| Peaking | 5827 Hz  | 3.71 | -11.4 dB |
| Peaking | 1139 Hz  | 1.84 | 1.6 dB   |
| Peaking | 1738 Hz  | 3.63 | -1.5 dB  |
| Peaking | 7900 Hz  | 5.55 | 2.1 dB   |
| Peaking | 10359 Hz | 8.41 | -2.5 dB  |
| Peaking | 16786 Hz | 4.34 | -2.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Thinksound%20Rain2/Thinksound%20Rain2.png)