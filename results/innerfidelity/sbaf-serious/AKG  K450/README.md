# AKG  K450

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 5.9; 35 5.4; 37 5.1; 40 4.8; 42 4.5; 45 4.3; 49 3.9; 52 3.8; 56 3.6; 59 3.5; 64 3.3; 68 3.2; 73 3.1; 78 2.9; 83 2.7; 89 2.5; 95 2.1; 102 1.8; 109 1.4; 117 1.0; 125 0.6; 134 0.1; 143 -0.2; 153 -0.4; 164 -0.5; 175 -0.6; 188 -0.7; 201 -0.8; 215 -0.9; 230 -0.9; 246 -1.0; 263 -0.8; 282 -0.8; 301 -0.9; 323 -0.9; 345 -1.0; 369 -0.8; 395 -0.5; 423 -0.4; 452 -0.6; 484 -0.8; 518 -1.0; 554 -0.8; 593 -0.5; 635 -0.3; 679 -0.2; 726 -0.1; 777 -0.0; 832 0.1; 890 -0.2; 952 0.5; 1019 0.7; 1090 0.8; 1167 1.2; 1248 1.9; 1336 2.5; 1429 3.1; 1529 4.0; 1636 4.9; 1751 5.1; 1873 5.7; 2004 6.0; 2145 6.0; 2295 6.0; 2455 6.0; 2627 5.9; 2811 4.8; 3008 3.2; 3219 1.5; 3444 0.4; 3685 0.2; 3943 1.4; 4219 2.3; 4514 3.6; 4830 5.8; 5168 6.0; 5530 5.9; 5917 5.6; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG  K450 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 0.19 | 6.3 dB  |
| Peaking | 255 Hz  | 0.3  | -1.6 dB |
| Peaking | 3826 Hz | 0.7  | -8.4 dB |
| Peaking | 2321 Hz | 1.01 | 10.8 dB |
| Peaking | 5352 Hz | 1.67 | 10.9 dB |
| Peaking | 1603 Hz | 6.05 | 0.9 dB  |
| Peaking | 6759 Hz | 7.92 | 2.0 dB  |
| Peaking | 1076 Hz | 3.67 | -0.4 dB |
| Peaking | 6326 Hz | 9.44 | 1.6 dB  |
| Peaking | 7063 Hz | 2.73 | -1.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20%20K450/AKG%20%20K450.png)