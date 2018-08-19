# UBSound Fighter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -5.2; 22 -5.7; 23 -5.9; 25 -6.2; 26 -6.4; 28 -6.6; 30 -6.8; 32 -7.0; 35 -7.3; 37 -7.5; 40 -7.7; 42 -7.8; 45 -8.0; 49 -8.2; 52 -8.4; 56 -8.5; 59 -8.7; 64 -8.8; 68 -8.9; 73 -9.1; 78 -9.3; 83 -9.3; 89 -9.5; 95 -9.6; 102 -9.6; 109 -9.5; 117 -9.4; 125 -9.3; 134 -9.2; 143 -9.1; 153 -9.0; 164 -8.8; 175 -8.5; 188 -8.2; 201 -7.9; 215 -7.5; 230 -7.1; 246 -6.7; 263 -6.4; 282 -5.9; 301 -5.4; 323 -5.0; 345 -4.5; 369 -4.1; 395 -3.6; 423 -3.0; 452 -2.5; 484 -2.1; 518 -1.7; 554 -1.1; 593 -0.3; 635 0.2; 679 0.5; 726 1.4; 777 1.9; 832 0.5; 890 0.2; 952 0.2; 1019 -0.0; 1090 -0.2; 1167 -0.3; 1248 -0.2; 1336 -0.9; 1429 -1.4; 1529 -1.9; 1636 -2.3; 1751 -2.5; 1873 -2.3; 2004 -1.6; 2145 -0.4; 2295 1.4; 2455 3.6; 2627 5.7; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 5.3; 5917 1.5; 6331 -3.1; 6775 -1.1; 7249 1.0; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.0999999999731696dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `UBSound Fighter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 46 Hz   | 0.37 | -7.2 dB |
| Peaking | 135 Hz  | 0.8  | -5.2 dB |
| Peaking | 268 Hz  | 1.39 | -3.0 dB |
| Peaking | 1837 Hz | 2.44 | -5.4 dB |
| Peaking | 3322 Hz | 1.08 | 7.4 dB  |
| Peaking | 684 Hz  | 0.8  | -0.8 dB |
| Peaking | 735 Hz  | 2.76 | 3.0 dB  |
| Peaking | 3507 Hz | 6.21 | -1.3 dB |
| Peaking | 5453 Hz | 3.39 | 4.5 dB  |
| Peaking | 6366 Hz | 5.4  | -7.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/UBSound%20Fighter/UBSound%20Fighter.png)