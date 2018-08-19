# Beyerdynamic DT 100 2X2kOhm

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.2dB
GraphicEQ: 10 -84; 20 4.3; 22 3.6; 23 3.3; 25 2.7; 26 2.4; 28 1.9; 30 1.5; 32 1.1; 35 0.6; 37 0.3; 40 -0.1; 42 -0.3; 45 -0.5; 49 -0.9; 52 -1.0; 56 -1.2; 59 -1.3; 64 -1.4; 68 -1.6; 73 -1.5; 78 -1.2; 83 -1.8; 89 -2.5; 95 -2.0; 102 -1.0; 109 -1.3; 117 -4.5; 125 -7.4; 134 -8.6; 143 -8.8; 153 -8.5; 164 -7.1; 175 -8.7; 188 -9.5; 201 -9.3; 215 -9.1; 230 -8.9; 246 -8.7; 263 -8.6; 282 -8.2; 301 -7.8; 323 -7.5; 345 -7.0; 369 -6.6; 395 -6.1; 423 -5.4; 452 -4.9; 484 -4.5; 518 -4.0; 554 -3.3; 593 -2.5; 635 -2.0; 679 -1.7; 726 -1.5; 777 -1.0; 832 -0.7; 890 -0.4; 952 -0.3; 1019 0.4; 1090 0.3; 1167 0.6; 1248 0.4; 1336 -0.2; 1429 -1.0; 1529 -2.4; 1636 -3.3; 1751 -4.0; 1873 -4.3; 2004 -3.6; 2145 -2.7; 2295 -1.6; 2455 -0.4; 2627 1.4; 2811 3.0; 3008 3.9; 3219 4.1; 3444 3.8; 3685 3.0; 3943 2.8; 4219 2.8; 4514 3.6; 4830 5.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 -0.9; 8299 -3.6; 8880 -5.9; 9502 -5.1; 10167 -0.7; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.153361265406165dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT 100 2X2kOhm ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.3dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 1.65 | 4.1 dB  |
| Peaking | 139 Hz  | 4.48 | -4.5 dB |
| Peaking | 246 Hz  | 0.79 | -9.1 dB |
| Peaking | 5642 Hz | 1.39 | 6.8 dB  |
| Peaking | 8827 Hz | 3.64 | -8.4 dB |
| Peaking | 107 Hz  | 6.31 | 4.5 dB  |
| Peaking | 110 Hz  | 2.92 | -2.0 dB |
| Peaking | 1262 Hz | 1.47 | 4.3 dB  |
| Peaking | 1776 Hz | 1.27 | -6.6 dB |
| Peaking | 2981 Hz | 3.03 | 4.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%20100%202X2kOhm/Beyerdynamic%20DT%20100%202X2kOhm.png)