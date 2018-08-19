# Fischer Audio SBA-03

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 4.8; 22 4.6; 23 4.5; 25 4.3; 26 4.2; 28 4.1; 30 4.0; 32 3.8; 35 3.6; 37 3.5; 40 3.3; 42 3.1; 45 3.0; 49 2.7; 52 2.6; 56 2.3; 59 2.1; 64 1.8; 68 1.6; 73 1.3; 78 1.0; 83 0.7; 89 0.3; 95 0.0; 102 -0.3; 109 -0.4; 117 -0.6; 125 -0.9; 134 -1.1; 143 -1.3; 153 -1.4; 164 -1.6; 175 -1.6; 188 -1.7; 201 -1.9; 215 -1.8; 230 -1.8; 246 -1.9; 263 -1.8; 282 -1.8; 301 -1.7; 323 -1.6; 345 -1.5; 369 -1.4; 395 -1.2; 423 -1.0; 452 -0.8; 484 -0.7; 518 -0.5; 554 -0.2; 593 0.2; 635 0.2; 679 0.2; 726 0.3; 777 0.5; 832 0.5; 890 0.4; 952 0.2; 1019 0.0; 1090 -0.1; 1167 -0.3; 1248 -0.5; 1336 -0.9; 1429 -1.3; 1529 -1.7; 1636 -2.1; 1751 -2.3; 1873 -2.5; 2004 -2.7; 2145 -3.2; 2295 -3.9; 2455 -4.2; 2627 -3.9; 2811 -2.0; 3008 1.5; 3219 4.5; 3444 6.0; 3685 6.0; 3943 6.0; 4219 5.6; 4514 3.5; 4830 1.2; 5168 -1.1; 5530 -4.6; 5917 -3.4; 6331 0.8; 6775 3.2; 7249 1.3; 7756 0.3; 8299 -0.9; 8880 -2.1; 9502 -0.7; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999973023095dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fischer Audio SBA-03 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 24 Hz   |  1.4  | 4.6 dB   |
| Peaking | 46 Hz   |  2.18 | 2.3 dB   |
| Peaking | 2623 Hz |  1.48 | -10.1 dB |
| Peaking | 3463 Hz |  1.57 | 12.1 dB  |
| Peaking | 5561 Hz |  6.98 | -7.5 dB  |
| Peaking | 71 Hz   |  1.95 | 1.1 dB   |
| Peaking | 231 Hz  |  0.62 | -2.0 dB  |
| Peaking | 748 Hz  |  1.65 | 1.2 dB   |
| Peaking | 6796 Hz | 10.2  | 3.2 dB   |
| Peaking | 8828 Hz |  6.3  | -2.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fischer%20Audio%20SBA-03/Fischer%20Audio%20SBA-03.png)