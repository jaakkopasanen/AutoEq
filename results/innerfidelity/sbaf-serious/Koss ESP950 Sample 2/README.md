# Koss ESP950 sample 2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 5.9; 78 5.9; 83 5.8; 89 5.5; 95 4.8; 102 4.1; 109 3.5; 117 3.0; 125 2.9; 134 2.8; 143 2.8; 153 2.7; 164 2.6; 175 2.4; 188 2.2; 201 2.1; 215 2.1; 230 2.2; 246 2.1; 263 2.1; 282 2.1; 301 2.2; 323 2.1; 345 2.1; 369 2.0; 395 1.9; 423 1.9; 452 1.8; 484 1.5; 518 1.4; 554 1.4; 593 1.5; 635 1.3; 679 1.1; 726 1.0; 777 0.9; 832 0.6; 890 0.3; 952 0.1; 1019 -0.0; 1090 -0.1; 1167 -0.6; 1248 -1.1; 1336 -1.5; 1429 -1.8; 1529 -1.6; 1636 -1.2; 1751 -0.1; 1873 1.5; 2004 2.9; 2145 3.8; 2295 4.9; 2455 4.7; 2627 3.6; 2811 2.7; 3008 2.4; 3219 2.7; 3444 3.9; 3685 4.8; 3943 5.9; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 5.9; 5917 5.5; 6331 4.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.0; 8880 -1.9; 9502 -2.2; 10167 -0.4; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss ESP950 sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 40 Hz   | 0.35 | 6.5 dB  |
| Peaking | 418 Hz  | 0.81 | 1.5 dB  |
| Peaking | 1495 Hz | 2.21 | -3.1 dB |
| Peaking | 2262 Hz | 2.76 | 4.6 dB  |
| Peaking | 4756 Hz | 1.67 | 6.7 dB  |
| Peaking | 84 Hz   | 3.47 | 1.1 dB  |
| Peaking | 116 Hz  | 3.16 | -0.8 dB |
| Peaking | 6348 Hz | 5.73 | 2.0 dB  |
| Peaking | 9121 Hz | 3.81 | -3.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20ESP950%20sample%202/Koss%20ESP950%20sample%202.png)