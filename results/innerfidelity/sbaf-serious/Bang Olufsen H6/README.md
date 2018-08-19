# Bang Olufsen H6

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 2.3; 22 2.0; 23 1.9; 25 1.7; 26 1.6; 28 1.4; 30 1.3; 32 1.3; 35 1.2; 37 1.2; 40 1.2; 42 1.2; 45 1.3; 49 1.5; 52 1.7; 56 2.1; 59 2.3; 64 2.7; 68 2.9; 73 3.0; 78 3.2; 83 3.4; 89 3.8; 95 4.2; 102 4.4; 109 4.2; 117 3.3; 125 2.1; 134 2.1; 143 3.2; 153 4.3; 164 6.0; 175 5.6; 188 3.7; 201 3.5; 215 3.7; 230 4.4; 246 4.9; 263 5.2; 282 5.6; 301 5.8; 323 5.8; 345 5.8; 369 5.7; 395 5.6; 423 5.4; 452 5.0; 484 4.5; 518 4.2; 554 3.9; 593 3.7; 635 3.2; 679 2.6; 726 2.1; 777 1.8; 832 1.1; 890 0.6; 952 0.3; 1019 -0.0; 1090 -0.1; 1167 -0.2; 1248 -0.2; 1336 -0.4; 1429 -0.6; 1529 -0.7; 1636 -0.8; 1751 -0.8; 1873 -0.3; 2004 0.1; 2145 1.0; 2295 2.2; 2455 4.2; 2627 4.8; 2811 4.2; 3008 5.0; 3219 5.9; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.1; 8880 -1.1; 9502 -0.5; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bang Olufsen H6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.2dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.83 | 2.1 dB  |
| Peaking | 86 Hz   | 1.42 | 2.9 dB  |
| Peaking | 186 Hz  | 1.08 | 2.8 dB  |
| Peaking | 382 Hz  | 1.21 | 5.2 dB  |
| Peaking | 4269 Hz | 1.21 | 7.0 dB  |
| Peaking | 1858 Hz | 1.41 | -2.9 dB |
| Peaking | 2585 Hz | 2.11 | 3.5 dB  |
| Peaking | 6259 Hz | 2.73 | 6.8 dB  |
| Peaking | 6655 Hz | 1.16 | -4.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bang%20Olufsen%20H6/Bang%20Olufsen%20H6.png)