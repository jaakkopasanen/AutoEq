# Spider PowerForce

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -0.8; 22 -1.6; 23 -1.9; 25 -2.6; 26 -2.9; 28 -3.4; 30 -3.9; 32 -4.4; 35 -5.0; 37 -5.3; 40 -5.7; 42 -6.0; 45 -6.4; 49 -6.7; 52 -7.0; 56 -7.2; 59 -7.4; 64 -7.5; 68 -7.6; 73 -7.7; 78 -7.8; 83 -7.9; 89 -8.0; 95 -8.1; 102 -8.3; 109 -8.4; 117 -8.7; 125 -8.9; 134 -9.0; 143 -9.1; 153 -9.0; 164 -8.5; 175 -8.0; 188 -7.5; 201 -6.9; 215 -6.0; 230 -5.2; 246 -3.5; 263 -2.1; 282 -1.8; 301 -2.3; 323 -2.6; 345 -2.7; 369 -2.8; 395 -2.9; 423 -3.1; 452 -3.1; 484 -3.1; 518 -2.8; 554 -2.5; 593 -1.9; 635 -1.6; 679 -0.7; 726 0.1; 777 -0.2; 832 -0.1; 890 -0.2; 952 -0.0; 1019 0.1; 1090 0.2; 1167 0.4; 1248 0.4; 1336 0.1; 1429 -0.0; 1529 -0.2; 1636 -0.6; 1751 -0.8; 1873 -0.8; 2004 -0.9; 2145 -1.0; 2295 -1.0; 2455 -0.5; 2627 -0.1; 2811 0.5; 3008 1.2; 3219 1.7; 3444 3.0; 3685 4.8; 3943 6.0; 4219 6.0; 4514 5.4; 4830 -2.1; 5168 0.2; 5530 5.3; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Spider PowerForce ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 64 Hz   | 0.57 | -6.9 dB |
| Peaking | 154 Hz  | 1.28 | -6.1 dB |
| Peaking | 476 Hz  | 2.65 | -2.5 dB |
| Peaking | 3979 Hz | 4.77 | 6.6 dB  |
| Peaking | 6115 Hz | 5.24 | 6.4 dB  |
| Peaking | 262 Hz  | 1.9  | -1.7 dB |
| Peaking | 270 Hz  | 4.43 | 3.2 dB  |
| Peaking | 1999 Hz | 1.66 | -2.5 dB |
| Peaking | 8626 Hz | 2.56 | -0.5 dB |
| Peaking | 1725 Hz | 0.77 | 1.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Spider%20PowerForce/Spider%20PowerForce.png)