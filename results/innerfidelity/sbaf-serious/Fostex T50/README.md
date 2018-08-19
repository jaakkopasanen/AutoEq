# Fostex T50

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 6.0; 95 6.0; 102 6.0; 109 6.0; 117 6.0; 125 5.8; 134 4.4; 143 3.7; 153 3.4; 164 3.4; 175 3.5; 188 3.4; 201 3.3; 215 3.2; 230 3.0; 246 2.9; 263 2.7; 282 2.6; 301 2.4; 323 2.2; 345 2.1; 369 1.5; 395 0.6; 423 0.6; 452 0.9; 484 1.0; 518 0.9; 554 0.8; 593 0.8; 635 0.8; 679 0.4; 726 0.3; 777 0.4; 832 0.4; 890 0.3; 952 0.3; 1019 -0.0; 1090 0.0; 1167 0.3; 1248 0.4; 1336 0.3; 1429 0.1; 1529 -0.4; 1636 -0.7; 1751 -0.9; 1873 -0.7; 2004 -1.0; 2145 -0.8; 2295 -0.2; 2455 0.4; 2627 1.2; 2811 1.5; 3008 2.1; 3219 3.6; 3444 4.1; 3685 3.7; 3943 3.0; 4219 3.9; 4514 4.5; 4830 5.9; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fostex T50 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.27 | 6.1 dB  |
| Peaking | 106 Hz  | 1.76 | 2.3 dB  |
| Peaking | 259 Hz  | 1.43 | 1.6 dB  |
| Peaking | 3426 Hz | 4.29 | 3.1 dB  |
| Peaking | 5418 Hz | 2.32 | 6.7 dB  |
| Peaking | 70 Hz   | 3.26 | 0.2 dB  |
| Peaking | 1952 Hz | 2.11 | -1.9 dB |
| Peaking | 3225 Hz | 0.46 | 0.8 dB  |
| Peaking | 6503 Hz | 5.55 | 3.4 dB  |
| Peaking | 7073 Hz | 1.53 | -2.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fostex%20T50/Fostex%20T50.png)