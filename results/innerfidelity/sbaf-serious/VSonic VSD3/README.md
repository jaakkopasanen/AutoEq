# VSonic VSD3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.5dB
GraphicEQ: 10 -84; 20 0.1; 22 -0.3; 23 -0.5; 25 -0.8; 26 -0.9; 28 -1.2; 30 -1.4; 32 -1.6; 35 -1.9; 37 -2.0; 40 -2.2; 42 -2.3; 45 -2.5; 49 -2.7; 52 -2.9; 56 -3.1; 59 -3.2; 64 -3.5; 68 -3.7; 73 -4.0; 78 -4.2; 83 -4.4; 89 -4.7; 95 -4.9; 102 -5.1; 109 -5.2; 117 -5.2; 125 -5.4; 134 -5.4; 143 -5.5; 153 -5.5; 164 -5.5; 175 -5.4; 188 -5.3; 201 -5.2; 215 -5.0; 230 -4.8; 246 -4.7; 263 -4.5; 282 -4.2; 301 -4.0; 323 -3.8; 345 -3.5; 369 -3.3; 395 -3.1; 423 -2.7; 452 -2.5; 484 -2.3; 518 -2.1; 554 -1.7; 593 -1.2; 635 -1.0; 679 -0.8; 726 -0.6; 777 -0.3; 832 -0.2; 890 -0.1; 952 -0.0; 1019 0.0; 1090 0.0; 1167 -0.1; 1248 -0.1; 1336 -0.1; 1429 -0.0; 1529 0.1; 1636 0.2; 1751 0.4; 1873 0.7; 2004 1.0; 2145 1.4; 2295 1.8; 2455 2.5; 2627 2.7; 2811 3.0; 3008 3.8; 3219 4.6; 3444 5.4; 3685 5.3; 3943 4.7; 4219 3.0; 4514 1.6; 4830 0.6; 5168 -0.2; 5530 -1.1; 5917 -1.8; 6331 -0.8; 6775 1.0; 7249 1.2; 7756 0.3; 8299 0.0; 8880 -0.6; 9502 -3.2; 10167 -5.2; 10879 -5.2; 11640 -3.6; 12455 -1.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.5216384293591dB` and instead set Global volume in the UI for both channels to **-55**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `VSonic VSD3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.3dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 101 Hz   | 0.5  | -3.8 dB |
| Peaking | 235 Hz   | 0.65 | -3.1 dB |
| Peaking | 3527 Hz  | 1.58 | 5.5 dB  |
| Peaking | 5487 Hz  | 3.86 | -2.9 dB |
| Peaking | 10590 Hz | 3.99 | -6.2 dB |
| Peaking | 833 Hz   | 3.47 | 0.6 dB  |
| Peaking | 6148 Hz  | 8.55 | -1.4 dB |
| Peaking | 7026 Hz  | 5.51 | 1.8 dB  |
| Peaking | 13359 Hz | 7.63 | 0.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/VSonic%20VSD3/VSonic%20VSD3.png)