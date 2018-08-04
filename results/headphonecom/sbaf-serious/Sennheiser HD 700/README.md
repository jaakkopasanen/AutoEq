# Sennheiser HD 700

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.8dB
GraphicEQ: 10 -84; 20 5.1; 22 4.4; 23 4.1; 25 3.5; 26 3.3; 28 2.9; 30 2.5; 32 2.2; 35 1.8; 37 1.5; 40 1.2; 42 1.0; 45 0.8; 49 0.4; 52 0.2; 56 0.0; 59 -0.1; 64 -0.4; 68 -0.5; 73 -0.7; 78 -0.8; 83 -1.0; 89 -1.3; 95 -1.5; 102 -1.9; 109 -2.1; 117 -2.5; 125 -3.1; 134 -3.2; 143 -3.5; 153 -3.8; 164 -3.8; 175 -3.6; 188 -3.8; 201 -3.8; 215 -3.6; 230 -3.6; 246 -3.6; 263 -3.5; 282 -3.4; 301 -3.2; 323 -3.0; 345 -2.6; 369 -2.5; 395 -2.3; 423 -2.0; 452 -1.9; 484 -1.8; 518 -1.7; 554 -1.5; 593 -1.1; 635 -0.8; 679 -0.8; 726 -0.7; 777 -0.4; 832 -0.5; 890 -0.4; 952 0.1; 1019 0.0; 1090 0.3; 1167 0.9; 1248 0.9; 1336 1.1; 1429 1.5; 1529 1.6; 1636 2.2; 1751 2.5; 1873 3.2; 2004 3.7; 2145 3.6; 2295 3.3; 2455 4.8; 2627 5.2; 2811 4.3; 3008 3.7; 3219 4.0; 3444 4.6; 3685 4.2; 3943 3.4; 4219 -0.4; 4514 -2.9; 4830 -2.8; 5168 -2.3; 5530 -0.4; 5917 0.0; 6331 -4.8; 6775 -5.3; 7249 -2.0; 7756 -0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 -0.3; 16326 -3.4; 17469 -6.0; 18692 -7.2; 20000 -7.1
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.8dB` and instead set Global volume in the UI for both channels to **-58**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 12 Hz    | 0.55 | 6.8 dB   |
| Peaking | 210 Hz   | 0.51 | -3.9 dB  |
| Peaking | 3668 Hz  | 0.84 | 12.0 dB  |
| Peaking | 4724 Hz  | 1.11 | -11.8 dB |
| Peaking | 29049 Hz | 1.55 | -8.3 dB  |
| Peaking | 4492 Hz  | 9.16 | -2.2 dB  |
| Peaking | 6052 Hz  | 4.23 | 1.0 dB   |
| Peaking | 5849 Hz  | 5.77 | 3.2 dB   |
| Peaking | 6532 Hz  | 6.87 | -7.4 dB  |
| Peaking | 9066 Hz  | 0.65 | 0.8 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20700/Sennheiser%20HD%20700.png)