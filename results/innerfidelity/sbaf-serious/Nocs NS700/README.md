# Nocs NS700

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.5dB
GraphicEQ: 10 -84; 20 -1.7; 22 -2.3; 23 -2.5; 25 -2.9; 26 -3.1; 28 -3.4; 30 -3.7; 32 -3.9; 35 -4.3; 37 -4.4; 40 -4.6; 42 -4.7; 45 -4.8; 49 -4.8; 52 -4.9; 56 -5.0; 59 -5.1; 64 -5.2; 68 -5.2; 73 -5.5; 78 -5.5; 83 -5.4; 89 -5.4; 95 -5.1; 102 -4.6; 109 -3.8; 117 -3.4; 125 -4.1; 134 -4.3; 143 -4.3; 153 -4.0; 164 -3.1; 175 -2.3; 188 -1.8; 201 -1.0; 215 -0.2; 230 0.7; 246 1.4; 263 1.8; 282 1.8; 301 1.2; 323 -0.5; 345 -1.7; 369 -2.1; 395 -1.9; 423 -1.7; 452 -1.6; 484 -1.6; 518 -1.4; 554 -1.1; 593 -0.8; 635 -0.7; 679 -0.8; 726 -0.5; 777 -0.3; 832 -0.2; 890 -0.2; 952 0.0; 1019 0.2; 1090 0.7; 1167 1.1; 1248 1.4; 1336 1.3; 1429 1.1; 1529 0.5; 1636 0.8; 1751 1.3; 1873 1.5; 2004 1.7; 2145 1.6; 2295 1.3; 2455 1.2; 2627 0.6; 2811 -0.1; 3008 -0.9; 3219 -1.3; 3444 -1.2; 3685 -0.8; 3943 0.8; 4219 2.3; 4514 2.8; 4830 1.4; 5168 0.5; 5530 1.0; 5917 3.2; 6331 2.7; 6775 1.0; 7249 0.7; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.494891063917946dB` and instead set Global volume in the UI for both channels to **-34**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Nocs NS700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -3.2dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 45 Hz   | 0.69 | -4.4 dB |
| Peaking | 102 Hz  | 1.16 | -3.3 dB |
| Peaking | 465 Hz  | 2.87 | -1.7 dB |
| Peaking | 1766 Hz | 1.51 | 1.5 dB  |
| Peaking | 6055 Hz | 4.67 | 3.1 dB  |
| Peaking | 153 Hz  | 4.58 | -1.9 dB |
| Peaking | 274 Hz  | 2.64 | 3.3 dB  |
| Peaking | 354 Hz  | 4.2  | -2.3 dB |
| Peaking | 3348 Hz | 4.36 | -2.0 dB |
| Peaking | 4398 Hz | 7.35 | 3.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Nocs%20NS700/Nocs%20NS700.png)