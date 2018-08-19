# Sennheiser HD 558

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 5.8; 32 5.5; 35 5.0; 37 4.7; 40 4.2; 42 3.9; 45 3.5; 49 3.0; 52 2.6; 56 2.2; 59 2.0; 64 1.6; 68 1.5; 73 1.2; 78 0.8; 83 1.2; 89 1.9; 95 0.9; 102 -0.3; 109 -0.7; 117 -1.1; 125 -1.2; 134 -1.5; 143 -1.8; 153 -2.0; 164 -2.2; 175 -2.3; 188 -2.3; 201 -2.1; 215 -2.1; 230 -2.2; 246 -2.3; 263 -2.3; 282 -2.2; 301 -2.2; 323 -2.0; 345 -1.7; 369 -1.7; 395 -1.6; 423 -1.4; 452 -1.3; 484 -1.3; 518 -1.1; 554 -0.7; 593 -0.4; 635 -0.4; 679 -0.4; 726 -0.5; 777 -0.0; 832 0.2; 890 0.1; 952 0.1; 1019 -0.1; 1090 -0.1; 1167 -0.1; 1248 -0.2; 1336 -0.3; 1429 -0.4; 1529 -0.4; 1636 -0.1; 1751 -0.5; 1873 -1.1; 2004 -1.6; 2145 -2.1; 2295 -1.7; 2455 -1.5; 2627 -2.4; 2811 -3.1; 3008 -3.3; 3219 -3.8; 3444 -2.9; 3685 -2.0; 3943 -1.3; 4219 -2.9; 4514 -3.9; 4830 -3.1; 5168 -1.4; 5530 0.4; 5917 1.6; 6331 2.3; 6775 1.2; 7249 1.0; 7756 0.3; 8299 0.0; 8880 -1.4; 9502 -1.5; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -1.0; 18692 -3.9; 20000 -3.8
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 558 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.3dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 0.5  | 6.2 dB  |
| Peaking | 207 Hz   | 0.7  | -2.8 dB |
| Peaking | 2998 Hz  | 2.01 | -3.3 dB |
| Peaking | 4694 Hz  | 5.24 | -3.5 dB |
| Peaking | 6283 Hz  | 4.42 | 2.9 dB  |
| Peaking | 89 Hz    | 5.73 | 2.5 dB  |
| Peaking | 90 Hz    | 1.83 | -1.0 dB |
| Peaking | 884 Hz   | 3.03 | 0.6 dB  |
| Peaking | 2062 Hz  | 9.6  | -1.0 dB |
| Peaking | 19240 Hz | 2.36 | -4.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20558/Sennheiser%20HD%20558.png)