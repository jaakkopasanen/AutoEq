# Pioneer SE-A1000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 5.1; 68 3.9; 73 2.7; 78 1.7; 83 0.9; 89 0.1; 95 -0.5; 102 -1.0; 109 -1.2; 117 -1.4; 125 -1.7; 134 -1.8; 143 -1.9; 153 -2.0; 164 -1.8; 175 -1.7; 188 -1.7; 201 -1.6; 215 -1.3; 230 -1.1; 246 -1.0; 263 -0.9; 282 -0.7; 301 -0.7; 323 -0.7; 345 -0.5; 369 -0.1; 395 -0.0; 423 0.2; 452 0.4; 484 0.7; 518 1.2; 554 1.2; 593 1.1; 635 0.9; 679 0.7; 726 0.6; 777 0.7; 832 0.5; 890 0.1; 952 0.1; 1019 -0.1; 1090 -0.4; 1167 -0.3; 1248 -0.1; 1336 0.0; 1429 0.2; 1529 0.3; 1636 0.7; 1751 1.0; 1873 1.9; 2004 2.6; 2145 2.8; 2295 3.1; 2455 3.0; 2627 2.2; 2811 1.7; 3008 1.2; 3219 1.3; 3444 2.8; 3685 1.3; 3943 -3.3; 4219 -7.4; 4514 -8.3; 4830 -6.6; 5168 -4.3; 5530 -2.6; 5917 -1.6; 6331 -0.2; 6775 2.4; 7249 0.2; 7756 -2.0; 8299 -3.8; 8880 -5.0; 9502 -5.5; 10167 -5.0; 10879 -2.7; 11640 -0.2; 12455 0.0; 13327 -0.0; 14260 -0.8; 15258 -0.3; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pioneer SE-A1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.4dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 35 Hz   | 1.04 | 7.3 dB   |
| Peaking | 3618 Hz | 1.06 | 6.3 dB   |
| Peaking | 4422 Hz | 2.7  | -13.5 dB |
| Peaking | 6767 Hz | 7.19 | 3.8 dB   |
| Peaking | 9368 Hz | 2.75 | -6.2 dB  |
| Peaking | 61 Hz   | 2.58 | 4.1 dB   |
| Peaking | 127 Hz  | 0.63 | -2.6 dB  |
| Peaking | 580 Hz  | 1.49 | 1.6 dB   |
| Peaking | 1486 Hz | 0.69 | -1.0 dB  |
| Peaking | 2102 Hz | 3.27 | 2.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Pioneer%20SE-A1000/Pioneer%20SE-A1000.png)