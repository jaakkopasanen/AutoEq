# Music Hall DeBe

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 5.7; 37 5.5; 40 5.1; 42 4.9; 45 4.6; 49 4.3; 52 4.0; 56 3.7; 59 3.5; 64 3.1; 68 2.8; 73 2.4; 78 2.1; 83 1.7; 89 1.2; 95 0.8; 102 0.4; 109 0.2; 117 -0.1; 125 -0.6; 134 -1.0; 143 -1.1; 153 -1.5; 164 -1.8; 175 -1.7; 188 -1.9; 201 -2.2; 215 -2.5; 230 -2.6; 246 -2.9; 263 -2.9; 282 -2.7; 301 -2.6; 323 -2.7; 345 -2.7; 369 -2.6; 395 -2.4; 423 -2.2; 452 -2.1; 484 -1.8; 518 -1.1; 554 -0.0; 593 1.2; 635 2.0; 679 2.2; 726 2.0; 777 1.7; 832 1.1; 890 0.6; 952 0.3; 1019 0.0; 1090 0.1; 1167 0.1; 1248 0.1; 1336 0.2; 1429 0.5; 1529 1.1; 1636 1.8; 1751 2.8; 1873 4.1; 2004 5.3; 2145 6.0; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 5.5; 4830 2.2; 5168 2.4; 5530 5.4; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Music Hall DeBe ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.4dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.36 | 6.3 dB  |
| Peaking | 420 Hz  | 0.27 | -3.9 dB |
| Peaking | 690 Hz  | 1.75 | 5.5 dB  |
| Peaking | 2198 Hz | 1.8  | 4.7 dB  |
| Peaking | 3861 Hz | 0.91 | 5.6 dB  |
| Peaking | 5017 Hz | 7.49 | -4.8 dB |
| Peaking | 6196 Hz | 2.19 | 6.0 dB  |
| Peaking | 7439 Hz | 1.62 | -3.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Music%20Hall%20DeBe/Music%20Hall%20DeBe.png)