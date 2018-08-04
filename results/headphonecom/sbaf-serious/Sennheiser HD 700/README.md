# Sennheiser HD 700

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.8dB
GraphicEQ: 10 -84; 20 1.1; 22 0.4; 23 0.1; 25 -0.5; 26 -0.7; 28 -1.1; 30 -1.5; 32 -1.8; 35 -2.2; 37 -2.5; 40 -2.8; 42 -3.0; 45 -3.2; 49 -3.5; 52 -3.7; 56 -3.9; 59 -4.1; 64 -4.3; 68 -4.4; 73 -4.5; 78 -4.4; 83 -4.4; 89 -4.5; 95 -4.4; 102 -4.3; 109 -4.1; 117 -4.1; 125 -4.3; 134 -4.0; 143 -4.1; 153 -4.2; 164 -4.0; 175 -3.8; 188 -3.9; 201 -3.9; 215 -3.7; 230 -3.6; 246 -3.6; 263 -3.6; 282 -3.4; 301 -3.2; 323 -3.0; 345 -2.6; 369 -2.5; 395 -2.3; 423 -2.0; 452 -1.9; 484 -1.8; 518 -1.7; 554 -1.5; 593 -1.1; 635 -0.8; 679 -0.8; 726 -0.7; 777 -0.4; 832 -0.5; 890 -0.4; 952 0.1; 1019 0.0; 1090 0.3; 1167 0.9; 1248 0.9; 1336 1.1; 1429 1.5; 1529 1.6; 1636 2.2; 1751 2.5; 1873 3.2; 2004 3.7; 2145 3.6; 2295 3.3; 2455 4.8; 2627 5.2; 2811 4.3; 3008 3.7; 3219 4.0; 3444 4.6; 3685 4.2; 3943 3.4; 4219 -0.4; 4514 -2.9; 4830 -2.8; 5168 -2.3; 5530 -0.4; 5917 0.0; 6331 -4.8; 6775 -5.3; 7249 -2.0; 7756 -0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 -0.3; 16326 -3.4; 17469 -6.0; 18692 -7.2; 20000 -7.1
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.8dB` and instead set Global volume in the UI for both channels to **-58**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 700 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 121 Hz   | 0.29 | -4.4 dB |
| Peaking | 3369 Hz  | 0.71 | 5.7 dB  |
| Peaking | 4678 Hz  | 3.75 | -7.7 dB |
| Peaking | 6615 Hz  | 6.18 | -8.0 dB |
| Peaking | 29031 Hz | 1.4  | -8.2 dB |
| Peaking | 19 Hz    | 1.57 | 2.3 dB  |
| Peaking | 58 Hz    | 1.91 | -0.7 dB |
| Peaking | 1962 Hz  | 7.83 | 0.6 dB  |
| Peaking | 967 Hz   | 2.55 | -0.3 dB |
| Peaking | 38764 Hz | 4.53 | -0.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%20700/Sennheiser%20HD%20700.png)