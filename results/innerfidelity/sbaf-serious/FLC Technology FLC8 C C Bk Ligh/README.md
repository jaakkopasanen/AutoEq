# FLC Technology FLC8 C C Bk Ligh

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 5.9; 45 5.8; 49 5.6; 52 5.4; 56 5.1; 59 4.9; 64 4.6; 68 4.3; 73 4.0; 78 3.7; 83 3.4; 89 2.9; 95 2.6; 102 2.3; 109 2.1; 117 1.9; 125 1.6; 134 1.3; 143 1.1; 153 0.9; 164 0.8; 175 0.7; 188 0.6; 201 0.5; 215 0.5; 230 0.5; 246 0.4; 263 0.4; 282 0.6; 301 0.6; 323 0.6; 345 0.8; 369 0.9; 395 0.9; 423 1.2; 452 1.3; 484 1.3; 518 1.4; 554 1.6; 593 1.9; 635 1.9; 679 1.8; 726 1.6; 777 1.7; 832 1.7; 890 1.2; 952 0.6; 1019 -0.1; 1090 -0.8; 1167 -1.5; 1248 -1.7; 1336 -2.0; 1429 -1.9; 1529 -1.5; 1636 -0.8; 1751 0.0; 1873 1.0; 2004 1.5; 2145 1.8; 2295 2.0; 2455 2.2; 2627 1.8; 2811 1.6; 3008 4.5; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 3.9; 6775 0.3; 7249 -2.5; 7756 -3.7; 8299 -3.9; 8880 -3.9; 9502 -4.0; 10167 -3.6; 10879 -2.0; 11640 -0.2; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FLC Technology FLC8 C C Bk Ligh ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.4dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 0.43 | 6.3 dB  |
| Peaking | 1382 Hz  | 4.13 | -2.8 dB |
| Peaking | 3600 Hz  | 1.68 | 4.9 dB  |
| Peaking | 5880 Hz  | 1.58 | 9.0 dB  |
| Peaking | 7782 Hz  | 1.54 | -8.9 dB |
| Peaking | 677 Hz   | 1.38 | 2.0 dB  |
| Peaking | 1139 Hz  | 4.17 | -1.4 dB |
| Peaking | 2063 Hz  | 7.28 | 0.5 dB  |
| Peaking | 10231 Hz | 4.48 | -2.6 dB |
| Peaking | 11429 Hz | 1.89 | 1.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/FLC%20Technology%20FLC8%20C%20C%20Bk%20Ligh/FLC%20Technology%20FLC8%20C%20C%20Bk%20Ligh.png)