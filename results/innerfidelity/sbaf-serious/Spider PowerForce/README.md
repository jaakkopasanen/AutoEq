# Spider PowerForce

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -0.8; 22 -1.6; 23 -2.0; 25 -2.6; 26 -2.9; 28 -3.5; 30 -4.0; 32 -4.4; 35 -5.0; 37 -5.4; 40 -5.8; 42 -6.1; 45 -6.5; 49 -7.0; 52 -7.2; 56 -7.6; 59 -7.8; 64 -8.1; 68 -8.2; 73 -8.4; 78 -8.6; 83 -8.7; 89 -8.8; 95 -8.9; 102 -8.9; 109 -8.8; 117 -8.9; 125 -8.9; 134 -8.9; 143 -8.9; 153 -8.7; 164 -8.3; 175 -7.8; 188 -7.3; 201 -6.7; 215 -5.8; 230 -5.1; 246 -3.4; 263 -2.1; 282 -1.7; 301 -2.2; 323 -2.5; 345 -2.7; 369 -2.7; 395 -2.9; 423 -3.1; 452 -3.1; 484 -3.1; 518 -2.8; 554 -2.5; 593 -1.9; 635 -1.6; 679 -0.7; 726 0.1; 777 -0.2; 832 -0.1; 890 -0.2; 952 -0.0; 1019 0.1; 1090 0.2; 1167 0.4; 1248 0.4; 1336 0.1; 1429 -0.0; 1529 -0.2; 1636 -0.6; 1751 -0.8; 1873 -0.8; 2004 -0.9; 2145 -1.0; 2295 -1.0; 2455 -0.5; 2627 -0.1; 2811 0.5; 3008 1.2; 3219 1.7; 3444 3.0; 3685 4.8; 3943 6.0; 4219 6.0; 4514 5.4; 4830 -2.1; 5168 0.2; 5530 5.3; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999017734476dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Spider PowerForce ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 70 Hz   | 0.57 | -7.8 dB |
| Peaking | 156 Hz  | 1.35 | -5.0 dB |
| Peaking | 477 Hz  | 2.71 | -2.5 dB |
| Peaking | 3978 Hz | 4.75 | 6.6 dB  |
| Peaking | 6117 Hz | 5.2  | 6.4 dB  |
| Peaking | 262 Hz  | 2.01 | -2.0 dB |
| Peaking | 272 Hz  | 4.37 | 3.6 dB  |
| Peaking | 1716 Hz | 0.77 | 1.4 dB  |
| Peaking | 1985 Hz | 1.67 | -2.5 dB |
| Peaking | 8581 Hz | 2.74 | -0.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Spider%20PowerForce/Spider%20PowerForce.png)