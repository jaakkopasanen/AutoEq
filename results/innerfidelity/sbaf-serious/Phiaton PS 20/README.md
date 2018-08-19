# Phiaton PS 20

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 5.3; 22 4.7; 23 4.4; 25 3.8; 26 3.6; 28 3.1; 30 2.7; 32 2.3; 35 1.8; 37 1.5; 40 1.0; 42 0.7; 45 0.4; 49 -0.1; 52 -0.4; 56 -0.8; 59 -1.1; 64 -1.6; 68 -2.0; 73 -2.4; 78 -2.8; 83 -3.2; 89 -3.6; 95 -4.0; 102 -4.4; 109 -4.6; 117 -4.9; 125 -5.2; 134 -5.5; 143 -5.7; 153 -6.0; 164 -6.2; 175 -6.3; 188 -6.4; 201 -6.6; 215 -6.7; 230 -6.8; 246 -6.9; 263 -7.0; 282 -6.9; 301 -7.1; 323 -7.1; 345 -7.1; 369 -7.3; 395 -7.4; 423 -7.2; 452 -7.0; 484 -7.1; 518 -6.9; 554 -6.4; 593 -5.8; 635 -5.2; 679 -4.6; 726 -3.6; 777 -2.6; 832 -1.8; 890 -1.0; 952 -0.3; 1019 0.1; 1090 0.4; 1167 0.5; 1248 0.3; 1336 -0.3; 1429 -1.1; 1529 -2.2; 1636 -3.1; 1751 -4.2; 1873 -5.1; 2004 -5.6; 2145 -5.9; 2295 -4.8; 2455 -2.5; 2627 -0.2; 2811 2.0; 3008 4.5; 3219 5.9; 3444 6.0; 3685 6.0; 3943 5.5; 4219 2.9; 4514 0.2; 4830 -2.3; 5168 -4.0; 5530 -3.3; 5917 -0.4; 6331 2.1; 6775 3.2; 7249 1.3; 7756 0.2; 8299 -0.9; 8880 -0.4; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999993210627dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton PS 20 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.3dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 21 Hz   | 0.95 | 5.2 dB   |
| Peaking | 274 Hz  | 0.4  | -7.7 dB  |
| Peaking | 2176 Hz | 2.02 | -14.3 dB |
| Peaking | 2925 Hz | 0.73 | 10.6 dB  |
| Peaking | 5136 Hz | 3.74 | -9.0 dB  |
| Peaking | 587 Hz  | 1.14 | -5.5 dB  |
| Peaking | 769 Hz  | 0.59 | 4.6 dB   |
| Peaking | 1661 Hz | 2.68 | -3.2 dB  |
| Peaking | 6718 Hz | 5.78 | 3.6 dB   |
| Peaking | 8049 Hz | 1.62 | -2.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Phiaton%20PS%2020/Phiaton%20PS%2020.png)