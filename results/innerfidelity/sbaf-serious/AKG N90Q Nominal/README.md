# AKG N90Q Nominal

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.9dB
GraphicEQ: 10 -84; 20 -0.3; 22 -0.2; 23 -0.1; 25 -0.0; 26 0.0; 28 0.1; 30 0.3; 32 0.4; 35 0.6; 37 0.8; 40 1.0; 42 1.1; 45 1.3; 49 1.4; 52 1.6; 56 1.7; 59 1.7; 64 1.7; 68 1.5; 73 1.3; 78 1.0; 83 0.8; 89 0.5; 95 0.3; 102 0.0; 109 -0.0; 117 -0.1; 125 -0.3; 134 -0.6; 143 -0.7; 153 -0.6; 164 -0.7; 175 -0.7; 188 -0.7; 201 -0.7; 215 -0.7; 230 -0.6; 246 -0.6; 263 -0.6; 282 -0.5; 301 -0.5; 323 -0.5; 345 -0.4; 369 -0.4; 395 -0.6; 423 -0.6; 452 -0.7; 484 -0.9; 518 -1.0; 554 -0.9; 593 -0.5; 635 0.1; 679 -0.3; 726 -1.0; 777 -0.8; 832 -0.6; 890 -0.4; 952 -0.1; 1019 0.0; 1090 0.1; 1167 0.4; 1248 0.6; 1336 0.4; 1429 0.0; 1529 -0.4; 1636 -0.3; 1751 -0.6; 1873 -0.9; 2004 -0.9; 2145 -1.9; 2295 -2.7; 2455 -3.4; 2627 -3.6; 2811 -3.4; 3008 -3.8; 3219 -4.5; 3444 -4.6; 3685 -4.6; 3943 -5.1; 4219 -5.5; 4514 -4.2; 4830 -2.2; 5168 -0.1; 5530 0.5; 5917 0.3; 6331 2.9; 6775 3.6; 7249 1.3; 7756 0.2; 8299 -2.3; 8880 -4.9; 9502 -5.6; 10167 -4.2; 10879 -1.7; 11640 -0.1; 12455 0.0; 13327 -0.4; 14260 -2.3; 15258 -3.1; 16326 -1.3; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.903764133590761dB` and instead set Global volume in the UI for both channels to **-39**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG N90Q Nominal ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -3.2dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 56 Hz    | 2.12 | 2.0 dB  |
| Peaking | 3805 Hz  | 1.21 | -5.8 dB |
| Peaking | 6618 Hz  | 2.04 | 5.8 dB  |
| Peaking | 8764 Hz  | 2.91 | -1.6 dB |
| Peaking | 9397 Hz  | 3.36 | -5.4 dB |
| Peaking | 395 Hz   | 0.38 | -0.7 dB |
| Peaking | 1307 Hz  | 1.7  | 1.2 dB  |
| Peaking | 2462 Hz  | 7.68 | -1.2 dB |
| Peaking | 12103 Hz | 3.73 | 1.4 dB  |
| Peaking | 14966 Hz | 3.63 | -3.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20N90Q%20Nominal/AKG%20N90Q%20Nominal.png)