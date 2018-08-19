# SMS DJ Pro

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -4.2; 22 -4.4; 23 -4.5; 25 -4.7; 26 -4.7; 28 -4.8; 30 -4.8; 32 -4.7; 35 -4.6; 37 -4.6; 40 -4.4; 42 -4.3; 45 -4.1; 49 -3.8; 52 -3.5; 56 -3.3; 59 -3.0; 64 -2.4; 68 -2.0; 73 -1.9; 78 -2.1; 83 -2.7; 89 -4.0; 95 -5.2; 102 -5.3; 109 -4.6; 117 -3.6; 125 -2.7; 134 -2.3; 143 -2.0; 153 -1.2; 164 -0.5; 175 -1.0; 188 -1.1; 201 -1.3; 215 -1.2; 230 -1.3; 246 -1.6; 263 -1.8; 282 -2.3; 301 -2.2; 323 -2.3; 345 -2.5; 369 -3.9; 395 -4.5; 423 -3.9; 452 -3.5; 484 -3.5; 518 -3.1; 554 -2.7; 593 -2.0; 635 -1.6; 679 -1.1; 726 -0.2; 777 0.6; 832 -0.4; 890 -0.3; 952 -0.0; 1019 0.0; 1090 0.3; 1167 0.4; 1248 0.3; 1336 0.1; 1429 -0.5; 1529 -0.9; 1636 -1.1; 1751 -1.1; 1873 -0.7; 2004 0.2; 2145 1.1; 2295 1.6; 2455 2.6; 2627 3.4; 2811 4.0; 3008 4.7; 3219 4.7; 3444 4.5; 3685 4.2; 3943 3.2; 4219 3.6; 4514 2.9; 4830 2.0; 5168 3.4; 5530 5.8; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.079209687832977dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `SMS DJ Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 30 Hz   |  0.7  | -5.0 dB |
| Peaking | 103 Hz  |  3.14 | -4.5 dB |
| Peaking | 414 Hz  |  1.54 | -4.1 dB |
| Peaking | 3227 Hz |  2.17 | 4.9 dB  |
| Peaking | 5936 Hz |  3.73 | 6.1 dB  |
| Peaking | 761 Hz  | 12.07 | 1.5 dB  |
| Peaking | 1172 Hz |  3.73 | 0.8 dB  |
| Peaking | 1700 Hz |  3.04 | -1.8 dB |
| Peaking | 2503 Hz |  4.5  | 0.9 dB  |
| Peaking | 8242 Hz |  4.81 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/SMS%20DJ%20Pro/SMS%20DJ%20Pro.png)