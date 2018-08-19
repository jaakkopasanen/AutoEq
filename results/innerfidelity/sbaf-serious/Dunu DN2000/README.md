# Dunu DN2000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -4.4; 22 -4.4; 23 -4.3; 25 -4.2; 26 -4.2; 28 -4.1; 30 -3.9; 32 -3.8; 35 -3.7; 37 -3.6; 40 -3.4; 42 -3.3; 45 -3.2; 49 -3.1; 52 -3.0; 56 -2.9; 59 -2.9; 64 -2.8; 68 -2.8; 73 -2.9; 78 -2.9; 83 -3.0; 89 -3.1; 95 -3.1; 102 -3.2; 109 -3.1; 117 -3.1; 125 -3.2; 134 -3.3; 143 -3.3; 153 -3.3; 164 -3.4; 175 -3.3; 188 -3.3; 201 -3.3; 215 -3.2; 230 -3.1; 246 -3.0; 263 -3.0; 282 -2.8; 301 -2.7; 323 -2.6; 345 -2.5; 369 -2.4; 395 -2.3; 423 -2.0; 452 -1.9; 484 -1.7; 518 -1.6; 554 -1.3; 593 -0.9; 635 -0.7; 679 -0.7; 726 -0.5; 777 -0.1; 832 -0.1; 890 -0.1; 952 -0.1; 1019 0.0; 1090 0.0; 1167 0.2; 1248 0.2; 1336 0.2; 1429 0.1; 1529 0.2; 1636 0.3; 1751 0.8; 1873 1.5; 2004 2.2; 2145 2.8; 2295 3.4; 2455 3.9; 2627 4.0; 2811 4.3; 3008 5.5; 3219 6.0; 3444 6.0; 3685 6.0; 3943 4.4; 4219 1.3; 4514 -1.5; 4830 -2.4; 5168 -0.3; 5530 2.3; 5917 4.0; 6331 4.1; 6775 3.5; 7249 1.3; 7756 -1.4; 8299 -4.6; 8880 -6.4; 9502 -5.8; 10167 -3.1; 10879 -0.2; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999996093441dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dunu DN2000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.3dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 0.31 | -4.4 dB |
| Peaking | 191 Hz  | 0.49 | -3.1 dB |
| Peaking | 3090 Hz | 2.02 | 6.3 dB  |
| Peaking | 6474 Hz | 5.09 | 5.1 dB  |
| Peaking | 8969 Hz | 3.83 | -7.5 dB |
| Peaking | 1616 Hz | 4.76 | -0.3 dB |
| Peaking | 2139 Hz | 5.09 | 1.3 dB  |
| Peaking | 3819 Hz | 6.62 | 3.3 dB  |
| Peaking | 4746 Hz | 3.82 | -4.9 dB |
| Peaking | 5664 Hz | 5.79 | 2.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Dunu%20DN2000/Dunu%20DN2000.png)