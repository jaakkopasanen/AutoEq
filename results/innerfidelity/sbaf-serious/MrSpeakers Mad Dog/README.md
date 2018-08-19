# MrSpeakers Mad Dog

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 5.5; 68 5.5; 73 5.0; 78 3.3; 83 1.3; 89 -0.2; 95 -0.8; 102 -0.8; 109 -0.6; 117 -0.4; 125 -0.2; 134 -0.0; 143 0.3; 153 0.7; 164 0.9; 175 0.2; 188 0.5; 201 0.7; 215 0.9; 230 1.1; 246 1.2; 263 1.2; 282 1.3; 301 1.5; 323 1.6; 345 1.5; 369 1.3; 395 1.3; 423 1.2; 452 0.7; 484 0.0; 518 -0.4; 554 0.2; 593 1.1; 635 1.5; 679 1.3; 726 0.9; 777 0.1; 832 -0.5; 890 -0.7; 952 -0.4; 1019 0.3; 1090 0.7; 1167 0.4; 1248 0.7; 1336 0.9; 1429 1.1; 1529 1.3; 1636 1.6; 1751 2.5; 1873 3.0; 2004 4.3; 2145 5.1; 2295 5.8; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 4.5; 6775 3.1; 7249 1.3; 7756 0.1; 8299 -1.3; 8880 -2.4; 9502 -1.6; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `MrSpeakers Mad Dog ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.2dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.82 | 7.1 dB  |
| Peaking | 325 Hz  | 2.36 | 1.5 dB  |
| Peaking | 2531 Hz | 1.74 | 4.5 dB  |
| Peaking | 5141 Hz | 0.96 | 6.3 dB  |
| Peaking | 8607 Hz | 2.4  | -4.8 dB |
| Peaking | 38 Hz   | 2.9  | -1.6 dB |
| Peaking | 73 Hz   | 1.63 | 4.6 dB  |
| Peaking | 91 Hz   | 2.06 | -5.1 dB |
| Peaking | 667 Hz  | 5.62 | 1.5 dB  |
| Peaking | 878 Hz  | 3.4  | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/MrSpeakers%20Mad%20Dog/MrSpeakers%20Mad%20Dog.png)