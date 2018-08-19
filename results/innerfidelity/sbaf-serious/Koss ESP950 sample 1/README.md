# Koss ESP950 sample 1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 5.7; 89 4.8; 95 4.0; 102 3.3; 109 2.9; 117 2.7; 125 2.7; 134 2.8; 143 2.6; 153 2.7; 164 2.5; 175 2.4; 188 2.3; 201 2.2; 215 2.3; 230 2.3; 246 2.2; 263 2.2; 282 2.2; 301 2.1; 323 2.1; 345 2.1; 369 2.2; 395 2.1; 423 2.3; 452 2.2; 484 2.0; 518 1.9; 554 1.8; 593 1.8; 635 1.6; 679 1.5; 726 1.4; 777 1.3; 832 0.9; 890 0.6; 952 0.4; 1019 0.1; 1090 0.2; 1167 -0.5; 1248 -0.9; 1336 -1.1; 1429 -1.4; 1529 -1.5; 1636 -1.3; 1751 0.1; 1873 1.3; 2004 2.9; 2145 3.7; 2295 5.4; 2455 5.5; 2627 4.2; 2811 2.0; 3008 1.6; 3219 1.8; 3444 3.2; 3685 4.6; 3943 6.0; 4219 6.0; 4514 6.0; 4830 5.7; 5168 5.7; 5530 5.2; 5917 5.3; 6331 4.3; 6775 3.8; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.9; 9502 -0.2; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss ESP950 sample 1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 30 Hz   | 0.31 | 6.1 dB  |
| Peaking | 74 Hz   | 2.92 | 1.8 dB  |
| Peaking | 382 Hz  | 0.94 | 2.0 dB  |
| Peaking | 2368 Hz | 5.52 | 5.3 dB  |
| Peaking | 4759 Hz | 1.71 | 6.6 dB  |
| Peaking | 1564 Hz | 2.53 | -4.2 dB |
| Peaking | 1820 Hz | 2.07 | 2.4 dB  |
| Peaking | 4922 Hz | 7.02 | -1.4 dB |
| Peaking | 6490 Hz | 2.39 | 3.0 dB  |
| Peaking | 7911 Hz | 1.95 | -2.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20ESP950%20sample%201/Koss%20ESP950%20sample%201.png)