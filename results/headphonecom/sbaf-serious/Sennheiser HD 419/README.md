# Sennheiser HD 419

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -6.1; 22 -6.4; 23 -6.5; 25 -6.7; 26 -6.8; 28 -7.0; 30 -7.1; 32 -7.2; 35 -7.3; 37 -7.4; 40 -7.5; 42 -7.5; 45 -7.6; 49 -7.6; 52 -7.6; 56 -7.6; 59 -7.5; 64 -7.4; 68 -7.4; 73 -7.4; 78 -6.9; 83 -6.0; 89 -3.9; 95 -4.6; 102 -7.7; 109 -8.9; 117 -9.5; 125 -9.7; 134 -9.8; 143 -10.2; 153 -10.3; 164 -9.7; 175 -10.3; 188 -10.5; 201 -10.3; 215 -10.2; 230 -10.0; 246 -9.3; 263 -8.5; 282 -7.6; 301 -6.7; 323 -5.9; 345 -5.3; 369 -4.0; 395 -2.8; 423 -2.3; 452 -2.1; 484 -2.2; 518 -2.7; 554 -3.0; 593 -2.6; 635 -2.0; 679 -1.4; 726 -1.2; 777 -1.1; 832 -1.0; 890 -0.2; 952 -0.3; 1019 0.0; 1090 -0.5; 1167 -0.9; 1248 -0.4; 1336 -1.0; 1429 -1.6; 1529 -1.9; 1636 -1.9; 1751 -2.2; 1873 -2.3; 2004 -1.6; 2145 -0.3; 2295 1.1; 2455 1.7; 2627 1.1; 2811 2.0; 3008 2.2; 3219 2.1; 3444 2.0; 3685 1.8; 3943 3.8; 4219 6.0; 4514 6.0; 4830 6.0; 5168 5.0; 5530 5.2; 5917 5.5; 6331 4.9; 6775 3.4; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 419 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 27 Hz   | 0.84 | -6.3 dB |
| Peaking | 54 Hz   | 1.85 | -3.3 dB |
| Peaking | 170 Hz  | 0.73 | -9.8 dB |
| Peaking | 248 Hz  | 2.54 | -2.1 dB |
| Peaking | 4933 Hz | 1.77 | 6.5 dB  |
| Peaking | 91 Hz   | 6.39 | 5.9 dB  |
| Peaking | 95 Hz   | 2.35 | -2.8 dB |
| Peaking | 1867 Hz | 2.39 | -3.8 dB |
| Peaking | 2321 Hz | 2.03 | 2.3 dB  |
| Peaking | 8477 Hz | 4.37 | -1.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20419/Sennheiser%20HD%20419.png)