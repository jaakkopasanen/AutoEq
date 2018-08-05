# Sleek SA1- Normal Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -5.2; 22 -5.3; 23 -5.3; 25 -5.4; 26 -5.4; 28 -5.4; 30 -5.4; 32 -5.4; 35 -5.4; 37 -5.4; 40 -5.4; 42 -5.4; 45 -5.4; 49 -5.4; 52 -5.4; 56 -5.4; 59 -5.5; 64 -5.5; 68 -5.6; 73 -5.7; 78 -5.8; 83 -6.0; 89 -6.3; 95 -6.5; 102 -7.0; 109 -7.5; 117 -7.8; 125 -8.4; 134 -8.8; 143 -9.0; 153 -9.1; 164 -9.1; 175 -9.0; 188 -8.9; 201 -8.8; 215 -8.5; 230 -8.2; 246 -8.0; 263 -7.7; 282 -7.3; 301 -7.0; 323 -6.5; 345 -6.0; 369 -5.6; 395 -5.2; 423 -4.6; 452 -4.3; 484 -4.1; 518 -3.6; 554 -3.0; 593 -2.3; 635 -1.8; 679 -1.5; 726 -1.1; 777 -0.6; 832 -0.3; 890 -0.2; 952 -0.1; 1019 0.0; 1090 0.1; 1167 0.2; 1248 0.2; 1336 0.2; 1429 0.3; 1529 0.3; 1636 0.4; 1751 0.7; 1873 1.3; 2004 1.8; 2145 2.3; 2295 2.9; 2455 3.5; 2627 3.9; 2811 5.2; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 5.0; 4219 2.5; 4514 0.4; 4830 -1.1; 5168 -2.6; 5530 -3.6; 5917 -1.2; 6331 2.1; 6775 3.6; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sleek SA1- Normal Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.41 | -4.8 dB |
| Peaking | 185 Hz  | 0.55 | -8.8 dB |
| Peaking | 3533 Hz | 1.25 | 8.4 dB  |
| Peaking | 5404 Hz | 1.82 | -8.0 dB |
| Peaking | 6618 Hz | 4.88 | 6.4 dB  |
| Peaking | 493 Hz  | 1.5  | -1.1 dB |
| Peaking | 765 Hz  | 0.96 | 1.2 dB  |
| Peaking | 1598 Hz | 2.79 | -0.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sleek%20SA1-%20Normal%20Filter/Sleek%20SA1-%20Normal%20Filter.png)