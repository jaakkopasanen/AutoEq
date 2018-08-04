# Grado PS500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 5.2; 22 4.2; 23 3.8; 25 3.0; 26 2.6; 28 1.9; 30 1.2; 32 0.6; 35 -0.3; 37 -0.9; 40 -1.6; 42 -2.1; 45 -2.9; 49 -3.7; 52 -4.3; 56 -5.0; 59 -5.4; 64 -6.0; 68 -6.4; 73 -6.7; 78 -6.7; 83 -6.7; 89 -6.7; 95 -6.7; 102 -6.5; 109 -6.2; 117 -5.9; 125 -5.6; 134 -5.1; 143 -4.8; 153 -4.5; 164 -4.0; 175 -3.6; 188 -3.3; 201 -3.1; 215 -2.7; 230 -2.4; 246 -2.1; 263 -1.8; 282 -1.5; 301 -1.1; 323 -0.8; 345 -0.5; 369 -0.2; 395 0.1; 423 0.2; 452 0.3; 484 0.5; 518 0.5; 554 0.8; 593 1.1; 635 1.1; 679 0.8; 726 0.8; 777 0.9; 832 0.7; 890 0.5; 952 0.3; 1019 0.0; 1090 -0.3; 1167 -0.6; 1248 -1.1; 1336 -1.9; 1429 -2.8; 1529 -3.5; 1636 -3.8; 1751 -2.9; 1873 -2.7; 2004 -4.3; 2145 -5.2; 2295 -1.7; 2455 0.6; 2627 2.3; 2811 4.5; 3008 6.0; 3219 6.0; 3444 6.0; 3685 5.9; 3943 4.1; 4219 4.3; 4514 4.3; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.4; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -2.6; 9502 -3.9; 10167 -1.4; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado PS500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 1.14 | 5.7 dB  |
| Peaking | 70 Hz   | 0.92 | -5.6 dB |
| Peaking | 127 Hz  | 0.97 | -3.4 dB |
| Peaking | 3349 Hz | 4.06 | 6.4 dB  |
| Peaking | 5389 Hz | 2.69 | 6.6 dB  |
| Peaking | 684 Hz  | 1.26 | 1.7 dB  |
| Peaking | 2151 Hz | 1.43 | -8.0 dB |
| Peaking | 2676 Hz | 2.16 | 6.9 dB  |
| Peaking | 6436 Hz | 8.66 | 2.7 dB  |
| Peaking | 9325 Hz | 5.94 | -4.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20PS500/Grado%20PS500.png)