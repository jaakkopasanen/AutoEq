# Etymotic EK5

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 5.9; 52 5.8; 56 5.6; 59 5.4; 64 5.0; 68 4.7; 73 4.5; 78 4.2; 83 3.9; 89 3.5; 95 3.2; 102 3.0; 109 2.9; 117 2.7; 125 2.5; 134 2.2; 143 2.0; 153 1.9; 164 1.7; 175 1.8; 188 1.7; 201 1.5; 215 1.5; 230 1.5; 246 1.5; 263 1.4; 282 1.5; 301 1.6; 323 1.6; 345 1.7; 369 1.7; 395 1.7; 423 1.9; 452 1.9; 484 1.7; 518 1.8; 554 2.0; 593 2.1; 635 2.1; 679 1.8; 726 1.8; 777 1.8; 832 1.5; 890 1.0; 952 0.5; 1019 -0.1; 1090 -0.8; 1167 -1.4; 1248 -2.2; 1336 -2.7; 1429 -2.9; 1529 -3.8; 1636 -4.6; 1751 -5.3; 1873 -5.8; 2004 -6.2; 2145 -6.3; 2295 -5.3; 2455 -3.1; 2627 -2.6; 2811 -1.8; 3008 -0.3; 3219 0.7; 3444 1.8; 3685 2.1; 3943 2.2; 4219 1.5; 4514 1.3; 4830 1.3; 5168 1.8; 5530 2.0; 5917 2.9; 6331 3.8; 6775 3.8; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Etymotic EK5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.4dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.37 | 6.3 dB  |
| Peaking | 679 Hz  | 0.69 | 2.7 dB  |
| Peaking | 2028 Hz | 1.06 | -7.9 dB |
| Peaking | 3488 Hz | 1.46 | 4.6 dB  |
| Peaking | 6430 Hz | 4.75 | 4.1 dB  |
| Peaking | 7938 Hz | 5.8  | -0.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Etymotic%20EK5/Etymotic%20EK5.png)