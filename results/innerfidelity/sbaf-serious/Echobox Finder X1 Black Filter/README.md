# Echobox Finder X1 Black Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.2dB
GraphicEQ: 10 -84; 20 -10.6; 22 -10.6; 23 -10.6; 25 -10.5; 26 -10.5; 28 -10.4; 30 -10.3; 32 -10.2; 35 -10.0; 37 -9.9; 40 -9.7; 42 -9.6; 45 -9.4; 49 -9.1; 52 -8.8; 56 -8.6; 59 -8.4; 64 -8.1; 68 -7.8; 73 -7.6; 78 -7.5; 83 -7.4; 89 -7.4; 95 -7.5; 102 -7.6; 109 -7.7; 117 -7.9; 125 -8.1; 134 -8.1; 143 -8.0; 153 -7.9; 164 -7.7; 175 -7.3; 188 -7.0; 201 -6.6; 215 -6.1; 230 -5.7; 246 -5.3; 263 -4.9; 282 -4.4; 301 -4.0; 323 -3.6; 345 -3.1; 369 -2.8; 395 -2.4; 423 -1.9; 452 -1.6; 484 -1.3; 518 -1.0; 554 -0.5; 593 -0.0; 635 0.2; 679 0.3; 726 0.4; 777 0.7; 832 0.5; 890 0.4; 952 0.2; 1019 -0.1; 1090 -0.4; 1167 -0.6; 1248 -0.9; 1336 -1.4; 1429 -1.9; 1529 -2.4; 1636 -2.8; 1751 -3.0; 1873 -3.1; 2004 -3.2; 2145 -3.3; 2295 -3.5; 2455 -3.4; 2627 -3.7; 2811 -4.4; 3008 -4.8; 3219 -5.2; 3444 -5.4; 3685 -5.6; 3943 -6.0; 4219 -7.2; 4514 -8.4; 4830 -9.1; 5168 -9.6; 5530 -10.6; 5917 -11.3; 6331 -11.5; 6775 -9.5; 7249 -7.9; 7756 -7.2; 8299 -7.6; 8880 -8.9; 9502 -9.9; 10167 -9.0; 10879 -5.2; 11640 -0.7; 12455 0.0; 13327 -0.9; 14260 -4.0; 15258 -4.2; 16326 -0.9; 17469 0.0; 18692 0.0; 20000 -0.6
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-1.2dB` and instead set Global volume in the UI for both channels to **-12**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Echobox Finder X1 Black Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 8 Hz     | 0.71 | -10.1 dB |
| Peaking | 32 Hz    | 0.36 | -8.5 dB  |
| Peaking | 166 Hz   | 0.85 | -5.7 dB  |
| Peaking | 5666 Hz  | 0.83 | -10.4 dB |
| Peaking | 9674 Hz  | 5.29 | -5.9 dB  |
| Peaking | 804 Hz   | 1.8  | 1.7 dB   |
| Peaking | 1793 Hz  | 1.76 | -1.5 dB  |
| Peaking | 3916 Hz  | 5.73 | 1.3 dB   |
| Peaking | 12331 Hz | 4.99 | 3.7 dB   |
| Peaking | 14825 Hz | 4.98 | -4.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Echobox%20Finder%20X1%20Black%20Filter/Echobox%20Finder%20X1%20Black%20Filter.png)