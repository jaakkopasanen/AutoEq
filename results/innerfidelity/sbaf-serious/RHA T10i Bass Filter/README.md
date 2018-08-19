# RHA T10i Bass Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -9.8; 22 -10.0; 23 -10.0; 25 -10.2; 26 -10.3; 28 -10.4; 30 -10.6; 32 -10.7; 35 -10.8; 37 -10.9; 40 -10.9; 42 -10.9; 45 -10.9; 49 -11.1; 52 -11.1; 56 -11.1; 59 -11.1; 64 -11.2; 68 -11.3; 73 -11.2; 78 -11.4; 83 -11.4; 89 -11.4; 95 -11.4; 102 -11.3; 109 -11.2; 117 -11.0; 125 -10.9; 134 -10.8; 143 -10.7; 153 -10.5; 164 -10.2; 175 -9.9; 188 -9.6; 201 -9.3; 215 -8.8; 230 -8.4; 246 -8.1; 263 -7.7; 282 -7.1; 301 -6.7; 323 -6.2; 345 -5.8; 369 -5.3; 395 -4.9; 423 -4.2; 452 -3.7; 484 -3.4; 518 -3.0; 554 -2.5; 593 -1.8; 635 -1.3; 679 -1.3; 726 -1.1; 777 -0.6; 832 -0.2; 890 0.1; 952 0.3; 1019 -0.1; 1090 -0.3; 1167 -0.5; 1248 -0.8; 1336 -1.2; 1429 -1.8; 1529 -2.4; 1636 -2.9; 1751 -3.3; 1873 -3.5; 2004 -3.6; 2145 -3.6; 2295 -3.2; 2455 -2.3; 2627 -1.3; 2811 -0.3; 3008 0.8; 3219 1.3; 3444 1.3; 3685 1.3; 3943 2.4; 4219 3.3; 4514 5.5; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 -1.0; 8299 -7.6; 8880 -10.9; 9502 -11.4; 10167 -9.6; 10879 -4.3; 11640 -0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099856830925146dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RHA T10i Bass Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 40 Hz    | 0.23 | -10.5 dB |
| Peaking | 187 Hz   | 0.61 | -4.8 dB  |
| Peaking | 2062 Hz  | 2.02 | -4.6 dB  |
| Peaking | 5850 Hz  | 1.18 | 8.5 dB   |
| Peaking | 9162 Hz  | 2.95 | -16.1 dB |
| Peaking | 939 Hz   | 2.31 | 1.5 dB   |
| Peaking | 1789 Hz  | 1.82 | -1.2 dB  |
| Peaking | 1971 Hz  | 4.67 | 1.4 dB   |
| Peaking | 10333 Hz | 6.87 | -4.5 dB  |
| Peaking | 11472 Hz | 3.09 | 3.1 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/RHA%20T10i%20Bass%20Filter/RHA%20T10i%20Bass%20Filter.png)