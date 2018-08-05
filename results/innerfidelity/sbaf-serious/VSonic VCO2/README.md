# VSonic VCO2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 4.3; 22 4.3; 23 4.3; 25 4.3; 26 4.3; 28 4.3; 30 4.3; 32 4.3; 35 4.3; 37 4.2; 40 4.2; 42 4.2; 45 4.2; 49 4.2; 52 4.2; 56 4.2; 59 4.2; 64 4.1; 68 4.1; 73 4.0; 78 3.8; 83 3.5; 89 3.2; 95 2.9; 102 2.3; 109 1.8; 117 1.3; 125 0.7; 134 0.2; 143 -0.1; 153 -0.4; 164 -0.5; 175 -0.5; 188 -0.5; 201 -0.6; 215 -0.6; 230 -0.5; 246 -0.4; 263 -0.4; 282 -0.3; 301 -0.3; 323 -0.2; 345 -0.1; 369 -0.0; 395 0.0; 423 0.3; 452 0.4; 484 0.4; 518 0.4; 554 0.7; 593 0.9; 635 1.0; 679 0.9; 726 1.0; 777 1.0; 832 0.8; 890 0.5; 952 0.2; 1019 -0.1; 1090 -0.4; 1167 -0.7; 1248 -1.1; 1336 -1.5; 1429 -2.0; 1529 -2.3; 1636 -2.5; 1751 -2.4; 1873 -1.7; 2004 -0.3; 2145 1.0; 2295 1.6; 2455 2.9; 2627 4.7; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 5.9; 4514 3.7; 4830 3.0; 5168 3.0; 5530 2.2; 5917 0.8; 6331 -1.6; 6775 -3.8; 7249 -3.5; 7756 -2.2; 8299 -0.3; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `VSonic VCO2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 40 Hz   | 0.61 | 5.0 dB  |
| Peaking | 743 Hz  | 2.33 | 1.3 dB  |
| Peaking | 1738 Hz | 1.4  | -5.4 dB |
| Peaking | 3215 Hz | 0.94 | 7.7 dB  |
| Peaking | 6972 Hz | 3.69 | -6.0 dB |
| Peaking | 16 Hz   | 1.02 | 2.1 dB  |
| Peaking | 38 Hz   | 1.11 | -1.4 dB |
| Peaking | 84 Hz   | 1.22 | 1.8 dB  |
| Peaking | 158 Hz  | 1.13 | -1.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/VSonic%20VCO2/VSonic%20VCO2.png)