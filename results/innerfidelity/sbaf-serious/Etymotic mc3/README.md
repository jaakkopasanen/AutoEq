# Etymotic mc3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 5.9; 59 5.8; 64 5.5; 68 5.3; 73 5.0; 78 4.7; 83 4.4; 89 4.1; 95 3.8; 102 3.5; 109 3.4; 117 3.2; 125 2.9; 134 2.7; 143 2.5; 153 2.4; 164 2.2; 175 2.2; 188 2.0; 201 2.0; 215 2.0; 230 1.9; 246 1.9; 263 1.9; 282 1.9; 301 1.9; 323 1.9; 345 2.0; 369 1.9; 395 2.0; 423 2.0; 452 2.1; 484 2.0; 518 2.0; 554 2.2; 593 2.3; 635 2.2; 679 2.0; 726 1.9; 777 1.8; 832 1.4; 890 0.9; 952 0.4; 1019 -0.2; 1090 -0.8; 1167 -1.3; 1248 -1.9; 1336 -2.6; 1429 -3.4; 1529 -4.0; 1636 -4.3; 1751 -4.3; 1873 -3.6; 2004 -3.3; 2145 -2.9; 2295 -2.1; 2455 -0.9; 2627 0.1; 2811 1.2; 3008 2.8; 3219 4.0; 3444 5.2; 3685 5.7; 3943 5.5; 4219 4.3; 4514 3.6; 4830 3.9; 5168 5.2; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic mc3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 34 Hz   | 0.34 | 6.3 dB  |
| Peaking | 759 Hz  | 0.56 | 3.2 dB  |
| Peaking | 1671 Hz | 0.98 | -6.4 dB |
| Peaking | 3574 Hz | 2.02 | 6.6 dB  |
| Peaking | 5842 Hz | 3.33 | 5.9 dB  |
| Peaking | 8211 Hz | 4.78 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Etymotic%20mc3/Etymotic%20mc3.png)