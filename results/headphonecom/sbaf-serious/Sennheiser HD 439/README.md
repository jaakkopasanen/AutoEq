# Sennheiser HD 439

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 0.5; 22 0.2; 23 0.1; 25 -0.1; 26 -0.2; 28 -0.4; 30 -0.6; 32 -0.7; 35 -0.9; 37 -1.0; 40 -1.1; 42 -1.2; 45 -1.3; 49 -1.5; 52 -1.5; 56 -1.6; 59 -1.7; 64 -1.7; 68 -1.7; 73 -1.5; 78 -1.2; 83 -1.6; 89 -1.9; 95 -1.3; 102 0.5; 109 1.3; 117 -0.4; 125 -1.9; 134 -2.6; 143 -2.7; 153 -2.8; 164 -2.4; 175 -2.5; 188 -2.4; 201 -2.4; 215 -2.8; 230 -2.7; 246 -2.5; 263 -2.5; 282 -1.8; 301 -1.2; 323 -1.3; 345 -0.7; 369 0.5; 395 0.5; 423 0.4; 452 0.7; 484 1.0; 518 1.1; 554 0.9; 593 0.7; 635 0.4; 679 0.4; 726 0.5; 777 0.2; 832 -0.2; 890 -0.2; 952 -0.7; 1019 0.1; 1090 0.1; 1167 0.3; 1248 0.5; 1336 -0.6; 1429 -1.4; 1529 -1.6; 1636 -1.4; 1751 -1.0; 1873 -0.2; 2004 0.9; 2145 2.1; 2295 3.6; 2455 4.7; 2627 5.3; 2811 5.4; 3008 5.9; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999998715983dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 439 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 55 Hz   | 1.49 | -1.6 dB |
| Peaking | 212 Hz  | 1.05 | -3.0 dB |
| Peaking | 449 Hz  | 1.83 | 1.6 dB  |
| Peaking | 1628 Hz | 2.51 | -3.8 dB |
| Peaking | 3732 Hz | 0.83 | 7.0 dB  |
| Peaking | 108 Hz  | 2.22 | -2.5 dB |
| Peaking | 110 Hz  | 5.96 | 5.2 dB  |
| Peaking | 3893 Hz | 5.01 | -1.0 dB |
| Peaking | 6291 Hz | 2.4  | 4.9 dB  |
| Peaking | 7518 Hz | 1.61 | -4.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20439/Sennheiser%20HD%20439.png)