# Sennheiser HD 219

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.1dB
GraphicEQ: 10 -84; 20 2.8; 22 2.0; 23 1.7; 25 1.1; 26 0.8; 28 0.3; 30 -0.2; 32 -0.6; 35 -1.2; 37 -1.5; 40 -2.0; 42 -2.3; 45 -2.7; 49 -3.1; 52 -3.4; 56 -3.8; 59 -4.0; 64 -4.3; 68 -4.5; 73 -4.6; 78 -4.8; 83 -4.8; 89 -4.8; 95 -5.0; 102 -5.1; 109 -5.0; 117 -4.8; 125 -4.5; 134 -4.0; 143 -3.5; 153 -3.4; 164 -4.1; 175 -3.2; 188 -3.7; 201 -3.4; 215 -2.3; 230 -2.1; 246 -2.0; 263 -1.6; 282 -0.8; 301 0.1; 323 0.9; 345 1.5; 369 1.7; 395 1.9; 423 2.1; 452 1.9; 484 1.7; 518 1.5; 554 1.2; 593 1.0; 635 0.9; 679 1.7; 726 2.0; 777 1.5; 832 1.0; 890 0.6; 952 0.2; 1019 -0.0; 1090 -0.2; 1167 -0.2; 1248 -0.3; 1336 -0.3; 1429 -0.1; 1529 0.2; 1636 -0.6; 1751 -1.5; 1873 -1.5; 2004 -1.2; 2145 -0.9; 2295 -0.4; 2455 -0.1; 2627 0.1; 2811 0.4; 3008 0.4; 3219 0.8; 3444 1.2; 3685 1.6; 3943 0.5; 4219 -1.4; 4514 -1.8; 4830 -0.5; 5168 1.6; 5530 3.3; 5917 4.6; 6331 4.9; 6775 3.8; 7249 1.3; 7756 -1.5; 8299 -4.1; 8880 -5.2; 9502 -4.2; 10167 -0.6; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -1.8; 20000 -6.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.068039287484228dB` and instead set Global volume in the UI for both channels to **-50**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 219 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.6dB** and build filters manually
with these parameters. The first 4 filters can be used independently.
When using independent subset of filters, apply preamp of -5.6dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 85 Hz   | 0.98 | -5.3 dB |
| Peaking | 179 Hz  | 2.78 | -2.4 dB |
| Peaking | 6292 Hz | 3.97 | 6.1 dB  |
| Peaking | 8773 Hz | 4.18 | -6.3 dB |
| Peaking | 20 Hz   | 2.7  | 2.8 dB  |
| Peaking | 419 Hz  | 2.49 | 2.6 dB  |
| Peaking | 726 Hz  | 4.34 | 1.9 dB  |
| Peaking | 1863 Hz | 4.94 | -1.8 dB |
| Peaking | 4484 Hz | 9.8  | -2.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20219/Sennheiser%20HD%20219.png)