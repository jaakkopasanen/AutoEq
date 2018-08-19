# Sennheiser HD 700

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.7dB
GraphicEQ: 10 -84; 20 5.6; 22 5.0; 23 4.7; 25 4.1; 26 3.9; 28 3.4; 30 3.0; 32 2.6; 35 2.0; 37 1.7; 40 1.4; 42 1.1; 45 0.8; 49 0.4; 52 0.2; 56 -0.2; 59 -0.4; 64 -0.7; 68 -0.9; 73 -1.2; 78 -1.4; 83 -1.6; 89 -2.0; 95 -2.4; 102 -2.8; 109 -3.1; 117 -3.2; 125 -3.5; 134 -3.7; 143 -4.0; 153 -4.2; 164 -4.2; 175 -4.2; 188 -4.4; 201 -4.4; 215 -4.3; 230 -4.3; 246 -4.3; 263 -4.2; 282 -4.1; 301 -3.9; 323 -3.8; 345 -3.6; 369 -3.5; 395 -3.3; 423 -3.0; 452 -2.8; 484 -2.7; 518 -2.5; 554 -2.2; 593 -1.9; 635 -1.7; 679 -1.7; 726 -1.4; 777 -1.0; 832 -0.9; 890 -0.6; 952 -0.3; 1019 0.1; 1090 0.5; 1167 0.7; 1248 1.4; 1336 1.7; 1429 2.3; 1529 2.9; 1636 3.0; 1751 3.5; 1873 4.2; 2004 4.5; 2145 4.2; 2295 3.8; 2455 3.4; 2627 3.1; 2811 2.6; 3008 2.5; 3219 2.6; 3444 3.2; 3685 3.7; 3943 2.3; 4219 -0.6; 4514 -2.1; 4830 -4.1; 5168 -5.1; 5530 -5.4; 5917 -7.2; 6331 -9.6; 6775 -6.7; 7249 -3.2; 7756 -1.2; 8299 -1.3; 8880 -2.3; 9502 -2.5; 10167 -2.0; 10879 -0.8; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.4; 17469 -2.6; 18692 -5.5; 20000 -9.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.737383442900156dB` and instead set Global volume in the UI for both channels to **-57**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.7dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 14 Hz    | 0.54 | 6.9 dB  |
| Peaking | 212 Hz   | 0.41 | -4.5 dB |
| Peaking | 2014 Hz  | 1.2  | 4.8 dB  |
| Peaking | 3722 Hz  | 5.44 | 3.9 dB  |
| Peaking | 6081 Hz  | 2.27 | -8.8 dB |
| Peaking | 3266 Hz  | 5.59 | 0.5 dB  |
| Peaking | 4810 Hz  | 7.18 | -1.3 dB |
| Peaking | 7757 Hz  | 7.33 | 2.4 dB  |
| Peaking | 9498 Hz  | 6.57 | -1.6 dB |
| Peaking | 19674 Hz | 2.1  | -9.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20700/Sennheiser%20HD%20700.png)