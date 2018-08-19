# Panasonic HJE120

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -7.3; 22 -7.4; 23 -7.4; 25 -7.5; 26 -7.6; 28 -7.6; 30 -7.6; 32 -7.5; 35 -7.2; 37 -7.1; 40 -7.1; 42 -7.2; 45 -7.4; 49 -7.6; 52 -7.7; 56 -7.8; 59 -7.7; 64 -7.7; 68 -7.9; 73 -8.2; 78 -8.3; 83 -8.3; 89 -8.4; 95 -8.4; 102 -8.6; 109 -8.2; 117 -8.2; 125 -8.4; 134 -8.2; 143 -8.2; 153 -7.9; 164 -7.8; 175 -7.5; 188 -7.4; 201 -7.1; 215 -6.8; 230 -6.4; 246 -6.2; 263 -5.7; 282 -5.4; 301 -5.0; 323 -4.6; 345 -4.2; 369 -3.7; 395 -3.4; 423 -2.8; 452 -2.4; 484 -2.2; 518 -1.7; 554 -1.3; 593 -0.7; 635 -0.3; 679 -0.3; 726 0.0; 777 0.4; 832 0.5; 890 0.5; 952 0.2; 1019 -0.1; 1090 -0.4; 1167 -0.7; 1248 -1.2; 1336 -1.7; 1429 -2.6; 1529 -3.7; 1636 -5.0; 1751 -6.3; 1873 -7.4; 2004 -7.5; 2145 -7.0; 2295 -4.3; 2455 -1.4; 2627 0.7; 2811 2.2; 3008 4.3; 3219 5.9; 3444 6.0; 3685 6.0; 3943 6.0; 4219 4.9; 4514 4.3; 4830 1.7; 5168 3.4; 5530 5.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999991048581dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Panasonic HJE120 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.2  | -7.2 dB |
| Peaking | 175 Hz  | 0.68 | -4.4 dB |
| Peaking | 1986 Hz | 2.53 | -9.7 dB |
| Peaking | 3449 Hz | 1.76 | 7.5 dB  |
| Peaking | 6069 Hz | 4.77 | 5.4 dB  |
| Peaking | 42 Hz   | 2.91 | 0.5 dB  |
| Peaking | 353 Hz  | 2.15 | -0.7 dB |
| Peaking | 818 Hz  | 1.63 | 1.6 dB  |
| Peaking | 1562 Hz | 4.87 | -1.1 dB |
| Peaking | 8352 Hz | 4.08 | -0.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Panasonic%20HJE120/Panasonic%20HJE120.png)