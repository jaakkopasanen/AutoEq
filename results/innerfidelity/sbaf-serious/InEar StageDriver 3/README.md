# InEar StageDriver 3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -1.5; 22 -1.6; 23 -1.6; 25 -1.7; 26 -1.8; 28 -1.9; 30 -1.9; 32 -2.0; 35 -2.2; 37 -2.2; 40 -2.3; 42 -2.4; 45 -2.6; 49 -2.8; 52 -2.9; 56 -3.1; 59 -3.3; 64 -3.5; 68 -3.7; 73 -4.0; 78 -4.3; 83 -4.6; 89 -4.9; 95 -5.2; 102 -5.4; 109 -5.6; 117 -5.7; 125 -5.9; 134 -6.2; 143 -6.3; 153 -6.4; 164 -6.5; 175 -6.5; 188 -6.5; 201 -6.5; 215 -6.3; 230 -6.1; 246 -6.0; 263 -5.8; 282 -5.4; 301 -5.1; 323 -4.8; 345 -4.3; 369 -3.9; 395 -3.5; 423 -2.9; 452 -2.5; 484 -2.2; 518 -1.8; 554 -1.3; 593 -0.8; 635 -0.5; 679 -0.3; 726 -0.0; 777 0.3; 832 0.4; 890 0.3; 952 0.2; 1019 -0.1; 1090 -0.2; 1167 -0.5; 1248 -0.8; 1336 -1.3; 1429 -1.9; 1529 -2.6; 1636 -3.2; 1751 -3.8; 1873 -4.2; 2004 -4.5; 2145 -4.7; 2295 -4.0; 2455 -2.0; 2627 0.2; 2811 2.3; 3008 4.6; 3219 5.8; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 5.4; 5168 2.9; 5530 4.8; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 -1.6
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999991048582dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `InEar StageDriver 3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 108 Hz  | 0.5  | -4.6 dB |
| Peaking | 239 Hz  | 1.01 | -3.8 dB |
| Peaking | 2123 Hz | 1.95 | -7.6 dB |
| Peaking | 3547 Hz | 1.33 | 7.9 dB  |
| Peaking | 6077 Hz | 5.49 | 4.4 dB  |
| Peaking | 22 Hz   | 1.58 | -0.8 dB |
| Peaking | 828 Hz  | 2.38 | 1.3 dB  |
| Peaking | 1560 Hz | 5.56 | -1.0 dB |
| Peaking | 6715 Hz | 9.63 | 1.7 dB  |
| Peaking | 8093 Hz | 2.29 | -1.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/InEar%20StageDriver%203/InEar%20StageDriver%203.png)