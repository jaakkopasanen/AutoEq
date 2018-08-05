# AKG N90Q Nominal

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.4dB
GraphicEQ: 10 -84; 20 -0.3; 22 -0.2; 23 -0.1; 25 -0.0; 26 0.0; 28 0.2; 30 0.3; 32 0.5; 35 0.7; 37 0.8; 40 1.1; 42 1.2; 45 1.4; 49 1.7; 52 1.9; 56 2.0; 59 2.1; 64 2.2; 68 2.1; 73 2.0; 78 1.8; 83 1.6; 89 1.3; 95 1.0; 102 0.6; 109 0.4; 117 0.1; 125 -0.3; 134 -0.7; 143 -0.9; 153 -0.9; 164 -0.9; 175 -0.9; 188 -0.9; 201 -0.8; 215 -0.8; 230 -0.7; 246 -0.7; 263 -0.6; 282 -0.6; 301 -0.6; 323 -0.5; 345 -0.4; 369 -0.5; 395 -0.6; 423 -0.6; 452 -0.7; 484 -0.9; 518 -1.0; 554 -0.9; 593 -0.5; 635 0.1; 679 -0.3; 726 -1.0; 777 -0.8; 832 -0.6; 890 -0.4; 952 -0.1; 1019 0.0; 1090 0.1; 1167 0.4; 1248 0.6; 1336 0.4; 1429 0.0; 1529 -0.4; 1636 -0.3; 1751 -0.6; 1873 -0.9; 2004 -0.9; 2145 -1.9; 2295 -2.7; 2455 -3.4; 2627 -3.6; 2811 -3.4; 3008 -3.8; 3219 -4.5; 3444 -4.6; 3685 -4.6; 3943 -5.1; 4219 -5.5; 4514 -4.2; 4830 -2.2; 5168 -0.1; 5530 0.5; 5917 0.3; 6331 2.9; 6775 3.6; 7249 1.3; 7756 0.2; 8299 -2.3; 8880 -4.9; 9502 -5.6; 10167 -4.2; 10879 -1.7; 11640 -0.1; 12455 0.0; 13327 -0.4; 14260 -2.3; 15258 -3.1; 16326 -1.3; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.4dB` and instead set Global volume in the UI for both channels to **-44**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG N90Q Nominal ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 62 Hz    | 1.92 | 2.5 dB  |
| Peaking | 3935 Hz  | 1.18 | -6.7 dB |
| Peaking | 6534 Hz  | 1.44 | 6.0 dB  |
| Peaking | 9197 Hz  | 3.23 | -7.6 dB |
| Peaking | 32883 Hz | 4.55 | -3.4 dB |
| Peaking | 171 Hz   | 2.19 | -1.0 dB |
| Peaking | 573 Hz   | 0.64 | -0.8 dB |
| Peaking | 1292 Hz  | 1.54 | 1.2 dB  |
| Peaking | 2457 Hz  | 6.83 | -1.3 dB |
| Peaking | 12052 Hz | 6.46 | 1.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20N90Q%20Nominal/AKG%20N90Q%20Nominal.png)