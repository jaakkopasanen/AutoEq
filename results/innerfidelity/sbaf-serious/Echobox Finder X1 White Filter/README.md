# Echobox Finder X1 White Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.4dB
GraphicEQ: 10 -84; 20 -10.4; 22 -10.3; 23 -10.3; 25 -10.2; 26 -10.2; 28 -10.1; 30 -10.0; 32 -9.9; 35 -9.7; 37 -9.6; 40 -9.4; 42 -9.3; 45 -9.0; 49 -8.7; 52 -8.5; 56 -8.3; 59 -8.1; 64 -7.8; 68 -7.6; 73 -7.3; 78 -7.2; 83 -7.1; 89 -7.1; 95 -7.2; 102 -7.4; 109 -7.4; 117 -7.6; 125 -7.8; 134 -7.8; 143 -7.8; 153 -7.6; 164 -7.4; 175 -7.1; 188 -6.7; 201 -6.3; 215 -5.8; 230 -5.4; 246 -5.1; 263 -4.7; 282 -4.2; 301 -3.8; 323 -3.4; 345 -3.0; 369 -2.6; 395 -2.2; 423 -1.7; 452 -1.3; 484 -1.1; 518 -0.8; 554 -0.3; 593 0.1; 635 0.4; 679 0.4; 726 0.6; 777 0.8; 832 0.7; 890 0.5; 952 0.3; 1019 -0.0; 1090 -0.3; 1167 -0.6; 1248 -0.9; 1336 -1.4; 1429 -1.9; 1529 -2.3; 1636 -2.7; 1751 -3.0; 1873 -3.0; 2004 -2.9; 2145 -3.0; 2295 -3.0; 2455 -2.8; 2627 -2.9; 2811 -3.2; 3008 -3.4; 3219 -3.7; 3444 -4.1; 3685 -4.6; 3943 -5.2; 4219 -6.6; 4514 -7.6; 4830 -7.9; 5168 -7.8; 5530 -8.3; 5917 -8.2; 6331 -8.7; 6775 -7.4; 7249 -5.9; 7756 -4.6; 8299 -3.7; 8880 -3.5; 9502 -4.5; 10167 -6.4; 10879 -7.2; 11640 -5.4; 12455 -2.7; 13327 -1.9; 14260 -3.4; 15258 -3.9; 16326 -1.2; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-1.4dB` and instead set Global volume in the UI for both channels to **-14**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Echobox Finder X1 White Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 9 Hz     | 0.75 | -9.9 dB |
| Peaking | 33 Hz    | 0.38 | -8.1 dB |
| Peaking | 166 Hz   | 0.87 | -5.5 dB |
| Peaking | 5381 Hz  | 0.82 | -8.0 dB |
| Peaking | 10977 Hz | 4.07 | -5.1 dB |
| Peaking | 782 Hz   | 1.92 | 1.7 dB  |
| Peaking | 1739 Hz  | 2.16 | -1.8 dB |
| Peaking | 3473 Hz  | 3.82 | 1.0 dB  |
| Peaking | 8423 Hz  | 6.63 | 1.7 dB  |
| Peaking | 15040 Hz | 5.23 | -3.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Echobox%20Finder%20X1%20White%20Filter/Echobox%20Finder%20X1%20White%20Filter.png)