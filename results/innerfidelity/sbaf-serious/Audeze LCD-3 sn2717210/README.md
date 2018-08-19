# Audeze LCD-3 sn2717210

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 5.9; 26 5.6; 28 4.7; 30 3.8; 32 3.1; 35 2.5; 37 2.3; 40 2.1; 42 2.0; 45 2.1; 49 2.2; 52 2.1; 56 2.1; 59 2.1; 64 2.1; 68 1.9; 73 1.7; 78 1.5; 83 1.3; 89 1.1; 95 0.8; 102 0.5; 109 0.5; 117 0.4; 125 0.1; 134 -0.1; 143 -0.2; 153 -0.3; 164 -0.5; 175 -0.6; 188 -0.7; 201 -0.8; 215 -0.8; 230 -0.8; 246 -0.9; 263 -1.0; 282 -0.9; 301 -0.9; 323 -1.0; 345 -1.0; 369 -0.9; 395 -1.0; 423 -0.9; 452 -0.9; 484 -0.9; 518 -0.7; 554 -0.2; 593 0.4; 635 0.8; 679 0.4; 726 -0.1; 777 -0.3; 832 -0.5; 890 -0.4; 952 -0.2; 1019 0.0; 1090 0.4; 1167 0.6; 1248 0.9; 1336 0.4; 1429 -0.7; 1529 -1.6; 1636 -1.7; 1751 -1.1; 1873 -0.3; 2004 0.3; 2145 0.4; 2295 0.7; 2455 1.7; 2627 2.7; 2811 3.3; 3008 3.6; 3219 3.8; 3444 4.9; 3685 5.8; 3943 6.0; 4219 5.8; 4514 4.3; 4830 3.4; 5168 3.3; 5530 0.3; 5917 -0.6; 6331 2.3; 6775 3.8; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.2; 17469 -1.4; 18692 -3.0; 20000 -4.2
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-3 sn2717210 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.3dB.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 22 Hz    |  1.42 | 6.2 dB  |
| Peaking | 62 Hz    |  2.09 | 1.7 dB  |
| Peaking | 1613 Hz  |  5.03 | -2.3 dB |
| Peaking | 2799 Hz  |  4.15 | 1.5 dB  |
| Peaking | 3939 Hz  |  2.11 | 6.0 dB  |
| Peaking | 486 Hz   |  0.5  | -1.3 dB |
| Peaking | 634 Hz   |  3.68 | 1.9 dB  |
| Peaking | 1215 Hz  |  3.74 | 1.5 dB  |
| Peaking | 6689 Hz  | 13.06 | 3.5 dB  |
| Peaking | 19524 Hz |  1.76 | -4.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-3%20sn2717210/Audeze%20LCD-3%20sn2717210.png)