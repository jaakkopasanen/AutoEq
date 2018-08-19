# Sennheiser HD 518

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.3dB
GraphicEQ: 10 -84; 20 6.2; 22 5.5; 23 5.1; 25 4.5; 26 4.2; 28 3.7; 30 3.1; 32 2.6; 35 2.0; 37 1.7; 40 1.2; 42 0.9; 45 0.5; 49 0.0; 52 -0.3; 56 -0.8; 59 -1.1; 64 -1.5; 68 -1.8; 73 -2.1; 78 -2.4; 83 -2.6; 89 -2.1; 95 -1.6; 102 -2.3; 109 -3.1; 117 -3.5; 125 -4.0; 134 -4.1; 143 -4.3; 153 -4.6; 164 -4.4; 175 -4.4; 188 -4.6; 201 -4.5; 215 -4.4; 230 -4.4; 246 -4.4; 263 -4.4; 282 -4.1; 301 -4.0; 323 -3.7; 345 -3.5; 369 -3.4; 395 -3.1; 423 -3.0; 452 -2.7; 484 -2.6; 518 -2.1; 554 -1.7; 593 -1.5; 635 -1.5; 679 -1.6; 726 -1.5; 777 -0.5; 832 -0.8; 890 -0.6; 952 -0.1; 1019 0.0; 1090 0.7; 1167 1.5; 1248 1.8; 1336 2.7; 1429 3.4; 1529 3.9; 1636 4.9; 1751 4.8; 1873 4.1; 2004 3.1; 2145 2.1; 2295 2.1; 2455 2.3; 2627 1.6; 2811 1.0; 3008 0.1; 3219 -0.4; 3444 0.7; 3685 1.6; 3943 1.4; 4219 -1.1; 4514 -2.3; 4830 -1.7; 5168 -0.7; 5530 0.5; 5917 2.1; 6331 3.1; 6775 2.6; 7249 1.3; 7756 0.3; 8299 -0.3; 8880 -1.2; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -1.0; 18692 -3.1; 20000 -3.2
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.295820582041435dB` and instead set Global volume in the UI for both channels to **-62**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 518 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.0dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 0.96 | 6.2 dB  |
| Peaking | 195 Hz   | 0.95 | -1.1 dB |
| Peaking | 205 Hz   | 0.37 | -3.7 dB |
| Peaking | 1672 Hz  | 1.78 | 5.2 dB  |
| Peaking | 19372 Hz | 2.31 | -3.9 dB |
| Peaking | 69 Hz    | 3.97 | -0.6 dB |
| Peaking | 3856 Hz  | 6.37 | 3.7 dB  |
| Peaking | 4451 Hz  | 2.65 | -3.7 dB |
| Peaking | 6378 Hz  | 3.51 | 3.8 dB  |
| Peaking | 8720 Hz  | 7.68 | -1.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20518/Sennheiser%20HD%20518.png)