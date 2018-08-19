# Pioneer HDJ-1000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 5.9; 73 5.0; 78 4.0; 83 3.1; 89 2.4; 95 1.8; 102 1.5; 109 1.4; 117 1.4; 125 1.2; 134 1.3; 143 1.3; 153 1.4; 164 1.5; 175 1.7; 188 1.6; 201 1.6; 215 1.8; 230 1.8; 246 2.1; 263 2.3; 282 2.6; 301 2.7; 323 2.8; 345 2.9; 369 3.2; 395 3.5; 423 3.9; 452 3.6; 484 2.9; 518 2.2; 554 2.6; 593 2.6; 635 2.2; 679 1.7; 726 1.3; 777 1.0; 832 0.6; 890 0.4; 952 0.2; 1019 -0.1; 1090 -0.4; 1167 -0.8; 1248 -1.4; 1336 -2.2; 1429 -2.8; 1529 -3.2; 1636 -3.2; 1751 -2.7; 1873 -1.7; 2004 -0.7; 2145 0.6; 2295 1.8; 2455 3.2; 2627 4.3; 2811 5.1; 3008 6.0; 3219 6.0; 3444 6.0; 3685 5.2; 3943 1.9; 4219 1.2; 4514 2.8; 4830 5.7; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Pioneer HDJ-1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.58 | 6.8 dB  |
| Peaking | 422 Hz  | 1.04 | 3.4 dB  |
| Peaking | 1587 Hz | 2.06 | -4.4 dB |
| Peaking | 3027 Hz | 2.21 | 6.5 dB  |
| Peaking | 5673 Hz | 2.99 | 6.3 dB  |
| Peaking | 38 Hz   | 2.65 | -0.9 dB |
| Peaking | 65 Hz   | 2.7  | 2.0 dB  |
| Peaking | 98 Hz   | 2.2  | -1.4 dB |
| Peaking | 2397 Hz | 4.34 | 0.3 dB  |
| Peaking | 8311 Hz | 4.44 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Pioneer%20HDJ-1000/Pioneer%20HDJ-1000.png)