# VSonic VS05

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.5dB
GraphicEQ: 10 -84; 20 3.3; 22 2.8; 23 2.5; 25 2.1; 26 1.9; 28 1.6; 30 1.3; 32 1.1; 35 0.8; 37 0.5; 40 0.3; 42 0.1; 45 -0.2; 49 -0.5; 52 -0.7; 56 -1.0; 59 -1.1; 64 -1.5; 68 -1.8; 73 -2.1; 78 -2.3; 83 -2.6; 89 -2.9; 95 -3.3; 102 -3.6; 109 -3.7; 117 -3.8; 125 -4.1; 134 -4.2; 143 -4.4; 153 -4.5; 164 -4.6; 175 -4.6; 188 -4.6; 201 -4.7; 215 -4.6; 230 -4.4; 246 -4.4; 263 -4.3; 282 -4.1; 301 -4.0; 323 -3.8; 345 -3.5; 369 -3.3; 395 -3.1; 423 -2.7; 452 -2.5; 484 -2.3; 518 -2.0; 554 -1.6; 593 -1.1; 635 -0.8; 679 -0.7; 726 -0.4; 777 -0.0; 832 0.1; 890 0.1; 952 0.1; 1019 0.0; 1090 0.0; 1167 0.1; 1248 0.1; 1336 -0.0; 1429 -0.0; 1529 0.1; 1636 0.3; 1751 0.6; 1873 0.9; 2004 1.3; 2145 1.6; 2295 1.9; 2455 2.5; 2627 2.9; 2811 3.1; 3008 3.6; 3219 4.0; 3444 4.4; 3685 4.1; 3943 3.3; 4219 1.6; 4514 0.2; 4830 -0.7; 5168 -1.3; 5530 -2.6; 5917 -3.9; 6331 -4.3; 6775 -3.2; 7249 -2.9; 7756 -3.4; 8299 -4.7; 8880 -5.5; 9502 -4.6; 10167 -1.8; 10879 -0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.4637820190882485dB` and instead set Global volume in the UI for both channels to **-44**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `VSonic VS05 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.3dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 17 Hz    | 0.8  | 3.7 dB  |
| Peaking | 182 Hz   | 0.51 | -4.9 dB |
| Peaking | 3389 Hz  | 1.35 | 5.0 dB  |
| Peaking | 5989 Hz  | 1.96 | -4.9 dB |
| Peaking | 8887 Hz  | 4.38 | -5.3 dB |
| Peaking | 396 Hz   | 2.29 | -0.4 dB |
| Peaking | 803 Hz   | 2.63 | 0.9 dB  |
| Peaking | 11159 Hz | 6.28 | 1.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/VSonic%20VS05/VSonic%20VS05.png)