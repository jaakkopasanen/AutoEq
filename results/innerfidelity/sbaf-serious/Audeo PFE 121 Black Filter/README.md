# Audeo PFE 121 Black Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 0.6; 22 0.4; 23 0.4; 25 0.3; 26 0.3; 28 0.2; 30 0.2; 32 0.1; 35 0.1; 37 0.0; 40 -0.0; 42 -0.0; 45 -0.1; 49 -0.1; 52 -0.1; 56 -0.2; 59 -0.2; 64 -0.3; 68 -0.4; 73 -0.5; 78 -0.7; 83 -1.0; 89 -1.4; 95 -1.7; 102 -2.2; 109 -2.7; 117 -3.3; 125 -3.8; 134 -4.2; 143 -4.5; 153 -4.6; 164 -4.8; 175 -4.7; 188 -4.6; 201 -4.6; 215 -4.5; 230 -4.3; 246 -4.2; 263 -4.0; 282 -3.7; 301 -3.6; 323 -3.3; 345 -3.1; 369 -2.9; 395 -2.7; 423 -2.2; 452 -2.0; 484 -1.9; 518 -1.6; 554 -1.2; 593 -0.6; 635 -0.4; 679 -0.2; 726 -0.1; 777 0.3; 832 0.3; 890 0.2; 952 0.0; 1019 0.0; 1090 -0.2; 1167 -0.1; 1248 -0.1; 1336 -0.2; 1429 -0.4; 1529 -0.6; 1636 -0.6; 1751 -0.2; 1873 0.4; 2004 0.9; 2145 1.7; 2295 2.7; 2455 3.5; 2627 3.2; 2811 2.9; 3008 3.5; 3219 4.1; 3444 4.9; 3685 5.5; 3943 5.5; 4219 5.0; 4514 5.1; 4830 5.9; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 -1.2; 8299 -3.8; 8880 -4.2; 9502 -3.3; 10167 -2.2; 10879 -0.4; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeo PFE 121 Black Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 80 Hz   | 0.76 | 2.1 dB  |
| Peaking | 167 Hz  | 0.59 | -5.6 dB |
| Peaking | 6021 Hz | 1.57 | 6.2 dB  |
| Peaking | 3568 Hz | 1.35 | 3.9 dB  |
| Peaking | 8562 Hz | 2.59 | -7.1 dB |
| Peaking | 18 Hz   | 1.36 | 0.5 dB  |
| Peaking | 786 Hz  | 3.04 | 0.9 dB  |
| Peaking | 1627 Hz | 2.72 | -1.2 dB |
| Peaking | 2386 Hz | 7.29 | 1.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeo%20PFE%20121%20Black%20Filter/Audeo%20PFE%20121%20Black%20Filter.png)