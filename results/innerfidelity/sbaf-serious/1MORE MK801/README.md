# 1MORE MK801

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 5.7; 22 5.0; 23 4.6; 25 4.0; 26 3.7; 28 3.1; 30 2.6; 32 2.2; 35 1.7; 37 1.4; 40 1.0; 42 0.8; 45 0.4; 49 0.1; 52 -0.1; 56 -0.3; 59 -0.5; 64 -0.8; 68 -1.0; 73 -1.2; 78 -1.5; 83 -1.7; 89 -2.0; 95 -2.1; 102 -2.3; 109 -2.3; 117 -2.3; 125 -2.5; 134 -2.7; 143 -2.8; 153 -3.0; 164 -2.9; 175 -2.6; 188 -2.9; 201 -3.1; 215 -3.1; 230 -3.0; 246 -3.0; 263 -2.9; 282 -2.5; 301 -2.0; 323 -1.5; 345 -1.1; 369 -0.6; 395 -0.2; 423 0.5; 452 1.2; 484 1.8; 518 2.2; 554 2.3; 593 2.4; 635 2.2; 679 1.7; 726 1.2; 777 1.6; 832 2.4; 890 1.5; 952 0.5; 1019 -0.1; 1090 -0.2; 1167 0.1; 1248 0.4; 1336 1.0; 1429 1.4; 1529 1.8; 1636 2.4; 1751 3.1; 1873 3.8; 2004 4.4; 2145 4.6; 2295 4.6; 2455 4.8; 2627 4.8; 2811 4.4; 3008 4.4; 3219 4.3; 3444 4.7; 3685 5.2; 3943 4.8; 4219 2.4; 4514 2.7; 4830 2.8; 5168 4.5; 5530 5.9; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.079209687832978dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `1MORE MK801 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.95 | 6.0 dB  |
| Peaking | 477 Hz  | 0.22 | -5.3 dB |
| Peaking | 571 Hz  | 0.89 | 7.1 dB  |
| Peaking | 2463 Hz | 0.82 | 6.9 dB  |
| Peaking | 5888 Hz | 3.98 | 5.3 dB  |
| Peaking | 854 Hz  | 6.48 | 2.8 dB  |
| Peaking | 870 Hz  | 2.51 | -1.4 dB |
| Peaking | 3802 Hz | 7.66 | 2.4 dB  |
| Peaking | 4239 Hz | 7.58 | -1.5 dB |
| Peaking | 8449 Hz | 3.73 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/1MORE%20MK801/1MORE%20MK801.png)