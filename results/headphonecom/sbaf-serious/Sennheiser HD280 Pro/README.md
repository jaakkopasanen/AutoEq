# Sennheiser HD280 Pro

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 0.5; 22 0.2; 23 0.1; 25 -0.2; 26 -0.3; 28 -0.4; 30 -0.5; 32 -0.6; 35 -0.7; 37 -0.7; 40 -0.6; 42 -0.5; 45 -0.3; 49 -0.0; 52 0.4; 56 1.3; 59 2.0; 64 3.5; 68 5.4; 73 6.0; 78 6.0; 83 5.2; 89 2.7; 95 1.6; 102 4.1; 109 6.0; 117 5.9; 125 4.6; 134 3.6; 143 3.3; 153 3.7; 164 4.5; 175 2.3; 188 1.4; 201 0.7; 215 0.2; 230 0.0; 246 -0.3; 263 -0.5; 282 -0.5; 301 -0.4; 323 -0.4; 345 -0.3; 369 -0.2; 395 -0.3; 423 -0.2; 452 0.1; 484 0.1; 518 0.1; 554 -0.1; 593 -0.2; 635 -0.2; 679 -0.2; 726 -0.2; 777 0.0; 832 0.1; 890 0.1; 952 0.1; 1019 -0.0; 1090 -0.2; 1167 -0.2; 1248 -0.1; 1336 0.0; 1429 0.4; 1529 0.7; 1636 0.2; 1751 -0.8; 1873 -0.8; 2004 -1.1; 2145 -1.2; 2295 -1.9; 2455 -1.8; 2627 -0.9; 2811 1.2; 3008 3.4; 3219 3.3; 3444 1.9; 3685 1.1; 3943 1.3; 4219 1.8; 4514 1.2; 4830 1.9; 5168 3.2; 5530 3.4; 5917 2.4; 6331 1.1; 6775 1.0; 7249 0.0; 7756 -1.3; 8299 -3.2; 8880 -4.9; 9502 -5.5; 10167 -4.9; 10879 -3.2; 11640 -0.5; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD280 Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 73 Hz   | 4.26 | 5.8 dB  |
| Peaking | 122 Hz  | 2.09 | 5.2 dB  |
| Peaking | 5485 Hz | 2.77 | 3.7 dB  |
| Peaking | 3128 Hz | 8.12 | 3.8 dB  |
| Peaking | 9456 Hz | 3.06 | -6.3 dB |
| Peaking | 38 Hz   | 2.35 | -1.0 dB |
| Peaking | 165 Hz  | 9.31 | 2.8 dB  |
| Peaking | 263 Hz  | 1.16 | -0.8 dB |
| Peaking | 2312 Hz | 4.06 | -2.4 dB |
| Peaking | 7096 Hz | 0.15 | 0.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD280%20Pro/Sennheiser%20HD280%20Pro.png)