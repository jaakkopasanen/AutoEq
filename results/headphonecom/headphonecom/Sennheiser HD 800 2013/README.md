# Sennheiser HD 800 2013

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.6dB
GraphicEQ: 10 -84; 20 -2.2; 22 -2.5; 23 -2.7; 25 -3.0; 26 -3.2; 28 -3.4; 30 -3.7; 32 -3.8; 35 -4.0; 37 -4.2; 40 -4.3; 42 -4.4; 45 -4.4; 49 -4.1; 52 -3.8; 56 -4.0; 59 -4.4; 64 -4.1; 68 -4.0; 73 -4.7; 78 -5.2; 83 -5.5; 89 -5.6; 95 -5.8; 102 -5.8; 109 -6.0; 117 -6.0; 125 -6.0; 134 -5.9; 143 -5.9; 153 -5.9; 164 -5.8; 175 -5.8; 188 -5.8; 201 -5.8; 215 -5.8; 230 -5.7; 246 -5.7; 263 -5.6; 282 -5.5; 301 -5.4; 323 -5.1; 345 -4.9; 369 -4.8; 395 -4.6; 423 -4.2; 452 -3.9; 484 -3.6; 518 -3.1; 554 -2.8; 593 -2.6; 635 -2.1; 679 -1.8; 726 -1.5; 777 -1.2; 832 -1.2; 890 -0.8; 952 -0.1; 1019 0.1; 1090 0.7; 1167 1.6; 1248 1.9; 1336 2.5; 1429 3.0; 1529 3.3; 1636 4.0; 1751 4.2; 1873 4.0; 2004 4.3; 2145 3.9; 2295 3.4; 2455 4.5; 2627 5.0; 2811 3.9; 3008 2.6; 3219 2.4; 3444 2.8; 3685 1.4; 3943 -0.2; 4219 0.3; 4514 1.6; 4830 2.2; 5168 1.4; 5530 -0.2; 5917 -4.4; 6331 -7.6; 6775 -4.3; 7249 -3.1; 7756 -3.5; 8299 -4.8; 8880 -6.4; 9502 -6.6; 10167 -3.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.6dB` and instead set Global volume in the UI for both channels to **-56**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 800 2013 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 73 Hz    | 0.21 | -3.6 dB |
| Peaking | 533 Hz   | 0.17 | -3.7 dB |
| Peaking | 1887 Hz  | 0.6  | 7.2 dB  |
| Peaking | 9003 Hz  | 3.8  | -7.4 dB |
| Peaking | 6325 Hz  | 6.54 | -8.1 dB |
| Peaking | 102 Hz   | 4.34 | -0.3 dB |
| Peaking | 2639 Hz  | 9.57 | 1.8 dB  |
| Peaking | 4428 Hz  | 2.34 | -3.1 dB |
| Peaking | 4835 Hz  | 4.2  | 4.3 dB  |
| Peaking | 10992 Hz | 7.74 | 1.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Sennheiser%20HD%20800%202013/Sennheiser%20HD%20800%202013.png)