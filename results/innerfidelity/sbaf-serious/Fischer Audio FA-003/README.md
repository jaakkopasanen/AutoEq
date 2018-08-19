# Fischer Audio FA-003

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.6dB
GraphicEQ: 10 -84; 20 3.5; 22 2.9; 23 2.7; 25 2.2; 26 1.9; 28 1.5; 30 1.2; 32 0.8; 35 0.4; 37 0.2; 40 -0.1; 42 -0.3; 45 -0.5; 49 -0.7; 52 -0.8; 56 -0.9; 59 -1.0; 64 -1.0; 68 -1.0; 73 -1.1; 78 -1.2; 83 -1.6; 89 -2.3; 95 -3.2; 102 -4.0; 109 -4.3; 117 -4.3; 125 -4.7; 134 -5.0; 143 -5.2; 153 -5.2; 164 -4.5; 175 -4.7; 188 -4.5; 201 -4.0; 215 -3.2; 230 -2.1; 246 -0.6; 263 1.2; 282 3.4; 301 4.5; 323 3.8; 345 2.5; 369 1.3; 395 0.9; 423 -0.1; 452 -0.8; 484 -1.2; 518 -1.5; 554 -1.4; 593 -1.3; 635 -1.4; 679 -1.3; 726 -1.1; 777 -0.5; 832 -0.2; 890 -0.6; 952 -0.4; 1019 0.1; 1090 0.4; 1167 0.7; 1248 0.9; 1336 0.8; 1429 0.5; 1529 0.3; 1636 0.1; 1751 -0.2; 1873 -0.2; 2004 -0.3; 2145 -0.2; 2295 -0.3; 2455 -0.3; 2627 -0.5; 2811 -1.3; 3008 -1.6; 3219 -0.4; 3444 0.4; 3685 -0.1; 3943 -1.7; 4219 -3.1; 4514 -3.9; 4830 -3.4; 5168 -2.3; 5530 -3.4; 5917 -3.9; 6331 -0.9; 6775 3.4; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -0.1; 18692 -1.8; 20000 -4.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.623794055647293dB` and instead set Global volume in the UI for both channels to **-46**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fischer Audio FA-003 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.41 | 3.5 dB  |
| Peaking | 158 Hz  | 0.88 | -5.7 dB |
| Peaking | 302 Hz  | 2.87 | 7.0 dB  |
| Peaking | 564 Hz  | 2.46 | -1.5 dB |
| Peaking | 4758 Hz | 3.04 | -4.0 dB |
| Peaking | 1261 Hz | 4.03 | 1.1 dB  |
| Peaking | 3003 Hz | 4.92 | -1.7 dB |
| Peaking | 3398 Hz | 6.17 | 1.9 dB  |
| Peaking | 5943 Hz | 7.71 | -3.9 dB |
| Peaking | 6714 Hz | 7.04 | 4.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fischer%20Audio%20FA-003/Fischer%20Audio%20FA-003.png)