# HZSOUND HZ3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.5dB
GraphicEQ: 10 -84; 20 0.9; 22 0.5; 23 0.4; 25 0.1; 26 -0.0; 28 -0.2; 30 -0.4; 32 -0.5; 35 -0.7; 37 -0.9; 40 -1.0; 42 -1.1; 45 -1.3; 49 -1.5; 52 -1.7; 56 -1.9; 59 -2.1; 64 -2.3; 68 -2.5; 73 -2.8; 78 -3.1; 83 -3.3; 89 -3.7; 95 -3.9; 102 -4.1; 109 -4.2; 117 -4.3; 125 -4.5; 134 -4.7; 143 -4.8; 153 -4.9; 164 -5.0; 175 -5.0; 188 -4.9; 201 -5.0; 215 -4.8; 230 -4.7; 246 -4.7; 263 -4.6; 282 -4.4; 301 -4.2; 323 -4.0; 345 -3.9; 369 -3.6; 395 -3.4; 423 -3.1; 452 -2.8; 484 -2.7; 518 -2.5; 554 -2.1; 593 -1.7; 635 -1.4; 679 -1.3; 726 -1.1; 777 -0.8; 832 -0.8; 890 -0.8; 952 0.5; 1019 -0.2; 1090 -0.6; 1167 -0.8; 1248 -0.4; 1336 0.5; 1429 -0.3; 1529 -0.7; 1636 -0.8; 1751 -0.9; 1873 -0.7; 2004 -0.5; 2145 -0.4; 2295 -0.2; 2455 0.1; 2627 0.5; 2811 0.8; 3008 1.4; 3219 2.0; 3444 2.3; 3685 1.3; 3943 1.2; 4219 1.5; 4514 -2.4; 4830 -5.2; 5168 -7.9; 5530 -8.1; 5917 -4.0; 6331 -0.6; 6775 1.8; 7249 1.3; 7756 0.3; 8299 -0.0; 8880 -1.2; 9502 -1.4; 10167 -0.2; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.475827490761069dB` and instead set Global volume in the UI for both channels to **-24**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HZSOUND HZ3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -2.1dB.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 119 Hz  |  0.65 | -3.3 dB  |
| Peaking | 279 Hz  |  0.67 | -3.2 dB  |
| Peaking | 3979 Hz |  1.97 | 4.6 dB   |
| Peaking | 5280 Hz |  2.74 | -11.1 dB |
| Peaking | 6651 Hz |  4.36 | 4.9 dB   |
| Peaking | 20 Hz   |  1.68 | 1.1 dB   |
| Peaking | 955 Hz  | 12.53 | 1.3 dB   |
| Peaking | 1829 Hz |  3.54 | -0.8 dB  |
| Peaking | 3236 Hz |  8.43 | 0.9 dB   |
| Peaking | 9205 Hz | 10.42 | -1.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HZSOUND%20HZ3/HZSOUND%20HZ3.png)