# Grado PS1000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -7.4dB
GraphicEQ: 10 -84; 20 6.8; 22 5.9; 23 5.5; 25 4.7; 26 4.2; 28 3.4; 30 2.6; 32 1.9; 35 0.9; 37 0.3; 40 -0.7; 42 -1.3; 45 -2.1; 49 -3.1; 52 -3.8; 56 -4.7; 59 -5.2; 64 -6.0; 68 -6.5; 73 -7.0; 78 -7.4; 83 -7.5; 89 -7.6; 95 -7.5; 102 -7.2; 109 -6.9; 117 -6.4; 125 -6.0; 134 -5.4; 143 -4.9; 153 -4.5; 164 -4.0; 175 -3.5; 188 -3.0; 201 -2.7; 215 -2.3; 230 -1.9; 246 -1.7; 263 -1.5; 282 -1.2; 301 -0.8; 323 -0.5; 345 0.1; 369 0.4; 395 -0.0; 423 0.0; 452 0.1; 484 0.0; 518 0.1; 554 0.4; 593 0.6; 635 0.5; 679 0.5; 726 0.5; 777 0.6; 832 0.5; 890 0.3; 952 0.2; 1019 -0.0; 1090 -0.3; 1167 -0.5; 1248 -0.7; 1336 -1.1; 1429 -1.7; 1529 -2.4; 1636 -2.6; 1751 -1.6; 1873 -1.2; 2004 -1.1; 2145 -1.1; 2295 -1.0; 2455 -1.0; 2627 -1.1; 2811 -1.1; 3008 -1.1; 3219 -1.0; 3444 -0.0; 3685 -2.8; 3943 -7.8; 4219 -8.2; 4514 -6.3; 4830 -6.6; 5168 -7.2; 5530 -8.1; 5917 -8.9; 6331 -11.9; 6775 -11.6; 7249 -10.1; 7756 -9.3; 8299 -9.0; 8880 -8.6; 9502 -7.2; 10167 -5.1; 10879 -2.4; 11640 -0.1; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-7.4dB` and instead set Global volume in the UI for both channels to **-74**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado PS1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 20 Hz    |  1.05 | 7.2 dB   |
| Peaking | 75 Hz    |  0.99 | -6.5 dB  |
| Peaking | 123 Hz   |  1.17 | -3.3 dB  |
| Peaking | 4136 Hz  |  7.02 | -5.4 dB  |
| Peaking | 6897 Hz  |  1.44 | -11.8 dB |
| Peaking | 661 Hz   |  1.11 | 0.9 dB   |
| Peaking | 1558 Hz  |  3.61 | -2.3 dB  |
| Peaking | 3449 Hz  | 10.18 | 2.9 dB   |
| Peaking | 9532 Hz  |  3.57 | -3.9 dB  |
| Peaking | 11670 Hz |  1.55 | 2.8 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20PS1000/Grado%20PS1000.png)