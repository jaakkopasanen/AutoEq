# Dunu Titan 3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.1dB
GraphicEQ: 10 -84; 20 -1.4; 22 -1.4; 23 -1.4; 25 -1.4; 26 -1.4; 28 -1.5; 30 -1.6; 32 -1.6; 35 -1.7; 37 -1.7; 40 -1.8; 42 -1.9; 45 -2.0; 49 -2.1; 52 -2.1; 56 -2.1; 59 -2.2; 64 -2.5; 68 -2.7; 73 -2.9; 78 -3.1; 83 -3.2; 89 -3.4; 95 -3.6; 102 -3.7; 109 -3.7; 117 -3.7; 125 -3.8; 134 -3.9; 143 -3.8; 153 -3.8; 164 -3.7; 175 -3.5; 188 -3.4; 201 -3.3; 215 -3.0; 230 -2.8; 246 -2.6; 263 -2.4; 282 -2.0; 301 -1.9; 323 -1.6; 345 -1.4; 369 -1.1; 395 -0.9; 423 -0.0; 452 0.3; 484 0.1; 518 0.2; 554 0.5; 593 0.9; 635 1.0; 679 1.0; 726 1.0; 777 1.0; 832 0.9; 890 0.6; 952 0.3; 1019 -0.0; 1090 -0.4; 1167 -0.7; 1248 -1.1; 1336 -1.7; 1429 -2.3; 1529 -2.9; 1636 -3.5; 1751 -3.9; 1873 -4.2; 2004 -4.5; 2145 -4.8; 2295 -5.1; 2455 -4.7; 2627 -4.1; 2811 -2.9; 3008 -1.0; 3219 0.9; 3444 2.1; 3685 2.2; 3943 1.2; 4219 -1.4; 4514 -4.1; 4830 -7.4; 5168 -8.9; 5530 -5.1; 5917 -0.1; 6331 2.9; 6775 3.7; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.087731153103866dB` and instead set Global volume in the UI for both channels to **-40**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dunu Titan 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -3.8dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 69 Hz   | 0.52 | -2.3 dB  |
| Peaking | 163 Hz  | 1.04 | -2.8 dB  |
| Peaking | 2075 Hz | 2.28 | -5.4 dB  |
| Peaking | 5126 Hz | 6.02 | -10.4 dB |
| Peaking | 6539 Hz | 4.5  | 4.9 dB   |
| Peaking | 20 Hz   | 1.49 | -0.7 dB  |
| Peaking | 716 Hz  | 1.71 | 1.6 dB   |
| Peaking | 1471 Hz | 4.99 | -1.1 dB  |
| Peaking | 3481 Hz | 1.44 | -3.1 dB  |
| Peaking | 3557 Hz | 3.5  | 7.0 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Dunu%20Titan%203/Dunu%20Titan%203.png)