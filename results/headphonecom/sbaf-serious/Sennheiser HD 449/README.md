# Sennheiser HD 449

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 0.4; 22 -0.3; 23 -0.7; 25 -1.3; 26 -1.6; 28 -2.1; 30 -2.5; 32 -3.0; 35 -3.6; 37 -3.9; 40 -4.3; 42 -4.6; 45 -5.0; 49 -5.4; 52 -5.6; 56 -5.9; 59 -6.0; 64 -6.1; 68 -6.1; 73 -5.9; 78 -5.5; 83 -5.3; 89 -5.0; 95 -4.2; 102 -2.4; 109 -1.3; 117 -2.2; 125 -4.1; 134 -4.9; 143 -4.7; 153 -3.8; 164 -2.2; 175 -3.4; 188 -4.0; 201 -3.6; 215 -3.2; 230 -3.5; 246 -3.3; 263 -2.4; 282 -1.3; 301 -0.5; 323 0.1; 345 0.6; 369 0.8; 395 1.1; 423 1.6; 452 1.7; 484 1.4; 518 1.5; 554 1.6; 593 1.4; 635 0.7; 679 0.3; 726 0.2; 777 0.3; 832 0.3; 890 0.1; 952 -0.1; 1019 0.0; 1090 0.1; 1167 0.0; 1248 -0.6; 1336 -1.4; 1429 -1.9; 1529 -2.2; 1636 -2.2; 1751 -2.1; 1873 -1.4; 2004 -0.6; 2145 0.5; 2295 2.1; 2455 2.7; 2627 2.6; 2811 3.2; 3008 3.8; 3219 3.6; 3444 3.7; 3685 4.5; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 449 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 45 Hz   | 1.25 | -3.9 dB |
| Peaking | 72 Hz   | 1.67 | -4.3 dB |
| Peaking | 176 Hz  | 1.59 | -3.5 dB |
| Peaking | 1627 Hz | 3.27 | -3.4 dB |
| Peaking | 4525 Hz | 1.17 | 6.6 dB  |
| Peaking | 296 Hz  | 1.44 | 0.7 dB  |
| Peaking | 247 Hz  | 4.05 | -2.3 dB |
| Peaking | 471 Hz  | 1.88 | 1.9 dB  |
| Peaking | 6365 Hz | 3.45 | 4.3 dB  |
| Peaking | 7342 Hz | 1.58 | -3.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20449/Sennheiser%20HD%20449.png)