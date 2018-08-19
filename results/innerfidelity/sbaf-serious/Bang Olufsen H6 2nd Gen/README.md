# Bang Olufsen H6 2nd Gen

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 5.6; 22 4.7; 23 4.2; 25 3.5; 26 3.2; 28 2.6; 30 2.1; 32 1.6; 35 1.0; 37 0.7; 40 0.3; 42 0.1; 45 -0.1; 49 -0.4; 52 -0.5; 56 -0.6; 59 -0.6; 64 -0.6; 68 -0.6; 73 -0.4; 78 -0.3; 83 -0.3; 89 -0.0; 95 0.4; 102 1.2; 109 1.6; 117 1.4; 125 0.7; 134 0.2; 143 0.7; 153 2.3; 164 4.7; 175 5.3; 188 4.9; 201 5.4; 215 6.0; 230 6.0; 246 6.0; 263 6.0; 282 5.4; 301 4.7; 323 4.0; 345 3.5; 369 3.1; 395 2.8; 423 2.6; 452 2.2; 484 1.8; 518 1.6; 554 1.5; 593 1.6; 635 1.3; 679 1.0; 726 0.8; 777 0.7; 832 0.3; 890 0.2; 952 0.1; 1019 -0.0; 1090 0.0; 1167 0.2; 1248 0.2; 1336 0.1; 1429 -0.1; 1529 -0.3; 1636 -0.4; 1751 -0.5; 1873 -0.2; 2004 0.3; 2145 0.8; 2295 1.6; 2455 3.0; 2627 4.3; 2811 5.5; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.4; 8880 -1.9; 9502 -2.1; 10167 -0.4; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bang Olufsen H6 2nd Gen ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 2.35 | 5.1 dB  |
| Peaking | 178 Hz  | 4.55 | 2.7 dB  |
| Peaking | 254 Hz  | 1.42 | 5.9 dB  |
| Peaking | 4552 Hz | 0.95 | 7.1 dB  |
| Peaking | 8986 Hz | 2.85 | -4.1 dB |
| Peaking | 56 Hz   | 2.74 | -0.8 dB |
| Peaking | 73 Hz   | 2.89 | -0.6 dB |
| Peaking | 1864 Hz | 1.76 | -2.2 dB |
| Peaking | 2894 Hz | 2.97 | 2.7 dB  |
| Peaking | 4379 Hz | 5.19 | -1.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bang%20Olufsen%20H6%202nd%20Gen/Bang%20Olufsen%20H6%202nd%20Gen.png)