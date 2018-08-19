# Sennheiser HD 650 (balanced)

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 5.7; 23 5.6; 25 5.1; 26 4.9; 28 4.3; 30 3.8; 32 3.4; 35 2.9; 37 2.7; 40 2.3; 42 2.1; 45 2.0; 49 2.0; 52 1.7; 56 1.0; 59 0.5; 64 0.2; 68 0.2; 73 0.0; 78 -0.5; 83 -1.0; 89 -1.4; 95 -1.7; 102 -2.0; 109 -2.1; 117 -2.3; 125 -2.6; 134 -2.8; 143 -2.9; 153 -3.0; 164 -2.7; 175 -2.8; 188 -2.9; 201 -2.8; 215 -2.8; 230 -2.7; 246 -2.5; 263 -2.5; 282 -2.3; 301 -2.2; 323 -2.0; 345 -1.7; 369 -1.6; 395 -1.3; 423 -1.1; 452 -0.9; 484 -0.8; 518 -0.8; 554 -0.8; 593 -0.6; 635 -0.4; 679 -0.4; 726 -0.5; 777 -0.5; 832 -0.6; 890 -0.7; 952 -0.1; 1019 -0.1; 1090 -0.6; 1167 -0.9; 1248 -1.1; 1336 -1.2; 1429 -1.5; 1529 -1.7; 1636 -2.0; 1751 -2.1; 1873 -2.3; 2004 -2.3; 2145 -2.1; 2295 -1.9; 2455 -1.8; 2627 -1.7; 2811 -1.8; 3008 -1.6; 3219 -1.8; 3444 -1.5; 3685 -0.6; 3943 0.3; 4219 0.1; 4514 -1.0; 4830 -0.5; 5168 2.0; 5530 3.1; 5917 1.5; 6331 -0.8; 6775 -1.0; 7249 -0.7; 7756 -0.8; 8299 -1.8; 8880 -3.1; 9502 -2.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -0.0; 20000 -3.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 650 (balanced) ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.0dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 13 Hz    | 0.42 | 6.9 dB  |
| Peaking | 161 Hz   | 0.59 | -3.3 dB |
| Peaking | 1866 Hz  | 1.84 | -2.3 dB |
| Peaking | 2987 Hz  | 3.7  | -1.4 dB |
| Peaking | 8897 Hz  | 6.19 | -3.3 dB |
| Peaking | 5473 Hz  | 5.79 | 5.5 dB  |
| Peaking | 6033 Hz  | 2.15 | -1.9 dB |
| Peaking | 10849 Hz | 3.46 | 0.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20650%20(balanced)/Sennheiser%20HD%20650%20(balanced).png)