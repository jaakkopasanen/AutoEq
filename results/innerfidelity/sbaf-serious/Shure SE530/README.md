# Shure SE530

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 2.2; 22 2.1; 23 2.1; 25 2.0; 26 2.0; 28 1.9; 30 1.8; 32 1.8; 35 1.6; 37 1.5; 40 1.4; 42 1.3; 45 1.2; 49 1.0; 52 0.8; 56 0.6; 59 0.4; 64 0.1; 68 -0.1; 73 -0.4; 78 -0.6; 83 -0.9; 89 -1.2; 95 -1.5; 102 -1.9; 109 -2.0; 117 -2.2; 125 -2.5; 134 -2.7; 143 -2.8; 153 -3.0; 164 -3.1; 175 -3.2; 188 -3.3; 201 -3.4; 215 -3.4; 230 -3.3; 246 -3.3; 263 -3.3; 282 -3.1; 301 -3.1; 323 -2.9; 345 -2.8; 369 -2.7; 395 -2.5; 423 -2.2; 452 -2.0; 484 -1.8; 518 -1.6; 554 -1.3; 593 -0.8; 635 -0.6; 679 -0.5; 726 -0.2; 777 0.1; 832 0.2; 890 0.1; 952 0.1; 1019 0.0; 1090 -0.1; 1167 -0.2; 1248 -0.4; 1336 -0.7; 1429 -1.0; 1529 -1.3; 1636 -1.6; 1751 -1.7; 1873 -1.8; 2004 -1.8; 2145 -1.6; 2295 -0.8; 2455 0.4; 2627 1.8; 2811 2.9; 3008 4.2; 3219 5.2; 3444 5.9; 3685 5.8; 3943 5.5; 4219 4.6; 4514 4.4; 4830 5.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.09916874061621dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Shure SE530 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.54 | 2.2 dB  |
| Peaking | 203 Hz  | 0.59 | -3.7 dB |
| Peaking | 2017 Hz | 2.12 | -3.2 dB |
| Peaking | 3481 Hz | 1.75 | 6.0 dB  |
| Peaking | 5741 Hz | 3.07 | 5.5 dB  |
| Peaking | 459 Hz  | 1.06 | -1.8 dB |
| Peaking | 596 Hz  | 0.62 | 1.6 dB  |
| Peaking | 1476 Hz | 2.71 | -0.8 dB |
| Peaking | 6563 Hz | 7.82 | 2.1 dB  |
| Peaking | 7763 Hz | 2.2  | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Shure%20SE530/Shure%20SE530.png)