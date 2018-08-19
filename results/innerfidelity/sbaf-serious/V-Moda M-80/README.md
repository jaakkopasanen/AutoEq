# V-Moda M-80

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 3.1; 22 2.6; 23 2.4; 25 2.0; 26 1.8; 28 1.5; 30 1.2; 32 0.9; 35 0.6; 37 0.5; 40 0.2; 42 0.1; 45 -0.1; 49 -0.4; 52 -0.5; 56 -0.8; 59 -0.9; 64 -1.2; 68 -1.4; 73 -1.7; 78 -1.9; 83 -2.0; 89 -2.2; 95 -2.6; 102 -2.9; 109 -2.8; 117 -2.7; 125 -2.7; 134 -2.9; 143 -3.0; 153 -3.2; 164 -3.1; 175 -2.8; 188 -2.8; 201 -2.5; 215 -3.1; 230 -4.3; 246 -4.1; 263 -3.6; 282 -2.9; 301 -2.3; 323 -1.6; 345 -0.9; 369 -0.3; 395 0.0; 423 0.4; 452 0.7; 484 1.1; 518 1.6; 554 2.4; 593 3.0; 635 3.2; 679 3.0; 726 2.7; 777 2.5; 832 1.9; 890 1.3; 952 0.6; 1019 -0.2; 1090 -0.8; 1167 -1.4; 1248 -2.0; 1336 -2.3; 1429 -2.5; 1529 -2.6; 1636 -2.4; 1751 -1.9; 1873 -1.1; 2004 -0.3; 2145 0.3; 2295 0.5; 2455 0.7; 2627 0.4; 2811 -0.4; 3008 -1.0; 3219 -1.7; 3444 -1.5; 3685 -0.1; 3943 1.6; 4219 2.5; 4514 1.4; 4830 2.2; 5168 5.7; 5530 6.0; 5917 5.8; 6331 3.5; 6775 2.2; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.093091504264768dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-Moda M-80 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 17 Hz   | 0.81 | 3.5 dB  |
| Peaking | 128 Hz  | 0.65 | -2.9 dB |
| Peaking | 249 Hz  | 3.38 | -2.9 dB |
| Peaking | 628 Hz  | 2.55 | 3.9 dB  |
| Peaking | 5595 Hz | 3.85 | 6.7 dB  |
| Peaking | 836 Hz  | 3.34 | 1.6 dB  |
| Peaking | 1499 Hz | 1.57 | -3.2 dB |
| Peaking | 2349 Hz | 2.07 | 2.0 dB  |
| Peaking | 3317 Hz | 3.17 | -2.5 dB |
| Peaking | 4082 Hz | 6.9  | 2.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/V-Moda%20M-80/V-Moda%20M-80.png)