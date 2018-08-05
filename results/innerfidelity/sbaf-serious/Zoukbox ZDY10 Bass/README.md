# Zoukbox ZDY10 Bass

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.6dB
GraphicEQ: 10 -84; 20 -7.1; 22 -7.3; 23 -7.3; 25 -7.4; 26 -7.5; 28 -7.6; 30 -7.7; 32 -7.7; 35 -7.8; 37 -7.8; 40 -7.8; 42 -7.8; 45 -7.8; 49 -7.8; 52 -7.7; 56 -7.7; 59 -7.7; 64 -7.6; 68 -7.6; 73 -7.6; 78 -7.7; 83 -7.8; 89 -8.1; 95 -8.4; 102 -8.7; 109 -9.0; 117 -9.3; 125 -9.7; 134 -10.0; 143 -10.0; 153 -10.0; 164 -9.8; 175 -9.6; 188 -9.3; 201 -9.1; 215 -8.7; 230 -8.3; 246 -7.9; 263 -7.5; 282 -7.0; 301 -6.5; 323 -6.1; 345 -5.6; 369 -5.1; 395 -4.7; 423 -4.1; 452 -3.6; 484 -3.3; 518 -2.8; 554 -2.0; 593 -1.3; 635 -1.1; 679 -0.9; 726 -0.5; 777 -0.1; 832 0.0; 890 0.1; 952 0.1; 1019 0.0; 1090 -0.1; 1167 -0.2; 1248 -0.3; 1336 -0.6; 1429 -1.0; 1529 -1.3; 1636 -1.6; 1751 -1.7; 1873 -1.7; 2004 -1.9; 2145 -2.2; 2295 -2.3; 2455 -2.5; 2627 -2.2; 2811 -2.4; 3008 -2.2; 3219 -2.0; 3444 -1.8; 3685 -2.5; 3943 -3.2; 4219 -4.9; 4514 -6.4; 4830 -6.9; 5168 -6.8; 5530 -5.7; 5917 -4.3; 6331 -3.3; 6775 -2.2; 7249 -1.5; 7756 -1.9; 8299 -2.5; 8880 -3.2; 9502 -4.0; 10167 -4.6; 10879 -4.0; 11640 -2.1; 12455 -0.4; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-0.6dB` and instead set Global volume in the UI for both channels to **-6**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Zoukbox ZDY10 Bass ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 6 Hz     | 1.49 | -6.5 dB |
| Peaking | 28 Hz    | 0.28 | -6.9 dB |
| Peaking | 181 Hz   | 0.65 | -8.1 dB |
| Peaking | 4874 Hz  | 1.76 | -6.6 dB |
| Peaking | 10165 Hz | 3.5  | -4.5 dB |
| Peaking | 421 Hz   | 1.44 | -1.3 dB |
| Peaking | 855 Hz   | 0.71 | 1.7 dB  |
| Peaking | 2014 Hz  | 1.27 | -2.7 dB |
| Peaking | 3638 Hz  | 3.95 | 1.6 dB  |
| Peaking | 1951 Hz  | 4.01 | 0.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Zoukbox%20ZDY10%20Bass/Zoukbox%20ZDY10%20Bass.png)