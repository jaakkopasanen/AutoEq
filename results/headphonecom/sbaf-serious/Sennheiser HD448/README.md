# Sennheiser HD448

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 6.0; 95 6.0; 102 6.0; 109 5.6; 117 4.8; 125 3.9; 134 2.7; 143 1.5; 153 -0.1; 164 -0.7; 175 -0.5; 188 0.5; 201 1.7; 215 2.9; 230 3.4; 246 2.2; 263 1.7; 282 2.0; 301 2.5; 323 2.1; 345 1.8; 369 2.1; 395 2.3; 423 2.4; 452 2.4; 484 2.4; 518 1.8; 554 1.6; 593 1.6; 635 1.4; 679 0.7; 726 0.1; 777 -0.1; 832 0.0; 890 0.3; 952 0.6; 1019 0.0; 1090 0.1; 1167 0.0; 1248 -0.9; 1336 -0.6; 1429 -0.9; 1529 -1.3; 1636 -1.5; 1751 -1.8; 1873 -2.2; 2004 -2.5; 2145 -1.7; 2295 -0.2; 2455 1.2; 2627 0.5; 2811 1.1; 3008 1.4; 3219 1.5; 3444 1.4; 3685 1.4; 3943 2.8; 4219 5.8; 4514 6.0; 4830 6.0; 5168 3.4; 5530 2.7; 5917 3.6; 6331 5.3; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD448 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 44 Hz   | 0.42 | 6.8 dB  |
| Peaking | 457 Hz  | 1.21 | 2.3 dB  |
| Peaking | 4045 Hz | 0.32 | -3.4 dB |
| Peaking | 5030 Hz | 0.84 | 6.9 dB  |
| Peaking | 4445 Hz | 5.47 | 3.0 dB  |
| Peaking | 20 Hz   | 2.64 | 1.3 dB  |
| Peaking | 103 Hz  | 2.91 | 2.1 dB  |
| Peaking | 162 Hz  | 4.97 | -3.8 dB |
| Peaking | 2019 Hz | 4.21 | -2.4 dB |
| Peaking | 2403 Hz | 3.62 | 2.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD448/Sennheiser%20HD448.png)