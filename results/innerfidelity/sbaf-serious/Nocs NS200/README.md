# Nocs NS200

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.9dB
GraphicEQ: 10 -84; 20 -8.6; 22 -8.4; 23 -8.3; 25 -8.1; 26 -8.0; 28 -7.7; 30 -7.5; 32 -7.4; 35 -7.1; 37 -7.0; 40 -6.8; 42 -6.6; 45 -6.5; 49 -6.3; 52 -6.2; 56 -6.1; 59 -6.0; 64 -6.0; 68 -6.0; 73 -5.9; 78 -6.0; 83 -6.0; 89 -6.1; 95 -6.2; 102 -6.2; 109 -6.1; 117 -6.1; 125 -6.1; 134 -6.1; 143 -6.0; 153 -6.0; 164 -5.9; 175 -5.7; 188 -5.6; 201 -5.5; 215 -5.3; 230 -5.1; 246 -4.8; 263 -4.6; 282 -4.2; 301 -4.0; 323 -3.7; 345 -3.4; 369 -3.1; 395 -2.8; 423 -2.3; 452 -1.9; 484 -1.7; 518 -1.4; 554 -0.9; 593 -0.4; 635 -0.1; 679 0.0; 726 0.3; 777 0.5; 832 0.5; 890 0.4; 952 0.2; 1019 -0.1; 1090 -0.3; 1167 -0.5; 1248 -0.9; 1336 -1.3; 1429 -1.8; 1529 -2.2; 1636 -2.6; 1751 -3.0; 1873 -3.1; 2004 -3.3; 2145 -3.5; 2295 -3.7; 2455 -3.4; 2627 -3.1; 2811 -2.1; 3008 -0.1; 3219 1.7; 3444 3.3; 3685 3.8; 3943 3.4; 4219 1.7; 4514 0.2; 4830 -0.9; 5168 -1.7; 5530 -3.7; 5917 -5.7; 6331 -4.6; 6775 -2.2; 7249 -0.3; 7756 0.2; 8299 0.0; 8880 -0.3; 9502 -0.9; 10167 -0.2; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.9208490926752853dB` and instead set Global volume in the UI for both channels to **-39**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Nocs NS200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.2dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 13 Hz   | 0.15 | -8.0 dB |
| Peaking | 184 Hz  | 0.71 | -4.5 dB |
| Peaking | 2285 Hz | 1.62 | -4.4 dB |
| Peaking | 3617 Hz | 3.15 | 5.7 dB  |
| Peaking | 5935 Hz | 4.75 | -6.2 dB |
| Peaking | 16 Hz   | 1.79 | -1.2 dB |
| Peaking | 369 Hz  | 2.09 | -0.7 dB |
| Peaking | 787 Hz  | 1.63 | 1.4 dB  |
| Peaking | 1549 Hz | 3.75 | -0.9 dB |
| Peaking | 7622 Hz | 9.71 | 1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Nocs%20NS200/Nocs%20NS200.png)