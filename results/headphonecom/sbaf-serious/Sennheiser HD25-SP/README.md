# Sennheiser HD25-SP

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -1.2; 22 -1.9; 23 -2.3; 25 -2.9; 26 -3.2; 28 -3.7; 30 -4.2; 32 -4.6; 35 -4.8; 37 -4.8; 40 -5.1; 42 -5.6; 45 -6.4; 49 -7.1; 52 -7.3; 56 -7.4; 59 -7.5; 64 -7.5; 68 -7.6; 73 -7.6; 78 -7.2; 83 -6.6; 89 -6.5; 95 -7.6; 102 -8.5; 109 -8.7; 117 -8.4; 125 -8.1; 134 -7.4; 143 -6.6; 153 -5.9; 164 -5.5; 175 -6.3; 188 -6.8; 201 -6.9; 215 -6.4; 230 -5.9; 246 -5.1; 263 -4.4; 282 -3.8; 301 -2.9; 323 -1.7; 345 -0.6; 369 0.1; 395 0.8; 423 1.2; 452 1.2; 484 1.2; 518 1.3; 554 1.3; 593 1.5; 635 1.4; 679 1.1; 726 1.0; 777 1.0; 832 0.7; 890 0.5; 952 0.2; 1019 -0.1; 1090 -0.4; 1167 -0.8; 1248 -1.3; 1336 -2.1; 1429 -2.7; 1529 -3.3; 1636 -4.1; 1751 -4.6; 1873 -4.7; 2004 -4.7; 2145 -4.3; 2295 -3.8; 2455 -3.5; 2627 -3.1; 2811 -1.8; 3008 -0.0; 3219 0.6; 3444 1.1; 3685 1.4; 3943 0.7; 4219 0.7; 4514 0.8; 4830 0.6; 5168 2.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -4.2; 8880 -9.0; 9502 -8.3; 10167 -4.7; 10879 -1.5; 11640 -0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD25-SP ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 9 Hz    | 1.71 | -6.5 dB  |
| Peaking | 78 Hz   | 0.57 | -8.1 dB  |
| Peaking | 207 Hz  | 2.55 | -3.9 dB  |
| Peaking | 6107 Hz | 3.42 | 7.3 dB   |
| Peaking | 9150 Hz | 4.58 | -10.8 dB |
| Peaking | 86 Hz   | 2.86 | 5.1 dB   |
| Peaking | 96 Hz   | 1.54 | -3.8 dB  |
| Peaking | 570 Hz  | 1.07 | 2.5 dB   |
| Peaking | 1970 Hz | 1.38 | -5.3 dB  |
| Peaking | 3421 Hz | 3.35 | 2.4 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD25-SP/Sennheiser%20HD25-SP.png)