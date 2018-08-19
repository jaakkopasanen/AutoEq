# Bose AE2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -3.8; 22 -3.9; 23 -3.9; 25 -4.0; 26 -4.0; 28 -3.9; 30 -3.9; 32 -3.8; 35 -3.7; 37 -3.6; 40 -3.5; 42 -3.3; 45 -3.1; 49 -2.9; 52 -2.6; 56 -2.3; 59 -2.1; 64 -1.7; 68 -1.5; 73 -1.1; 78 -0.9; 83 -0.7; 89 -0.4; 95 -0.3; 102 -0.1; 109 0.2; 117 0.3; 125 0.1; 134 -0.5; 143 -1.3; 153 -1.9; 164 -0.1; 175 0.1; 188 -0.8; 201 -0.6; 215 -0.5; 230 0.2; 246 1.2; 263 2.3; 282 2.4; 301 2.3; 323 2.8; 345 3.3; 369 3.7; 395 4.0; 423 4.2; 452 4.2; 484 3.9; 518 3.7; 554 3.5; 593 3.4; 635 2.9; 679 2.2; 726 1.7; 777 1.1; 832 0.5; 890 0.1; 952 0.0; 1019 0.3; 1090 0.7; 1167 1.2; 1248 1.8; 1336 2.1; 1429 2.4; 1529 2.6; 1636 2.9; 1751 3.2; 1873 3.4; 2004 3.5; 2145 4.3; 2295 4.2; 2455 3.8; 2627 3.4; 2811 2.0; 3008 1.3; 3219 1.0; 3444 1.0; 3685 1.3; 3943 1.0; 4219 0.7; 4514 1.8; 4830 4.3; 5168 6.0; 5530 6.0; 5917 3.7; 6331 2.2; 6775 0.4; 7249 -0.5; 7756 0.1; 8299 -0.2; 8880 -1.3; 9502 -0.9; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.098269946750708dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bose AE2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.73 | -4.2 dB |
| Peaking | 194 Hz  | 2.53 | -1.4 dB |
| Peaking | 420 Hz  | 1.17 | 4.4 dB  |
| Peaking | 2110 Hz | 1.79 | 4.1 dB  |
| Peaking | 5336 Hz | 4.87 | 6.5 dB  |
| Peaking | 138 Hz  | 1.92 | 1.1 dB  |
| Peaking | 148 Hz  | 6.5  | -2.7 dB |
| Peaking | 934 Hz  | 4.53 | -1.4 dB |
| Peaking | 1385 Hz | 4.3  | 0.9 dB  |
| Peaking | 9028 Hz | 5.61 | -1.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bose%20AE2/Bose%20AE2.png)