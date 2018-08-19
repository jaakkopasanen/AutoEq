# Sennheiser HD 600

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 5.7; 37 5.4; 40 4.8; 42 4.5; 45 4.1; 49 3.6; 52 3.5; 56 3.6; 59 3.5; 64 2.4; 68 1.5; 73 0.9; 78 0.5; 83 0.2; 89 -0.2; 95 -0.5; 102 -0.8; 109 -0.9; 117 -1.1; 125 -1.5; 134 -1.5; 143 -1.5; 153 -1.7; 164 -1.7; 175 -1.8; 188 -1.6; 201 -1.7; 215 -1.5; 230 -1.4; 246 -1.4; 263 -1.2; 282 -1.1; 301 -0.8; 323 -0.7; 345 -0.5; 369 -0.2; 395 -0.1; 423 0.2; 452 0.3; 484 0.4; 518 0.3; 554 0.4; 593 0.5; 635 0.7; 679 0.8; 726 1.0; 777 0.9; 832 0.6; 890 0.4; 952 0.1; 1019 0.2; 1090 0.4; 1167 0.2; 1248 0.1; 1336 -0.1; 1429 -0.4; 1529 -0.6; 1636 -0.7; 1751 -0.6; 1873 -0.8; 2004 -0.7; 2145 -0.9; 2295 -1.3; 2455 -1.5; 2627 -1.7; 2811 -2.2; 3008 -2.7; 3219 -3.5; 3444 -4.1; 3685 -4.4; 3943 -4.2; 4219 -4.3; 4514 -4.6; 4830 -4.1; 5168 -2.3; 5530 0.9; 5917 2.8; 6331 1.8; 6775 1.2; 7249 1.1; 7756 0.3; 8299 0.0; 8880 -0.2; 9502 -0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 -0.3; 13327 -3.3; 14260 -5.6; 15258 -5.0; 16326 -2.0; 17469 -0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.3dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 27 Hz    | 0.52 | 6.3 dB  |
| Peaking | 134 Hz   | 0.83 | -2.6 dB |
| Peaking | 4412 Hz  | 1.39 | -6.4 dB |
| Peaking | 6037 Hz  | 2.48 | 5.9 dB  |
| Peaking | 14727 Hz | 3.54 | -6.3 dB |
| Peaking | 269 Hz   | 1.39 | -1.2 dB |
| Peaking | 352 Hz   | 0.67 | 0.8 dB  |
| Peaking | 735 Hz   | 2.4  | 0.8 dB  |
| Peaking | 3224 Hz  | 7.23 | -0.6 dB |
| Peaking | 11607 Hz | 5.44 | 1.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20600/Sennheiser%20HD%20600.png)