# Koss KPH7

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 6.0; 95 6.0; 102 6.0; 109 6.0; 117 6.0; 125 5.4; 134 4.1; 143 2.6; 153 1.3; 164 -0.3; 175 -1.6; 188 -2.8; 201 -4.1; 215 -5.0; 230 -5.4; 246 -5.9; 263 -6.0; 282 -5.6; 301 -5.0; 323 -4.0; 345 -3.6; 369 -3.4; 395 -2.4; 423 -1.5; 452 -0.1; 484 2.4; 518 -1.3; 554 -1.7; 593 -0.5; 635 0.8; 679 0.0; 726 -1.5; 777 -0.6; 832 -0.3; 890 -0.0; 952 -0.0; 1019 0.1; 1090 0.1; 1167 0.2; 1248 -0.1; 1336 -0.6; 1429 -1.2; 1529 -2.1; 1636 -2.4; 1751 -2.9; 1873 -3.2; 2004 -4.2; 2145 -5.7; 2295 -7.6; 2455 -8.0; 2627 -6.5; 2811 -4.8; 3008 -2.6; 3219 -0.7; 3444 0.5; 3685 1.0; 3943 2.4; 4219 4.7; 4514 5.2; 4830 3.3; 5168 4.2; 5530 4.4; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -2.0; 8880 -4.0; 9502 -3.8; 10167 -1.5; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss KPH7 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 78 Hz   |  0.24 | 7.7 dB   |
| Peaking | 244 Hz  |  1.15 | -11.7 dB |
| Peaking | 2434 Hz |  2.04 | -9.8 dB  |
| Peaking | 5585 Hz |  0.82 | 6.7 dB   |
| Peaking | 8923 Hz |  2.59 | -7.5 dB  |
| Peaking | 16 Hz   |  0.69 | 2.5 dB   |
| Peaking | 111 Hz  |  0.3  | -3.0 dB  |
| Peaking | 150 Hz  |  0.89 | 6.6 dB   |
| Peaking | 166 Hz  |  2.27 | -4.5 dB  |
| Peaking | 479 Hz  | 14.88 | 4.0 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20KPH7/Koss%20KPH7.png)