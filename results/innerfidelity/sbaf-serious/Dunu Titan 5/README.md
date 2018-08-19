# Dunu Titan 5

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.1dB
GraphicEQ: 10 -84; 20 -4.2; 22 -4.3; 23 -4.3; 25 -4.4; 26 -4.4; 28 -4.4; 30 -4.4; 32 -4.5; 35 -4.5; 37 -4.6; 40 -4.6; 42 -4.6; 45 -4.7; 49 -4.7; 52 -4.8; 56 -4.9; 59 -5.0; 64 -5.1; 68 -5.2; 73 -5.3; 78 -5.4; 83 -5.5; 89 -5.6; 95 -5.8; 102 -5.8; 109 -5.7; 117 -5.7; 125 -5.7; 134 -5.6; 143 -5.5; 153 -5.4; 164 -5.3; 175 -5.1; 188 -4.8; 201 -4.6; 215 -4.3; 230 -4.1; 246 -3.8; 263 -3.5; 282 -3.1; 301 -2.8; 323 -2.5; 345 -2.1; 369 -1.8; 395 -1.6; 423 -1.3; 452 -0.9; 484 -0.3; 518 -0.3; 554 -0.1; 593 0.4; 635 0.8; 679 0.7; 726 0.8; 777 1.0; 832 0.8; 890 0.5; 952 0.2; 1019 -0.1; 1090 -0.5; 1167 -0.8; 1248 -1.2; 1336 -1.7; 1429 -2.3; 1529 -2.9; 1636 -3.4; 1751 -3.7; 1873 -3.9; 2004 -4.1; 2145 -4.3; 2295 -4.4; 2455 -4.1; 2627 -3.7; 2811 -2.9; 3008 -1.4; 3219 0.2; 3444 1.7; 3685 2.0; 3943 1.4; 4219 -0.4; 4514 -2.2; 4830 -3.7; 5168 -5.3; 5530 -7.9; 5917 -7.8; 6331 -4.4; 6775 -1.1; 7249 0.7; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.2; 10167 -1.6; 10879 -1.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.1024970088945363dB` and instead set Global volume in the UI for both channels to **-21**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dunu Titan 5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -0.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 32 Hz   | 0.34 | -4.2 dB |
| Peaking | 120 Hz  | 0.9  | -3.7 dB |
| Peaking | 227 Hz  | 1.51 | -2.2 dB |
| Peaking | 2048 Hz | 2.11 | -4.8 dB |
| Peaking | 5669 Hz | 5.3  | -9.0 dB |
| Peaking | 744 Hz  | 2.44 | 1.6 dB  |
| Peaking | 2699 Hz | 5.37 | -1.6 dB |
| Peaking | 3602 Hz | 3.15 | 4.9 dB  |
| Peaking | 4596 Hz | 0.83 | -1.8 dB |
| Peaking | 7393 Hz | 4.33 | 2.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Dunu%20Titan%205/Dunu%20Titan%205.png)