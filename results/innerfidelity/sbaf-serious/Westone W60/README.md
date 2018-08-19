# Westone W60

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 0.1; 22 -0.1; 23 -0.2; 25 -0.3; 26 -0.4; 28 -0.5; 30 -0.6; 32 -0.6; 35 -0.7; 37 -0.8; 40 -1.0; 42 -1.1; 45 -1.2; 49 -1.4; 52 -1.5; 56 -1.7; 59 -1.8; 64 -2.1; 68 -2.3; 73 -2.6; 78 -2.8; 83 -3.0; 89 -3.3; 95 -3.6; 102 -3.7; 109 -3.8; 117 -4.0; 125 -4.1; 134 -4.3; 143 -4.4; 153 -4.5; 164 -4.5; 175 -4.5; 188 -4.5; 201 -4.5; 215 -4.3; 230 -4.2; 246 -4.1; 263 -4.0; 282 -3.7; 301 -3.5; 323 -3.3; 345 -3.0; 369 -2.8; 395 -2.6; 423 -2.2; 452 -1.9; 484 -1.7; 518 -1.5; 554 -1.0; 593 -0.5; 635 -0.3; 679 -0.1; 726 0.1; 777 0.4; 832 0.5; 890 0.3; 952 0.2; 1019 -0.0; 1090 -0.3; 1167 -0.6; 1248 -0.9; 1336 -1.5; 1429 -2.1; 1529 -2.4; 1636 -2.4; 1751 -2.0; 1873 -1.0; 2004 0.5; 2145 2.2; 2295 3.8; 2455 5.3; 2627 5.9; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.0; 9502 -2.3; 10167 -3.4; 10879 -1.8; 11640 -0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.0999999998930665dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Westone W60 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 113 Hz  | 0.63 | -2.2 dB |
| Peaking | 249 Hz  | 0.53 | -3.4 dB |
| Peaking | 1618 Hz | 1.5  | -8.5 dB |
| Peaking | 3196 Hz | 0.37 | 8.1 dB  |
| Peaking | 9693 Hz | 1.7  | -5.9 dB |
| Peaking | 1995 Hz | 5.49 | -0.8 dB |
| Peaking | 2510 Hz | 3.18 | 1.5 dB  |
| Peaking | 3952 Hz | 1.2  | -1.1 dB |
| Peaking | 6613 Hz | 1.89 | 2.4 dB  |
| Peaking | 7394 Hz | 5.3  | -3.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Westone%20W60/Westone%20W60.png)