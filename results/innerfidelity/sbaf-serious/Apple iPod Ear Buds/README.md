# Apple iPod Ear Buds

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 6.0; 95 6.0; 102 6.0; 109 6.0; 117 6.0; 125 6.0; 134 6.0; 143 6.0; 153 5.4; 164 4.3; 175 3.3; 188 2.3; 201 1.5; 215 0.7; 230 0.1; 246 -0.4; 263 -0.8; 282 -1.0; 301 -1.2; 323 -1.3; 345 -1.2; 369 -1.1; 395 -0.8; 423 -0.3; 452 -0.0; 484 0.1; 518 0.1; 554 0.3; 593 0.4; 635 0.2; 679 -0.0; 726 -0.1; 777 0.0; 832 -0.0; 890 -0.0; 952 -0.0; 1019 0.0; 1090 0.0; 1167 0.1; 1248 0.0; 1336 -0.2; 1429 -0.5; 1529 -0.9; 1636 -1.2; 1751 -1.2; 1873 -0.9; 2004 -0.2; 2145 0.6; 2295 1.1; 2455 0.3; 2627 -1.7; 2811 -3.7; 3008 -5.3; 3219 -4.5; 3444 -2.4; 3685 -0.5; 3943 -0.0; 4219 -0.7; 4514 -1.3; 4830 -1.1; 5168 -0.5; 5530 -0.9; 5917 -3.7; 6331 -5.6; 6775 -4.4; 7249 -2.8; 7756 -2.5; 8299 -3.1; 8880 -2.9; 9502 -0.6; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Apple iPod Ear Buds ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 61 Hz   | 0.2  | 6.6 dB  |
| Peaking | 230 Hz  | 2.9  | -2.4 dB |
| Peaking | 325 Hz  | 1.29 | -4.1 dB |
| Peaking | 3045 Hz | 5.78 | -5.6 dB |
| Peaking | 6637 Hz | 2.88 | -4.9 dB |
| Peaking | 143 Hz  | 6.02 | 1.2 dB  |
| Peaking | 1629 Hz | 4.43 | -1.4 dB |
| Peaking | 6521 Hz | 0.35 | 0.4 dB  |
| Peaking | 8689 Hz | 7.68 | -2.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Apple%20iPod%20Ear%20Buds/Apple%20iPod%20Ear%20Buds.png)