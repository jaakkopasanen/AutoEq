# Sennheiser HD 800 2013

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.6dB
GraphicEQ: 10 -84; 20 -1.7; 22 -2.0; 23 -2.2; 25 -2.5; 26 -2.7; 28 -2.9; 30 -3.1; 32 -3.3; 35 -3.5; 37 -3.6; 40 -3.7; 42 -3.8; 45 -3.9; 49 -3.5; 52 -3.2; 56 -3.5; 59 -3.9; 64 -3.6; 68 -3.4; 73 -4.1; 78 -4.6; 83 -4.8; 89 -4.8; 95 -4.9; 102 -4.8; 109 -4.8; 117 -4.7; 125 -4.7; 134 -4.7; 143 -4.6; 153 -4.6; 164 -4.4; 175 -4.5; 188 -4.5; 201 -4.4; 215 -4.4; 230 -4.3; 246 -4.3; 263 -4.2; 282 -4.1; 301 -4.0; 323 -3.7; 345 -3.5; 369 -3.4; 395 -3.3; 423 -3.0; 452 -2.9; 484 -2.9; 518 -2.6; 554 -2.4; 593 -2.1; 635 -1.8; 679 -1.8; 726 -1.5; 777 -1.1; 832 -1.1; 890 -0.8; 952 -0.1; 1019 0.1; 1090 0.6; 1167 1.3; 1248 1.2; 1336 1.1; 1429 0.8; 1529 0.6; 1636 1.0; 1751 1.1; 1873 1.1; 2004 1.3; 2145 0.8; 2295 0.4; 2455 1.6; 2627 2.0; 2811 1.0; 3008 0.0; 3219 0.1; 3444 0.7; 3685 -0.7; 3943 -2.6; 4219 -3.3; 4514 -3.2; 4830 -3.3; 5168 -4.0; 5530 -4.9; 5917 -8.0; 6331 -9.8; 6775 -5.6; 7249 -4.1; 7756 -4.5; 8299 -6.2; 8880 -8.3; 9502 -9.2; 10167 -6.5; 10879 -0.9; 11640 0.0; 12455 0.0; 13327 -0.1; 14260 -2.9; 15258 -3.9; 16326 -3.7; 17469 -4.3; 18692 -5.2; 20000 -5.7
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.6dB` and instead set Global volume in the UI for both channels to **-26**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 800 2013 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 34 Hz    | 0.97 | -2.4 dB |
| Peaking | 117 Hz   | 0.55 | -4.4 dB |
| Peaking | 344 Hz   | 1.06 | -2.4 dB |
| Peaking | 7334 Hz  | 1.18 | -7.1 dB |
| Peaking | 28888 Hz | 1.06 | -5.7 dB |
| Peaking | 2129 Hz  | 1.04 | 2.0 dB  |
| Peaking | 6195 Hz  | 6.8  | -5.7 dB |
| Peaking | 7397 Hz  | 3.53 | 5.4 dB  |
| Peaking | 9640 Hz  | 2.68 | -7.7 dB |
| Peaking | 11253 Hz | 2.91 | 6.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20800%202013/Sennheiser%20HD%20800%202013.png)