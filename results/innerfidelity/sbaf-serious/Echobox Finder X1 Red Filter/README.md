# Echobox Finder X1 Red Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.4dB
GraphicEQ: 10 -84; 20 -10.2; 22 -10.2; 23 -10.2; 25 -10.2; 26 -10.1; 28 -10.1; 30 -10.0; 32 -9.9; 35 -9.7; 37 -9.5; 40 -9.3; 42 -9.2; 45 -9.0; 49 -8.7; 52 -8.5; 56 -8.2; 59 -8.0; 64 -7.7; 68 -7.5; 73 -7.3; 78 -7.2; 83 -7.1; 89 -7.1; 95 -7.2; 102 -7.3; 109 -7.4; 117 -7.6; 125 -7.8; 134 -7.8; 143 -7.8; 153 -7.6; 164 -7.4; 175 -7.0; 188 -6.6; 201 -6.3; 215 -5.8; 230 -5.4; 246 -5.0; 263 -4.6; 282 -4.2; 301 -3.7; 323 -3.3; 345 -2.9; 369 -2.5; 395 -2.2; 423 -1.7; 452 -1.3; 484 -1.0; 518 -0.8; 554 -0.3; 593 0.1; 635 0.4; 679 0.4; 726 0.6; 777 0.8; 832 0.7; 890 0.5; 952 0.3; 1019 -0.1; 1090 -0.3; 1167 -0.6; 1248 -0.9; 1336 -1.4; 1429 -1.9; 1529 -2.4; 1636 -2.8; 1751 -3.0; 1873 -3.1; 2004 -3.1; 2145 -3.2; 2295 -3.4; 2455 -3.3; 2627 -3.6; 2811 -4.1; 3008 -4.8; 3219 -5.7; 3444 -6.2; 3685 -6.4; 3943 -6.4; 4219 -7.3; 4514 -8.0; 4830 -8.2; 5168 -8.3; 5530 -9.6; 5917 -10.7; 6331 -12.0; 6775 -10.4; 7249 -8.2; 7756 -6.1; 8299 -4.7; 8880 -4.1; 9502 -4.9; 10167 -7.0; 10879 -8.2; 11640 -6.5; 12455 -3.3; 13327 -2.1; 14260 -3.8; 15258 -4.8; 16326 -2.4; 17469 -0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-1.4dB` and instead set Global volume in the UI for both channels to **-14**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Echobox Finder X1 Red Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 8 Hz     | 0.66 | -9.7 dB |
| Peaking | 33 Hz    | 0.38 | -8.1 dB |
| Peaking | 165 Hz   | 0.89 | -5.5 dB |
| Peaking | 5638 Hz  | 0.74 | -9.7 dB |
| Peaking | 11070 Hz | 5.16 | -4.9 dB |
| Peaking | 793 Hz   | 1.87 | 1.8 dB  |
| Peaking | 1737 Hz  | 2.12 | -1.4 dB |
| Peaking | 6426 Hz  | 4.04 | -6.3 dB |
| Peaking | 7022 Hz  | 1.55 | 3.7 dB  |
| Peaking | 32667 Hz | 4.62 | -4.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Echobox%20Finder%20X1%20Red%20Filter/Echobox%20Finder%20X1%20Red%20Filter.png)