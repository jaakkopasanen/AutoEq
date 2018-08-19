# MrSpeakers Ether C 1 Black Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 2.7; 22 2.6; 23 2.5; 25 2.5; 26 2.4; 28 2.5; 30 2.5; 32 2.7; 35 3.0; 37 3.1; 40 3.4; 42 3.8; 45 4.3; 49 4.4; 52 3.8; 56 3.0; 59 2.7; 64 2.6; 68 3.1; 73 4.0; 78 3.8; 83 2.8; 89 2.6; 95 2.5; 102 1.9; 109 2.1; 117 2.3; 125 2.2; 134 2.5; 143 3.1; 153 3.6; 164 4.0; 175 2.2; 188 2.0; 201 1.6; 215 1.3; 230 1.1; 246 0.9; 263 0.8; 282 0.7; 301 0.6; 323 0.6; 345 0.8; 369 1.0; 395 1.4; 423 1.9; 452 2.3; 484 2.4; 518 2.0; 554 1.7; 593 1.5; 635 1.3; 679 1.0; 726 0.9; 777 0.8; 832 0.5; 890 -0.2; 952 -0.1; 1019 0.2; 1090 0.7; 1167 1.1; 1248 1.0; 1336 0.8; 1429 0.9; 1529 0.7; 1636 0.2; 1751 0.1; 1873 0.9; 2004 1.3; 2145 1.2; 2295 1.5; 2455 1.4; 2627 1.4; 2811 1.5; 3008 1.7; 3219 1.6; 3444 1.7; 3685 2.2; 3943 2.4; 4219 2.0; 4514 2.1; 4830 3.2; 5168 5.3; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.093091504264768dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MrSpeakers Ether C 1 Black Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.4dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 1.44 | 2.2 dB  |
| Peaking | 52 Hz   | 0.6  | 3.6 dB  |
| Peaking | 159 Hz  | 3.74 | 2.8 dB  |
| Peaking | 499 Hz  | 1.72 | 2.0 dB  |
| Peaking | 5635 Hz | 2.3  | 6.3 dB  |
| Peaking | 3094 Hz | 0.87 | 1.3 dB  |
| Peaking | 4583 Hz | 6.45 | -1.4 dB |
| Peaking | 6551 Hz | 5.88 | 2.2 dB  |
| Peaking | 7353 Hz | 1.23 | -1.2 dB |
| Peaking | 7525 Hz | 4.31 | -0.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/MrSpeakers%20Ether%20C%201%20Black%20Filter/MrSpeakers%20Ether%20C%201%20Black%20Filter.png)