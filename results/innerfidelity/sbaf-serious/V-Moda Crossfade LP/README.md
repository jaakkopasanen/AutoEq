# V-Moda Crossfade LP

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 4.1; 22 3.1; 23 2.7; 25 2.0; 26 1.6; 28 1.0; 30 0.5; 32 -0.1; 35 -0.9; 37 -1.3; 40 -1.8; 42 -2.1; 45 -2.5; 49 -2.8; 52 -3.0; 56 -3.1; 59 -3.2; 64 -3.2; 68 -3.4; 73 -3.8; 78 -4.1; 83 -4.0; 89 -3.9; 95 -4.4; 102 -4.7; 109 -4.8; 117 -5.0; 125 -5.1; 134 -5.2; 143 -5.4; 153 -5.4; 164 -5.2; 175 -5.3; 188 -5.2; 201 -4.9; 215 -4.5; 230 -3.7; 246 -2.9; 263 -2.5; 282 -1.3; 301 -0.2; 323 1.0; 345 2.1; 369 2.7; 395 3.2; 423 3.9; 452 4.2; 484 4.2; 518 4.0; 554 3.7; 593 3.2; 635 2.4; 679 1.4; 726 0.8; 777 0.6; 832 0.3; 890 0.1; 952 -0.0; 1019 0.0; 1090 -0.2; 1167 -0.4; 1248 -0.8; 1336 -1.5; 1429 -1.8; 1529 -2.1; 1636 -2.4; 1751 -2.3; 1873 -2.4; 2004 -2.6; 2145 -3.2; 2295 -3.5; 2455 -2.8; 2627 -2.3; 2811 -2.1; 3008 -1.4; 3219 -1.6; 3444 -1.2; 3685 0.1; 3943 2.0; 4219 3.0; 4514 4.5; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.2; 10167 -0.7; 10879 -0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099750969753472dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-Moda Crossfade LP ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.1dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 31 Hz   | 0.38 | 9.3 dB   |
| Peaking | 39 Hz   | 1.25 | -3.9 dB  |
| Peaking | 308 Hz  | 0.14 | -18.7 dB |
| Peaking | 477 Hz  | 0.42 | 22.3 dB  |
| Peaking | 5294 Hz | 1.93 | 8.8 dB   |
| Peaking | 201 Hz  | 5.29 | -0.9 dB  |
| Peaking | 1138 Hz | 4.2  | 1.4 dB   |
| Peaking | 2286 Hz | 4.91 | -1.2 dB  |
| Peaking | 6541 Hz | 6.41 | 2.9 dB   |
| Peaking | 7441 Hz | 1.98 | -1.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/V-Moda%20Crossfade%20LP/V-Moda%20Crossfade%20LP.png)