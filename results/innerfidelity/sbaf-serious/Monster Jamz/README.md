# Monster Jamz

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.4dB
GraphicEQ: 10 -84; 20 -8.4; 22 -8.3; 23 -8.3; 25 -8.2; 26 -8.2; 28 -8.1; 30 -8.0; 32 -7.9; 35 -7.8; 37 -7.7; 40 -7.5; 42 -7.4; 45 -7.3; 49 -7.2; 52 -7.1; 56 -7.0; 59 -7.0; 64 -6.8; 68 -6.8; 73 -6.7; 78 -6.7; 83 -6.7; 89 -6.5; 95 -6.5; 102 -6.4; 109 -6.2; 117 -6.0; 125 -5.9; 134 -5.7; 143 -5.6; 153 -5.4; 164 -5.2; 175 -4.9; 188 -4.6; 201 -4.4; 215 -4.0; 230 -3.8; 246 -3.4; 263 -3.2; 282 -2.8; 301 -2.5; 323 -2.1; 345 -1.8; 369 -1.5; 395 -1.2; 423 -0.8; 452 -0.5; 484 -0.4; 518 -0.1; 554 0.2; 593 0.7; 635 0.8; 679 0.8; 726 0.9; 777 1.1; 832 0.9; 890 0.6; 952 0.3; 1019 -0.1; 1090 -0.5; 1167 -1.1; 1248 -1.2; 1336 -1.0; 1429 -2.0; 1529 -2.8; 1636 -3.4; 1751 -4.0; 1873 -4.4; 2004 -4.8; 2145 -5.3; 2295 -5.0; 2455 -4.7; 2627 -4.4; 2811 -3.1; 3008 -0.5; 3219 1.6; 3444 3.2; 3685 3.6; 3943 2.9; 4219 0.9; 4514 -0.7; 4830 -1.6; 5168 -1.3; 5530 -0.3; 5917 1.8; 6331 3.6; 6775 3.8; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -0.6; 15258 -1.8; 16326 -0.1; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.412808445253533dB` and instead set Global volume in the UI for both channels to **-44**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Monster Jamz ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.8dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 0.21 | -8.1 dB |
| Peaking | 152 Hz  | 0.89 | -2.9 dB |
| Peaking | 2246 Hz | 1.64 | -5.9 dB |
| Peaking | 3537 Hz | 4.31 | 5.8 dB  |
| Peaking | 6552 Hz | 7.25 | 4.8 dB  |
| Peaking | 287 Hz  | 2.09 | -0.7 dB |
| Peaking | 724 Hz  | 1.55 | 1.7 dB  |
| Peaking | 1611 Hz | 4.95 | -1.0 dB |
| Peaking | 4928 Hz | 7.56 | -2.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Monster%20Jamz/Monster%20Jamz.png)