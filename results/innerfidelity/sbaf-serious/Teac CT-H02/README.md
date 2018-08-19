# Teac CT-H02

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 2.4; 22 2.1; 23 2.1; 25 1.9; 26 1.8; 28 1.7; 30 1.7; 32 1.6; 35 1.6; 37 1.6; 40 1.6; 42 1.6; 45 1.6; 49 1.6; 52 1.5; 56 1.5; 59 1.4; 64 1.4; 68 1.3; 73 1.1; 78 1.0; 83 0.9; 89 0.7; 95 0.7; 102 0.5; 109 0.2; 117 0.0; 125 0.1; 134 0.4; 143 0.7; 153 0.1; 164 -0.2; 175 0.3; 188 -0.4; 201 -1.1; 215 -1.5; 230 -1.6; 246 -1.5; 263 -1.3; 282 -1.4; 301 -1.5; 323 -1.5; 345 -1.4; 369 -1.4; 395 -1.4; 423 -1.3; 452 -1.3; 484 -1.4; 518 -1.4; 554 -1.3; 593 -1.2; 635 -1.3; 679 -1.2; 726 -0.8; 777 -0.5; 832 -0.7; 890 -0.6; 952 -0.2; 1019 -0.1; 1090 -0.4; 1167 -0.3; 1248 -0.2; 1336 -0.2; 1429 -0.2; 1529 -0.3; 1636 -0.4; 1751 -0.2; 1873 0.4; 2004 1.3; 2145 1.8; 2295 2.9; 2455 4.4; 2627 5.1; 2811 5.8; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 5.0; 4514 5.9; 4830 6.0; 5168 5.9; 5530 5.7; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 -1.7; 8299 -4.9; 8880 -6.5; 9502 -5.9; 10167 -3.1; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999755221dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Teac CT-H02 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 19 Hz   |  0.13 | 1.9 dB   |
| Peaking | 370 Hz  |  0.34 | -1.7 dB  |
| Peaking | 3002 Hz |  2.09 | 4.6 dB   |
| Peaking | 5946 Hz |  0.96 | 7.2 dB   |
| Peaking | 8780 Hz |  2.61 | -11.0 dB |
| Peaking | 181 Hz  |  2.86 | 1.6 dB   |
| Peaking | 206 Hz  |  2.28 | -1.5 dB  |
| Peaking | 1566 Hz |  0.71 | 0.7 dB   |
| Peaking | 1677 Hz |  2.49 | -1.7 dB  |
| Peaking | 5404 Hz | 10.04 | -0.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Teac%20CT-H02/Teac%20CT-H02.png)