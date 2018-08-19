# Zoukbox ZDY10 Bass

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.2dB
GraphicEQ: 10 -84; 20 -7.2; 22 -7.3; 23 -7.4; 25 -7.6; 26 -7.6; 28 -7.8; 30 -7.9; 32 -8.0; 35 -8.1; 37 -8.1; 40 -8.2; 42 -8.3; 45 -8.4; 49 -8.5; 52 -8.5; 56 -8.6; 59 -8.8; 64 -8.9; 68 -9.0; 73 -9.2; 78 -9.3; 83 -9.5; 89 -9.6; 95 -9.8; 102 -9.8; 109 -9.7; 117 -9.7; 125 -9.7; 134 -9.7; 143 -9.6; 153 -9.5; 164 -9.3; 175 -9.1; 188 -8.9; 201 -8.6; 215 -8.3; 230 -7.9; 246 -7.6; 263 -7.3; 282 -6.8; 301 -6.4; 323 -6.0; 345 -5.5; 369 -5.0; 395 -4.7; 423 -4.0; 452 -3.6; 484 -3.2; 518 -2.8; 554 -2.0; 593 -1.3; 635 -1.1; 679 -0.9; 726 -0.5; 777 -0.1; 832 0.0; 890 0.1; 952 0.1; 1019 0.0; 1090 -0.1; 1167 -0.2; 1248 -0.3; 1336 -0.6; 1429 -1.0; 1529 -1.3; 1636 -1.6; 1751 -1.7; 1873 -1.7; 2004 -1.9; 2145 -2.2; 2295 -2.3; 2455 -2.5; 2627 -2.2; 2811 -2.4; 3008 -2.2; 3219 -2.0; 3444 -1.8; 3685 -2.5; 3943 -3.2; 4219 -4.9; 4514 -6.4; 4830 -6.9; 5168 -6.8; 5530 -5.7; 5917 -4.3; 6331 -3.3; 6775 -2.2; 7249 -1.5; 7756 -1.9; 8299 -2.5; 8880 -3.2; 9502 -4.0; 10167 -4.6; 10879 -4.0; 11640 -2.1; 12455 -0.4; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-0.17210658924167632dB` and instead set Global volume in the UI for both channels to **-1**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Zoukbox ZDY10 Bass ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-0.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -0.1dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 34 Hz    | 0.26 | -7.4 dB |
| Peaking | 142 Hz   | 0.67 | -5.4 dB |
| Peaking | 292 Hz   | 1.17 | -2.9 dB |
| Peaking | 4869 Hz  | 1.72 | -6.6 dB |
| Peaking | 10171 Hz | 3.54 | -4.5 dB |
| Peaking | 933 Hz   | 1.03 | 2.7 dB  |
| Peaking | 1422 Hz  | 0.4  | -2.0 dB |
| Peaking | 2365 Hz  | 2.29 | -0.5 dB |
| Peaking | 3654 Hz  | 3.24 | 2.1 dB  |
| Peaking | 6779 Hz  | 5.05 | 1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Zoukbox%20ZDY10%20Bass/Zoukbox%20ZDY10%20Bass.png)