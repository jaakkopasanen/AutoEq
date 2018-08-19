# Dunu DN900

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -2.7; 22 -2.5; 23 -2.4; 25 -2.2; 26 -2.1; 28 -1.9; 30 -1.8; 32 -1.6; 35 -1.4; 37 -1.3; 40 -1.1; 42 -1.1; 45 -0.9; 49 -0.8; 52 -0.7; 56 -0.6; 59 -0.6; 64 -0.6; 68 -0.7; 73 -0.7; 78 -0.8; 83 -0.9; 89 -1.0; 95 -1.2; 102 -1.3; 109 -1.3; 117 -1.3; 125 -1.5; 134 -1.6; 143 -1.7; 153 -1.8; 164 -1.8; 175 -1.8; 188 -1.8; 201 -1.9; 215 -1.8; 230 -1.7; 246 -1.7; 263 -1.7; 282 -1.6; 301 -1.6; 323 -1.4; 345 -1.4; 369 -1.3; 395 -1.2; 423 -1.0; 452 -0.9; 484 -0.9; 518 -0.8; 554 -0.6; 593 -0.2; 635 -0.2; 679 -0.2; 726 -0.1; 777 0.0; 832 -0.1; 890 -0.2; 952 -0.1; 1019 -0.0; 1090 -0.2; 1167 -0.5; 1248 -0.8; 1336 -1.1; 1429 -1.5; 1529 -1.8; 1636 -1.9; 1751 -1.7; 1873 -1.3; 2004 -0.5; 2145 0.4; 2295 1.6; 2455 3.2; 2627 4.6; 2811 5.8; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999814357dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dunu DN900 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.92 | -2.5 dB |
| Peaking | 154 Hz  | 0.85 | -1.4 dB |
| Peaking | 308 Hz  | 1    | -1.1 dB |
| Peaking | 1732 Hz | 1.87 | -4.3 dB |
| Peaking | 3743 Hz | 0.86 | 7.2 dB  |
| Peaking | 2234 Hz | 5.73 | -0.8 dB |
| Peaking | 2778 Hz | 3.59 | 1.5 dB  |
| Peaking | 3750 Hz | 2.84 | -1.2 dB |
| Peaking | 6269 Hz | 2.42 | 5.3 dB  |
| Peaking | 7389 Hz | 1.51 | -4.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Dunu%20DN900/Dunu%20DN900.png)