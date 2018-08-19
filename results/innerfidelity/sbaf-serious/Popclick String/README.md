# Popclick String

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.7dB
GraphicEQ: 10 -84; 20 -10.7; 22 -10.7; 23 -10.7; 25 -10.7; 26 -10.7; 28 -10.7; 30 -10.6; 32 -10.6; 35 -10.5; 37 -10.4; 40 -10.3; 42 -10.2; 45 -10.2; 49 -10.1; 52 -10.0; 56 -9.9; 59 -9.8; 64 -9.8; 68 -9.7; 73 -9.6; 78 -9.6; 83 -9.6; 89 -9.5; 95 -9.4; 102 -9.2; 109 -9.0; 117 -8.8; 125 -8.6; 134 -8.4; 143 -8.2; 153 -7.9; 164 -7.6; 175 -7.2; 188 -6.8; 201 -6.5; 215 -6.0; 230 -5.6; 246 -5.2; 263 -4.7; 282 -4.2; 301 -3.8; 323 -3.3; 345 -2.8; 369 -2.4; 395 -1.9; 423 -1.3; 452 -0.9; 484 -0.7; 518 -0.4; 554 -0.0; 593 0.3; 635 0.5; 679 0.5; 726 0.4; 777 0.7; 832 1.0; 890 0.7; 952 0.3; 1019 -0.0; 1090 -0.4; 1167 -0.7; 1248 -1.1; 1336 -1.8; 1429 -2.6; 1529 -3.6; 1636 -4.3; 1751 -4.8; 1873 -5.1; 2004 -5.6; 2145 -6.1; 2295 -6.4; 2455 -6.0; 2627 -4.8; 2811 -3.0; 3008 -0.5; 3219 1.6; 3444 3.3; 3685 3.6; 3943 2.9; 4219 0.9; 4514 -1.1; 4830 -2.8; 5168 -5.1; 5530 -8.7; 5917 -7.4; 6331 -2.5; 6775 0.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 -0.1; 10879 -0.5; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.694839791899632dB` and instead set Global volume in the UI for both channels to **-36**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Popclick String ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.1dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 28 Hz   | 0.25 | -10.5 dB |
| Peaking | 150 Hz  | 0.82 | -4.2 dB  |
| Peaking | 2234 Hz | 1.79 | -7.3 dB  |
| Peaking | 3571 Hz | 3.23 | 6.1 dB   |
| Peaking | 5589 Hz | 6.05 | -9.8 dB  |
| Peaking | 286 Hz  | 2.03 | -1.0 dB  |
| Peaking | 749 Hz  | 1.04 | 1.7 dB   |
| Peaking | 1563 Hz | 3.96 | -1.7 dB  |
| Peaking | 6263 Hz | 3.19 | -2.1 dB  |
| Peaking | 6916 Hz | 5.09 | 4.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Popclick%20String/Popclick%20String.png)