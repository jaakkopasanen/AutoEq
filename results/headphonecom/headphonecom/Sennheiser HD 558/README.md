# Sennheiser HD 558

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.8dB
GraphicEQ: 10 -84; 20 4.7; 22 3.9; 23 3.5; 25 2.8; 26 2.5; 28 2.0; 30 1.5; 32 1.1; 35 0.5; 37 0.2; 40 -0.3; 42 -0.6; 45 -0.9; 49 -1.4; 52 -1.6; 56 -2.0; 59 -2.1; 64 -2.3; 68 -2.4; 73 -2.5; 78 -2.7; 83 -2.1; 89 -1.3; 95 -2.1; 102 -3.2; 109 -3.5; 117 -3.7; 125 -3.7; 134 -3.7; 143 -3.9; 153 -4.0; 164 -4.0; 175 -4.0; 188 -4.0; 201 -3.8; 215 -3.7; 230 -3.8; 246 -3.8; 263 -3.8; 282 -3.7; 301 -3.6; 323 -3.5; 345 -3.1; 369 -3.1; 395 -2.9; 423 -2.5; 452 -2.3; 484 -2.1; 518 -1.8; 554 -1.2; 593 -0.8; 635 -0.7; 679 -0.5; 726 -0.5; 777 -0.1; 832 0.1; 890 0.1; 952 0.1; 1019 -0.1; 1090 0.0; 1167 0.2; 1248 0.5; 1336 1.1; 1429 1.7; 1529 2.3; 1636 2.9; 1751 2.5; 1873 1.9; 2004 1.3; 2145 0.9; 2295 1.4; 2455 1.5; 2627 0.6; 2811 -0.3; 3008 -0.7; 3219 -1.5; 3444 -0.9; 3685 -0.0; 3943 1.3; 4219 0.7; 4514 0.8; 4830 2.3; 5168 4.1; 5530 5.1; 5917 5.1; 6331 4.5; 6775 2.7; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.8dB` and instead set Global volume in the UI for both channels to **-58**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 558 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 1.21 | 5.0 dB  |
| Peaking | 56 Hz   | 1.75 | -1.4 dB |
| Peaking | 193 Hz  | 0.54 | -4.2 dB |
| Peaking | 1648 Hz | 2.58 | 3.0 dB  |
| Peaking | 5783 Hz | 3.54 | 5.8 dB  |
| Peaking | 395 Hz  | 2.93 | -0.6 dB |
| Peaking | 757 Hz  | 2.6  | 0.6 dB  |
| Peaking | 3107 Hz | 1.65 | 1.3 dB  |
| Peaking | 3231 Hz | 3.99 | -3.2 dB |
| Peaking | 8354 Hz | 4.43 | -0.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Sennheiser%20HD%20558/Sennheiser%20HD%20558.png)