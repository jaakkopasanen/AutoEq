# Audeze LCD-X

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 4.0; 22 4.0; 23 4.0; 25 3.9; 26 3.8; 28 3.6; 30 3.2; 32 2.8; 35 2.1; 37 1.6; 40 1.2; 42 1.1; 45 1.1; 49 1.0; 52 1.0; 56 0.9; 59 0.9; 64 0.8; 68 0.7; 73 0.6; 78 0.5; 83 0.3; 89 0.0; 95 -0.2; 102 -0.4; 109 -0.5; 117 -0.6; 125 -0.9; 134 -1.0; 143 -1.2; 153 -1.3; 164 -1.4; 175 -1.5; 188 -1.7; 201 -1.8; 215 -1.8; 230 -1.7; 246 -1.8; 263 -1.7; 282 -1.6; 301 -1.6; 323 -1.4; 345 -1.2; 369 -1.1; 395 -1.1; 423 -0.8; 452 -0.8; 484 -1.2; 518 -1.2; 554 -0.9; 593 -0.6; 635 -0.6; 679 -0.7; 726 -0.7; 777 -0.4; 832 -0.3; 890 -0.1; 952 0.0; 1019 0.1; 1090 0.3; 1167 0.1; 1248 0.1; 1336 -0.4; 1429 -0.6; 1529 -0.8; 1636 -0.9; 1751 -0.7; 1873 -0.8; 2004 -0.9; 2145 -0.9; 2295 -0.3; 2455 0.7; 2627 1.9; 2811 3.1; 3008 4.3; 3219 5.1; 3444 5.6; 3685 5.0; 3943 3.5; 4219 3.3; 4514 2.5; 4830 2.8; 5168 5.2; 5530 6.0; 5917 5.2; 6331 3.7; 6775 3.0; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 -0.2; 16326 -1.4; 17469 -2.6; 18692 -3.8; 20000 -5.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.093091504264768dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.3dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 15 Hz    | 0.52 | 4.7 dB  |
| Peaking | 238 Hz   | 0.57 | -1.8 dB |
| Peaking | 3383 Hz  | 3.36 | 5.7 dB  |
| Peaking | 5623 Hz  | 3.34 | 5.9 dB  |
| Peaking | 19625 Hz | 1.23 | -4.8 dB |
| Peaking | 1087 Hz  | 3.6  | 0.7 dB  |
| Peaking | 2056 Hz  | 1.65 | -1.6 dB |
| Peaking | 2783 Hz  | 4.43 | 1.6 dB  |
| Peaking | 8236 Hz  | 6.46 | -0.6 dB |
| Peaking | 14457 Hz | 3.53 | 0.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-X/Audeze%20LCD-X.png)