# Earsonics Velvet Pot CCW

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 0.5; 22 0.2; 23 0.1; 25 -0.1; 26 -0.1; 28 -0.3; 30 -0.4; 32 -0.4; 35 -0.5; 37 -0.5; 40 -0.6; 42 -0.6; 45 -0.6; 49 -0.6; 52 -0.6; 56 -0.5; 59 -0.5; 64 -0.5; 68 -0.4; 73 -0.3; 78 -0.2; 83 -0.1; 89 0.2; 95 0.4; 102 0.8; 109 1.3; 117 1.8; 125 2.4; 134 2.9; 143 3.6; 153 4.3; 164 5.0; 175 5.8; 188 6.0; 201 6.0; 215 6.0; 230 6.0; 246 6.0; 263 5.8; 282 5.3; 301 4.6; 323 4.1; 345 3.6; 369 3.1; 395 2.6; 423 2.3; 452 2.0; 484 1.7; 518 1.4; 554 1.4; 593 1.5; 635 1.4; 679 1.2; 726 1.1; 777 1.1; 832 0.9; 890 0.6; 952 0.3; 1019 -0.0; 1090 -0.3; 1167 -0.6; 1248 -0.8; 1336 -1.2; 1429 -1.5; 1529 -1.7; 1636 -1.6; 1751 -1.1; 1873 -0.2; 2004 1.3; 2145 2.8; 2295 3.6; 2455 4.7; 2627 5.8; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 5.5; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.0; 7249 1.2; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Earsonics Velvet Pot CCW ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 88 Hz   | 0.63 | -1.8 dB |
| Peaking | 207 Hz  | 0.86 | 7.0 dB  |
| Peaking | 1577 Hz | 1.86 | -4.5 dB |
| Peaking | 3514 Hz | 0.78 | 7.1 dB  |
| Peaking | 1860 Hz | 8.43 | -0.7 dB |
| Peaking | 2662 Hz | 2.85 | 1.2 dB  |
| Peaking | 3416 Hz | 2.56 | -1.1 dB |
| Peaking | 6120 Hz | 2.62 | 5.2 dB  |
| Peaking | 7304 Hz | 1.41 | -3.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Earsonics%20Velvet%20Pot%20CCW/Earsonics%20Velvet%20Pot%20CCW.png)