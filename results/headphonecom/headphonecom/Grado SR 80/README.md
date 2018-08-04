# Grado SR 80

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 5.9; 42 5.5; 45 4.8; 49 3.7; 52 2.9; 56 2.1; 59 1.5; 64 0.8; 68 0.2; 73 -0.6; 78 -1.3; 83 -1.8; 89 -2.3; 95 -2.7; 102 -2.8; 109 -3.0; 117 -3.2; 125 -3.2; 134 -3.2; 143 -3.2; 153 -3.1; 164 -2.9; 175 -2.7; 188 -2.5; 201 -2.4; 215 -2.3; 230 -2.2; 246 -2.0; 263 -1.8; 282 -1.5; 301 -1.5; 323 -1.4; 345 -1.3; 369 -1.1; 395 -0.9; 423 -0.7; 452 -0.5; 484 -0.2; 518 -0.0; 554 0.1; 593 0.4; 635 0.5; 679 0.6; 726 0.6; 777 0.6; 832 0.5; 890 0.4; 952 0.1; 1019 -0.1; 1090 -0.2; 1167 -0.4; 1248 -0.4; 1336 -0.2; 1429 -0.3; 1529 -0.5; 1636 -0.9; 1751 -1.5; 1873 -2.2; 2004 -2.9; 2145 -3.1; 2295 -3.1; 2455 -2.6; 2627 -2.3; 2811 -2.0; 3008 -1.8; 3219 -1.8; 3444 -2.4; 3685 -4.9; 3943 -7.6; 4219 -4.3; 4514 -0.1; 4830 1.1; 5168 0.9; 5530 -1.3; 5917 -3.3; 6331 -1.6; 6775 -3.0; 7249 -4.9; 7756 -6.5; 8299 -8.0; 8880 -8.8; 9502 -8.0; 10167 -5.3; 10879 -1.2; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR 80 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 33 Hz    | 0.52 | 7.9 dB  |
| Peaking | 101 Hz   | 0.59 | -5.7 dB |
| Peaking | 2222 Hz  | 2.62 | -3.2 dB |
| Peaking | 3908 Hz  | 7.92 | -7.4 dB |
| Peaking | 8713 Hz  | 2.84 | -9.5 dB |
| Peaking | 713 Hz   | 2.17 | 1.0 dB  |
| Peaking | 2329 Hz  | 5.26 | 0.3 dB  |
| Peaking | 4879 Hz  | 4.56 | 4.9 dB  |
| Peaking | 5044 Hz  | 1.45 | -2.1 dB |
| Peaking | 11765 Hz | 4.63 | 2.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Grado%20SR%2080/Grado%20SR%2080.png)