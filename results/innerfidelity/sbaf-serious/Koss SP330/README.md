# Koss SP330

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.2dB
GraphicEQ: 10 -84; 20 -3.8; 22 -3.9; 23 -3.9; 25 -4.0; 26 -4.1; 28 -4.1; 30 -4.2; 32 -4.3; 35 -4.4; 37 -4.4; 40 -4.4; 42 -4.4; 45 -4.4; 49 -4.4; 52 -4.4; 56 -4.3; 59 -4.3; 64 -4.2; 68 -4.1; 73 -4.2; 78 -4.5; 83 -4.7; 89 -4.8; 95 -4.8; 102 -4.8; 109 -4.7; 117 -4.6; 125 -4.5; 134 -4.3; 143 -4.1; 153 -3.8; 164 -3.7; 175 -3.1; 188 -2.5; 201 -2.2; 215 -2.0; 230 -1.7; 246 -1.1; 263 -0.5; 282 0.0; 301 0.3; 323 -0.0; 345 -0.5; 369 -1.1; 395 -1.6; 423 -1.8; 452 -1.9; 484 -2.1; 518 -2.2; 554 -2.0; 593 -1.7; 635 -1.5; 679 -1.5; 726 -1.0; 777 -0.2; 832 -0.5; 890 -0.5; 952 -0.2; 1019 0.1; 1090 0.4; 1167 0.8; 1248 1.0; 1336 1.1; 1429 1.0; 1529 0.9; 1636 0.8; 1751 0.8; 1873 1.0; 2004 1.3; 2145 1.2; 2295 1.1; 2455 1.2; 2627 1.1; 2811 0.7; 3008 0.6; 3219 0.8; 3444 0.9; 3685 0.2; 3943 -0.2; 4219 -1.6; 4514 -2.3; 4830 -1.6; 5168 0.5; 5530 2.5; 5917 4.2; 6331 5.1; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.8; 9502 -1.0; 10167 -0.2; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -0.4; 20000 -0.6
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.207041970096766dB` and instead set Global volume in the UI for both channels to **-52**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss SP330 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.5dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.43 | -4.2 dB |
| Peaking | 120 Hz  | 1.14 | -3.3 dB |
| Peaking | 520 Hz  | 2.82 | -2.2 dB |
| Peaking | 4575 Hz | 6.67 | -3.3 dB |
| Peaking | 6220 Hz | 4.3  | 5.5 dB  |
| Peaking | 299 Hz  | 3    | 2.9 dB  |
| Peaking | 306 Hz  | 1.43 | -1.6 dB |
| Peaking | 812 Hz  | 1.87 | -0.7 dB |
| Peaking | 1690 Hz | 0.74 | 1.3 dB  |
| Peaking | 9089 Hz | 3.88 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20SP330/Koss%20SP330.png)