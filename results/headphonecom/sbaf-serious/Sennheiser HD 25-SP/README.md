# Sennheiser HD 25-SP

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 2.8; 22 2.1; 23 1.7; 25 1.1; 26 0.8; 28 0.3; 30 -0.2; 32 -0.6; 35 -0.8; 37 -0.8; 40 -1.1; 42 -1.6; 45 -2.5; 49 -3.1; 52 -3.3; 56 -3.5; 59 -3.6; 64 -3.6; 68 -3.8; 73 -3.9; 78 -3.6; 83 -3.2; 89 -3.3; 95 -4.7; 102 -6.1; 109 -6.7; 117 -6.8; 125 -6.9; 134 -6.5; 143 -6.1; 153 -5.5; 164 -5.3; 175 -6.1; 188 -6.7; 201 -6.8; 215 -6.4; 230 -5.9; 246 -5.1; 263 -4.4; 282 -3.8; 301 -2.9; 323 -1.7; 345 -0.6; 369 0.1; 395 0.8; 423 1.2; 452 1.2; 484 1.2; 518 1.3; 554 1.3; 593 1.5; 635 1.4; 679 1.1; 726 1.0; 777 1.0; 832 0.7; 890 0.5; 952 0.2; 1019 -0.1; 1090 -0.4; 1167 -0.8; 1248 -1.3; 1336 -2.1; 1429 -2.7; 1529 -3.3; 1636 -4.1; 1751 -4.6; 1873 -4.7; 2004 -4.7; 2145 -4.3; 2295 -3.8; 2455 -3.5; 2627 -3.1; 2811 -1.8; 3008 -0.0; 3219 0.6; 3444 1.1; 3685 1.4; 3943 0.7; 4219 0.7; 4514 0.8; 4830 0.6; 5168 2.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -4.2; 8880 -9.0; 9502 -8.3; 10167 -4.7; 10879 -1.5; 11640 -0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 25-SP ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 114 Hz  | 1.05 | -6.2 dB  |
| Peaking | 213 Hz  | 2.66 | -4.9 dB  |
| Peaking | 1944 Hz | 2.1  | -5.4 dB  |
| Peaking | 6119 Hz | 2.58 | 7.1 dB   |
| Peaking | 9123 Hz | 4.36 | -11.1 dB |
| Peaking | 15 Hz   | 0.91 | 4.1 dB   |
| Peaking | 60 Hz   | 0.73 | -2.3 dB  |
| Peaking | 86 Hz   | 3.39 | 3.1 dB   |
| Peaking | 545 Hz  | 1.53 | 2.3 dB   |
| Peaking | 3457 Hz | 7.27 | 1.6 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD%2025-SP/Sennheiser%20HD%2025-SP.png)