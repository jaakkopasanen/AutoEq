# RBH EP1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.2dB
GraphicEQ: 10 -84; 20 -10.2; 22 -10.0; 23 -9.9; 25 -9.6; 26 -9.5; 28 -9.2; 30 -9.0; 32 -8.9; 35 -8.6; 37 -8.4; 40 -8.0; 42 -7.8; 45 -7.6; 49 -7.4; 52 -7.3; 56 -7.1; 59 -7.0; 64 -6.9; 68 -6.7; 73 -6.7; 78 -6.6; 83 -6.5; 89 -6.5; 95 -6.4; 102 -6.5; 109 -6.1; 117 -5.7; 125 -6.0; 134 -5.6; 143 -5.6; 153 -5.0; 164 -5.1; 175 -5.0; 188 -4.5; 201 -4.4; 215 -4.0; 230 -3.8; 246 -3.5; 263 -3.2; 282 -3.0; 301 -2.5; 323 -2.4; 345 -2.0; 369 -1.7; 395 -1.4; 423 -1.0; 452 -0.8; 484 -0.6; 518 -0.3; 554 0.1; 593 0.3; 635 1.1; 679 1.0; 726 1.0; 777 1.1; 832 0.9; 890 0.6; 952 0.3; 1019 -0.1; 1090 -0.4; 1167 -0.7; 1248 -1.0; 1336 -1.6; 1429 -2.4; 1529 -3.1; 1636 -3.8; 1751 -4.3; 1873 -4.4; 2004 -4.4; 2145 -4.5; 2295 -4.3; 2455 -3.6; 2627 -3.2; 2811 -2.3; 3008 -0.8; 3219 0.3; 3444 1.1; 3685 0.7; 3943 -0.8; 4219 -3.7; 4514 -5.7; 4830 -6.7; 5168 -4.5; 5530 -1.8; 5917 0.8; 6331 3.1; 6775 3.7; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.3; 10167 -0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.171304572192671dB` and instead set Global volume in the UI for both channels to **-41**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RBH EP1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 14 Hz   | 0.18 | -9.9 dB |
| Peaking | 152 Hz  | 0.8  | -3.4 dB |
| Peaking | 1978 Hz | 2.19 | -5.0 dB |
| Peaking | 4802 Hz | 5.19 | -7.4 dB |
| Peaking | 6546 Hz | 5.13 | 4.7 dB  |
| Peaking | 310 Hz  | 2.23 | -0.7 dB |
| Peaking | 724 Hz  | 1.74 | 1.8 dB  |
| Peaking | 1503 Hz | 6.17 | -1.0 dB |
| Peaking | 3389 Hz | 1.71 | -2.6 dB |
| Peaking | 3462 Hz | 3.76 | 5.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/RBH%20EP1/RBH%20EP1.png)