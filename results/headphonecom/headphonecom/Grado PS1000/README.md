# Grado PS1000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.8dB
GraphicEQ: 10 -84; 20 6.3; 22 5.4; 23 5.0; 25 4.1; 26 3.7; 28 2.9; 30 2.1; 32 1.4; 35 0.3; 37 -0.3; 40 -1.3; 42 -1.9; 45 -2.7; 49 -3.7; 52 -4.4; 56 -5.2; 59 -5.8; 64 -6.6; 68 -7.1; 73 -7.7; 78 -8.0; 83 -8.2; 89 -8.4; 95 -8.4; 102 -8.2; 109 -8.1; 117 -7.7; 125 -7.3; 134 -6.7; 143 -6.2; 153 -5.8; 164 -5.3; 175 -4.9; 188 -4.4; 201 -4.1; 215 -3.7; 230 -3.3; 246 -3.1; 263 -2.9; 282 -2.6; 301 -2.2; 323 -1.8; 345 -1.4; 369 -1.0; 395 -1.3; 423 -1.2; 452 -1.0; 484 -0.7; 518 -0.4; 554 -0.1; 593 0.1; 635 0.2; 679 0.5; 726 0.5; 777 0.5; 832 0.4; 890 0.3; 952 0.2; 1019 -0.0; 1090 -0.2; 1167 -0.2; 1248 -0.0; 1336 0.2; 1429 0.4; 1529 0.3; 1636 0.4; 1751 1.4; 1873 1.7; 2004 1.9; 2145 1.9; 2295 2.0; 2455 2.0; 2627 1.9; 2811 1.8; 3008 1.5; 3219 1.3; 3444 2.0; 3685 -0.7; 3943 -5.5; 4219 -4.6; 4514 -1.5; 4830 -1.2; 5168 -1.8; 5530 -3.4; 5917 -5.4; 6331 -9.7; 6775 -10.3; 7249 -9.1; 7756 -8.3; 8299 -7.6; 8880 -6.6; 9502 -4.6; 10167 -1.5; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.8dB` and instead set Global volume in the UI for both channels to **-68**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado PS1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 17 Hz    | 0.77 | 7.9 dB  |
| Peaking | 72 Hz    | 0.8  | -5.1 dB |
| Peaking | 116 Hz   | 0.7  | -5.0 dB |
| Peaking | 6641 Hz  | 3.67 | -9.5 dB |
| Peaking | 8368 Hz  | 3.4  | -6.1 dB |
| Peaking | 711 Hz   | 1.54 | 1.6 dB  |
| Peaking | 2894 Hz  | 0.62 | 5.5 dB  |
| Peaking | 4026 Hz  | 7.5  | -7.4 dB |
| Peaking | 2723 Hz  | 0.26 | -2.9 dB |
| Peaking | 11416 Hz | 2.68 | 1.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Grado%20PS1000/Grado%20PS1000.png)