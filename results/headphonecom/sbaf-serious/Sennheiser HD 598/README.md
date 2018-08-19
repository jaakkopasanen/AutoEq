# Sennheiser HD 598

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 5.8; 35 5.3; 37 5.0; 40 4.5; 42 4.2; 45 3.8; 49 3.4; 52 3.1; 56 2.6; 59 2.4; 64 2.5; 68 2.2; 73 1.6; 78 1.8; 83 2.2; 89 1.4; 95 0.6; 102 0.1; 109 -0.2; 117 -0.5; 125 -0.9; 134 -1.2; 143 -1.3; 153 -1.6; 164 -1.7; 175 -1.8; 188 -1.9; 201 -1.9; 215 -1.8; 230 -1.8; 246 -1.9; 263 -2.0; 282 -2.0; 301 -1.9; 323 -1.8; 345 -1.7; 369 -1.6; 395 -1.5; 423 -1.4; 452 -1.3; 484 -1.3; 518 -1.1; 554 -0.7; 593 -0.9; 635 -1.0; 679 0.8; 726 0.1; 777 -0.2; 832 -0.4; 890 -0.2; 952 0.1; 1019 -0.0; 1090 -0.1; 1167 0.1; 1248 -0.2; 1336 -0.1; 1429 -0.0; 1529 0.2; 1636 1.1; 1751 1.3; 1873 1.2; 2004 1.0; 2145 0.6; 2295 1.2; 2455 1.9; 2627 1.0; 2811 0.1; 3008 0.2; 3219 -0.3; 3444 -0.4; 3685 -0.1; 3943 -0.1; 4219 -2.4; 4514 -3.9; 4830 -3.2; 5168 -1.5; 5530 -0.5; 5917 0.0; 6331 -0.1; 6775 0.0; 7249 0.5; 7756 0.3; 8299 -0.3; 8880 -1.3; 9502 -0.3; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.0; 17469 -2.3; 18692 -4.9; 20000 -5.3
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 598 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.3dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 20 Hz    | 0.36 | 6.3 dB  |
| Peaking | 205 Hz   | 0.58 | -2.5 dB |
| Peaking | 2140 Hz  | 1.63 | 1.4 dB  |
| Peaking | 4608 Hz  | 5.71 | -4.3 dB |
| Peaking | 19262 Hz | 2.04 | -6.1 dB |
| Peaking | 223 Hz   | 5.36 | 0.3 dB  |
| Peaking | 457 Hz   | 4.07 | -0.2 dB |
| Peaking | 8341 Hz  | 2.12 | 1.0 dB  |
| Peaking | 8831 Hz  | 6.24 | -2.1 dB |
| Peaking | 15897 Hz | 3.71 | 0.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20598/Sennheiser%20HD%20598.png)