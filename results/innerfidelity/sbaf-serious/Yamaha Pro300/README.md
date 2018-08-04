# Yamaha Pro300

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 6.0; 95 6.0; 102 6.0; 109 6.0; 117 6.0; 125 6.0; 134 6.0; 143 6.0; 153 6.0; 164 6.0; 175 6.0; 188 5.5; 201 5.2; 215 5.0; 230 4.9; 246 5.1; 263 5.4; 282 5.1; 301 4.7; 323 4.5; 345 4.1; 369 3.4; 395 3.1; 423 2.8; 452 2.2; 484 1.6; 518 1.3; 554 1.9; 593 3.1; 635 3.0; 679 2.2; 726 1.8; 777 1.7; 832 1.4; 890 0.9; 952 0.4; 1019 -0.1; 1090 -0.6; 1167 -1.1; 1248 -1.8; 1336 -2.9; 1429 -4.0; 1529 -4.4; 1636 -5.1; 1751 -5.7; 1873 -5.3; 2004 -4.1; 2145 -2.4; 2295 -0.5; 2455 1.4; 2627 3.1; 2811 4.4; 3008 5.7; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 5.6; 5917 3.6; 6331 3.7; 6775 3.4; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Yamaha Pro300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.14 | 5.9 dB  |
| Peaking | 228 Hz  | 0.64 | 3.0 dB  |
| Peaking | 684 Hz  | 2.8  | 1.6 dB  |
| Peaking | 1778 Hz | 1.69 | -8.6 dB |
| Peaking | 3596 Hz | 0.95 | 7.9 dB  |
| Peaking | 895 Hz  | 4.97 | 0.4 dB  |
| Peaking | 2976 Hz | 2.91 | 2.0 dB  |
| Peaking | 3757 Hz | 1.31 | -3.0 dB |
| Peaking | 5326 Hz | 1.26 | 3.4 dB  |
| Peaking | 8187 Hz | 1.46 | -2.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Yamaha%20Pro300/Yamaha%20Pro300.png)