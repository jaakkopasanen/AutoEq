# NVX EX10S

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 5.9; 45 5.7; 49 5.4; 52 5.2; 56 4.9; 59 4.7; 64 4.4; 68 4.2; 73 3.9; 78 3.6; 83 3.3; 89 3.0; 95 2.7; 102 2.4; 109 2.3; 117 2.2; 125 1.9; 134 1.7; 143 1.6; 153 1.5; 164 1.3; 175 1.3; 188 1.2; 201 1.2; 215 1.3; 230 1.3; 246 1.3; 263 1.3; 282 1.4; 301 1.5; 323 1.5; 345 1.6; 369 1.7; 395 1.7; 423 1.9; 452 1.9; 484 1.8; 518 1.8; 554 1.9; 593 2.0; 635 1.9; 679 1.7; 726 1.6; 777 1.5; 832 1.1; 890 0.7; 952 0.3; 1019 -0.1; 1090 -0.4; 1167 -0.4; 1248 -0.7; 1336 -0.7; 1429 -0.6; 1529 -0.2; 1636 0.9; 1751 2.0; 1873 2.8; 2004 4.1; 2145 5.7; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `NVX EX10S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 0.42 | 6.2 dB  |
| Peaking | 550 Hz  | 0.71 | 1.9 dB  |
| Peaking | 1390 Hz | 1.4  | -4.2 dB |
| Peaking | 2590 Hz | 0.92 | 6.9 dB  |
| Peaking | 5351 Hz | 2.2  | 4.6 dB  |
| Peaking | 2194 Hz | 6.94 | 1.2 dB  |
| Peaking | 2667 Hz | 2.14 | -0.7 dB |
| Peaking | 4021 Hz | 2.61 | 1.5 dB  |
| Peaking | 6427 Hz | 4.24 | 4.4 dB  |
| Peaking | 6768 Hz | 1.39 | -3.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/NVX%20EX10S/NVX%20EX10S.png)