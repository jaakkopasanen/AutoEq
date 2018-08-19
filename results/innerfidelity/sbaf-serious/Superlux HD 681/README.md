# Superlux HD 681

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 5.7; 26 5.4; 28 4.8; 30 4.1; 32 3.5; 35 2.7; 37 2.3; 40 1.8; 42 1.5; 45 1.0; 49 0.6; 52 0.3; 56 -0.0; 59 -0.3; 64 -0.4; 68 -0.2; 73 -0.2; 78 -0.4; 83 -0.6; 89 -0.5; 95 -0.4; 102 -0.7; 109 -1.0; 117 -1.3; 125 -1.7; 134 -1.8; 143 -1.9; 153 -2.0; 164 -1.8; 175 -1.6; 188 -1.0; 201 -0.5; 215 -0.9; 230 -1.2; 246 -1.3; 263 -1.2; 282 -1.1; 301 -0.9; 323 -0.7; 345 -0.6; 369 -0.5; 395 -0.5; 423 -0.3; 452 -0.2; 484 -0.3; 518 -0.3; 554 -0.2; 593 0.0; 635 0.8; 679 0.8; 726 0.4; 777 0.5; 832 0.4; 890 0.2; 952 0.1; 1019 -0.1; 1090 -0.5; 1167 -0.8; 1248 -1.4; 1336 -2.1; 1429 -2.9; 1529 -3.6; 1636 -3.9; 1751 -4.5; 1873 -5.1; 2004 -5.6; 2145 -6.2; 2295 -6.3; 2455 -5.8; 2627 -5.0; 2811 -4.8; 3008 -4.0; 3219 -3.1; 3444 -2.2; 3685 -0.9; 3943 -0.3; 4219 -1.5; 4514 -3.9; 4830 -4.4; 5168 -3.9; 5530 -5.4; 5917 -4.1; 6331 -2.8; 6775 -0.8; 7249 -3.8; 7756 -7.5; 8299 -9.8; 8880 -10.2; 9502 -9.5; 10167 -7.9; 10879 -4.1; 11640 -0.3; 12455 0.0; 13327 -0.2; 14260 -2.7; 15258 -2.6; 16326 -0.3; 17469 0.0; 18692 -0.2; 20000 -3.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Superlux HD 681 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.3dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 23 Hz    | 1.38 | 6.4 dB   |
| Peaking | 146 Hz   | 1    | -1.9 dB  |
| Peaking | 2190 Hz  | 1.64 | -6.4 dB  |
| Peaking | 5284 Hz  | 4.12 | -3.5 dB  |
| Peaking | 8956 Hz  | 2.79 | -11.1 dB |
| Peaking | 765 Hz   | 2.51 | 1.2 dB   |
| Peaking | 11926 Hz | 8.58 | 2.1 dB   |
| Peaking | 12930 Hz | 5.48 | 1.7 dB   |
| Peaking | 14635 Hz | 4.71 | -3.0 dB  |
| Peaking | 19911 Hz | 5.13 | -2.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Superlux%20HD%20681/Superlux%20HD%20681.png)