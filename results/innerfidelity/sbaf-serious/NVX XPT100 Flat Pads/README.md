# NVX XPT100 Flat Pads

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 5.9; 25 5.7; 26 5.5; 28 5.3; 30 5.0; 32 4.8; 35 4.5; 37 4.3; 40 4.1; 42 4.0; 45 3.9; 49 3.8; 52 3.7; 56 3.6; 59 3.5; 64 3.3; 68 3.2; 73 3.0; 78 2.8; 83 2.6; 89 2.3; 95 2.0; 102 1.7; 109 1.6; 117 1.4; 125 1.2; 134 0.8; 143 0.2; 153 -0.4; 164 -0.1; 175 0.4; 188 -0.2; 201 -0.2; 215 0.0; 230 0.7; 246 1.6; 263 2.9; 282 4.4; 301 4.9; 323 4.4; 345 3.6; 369 2.9; 395 2.4; 423 2.1; 452 1.6; 484 1.1; 518 0.9; 554 1.0; 593 1.0; 635 1.0; 679 0.7; 726 0.7; 777 0.9; 832 1.1; 890 0.7; 952 0.2; 1019 -0.1; 1090 -0.3; 1167 -0.6; 1248 -0.8; 1336 -1.4; 1429 -2.3; 1529 -3.1; 1636 -3.4; 1751 -3.9; 1873 -4.2; 2004 -4.2; 2145 -4.1; 2295 -3.7; 2455 -3.0; 2627 -2.7; 2811 -2.1; 3008 0.4; 3219 1.8; 3444 -0.3; 3685 -1.0; 3943 -1.0; 4219 -0.2; 4514 0.5; 4830 1.8; 5168 3.7; 5530 5.2; 5917 5.5; 6331 4.3; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -1.0; 20000 -5.1
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NVX XPT100 Flat Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.71 | 5.8 dB  |
| Peaking | 66 Hz   | 1.44 | 2.2 dB  |
| Peaking | 320 Hz  | 2.48 | 4.7 dB  |
| Peaking | 1971 Hz | 1.92 | -4.8 dB |
| Peaking | 5850 Hz | 3.45 | 6.2 dB  |
| Peaking | 196 Hz  | 2.89 | -1.3 dB |
| Peaking | 1610 Hz | 0.57 | 2.2 dB  |
| Peaking | 1460 Hz | 1.78 | -2.4 dB |
| Peaking | 3166 Hz | 6.39 | 5.9 dB  |
| Peaking | 3123 Hz | 1.87 | -4.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NVX%20XPT100%20Flat%20Pads/NVX%20XPT100%20Flat%20Pads.png)