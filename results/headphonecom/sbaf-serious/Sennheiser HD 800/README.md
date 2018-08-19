# Sennheiser HD 800

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.6dB
GraphicEQ: 10 -84; 20 3.5; 22 3.1; 23 2.9; 25 2.6; 26 2.4; 28 2.1; 30 1.9; 32 1.7; 35 1.5; 37 1.3; 40 1.2; 42 1.3; 45 1.4; 49 1.5; 52 1.4; 56 0.9; 59 0.6; 64 0.5; 68 0.2; 73 -0.5; 78 -1.0; 83 -1.4; 89 -1.7; 95 -1.9; 102 -2.1; 109 -2.4; 117 -2.5; 125 -2.7; 134 -2.9; 143 -3.2; 153 -3.3; 164 -3.2; 175 -3.3; 188 -3.5; 201 -3.5; 215 -3.5; 230 -3.5; 246 -3.5; 263 -3.4; 282 -3.3; 301 -3.2; 323 -2.9; 345 -2.8; 369 -2.7; 395 -2.6; 423 -2.4; 452 -2.3; 484 -2.1; 518 -1.9; 554 -1.8; 593 -1.6; 635 -1.4; 679 -1.2; 726 -1.0; 777 -0.8; 832 -0.7; 890 -0.6; 952 -0.1; 1019 0.0; 1090 0.5; 1167 1.2; 1248 1.3; 1336 1.5; 1429 1.4; 1529 1.1; 1636 1.2; 1751 1.4; 1873 1.5; 2004 1.6; 2145 1.4; 2295 1.4; 2455 2.4; 2627 2.6; 2811 2.1; 3008 1.4; 3219 1.3; 3444 1.6; 3685 0.3; 3943 -1.7; 4219 -2.3; 4514 -2.2; 4830 -2.1; 5168 -3.1; 5530 -4.9; 5917 -8.1; 6331 -7.8; 6775 -3.7; 7249 -1.9; 7756 -1.4; 8299 -2.3; 8880 -4.4; 9502 -5.7; 10167 -3.3; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 -1.5; 14260 -4.1; 15258 -4.2; 16326 -3.2; 17469 -2.4; 18692 -2.2; 20000 -2.7
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.5605471717543518dB` and instead set Global volume in the UI for both channels to **-35**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 800 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -3.0dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 12 Hz    | 0.24 | 3.2 dB  |
| Peaking | 192 Hz   | 0.55 | -3.9 dB |
| Peaking | 6068 Hz  | 4.08 | -8.5 dB |
| Peaking | 15498 Hz | 1.21 | -3.5 dB |
| Peaking | 20447 Hz | 1.51 | -2.4 dB |
| Peaking | 1305 Hz  | 3.77 | 1.4 dB  |
| Peaking | 2828 Hz  | 1.12 | 2.6 dB  |
| Peaking | 4187 Hz  | 4.32 | -3.0 dB |
| Peaking | 9487 Hz  | 5.23 | -5.9 dB |
| Peaking | 11542 Hz | 2.81 | 2.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20800/Sennheiser%20HD%20800.png)