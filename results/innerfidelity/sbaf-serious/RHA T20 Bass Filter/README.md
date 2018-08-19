# RHA T20 Bass Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.7dB
GraphicEQ: 10 -84; 20 -5.0; 22 -5.3; 23 -5.4; 25 -5.6; 26 -5.7; 28 -5.8; 30 -5.9; 32 -6.0; 35 -6.1; 37 -6.2; 40 -6.3; 42 -6.3; 45 -6.3; 49 -6.3; 52 -6.3; 56 -6.3; 59 -6.3; 64 -6.3; 68 -6.3; 73 -6.4; 78 -6.4; 83 -6.4; 89 -6.4; 95 -6.4; 102 -6.3; 109 -6.1; 117 -6.0; 125 -5.9; 134 -5.8; 143 -5.5; 153 -5.4; 164 -5.2; 175 -4.8; 188 -4.6; 201 -4.3; 215 -4.0; 230 -3.7; 246 -3.3; 263 -3.1; 282 -2.7; 301 -2.3; 323 -2.0; 345 -1.6; 369 -1.4; 395 -1.0; 423 -0.6; 452 -0.3; 484 -0.2; 518 0.0; 554 0.4; 593 0.8; 635 1.0; 679 1.0; 726 1.1; 777 1.2; 832 1.0; 890 0.7; 952 0.4; 1019 -0.1; 1090 -0.5; 1167 -1.0; 1248 -1.6; 1336 -2.6; 1429 -3.5; 1529 -4.1; 1636 -3.7; 1751 -1.6; 1873 0.0; 2004 -1.7; 2145 -2.4; 2295 -2.5; 2455 -2.5; 2627 -2.4; 2811 -1.9; 3008 -0.9; 3219 -0.3; 3444 0.0; 3685 -0.9; 3943 -2.9; 4219 -5.9; 4514 -7.6; 4830 -5.8; 5168 -1.8; 5530 2.0; 5917 4.7; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -0.5; 15258 -0.7; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.694493761299576dB` and instead set Global volume in the UI for both channels to **-56**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RHA T20 Bass Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.1dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 41 Hz   | 0.36 | -6.1 dB |
| Peaking | 148 Hz  | 0.89 | -3.2 dB |
| Peaking | 1539 Hz | 3.66 | -4.1 dB |
| Peaking | 4559 Hz | 4.18 | -8.8 dB |
| Peaking | 6138 Hz | 4.09 | 7.1 dB  |
| Peaking | 275 Hz  | 2.4  | -0.7 dB |
| Peaking | 715 Hz  | 1.51 | 1.8 dB  |
| Peaking | 1838 Hz | 7.06 | 3.1 dB  |
| Peaking | 2369 Hz | 1.39 | -2.6 dB |
| Peaking | 3406 Hz | 3.87 | 2.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/RHA%20T20%20Bass%20Filter/RHA%20T20%20Bass%20Filter.png)