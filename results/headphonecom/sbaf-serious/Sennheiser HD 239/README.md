# Sennheiser HD 239

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -0.2; 22 -0.6; 23 -0.8; 25 -1.2; 26 -1.4; 28 -1.7; 30 -1.9; 32 -2.1; 35 -2.4; 37 -2.5; 40 -2.7; 42 -2.9; 45 -3.0; 49 -3.2; 52 -3.4; 56 -3.6; 59 -3.8; 64 -3.9; 68 -4.0; 73 -4.2; 78 -4.3; 83 -4.5; 89 -4.5; 95 -4.5; 102 -4.2; 109 -4.1; 117 -4.3; 125 -4.6; 134 -4.6; 143 -4.7; 153 -4.6; 164 -4.7; 175 -4.6; 188 -4.5; 201 -4.4; 215 -4.2; 230 -4.1; 246 -3.9; 263 -3.5; 282 -3.1; 301 -2.8; 323 -2.6; 345 -2.3; 369 -2.0; 395 -1.8; 423 -1.5; 452 -1.3; 484 -1.3; 518 -1.0; 554 -0.8; 593 -0.6; 635 -0.4; 679 -0.3; 726 -0.2; 777 -0.0; 832 0.1; 890 0.1; 952 0.2; 1019 0.0; 1090 -0.1; 1167 -0.0; 1248 -0.3; 1336 -0.4; 1429 0.3; 1529 -0.4; 1636 -0.1; 1751 0.4; 1873 1.5; 2004 3.3; 2145 4.9; 2295 5.9; 2455 6.0; 2627 6.0; 2811 5.8; 3008 4.8; 3219 3.7; 3444 4.9; 3685 6.0; 3943 5.9; 4219 2.9; 4514 1.4; 4830 2.5; 5168 4.3; 5530 5.9; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999999582dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 239 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.7dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 65 Hz    | 0.6  | -3.1 dB |
| Peaking | 190 Hz   | 0.69 | -3.6 dB |
| Peaking | 2792 Hz  | 1.55 | 6.1 dB  |
| Peaking | 5903 Hz  | 3.62 | 5.8 dB  |
| Peaking | 24000 Hz | 2.51 | 3.7 dB  |
| Peaking | 1707 Hz  | 2.56 | -2.3 dB |
| Peaking | 2214 Hz  | 2.86 | 2.8 dB  |
| Peaking | 3426 Hz  | 2.09 | -3.0 dB |
| Peaking | 3750 Hz  | 5.63 | 5.4 dB  |
| Peaking | 8289 Hz  | 4.81 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20239/Sennheiser%20HD%20239.png)