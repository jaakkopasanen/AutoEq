# Sennheiser Momentum

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -0.3; 22 -0.6; 23 -0.7; 25 -0.9; 26 -1.0; 28 -1.2; 30 -1.3; 32 -1.4; 35 -1.5; 37 -1.6; 40 -1.7; 42 -1.8; 45 -1.9; 49 -2.0; 52 -2.0; 56 -2.2; 59 -2.2; 64 -2.3; 68 -2.2; 73 -2.3; 78 -2.4; 83 -2.3; 89 -2.2; 95 -2.1; 102 -2.0; 109 -1.8; 117 -1.5; 125 -1.3; 134 -1.1; 143 -1.2; 153 -1.5; 164 -1.6; 175 -1.0; 188 -1.3; 201 -1.5; 215 -1.4; 230 -1.2; 246 -1.1; 263 -0.9; 282 -0.4; 301 -0.3; 323 0.1; 345 0.7; 369 1.2; 395 1.4; 423 1.6; 452 1.7; 484 1.6; 518 1.5; 554 1.6; 593 1.7; 635 1.4; 679 0.9; 726 0.5; 777 0.5; 832 0.3; 890 0.1; 952 0.1; 1019 0.0; 1090 0.1; 1167 0.2; 1248 -0.1; 1336 -0.7; 1429 -1.2; 1529 -1.5; 1636 -1.5; 1751 -1.5; 1873 -1.1; 2004 -0.4; 2145 0.5; 2295 1.8; 2455 3.4; 2627 4.8; 2811 5.7; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 66 Hz   | 0.6  | -2.3 dB |
| Peaking | 230 Hz  | 1.62 | -1.2 dB |
| Peaking | 459 Hz  | 1.39 | 2.0 dB  |
| Peaking | 1743 Hz | 1.88 | -4.1 dB |
| Peaking | 3749 Hz | 0.86 | 7.2 dB  |
| Peaking | 2237 Hz | 4.83 | -0.9 dB |
| Peaking | 2728 Hz | 3.05 | 1.5 dB  |
| Peaking | 3749 Hz | 2.87 | -1.2 dB |
| Peaking | 6280 Hz | 2.48 | 5.1 dB  |
| Peaking | 7404 Hz | 1.5  | -3.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20Momentum/Sennheiser%20Momentum.png)