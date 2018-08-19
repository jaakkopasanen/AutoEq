# Sennheiser HD 25-1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -7.0dB
GraphicEQ: 10 -84; 20 6.9; 22 6.0; 23 5.7; 25 5.1; 26 4.9; 28 4.6; 30 4.4; 32 4.4; 35 4.2; 37 3.6; 40 2.6; 42 2.0; 45 1.8; 49 2.1; 52 2.6; 56 3.2; 59 3.4; 64 3.3; 68 2.7; 73 1.3; 78 0.2; 83 0.0; 89 -0.5; 95 -1.7; 102 -1.8; 109 -1.4; 117 -0.8; 125 -1.0; 134 -1.6; 143 -1.3; 153 -0.1; 164 0.4; 175 0.1; 188 -0.5; 201 -1.5; 215 -1.7; 230 -1.3; 246 -0.7; 263 -0.5; 282 -0.1; 301 0.4; 323 0.8; 345 1.1; 369 1.3; 395 1.5; 423 1.6; 452 1.5; 484 1.3; 518 1.3; 554 1.3; 593 1.2; 635 1.0; 679 0.9; 726 0.7; 777 0.6; 832 0.5; 890 0.3; 952 0.1; 1019 -0.1; 1090 -0.2; 1167 -0.4; 1248 -0.7; 1336 -1.2; 1429 -1.9; 1529 -2.6; 1636 -3.1; 1751 -3.4; 1873 -3.7; 2004 -3.9; 2145 -3.6; 2295 -2.8; 2455 -1.6; 2627 -0.1; 2811 1.2; 3008 2.1; 3219 2.4; 3444 2.9; 3685 2.6; 3943 2.0; 4219 2.1; 4514 3.2; 4830 4.7; 5168 5.9; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -2.6; 8880 -6.5; 9502 -6.2; 10167 -3.5; 10879 -1.8; 11640 -1.8; 12455 -1.4; 13327 -0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.991139352110833dB` and instead set Global volume in the UI for both channels to **-69**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 25-1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.0dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 23 Hz   | 1.26 | 6.1 dB   |
| Peaking | 61 Hz   | 5.08 | 3.1 dB   |
| Peaking | 1935 Hz | 2.29 | -5.1 dB  |
| Peaking | 6168 Hz | 0.99 | 7.7 dB   |
| Peaking | 9055 Hz | 2.26 | -10.6 dB |
| Peaking | 104 Hz  | 2.87 | -2.1 dB  |
| Peaking | 221 Hz  | 3.71 | -2.0 dB  |
| Peaking | 457 Hz  | 1.16 | 1.6 dB   |
| Peaking | 3149 Hz | 3.12 | 3.9 dB   |
| Peaking | 3236 Hz | 1.63 | -2.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%2025-1/Sennheiser%20HD%2025-1.png)