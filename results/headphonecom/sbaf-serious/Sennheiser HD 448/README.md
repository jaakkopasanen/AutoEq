# Sennheiser HD 448

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 6.0; 95 6.0; 102 5.9; 109 5.2; 117 4.6; 125 3.9; 134 2.8; 143 1.7; 153 0.2; 164 -0.4; 175 -0.3; 188 0.7; 201 1.9; 215 3.1; 230 3.5; 246 2.3; 263 1.8; 282 2.1; 301 2.6; 323 2.2; 345 1.8; 369 2.1; 395 2.4; 423 2.4; 452 2.3; 484 2.5; 518 1.9; 554 1.6; 593 1.5; 635 1.3; 679 0.8; 726 0.2; 777 -0.2; 832 -0.0; 890 0.4; 952 0.6; 1019 -0.0; 1090 0.1; 1167 0.0; 1248 -0.9; 1336 -0.6; 1429 -0.9; 1529 -1.3; 1636 -1.5; 1751 -1.8; 1873 -2.2; 2004 -2.5; 2145 -1.7; 2295 -0.2; 2455 1.1; 2627 0.5; 2811 1.2; 3008 1.3; 3219 1.6; 3444 1.5; 3685 1.5; 3943 2.6; 4219 5.8; 4514 6.0; 4830 6.0; 5168 3.4; 5530 2.7; 5917 3.7; 6331 5.3; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 448 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 32 Hz    | 0.51 | 6.3 dB  |
| Peaking | 91 Hz    | 1.87 | 3.9 dB  |
| Peaking | 377 Hz   | 1.32 | 2.3 dB  |
| Peaking | 4798 Hz  | 2.09 | 5.7 dB  |
| Peaking | 24000 Hz | 2.44 | 2.1 dB  |
| Peaking | 166 Hz   | 5.48 | -2.8 dB |
| Peaking | 223 Hz   | 6.57 | 2.3 dB  |
| Peaking | 1850 Hz  | 3.13 | -2.8 dB |
| Peaking | 6402 Hz  | 5.72 | 6.7 dB  |
| Peaking | 6468 Hz  | 2.4  | -3.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20448/Sennheiser%20HD%20448.png)