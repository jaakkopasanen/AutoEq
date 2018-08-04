# AKG K701

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 5.9; 42 5.6; 45 5.1; 49 4.6; 52 4.1; 56 3.7; 59 3.9; 64 5.1; 68 4.7; 73 3.3; 78 2.6; 83 2.2; 89 1.9; 95 1.5; 102 1.1; 109 0.6; 117 0.1; 125 -0.5; 134 -0.9; 143 -1.1; 153 -1.2; 164 -1.3; 175 -1.4; 188 -1.7; 201 -1.5; 215 -1.4; 230 -1.5; 246 -1.5; 263 -1.3; 282 -1.2; 301 -1.1; 323 -0.9; 345 -0.8; 369 -0.7; 395 -0.6; 423 -0.3; 452 -0.1; 484 -0.2; 518 -0.2; 554 1.2; 593 1.8; 635 1.0; 679 1.0; 726 0.9; 777 0.8; 832 0.5; 890 0.2; 952 -0.0; 1019 -0.0; 1090 -0.3; 1167 -0.5; 1248 -0.7; 1336 -0.6; 1429 -1.1; 1529 -1.6; 1636 -1.9; 1751 -2.5; 1873 -3.4; 2004 -4.2; 2145 -4.7; 2295 -4.5; 2455 -4.0; 2627 -3.2; 2811 -2.7; 3008 -2.4; 3219 -2.2; 3444 -2.2; 3685 -2.0; 3943 -2.1; 4219 -2.9; 4514 -3.0; 4830 -1.9; 5168 -2.0; 5530 -4.0; 5917 -5.7; 6331 -5.3; 6775 -3.8; 7249 -4.0; 7756 -4.4; 8299 -4.2; 8880 -3.4; 9502 -2.0; 10167 -0.4; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 -0.5
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K701 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 26 Hz    | 0.28 | 6.2 dB  |
| Peaking | 160 Hz   | 0.93 | -3.2 dB |
| Peaking | 2240 Hz  | 1.92 | -4.6 dB |
| Peaking | 6084 Hz  | 2.35 | -4.8 dB |
| Peaking | 8269 Hz  | 4.1  | -3.2 dB |
| Peaking | 477 Hz   | 1.12 | -1.2 dB |
| Peaking | 611 Hz   | 1.72 | 2.5 dB  |
| Peaking | 4584 Hz  | 3.11 | -1.8 dB |
| Peaking | 4998 Hz  | 6.97 | 2.6 dB  |
| Peaking | 11017 Hz | 4.4  | 0.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/AKG%20K701/AKG%20K701.png)