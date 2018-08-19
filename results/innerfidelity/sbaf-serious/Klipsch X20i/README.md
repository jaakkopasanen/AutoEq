# Klipsch X20i

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -0.4; 22 -0.5; 23 -0.5; 25 -0.6; 26 -0.7; 28 -0.8; 30 -0.9; 32 -1.0; 35 -1.1; 37 -1.1; 40 -1.2; 42 -1.3; 45 -1.4; 49 -1.5; 52 -1.7; 56 -1.8; 59 -2.0; 64 -2.2; 68 -2.4; 73 -2.7; 78 -3.0; 83 -3.2; 89 -3.4; 95 -3.7; 102 -3.9; 109 -3.9; 117 -4.1; 125 -4.2; 134 -4.4; 143 -4.5; 153 -4.5; 164 -4.6; 175 -4.5; 188 -4.5; 201 -4.5; 215 -4.4; 230 -4.2; 246 -4.1; 263 -4.0; 282 -3.8; 301 -3.6; 323 -3.4; 345 -3.1; 369 -2.9; 395 -2.7; 423 -2.3; 452 -2.1; 484 -1.9; 518 -1.6; 554 -1.2; 593 -0.7; 635 -0.5; 679 -0.3; 726 -0.0; 777 0.2; 832 0.3; 890 0.2; 952 0.2; 1019 0.0; 1090 -0.0; 1167 -0.2; 1248 -0.3; 1336 -0.6; 1429 -0.9; 1529 -1.2; 1636 -1.4; 1751 -1.5; 1873 -1.4; 2004 -1.3; 2145 -1.4; 2295 -1.5; 2455 -1.2; 2627 -1.0; 2811 -0.2; 3008 1.8; 3219 4.5; 3444 6.0; 3685 6.0; 3943 6.0; 4219 5.6; 4514 4.4; 4830 3.7; 5168 3.8; 5530 3.8; 5917 4.8; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999973023095dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch X20i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 131 Hz  | 0.6  | -4.0 dB |
| Peaking | 285 Hz  | 1.2  | -2.0 dB |
| Peaking | 2560 Hz | 1.45 | -4.2 dB |
| Peaking | 3652 Hz | 1.8  | 8.3 dB  |
| Peaking | 6212 Hz | 4.75 | 4.5 dB  |
| Peaking | 491 Hz  | 1.79 | -1.0 dB |
| Peaking | 732 Hz  | 0.91 | 1.1 dB  |
| Peaking | 1565 Hz | 3.56 | -0.9 dB |
| Peaking | 8257 Hz | 4.13 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Klipsch%20X20i/Klipsch%20X20i.png)