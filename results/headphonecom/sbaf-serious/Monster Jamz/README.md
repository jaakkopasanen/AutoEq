# Monster Jamz

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.2dB
GraphicEQ: 10 -84; 20 6.1; 22 5.5; 23 5.2; 25 4.7; 26 4.5; 28 4.0; 30 3.6; 32 3.2; 35 2.7; 37 2.4; 40 2.0; 42 1.7; 45 1.4; 49 0.9; 52 0.5; 56 0.1; 59 -0.2; 64 -0.8; 68 -1.1; 73 -1.6; 78 -2.0; 83 -2.4; 89 -2.8; 95 -3.1; 102 -3.5; 109 -3.9; 117 -4.2; 125 -4.5; 134 -4.9; 143 -5.2; 153 -5.5; 164 -5.7; 175 -5.9; 188 -6.1; 201 -6.2; 215 -6.0; 230 -5.9; 246 -5.8; 263 -5.8; 282 -6.0; 301 -5.9; 323 -5.6; 345 -5.3; 369 -4.9; 395 -4.6; 423 -4.2; 452 -3.8; 484 -3.4; 518 -3.0; 554 -2.5; 593 -2.0; 635 -1.5; 679 -1.1; 726 -0.7; 777 -0.4; 832 -0.1; 890 -0.1; 952 -0.1; 1019 0.0; 1090 -0.0; 1167 -0.0; 1248 -0.1; 1336 -0.1; 1429 -0.3; 1529 -0.4; 1636 -0.3; 1751 -0.1; 1873 0.2; 2004 0.4; 2145 0.9; 2295 1.7; 2455 2.7; 2627 3.7; 2811 4.7; 3008 5.8; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 5.4; 4514 4.7; 4830 5.3; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.241222743010082dB` and instead set Global volume in the UI for both channels to **-62**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Jamz ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 17 Hz   | 0.6  | 6.5 dB  |
| Peaking | 162 Hz  | 0.65 | -5.3 dB |
| Peaking | 337 Hz  | 1.17 | -3.0 dB |
| Peaking | 3418 Hz | 1.84 | 6.2 dB  |
| Peaking | 5678 Hz | 2.85 | 5.5 dB  |
| Peaking | 506 Hz  | 2.25 | -0.8 dB |
| Peaking | 1534 Hz | 0.59 | 1.8 dB  |
| Peaking | 1661 Hz | 1.29 | -2.6 dB |
| Peaking | 6571 Hz | 6.96 | 2.5 dB  |
| Peaking | 7509 Hz | 1.81 | -1.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Monster%20Jamz/Monster%20Jamz.png)