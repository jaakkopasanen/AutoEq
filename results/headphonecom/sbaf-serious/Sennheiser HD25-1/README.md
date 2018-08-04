# Sennheiser HD25-1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -7.5dB
GraphicEQ: 10 -84; 20 6.9; 22 6.0; 23 5.7; 25 5.1; 26 4.9; 28 4.6; 30 4.5; 32 4.4; 35 4.2; 37 3.7; 40 2.7; 42 2.2; 45 2.0; 49 2.3; 52 2.9; 56 3.5; 59 3.8; 64 3.9; 68 3.3; 73 2.0; 78 1.0; 83 0.8; 89 0.3; 95 -0.9; 102 -1.2; 109 -0.9; 117 -0.6; 125 -1.0; 134 -1.7; 143 -1.5; 153 -0.4; 164 0.1; 175 -0.1; 188 -0.8; 201 -1.7; 215 -1.9; 230 -1.4; 246 -0.8; 263 -0.6; 282 -0.2; 301 0.4; 323 0.7; 345 1.0; 369 1.2; 395 1.5; 423 1.6; 452 1.5; 484 1.2; 518 1.2; 554 1.2; 593 1.3; 635 1.1; 679 0.8; 726 0.6; 777 0.6; 832 0.5; 890 0.3; 952 0.1; 1019 -0.0; 1090 -0.2; 1167 -0.4; 1248 -0.7; 1336 -1.2; 1429 -1.9; 1529 -2.5; 1636 -3.1; 1751 -3.4; 1873 -3.7; 2004 -3.9; 2145 -3.6; 2295 -2.8; 2455 -1.5; 2627 -0.2; 2811 1.1; 3008 2.2; 3219 2.4; 3444 2.8; 3685 2.5; 3943 2.2; 4219 2.1; 4514 3.1; 4830 4.7; 5168 5.9; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -2.8; 8880 -6.6; 9502 -6.0; 10167 -3.4; 10879 -2.0; 11640 -2.0; 12455 -1.2; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-7.5dB` and instead set Global volume in the UI for both channels to **-75**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD25-1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 23 Hz   | 1.15 | 6.1 dB   |
| Peaking | 62 Hz   | 4.43 | 3.6 dB   |
| Peaking | 1937 Hz | 2.27 | -5.1 dB  |
| Peaking | 6287 Hz | 0.96 | 8.1 dB   |
| Peaking | 9007 Hz | 2.12 | -11.0 dB |
| Peaking | 119 Hz  | 2.21 | -1.6 dB  |
| Peaking | 218 Hz  | 3.8  | -2.1 dB  |
| Peaking | 457 Hz  | 1.14 | 1.6 dB   |
| Peaking | 3124 Hz | 3.22 | 3.7 dB   |
| Peaking | 3184 Hz | 1.62 | -2.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD25-1/Sennheiser%20HD25-1.png)