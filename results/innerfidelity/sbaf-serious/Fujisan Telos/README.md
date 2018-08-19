# Fujisan Telos

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 5.8; 26 5.6; 28 5.2; 30 4.8; 32 4.4; 35 3.8; 37 3.5; 40 3.0; 42 2.7; 45 2.3; 49 1.8; 52 1.4; 56 1.0; 59 0.7; 64 0.2; 68 -0.2; 73 -0.7; 78 -1.1; 83 -1.5; 89 -2.0; 95 -2.3; 102 -2.8; 109 -3.0; 117 -3.2; 125 -3.6; 134 -3.9; 143 -4.2; 153 -4.3; 164 -4.5; 175 -4.5; 188 -4.7; 201 -4.8; 215 -4.7; 230 -4.7; 246 -4.7; 263 -4.6; 282 -4.4; 301 -4.2; 323 -3.9; 345 -3.6; 369 -3.2; 395 -2.8; 423 -2.3; 452 -2.0; 484 -1.6; 518 -1.2; 554 -0.7; 593 -0.1; 635 0.2; 679 0.6; 726 0.7; 777 0.9; 832 0.8; 890 0.6; 952 0.2; 1019 -0.1; 1090 -0.4; 1167 -0.5; 1248 -0.8; 1336 -1.4; 1429 -2.0; 1529 -2.4; 1636 -3.0; 1751 -3.3; 1873 -3.6; 2004 -3.8; 2145 -3.9; 2295 -3.6; 2455 -2.2; 2627 -0.7; 2811 1.1; 3008 3.4; 3219 5.5; 3444 6.0; 3685 6.0; 3943 5.9; 4219 4.3; 4514 2.1; 4830 0.3; 5168 -1.4; 5530 -3.1; 5917 -3.0; 6331 -0.1; 6775 2.7; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fujisan Telos ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 23 Hz   | 0.83 | 6.2 dB  |
| Peaking | 187 Hz  | 0.69 | -5.3 dB |
| Peaking | 2227 Hz | 1.6  | -8.1 dB |
| Peaking | 3477 Hz | 1.17 | 8.9 dB  |
| Peaking | 5434 Hz | 3.75 | -6.5 dB |
| Peaking | 355 Hz  | 2.33 | -1.0 dB |
| Peaking | 748 Hz  | 1.82 | 1.8 dB  |
| Peaking | 1537 Hz | 4.41 | -1.1 dB |
| Peaking | 6865 Hz | 7.61 | 3.9 dB  |
| Peaking | 7065 Hz | 1.79 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fujisan%20Telos/Fujisan%20Telos.png)