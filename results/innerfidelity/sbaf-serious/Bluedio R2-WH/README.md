# Bluedio R2-WH

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 1.2; 22 0.3; 23 -0.1; 25 -0.8; 26 -1.1; 28 -1.8; 30 -2.3; 32 -2.7; 35 -3.3; 37 -3.6; 40 -4.0; 42 -4.1; 45 -4.3; 49 -4.5; 52 -4.6; 56 -4.8; 59 -4.8; 64 -4.9; 68 -5.0; 73 -5.0; 78 -5.0; 83 -4.9; 89 -4.7; 95 -4.9; 102 -5.4; 109 -5.6; 117 -5.7; 125 -5.7; 134 -6.0; 143 -6.2; 153 -6.3; 164 -6.1; 175 -6.1; 188 -6.1; 201 -5.9; 215 -5.7; 230 -5.5; 246 -5.0; 263 -5.5; 282 -5.4; 301 -5.1; 323 -4.4; 345 -4.5; 369 -4.3; 395 -3.7; 423 -2.9; 452 -2.6; 484 -2.4; 518 -1.8; 554 -0.7; 593 0.6; 635 1.3; 679 2.1; 726 2.7; 777 3.1; 832 2.6; 890 1.4; 952 0.5; 1019 -0.1; 1090 -0.3; 1167 -0.2; 1248 0.0; 1336 0.0; 1429 0.1; 1529 0.1; 1636 -0.2; 1751 -0.6; 1873 -1.0; 2004 -1.4; 2145 -0.3; 2295 -0.2; 2455 -0.1; 2627 0.0; 2811 0.5; 3008 1.6; 3219 3.0; 3444 3.9; 3685 4.3; 3943 5.8; 4219 6.0; 4514 5.7; 4830 5.3; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099996068419183dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Bluedio R2-WH ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 14 Hz   | 0.56 | 3.7 dB  |
| Peaking | 37 Hz   | 0.9  | -2.8 dB |
| Peaking | 277 Hz  | 0.19 | -6.4 dB |
| Peaking | 733 Hz  | 1.15 | 7.8 dB  |
| Peaking | 4702 Hz | 1.4  | 7.0 dB  |
| Peaking | 1490 Hz | 2.91 | 2.7 dB  |
| Peaking | 1569 Hz | 1.59 | -1.7 dB |
| Peaking | 6084 Hz | 5.1  | 2.2 dB  |
| Peaking | 6623 Hz | 5.08 | 2.4 dB  |
| Peaking | 7389 Hz | 1.78 | -2.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Bluedio%20R2-WH/Bluedio%20R2-WH.png)