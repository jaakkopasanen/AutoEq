# Beyerdynamic T90

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.5dB
GraphicEQ: 10 -84; 20 4.4; 22 4.1; 23 3.9; 25 3.7; 26 3.5; 28 3.3; 30 3.0; 32 2.8; 35 2.6; 37 2.5; 40 2.4; 42 2.3; 45 2.2; 49 2.0; 52 1.9; 56 2.2; 59 2.4; 64 1.8; 68 0.9; 73 0.3; 78 -0.2; 83 -0.6; 89 -1.0; 95 -1.4; 102 -1.8; 109 -2.1; 117 -2.4; 125 -2.7; 134 -3.0; 143 -3.1; 153 -3.2; 164 -3.3; 175 -3.4; 188 -3.6; 201 -3.7; 215 -3.7; 230 -3.7; 246 -3.7; 263 -3.6; 282 -3.5; 301 -3.5; 323 -3.3; 345 -3.2; 369 -3.0; 395 -2.8; 423 -2.6; 452 -2.3; 484 -2.2; 518 -1.9; 554 -1.5; 593 -0.9; 635 -0.6; 679 -0.4; 726 -0.2; 777 0.1; 832 0.1; 890 0.2; 952 0.1; 1019 -0.0; 1090 -0.1; 1167 -0.1; 1248 -0.2; 1336 -0.7; 1429 -1.2; 1529 -1.8; 1636 -2.4; 1751 -2.8; 1873 -2.9; 2004 -3.0; 2145 -3.1; 2295 -3.2; 2455 -2.9; 2627 -3.2; 2811 -3.7; 3008 -4.1; 3219 -4.2; 3444 -3.7; 3685 -3.4; 3943 -3.6; 4219 -4.0; 4514 -1.8; 4830 2.1; 5168 0.8; 5530 0.5; 5917 -1.1; 6331 -6.3; 6775 -9.0; 7249 -9.6; 7756 -10.7; 8299 -11.8; 8880 -12.2; 9502 -10.9; 10167 -8.3; 10879 -6.0; 11640 -4.6; 12455 -3.9; 13327 -3.3; 14260 -2.9; 15258 -3.3; 16326 -4.8; 17469 -6.3; 18692 -5.8; 20000 -2.2
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.488884117657716dB` and instead set Global volume in the UI for both channels to **-44**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic T90 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -3.9dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 15 Hz    | 0.21 | 4.1 dB   |
| Peaking | 189 Hz   | 0.57 | -4.4 dB  |
| Peaking | 2633 Hz  | 1.48 | -3.6 dB  |
| Peaking | 8603 Hz  | 2.03 | -12.8 dB |
| Peaking | 18140 Hz | 1.25 | -6.1 dB  |
| Peaking | 864 Hz   | 2.7  | 1.2 dB   |
| Peaking | 4397 Hz  | 3.34 | -4.7 dB  |
| Peaking | 4808 Hz  | 5.04 | 7.2 dB   |
| Peaking | 5747 Hz  | 4.83 | 4.3 dB   |
| Peaking | 6626 Hz  | 5.67 | -4.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20T90/Beyerdynamic%20T90.png)