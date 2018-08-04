# Sennheiser HD 239

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -4.7; 22 -5.1; 23 -5.3; 25 -5.7; 26 -5.9; 28 -6.2; 30 -6.4; 32 -6.6; 35 -6.9; 37 -7.0; 40 -7.2; 42 -7.3; 45 -7.4; 49 -7.6; 52 -7.7; 56 -7.8; 59 -7.8; 64 -7.8; 68 -7.8; 73 -7.8; 78 -7.8; 83 -7.8; 89 -7.7; 95 -7.6; 102 -7.1; 109 -6.9; 117 -6.9; 125 -7.1; 134 -6.9; 143 -6.8; 153 -6.6; 164 -6.6; 175 -6.4; 188 -6.2; 201 -6.0; 215 -5.8; 230 -5.6; 246 -5.4; 263 -5.0; 282 -4.6; 301 -4.3; 323 -4.0; 345 -3.8; 369 -3.4; 395 -3.1; 423 -2.7; 452 -2.3; 484 -2.1; 518 -1.6; 554 -1.2; 593 -1.0; 635 -0.7; 679 -0.4; 726 -0.3; 777 -0.1; 832 -0.0; 890 0.1; 952 0.1; 1019 0.0; 1090 0.0; 1167 0.3; 1248 0.4; 1336 0.9; 1429 2.5; 1529 2.3; 1636 2.9; 1751 3.4; 1873 4.4; 2004 5.8; 2145 6.0; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 239 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 33 Hz   | 0.51 | -4.5 dB |
| Peaking | 126 Hz  | 0.36 | -6.1 dB |
| Peaking | 2631 Hz | 0.99 | 6.3 dB  |
| Peaking | 5311 Hz | 2.1  | 4.8 dB  |
| Peaking | 1170 Hz | 2.08 | -2.5 dB |
| Peaking | 1117 Hz | 1.03 | 1.6 dB  |
| Peaking | 6456 Hz | 5.73 | 2.7 dB  |
| Peaking | 6663 Hz | 3.23 | 0.3 dB  |
| Peaking | 7646 Hz | 1.86 | -2.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Sennheiser%20HD%20239/Sennheiser%20HD%20239.png)