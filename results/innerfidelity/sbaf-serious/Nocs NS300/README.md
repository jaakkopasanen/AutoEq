# Nocs NS300

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 5.6; 42 5.3; 45 4.7; 49 4.1; 52 3.8; 56 3.4; 59 3.2; 64 2.8; 68 2.6; 73 2.3; 78 2.1; 83 2.2; 89 2.4; 95 2.4; 102 2.7; 109 3.5; 117 4.0; 125 3.9; 134 3.4; 143 3.3; 153 3.3; 164 4.1; 175 4.4; 188 4.8; 201 5.5; 215 6.0; 230 6.0; 246 6.0; 263 6.0; 282 6.0; 301 5.6; 323 3.8; 345 2.4; 369 2.1; 395 1.8; 423 1.5; 452 1.2; 484 0.9; 518 0.7; 554 0.7; 593 0.6; 635 0.3; 679 0.0; 726 -0.2; 777 -0.2; 832 -0.5; 890 -0.6; 952 -0.3; 1019 0.3; 1090 1.0; 1167 2.1; 1248 2.8; 1336 3.0; 1429 3.3; 1529 4.4; 1636 4.0; 1751 4.7; 1873 4.8; 2004 4.8; 2145 4.5; 2295 4.1; 2455 4.0; 2627 3.2; 2811 2.7; 3008 2.5; 3219 1.9; 3444 2.8; 3685 3.7; 3943 4.7; 4219 5.9; 4514 6.0; 4830 4.5; 5168 4.5; 5530 5.7; 5917 5.9; 6331 5.3; 6775 3.2; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Nocs NS300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.1  | 2.4 dB  |
| Peaking | 28 Hz   | 1.01 | 4.0 dB  |
| Peaking | 238 Hz  | 1.52 | 5.6 dB  |
| Peaking | 1865 Hz | 1.71 | 4.7 dB  |
| Peaking | 4976 Hz | 1.56 | 5.7 dB  |
| Peaking | 119 Hz  | 7.34 | 1.3 dB  |
| Peaking | 939 Hz  | 1.63 | -2.0 dB |
| Peaking | 1226 Hz | 2.72 | 2.0 dB  |
| Peaking | 6275 Hz | 5.41 | 3.3 dB  |
| Peaking | 7566 Hz | 1.52 | -1.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Nocs%20NS300/Nocs%20NS300.png)