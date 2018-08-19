# Sony MDR-XB300

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 4.9; 22 3.6; 23 3.0; 25 1.8; 26 1.2; 28 0.2; 30 -0.7; 32 -1.5; 35 -2.6; 37 -3.2; 40 -4.0; 42 -4.5; 45 -5.1; 49 -5.9; 52 -6.3; 56 -6.7; 59 -6.9; 64 -6.9; 68 -6.8; 73 -6.8; 78 -7.2; 83 -7.5; 89 -7.9; 95 -8.2; 102 -8.3; 109 -8.3; 117 -8.1; 125 -8.1; 134 -7.9; 143 -7.6; 153 -7.3; 164 -6.9; 175 -6.7; 188 -6.5; 201 -6.3; 215 -5.7; 230 -5.2; 246 -4.4; 263 -4.0; 282 -3.6; 301 -3.0; 323 -2.3; 345 -1.6; 369 -0.8; 395 -0.2; 423 0.7; 452 1.3; 484 1.8; 518 2.2; 554 2.9; 593 3.6; 635 3.9; 679 4.2; 726 4.3; 777 4.2; 832 3.3; 890 2.1; 952 0.8; 1019 -0.2; 1090 -1.0; 1167 -1.2; 1248 -1.8; 1336 -3.0; 1429 -3.6; 1529 -3.9; 1636 -4.0; 1751 -4.6; 1873 -5.1; 2004 -5.6; 2145 -6.1; 2295 -6.1; 2455 -5.4; 2627 -4.2; 2811 -2.9; 3008 -1.0; 3219 0.5; 3444 2.2; 3685 3.4; 3943 4.5; 4219 4.7; 4514 5.9; 4830 6.0; 5168 6.0; 5530 6.0; 5917 4.6; 6331 0.8; 6775 1.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099917628730951dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sony MDR-XB300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 1.95 | 5.5 dB  |
| Peaking | 72 Hz   | 0.71 | -7.1 dB |
| Peaking | 161 Hz  | 1.32 | -5.1 dB |
| Peaking | 2173 Hz | 1.91 | -7.4 dB |
| Peaking | 4655 Hz | 1.77 | 7.2 dB  |
| Peaking | 77 Hz   | 6.88 | 0.9 dB  |
| Peaking | 273 Hz  | 1.99 | -1.8 dB |
| Peaking | 689 Hz  | 1.29 | 5.3 dB  |
| Peaking | 1302 Hz | 1.88 | -2.7 dB |
| Peaking | 8473 Hz | 2.9  | -0.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sony%20MDR-XB300/Sony%20MDR-XB300.png)