# Beyerdynamic DT X300p

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 5.9; 89 5.1; 95 4.4; 102 3.9; 109 3.5; 117 2.8; 125 2.5; 134 2.4; 143 2.2; 153 1.7; 164 1.5; 175 1.3; 188 1.2; 201 1.0; 215 1.0; 230 0.8; 246 0.8; 263 0.9; 282 1.0; 301 1.0; 323 0.9; 345 0.7; 369 0.0; 395 -0.1; 423 0.1; 452 -0.4; 484 -1.3; 518 -1.3; 554 -1.2; 593 -1.0; 635 -0.9; 679 -0.6; 726 -0.5; 777 -0.2; 832 -0.0; 890 0.0; 952 0.1; 1019 0.1; 1090 0.1; 1167 0.3; 1248 0.3; 1336 0.3; 1429 0.4; 1529 1.0; 1636 1.8; 1751 2.3; 1873 2.4; 2004 3.2; 2145 4.3; 2295 5.4; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 5.5; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000003dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Beyerdynamic DT X300p ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.32 | 6.0 dB  |
| Peaking | 76 Hz   | 1.96 | 2.2 dB  |
| Peaking | 577 Hz  | 1.83 | -1.6 dB |
| Peaking | 2969 Hz | 1.24 | 6.2 dB  |
| Peaking | 5472 Hz | 2.33 | 4.9 dB  |
| Peaking | 1358 Hz | 3.57 | -0.9 dB |
| Peaking | 2319 Hz | 7.54 | 1.1 dB  |
| Peaking | 6492 Hz | 6.49 | 2.0 dB  |
| Peaking | 6663 Hz | 4.71 | 0.7 dB  |
| Peaking | 7721 Hz | 2.06 | -1.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Beyerdynamic%20DT%20X300p/Beyerdynamic%20DT%20X300p.png)