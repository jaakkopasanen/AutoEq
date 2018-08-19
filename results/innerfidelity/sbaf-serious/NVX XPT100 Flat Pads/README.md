# NVX XPT100 Flat Pads

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 5.9; 25 5.7; 26 5.5; 28 5.2; 30 5.0; 32 4.7; 35 4.4; 37 4.2; 40 4.0; 42 3.9; 45 3.7; 49 3.6; 52 3.5; 56 3.3; 59 3.1; 64 2.8; 68 2.6; 73 2.3; 78 2.0; 83 1.8; 89 1.5; 95 1.2; 102 1.1; 109 1.2; 117 1.2; 125 1.2; 134 0.9; 143 0.4; 153 -0.2; 164 0.2; 175 0.6; 188 -0.0; 201 -0.0; 215 0.2; 230 0.8; 246 1.7; 263 3.0; 282 4.4; 301 5.0; 323 4.4; 345 3.6; 369 2.9; 395 2.4; 423 2.1; 452 1.6; 484 1.1; 518 0.9; 554 1.0; 593 1.0; 635 1.0; 679 0.7; 726 0.7; 777 0.9; 832 1.1; 890 0.7; 952 0.2; 1019 -0.1; 1090 -0.3; 1167 -0.6; 1248 -0.8; 1336 -1.4; 1429 -2.3; 1529 -3.1; 1636 -3.4; 1751 -3.9; 1873 -4.2; 2004 -4.2; 2145 -4.1; 2295 -3.7; 2455 -3.0; 2627 -2.7; 2811 -2.1; 3008 0.4; 3219 1.8; 3444 -0.3; 3685 -1.0; 3943 -1.0; 4219 -0.2; 4514 0.5; 4830 1.8; 5168 3.7; 5530 5.2; 5917 5.5; 6331 4.3; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -1.0; 20000 -5.1
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NVX XPT100 Flat Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 22 Hz   | 0.79 | 5.8 dB  |
| Peaking | 56 Hz   | 1.3  | 1.8 dB  |
| Peaking | 319 Hz  | 2.33 | 4.8 dB  |
| Peaking | 1971 Hz | 1.91 | -4.8 dB |
| Peaking | 5861 Hz | 3.45 | 6.2 dB  |
| Peaking | 204 Hz  | 4.34 | -1.2 dB |
| Peaking | 789 Hz  | 1.39 | 0.9 dB  |
| Peaking | 1498 Hz | 7.16 | -0.9 dB |
| Peaking | 3181 Hz | 7.27 | 5.4 dB  |
| Peaking | 3248 Hz | 2.62 | -2.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NVX%20XPT100%20Flat%20Pads/NVX%20XPT100%20Flat%20Pads.png)