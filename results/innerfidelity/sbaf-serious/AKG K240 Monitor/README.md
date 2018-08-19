# AKG K240 Monitor

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 5.8; 35 5.1; 37 4.6; 40 3.8; 42 3.3; 45 2.7; 49 1.9; 52 1.4; 56 0.8; 59 0.5; 64 -0.0; 68 -0.3; 73 -0.4; 78 -0.6; 83 -1.0; 89 -1.5; 95 -1.7; 102 -2.0; 109 -2.3; 117 -2.7; 125 -3.1; 134 -3.3; 143 -3.4; 153 -3.5; 164 -3.3; 175 -3.4; 188 -3.5; 201 -3.5; 215 -3.4; 230 -3.3; 246 -3.2; 263 -3.1; 282 -3.0; 301 -3.0; 323 -3.0; 345 -3.2; 369 -3.1; 395 -2.9; 423 -2.6; 452 -2.4; 484 -2.4; 518 -2.2; 554 -1.8; 593 -1.3; 635 -1.0; 679 -0.9; 726 -0.6; 777 -0.4; 832 -0.4; 890 -0.2; 952 -0.0; 1019 0.0; 1090 0.1; 1167 0.4; 1248 0.5; 1336 0.2; 1429 -0.3; 1529 -0.8; 1636 -1.3; 1751 -1.4; 1873 -1.6; 2004 -1.4; 2145 -0.9; 2295 0.1; 2455 1.2; 2627 1.5; 2811 1.9; 3008 3.1; 3219 1.8; 3444 -1.8; 3685 -3.9; 3943 -2.6; 4219 -0.8; 4514 0.9; 4830 2.2; 5168 4.6; 5530 5.9; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -1.4; 8880 -3.2; 9502 -3.4; 10167 -2.1; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K240 Monitor ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.82 | 6.8 dB  |
| Peaking | 186 Hz  | 0.45 | -3.8 dB |
| Peaking | 3799 Hz | 6.77 | -5.3 dB |
| Peaking | 5887 Hz | 2.2  | 6.7 dB  |
| Peaking | 9056 Hz | 3.31 | -4.7 dB |
| Peaking | 462 Hz  | 2.26 | -0.7 dB |
| Peaking | 1424 Hz | 0.82 | 1.4 dB  |
| Peaking | 1813 Hz | 2.22 | -3.0 dB |
| Peaking | 3099 Hz | 3.59 | 5.3 dB  |
| Peaking | 3394 Hz | 3.14 | -3.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K240%20Monitor/AKG%20K240%20Monitor.png)