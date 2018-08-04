# Sennheiser HD25-1

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 2.1; 22 1.4; 23 1.1; 25 0.6; 26 0.4; 28 0.1; 30 -0.1; 32 -0.1; 35 -0.3; 37 -0.8; 40 -1.9; 42 -2.4; 45 -2.6; 49 -2.2; 52 -1.7; 56 -1.0; 59 -0.7; 64 -0.6; 68 -1.1; 73 -2.4; 78 -3.3; 83 -3.4; 89 -3.7; 95 -4.7; 102 -4.7; 109 -4.1; 117 -3.5; 125 -3.4; 134 -3.9; 143 -3.4; 153 -2.1; 164 -1.5; 175 -1.6; 188 -2.2; 201 -3.1; 215 -3.3; 230 -2.8; 246 -2.2; 263 -1.9; 282 -1.5; 301 -1.0; 323 -0.7; 345 -0.4; 369 -0.1; 395 0.2; 423 0.4; 452 0.5; 484 0.5; 518 0.7; 554 0.8; 593 0.8; 635 0.8; 679 0.7; 726 0.6; 777 0.5; 832 0.4; 890 0.3; 952 0.1; 1019 -0.0; 1090 -0.2; 1167 -0.1; 1248 0.0; 1336 0.1; 1429 0.2; 1529 0.2; 1636 -0.0; 1751 -0.4; 1873 -0.8; 2004 -1.0; 2145 -0.6; 2295 0.3; 2455 1.4; 2627 2.8; 2811 4.1; 3008 4.8; 3219 4.7; 3444 4.9; 3685 4.6; 3943 4.5; 4219 5.6; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -1.5; 8880 -4.7; 9502 -3.4; 10167 -0.4; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD25-1 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 102 Hz  | 1.35 | -4.4 dB |
| Peaking | 221 Hz  | 3.52 | -2.6 dB |
| Peaking | 3138 Hz | 3.68 | 3.5 dB  |
| Peaking | 5304 Hz | 1.45 | 6.7 dB  |
| Peaking | 8981 Hz | 4.48 | -6.5 dB |
| Peaking | 17 Hz   | 1.42 | 2.5 dB  |
| Peaking | 46 Hz   | 2.84 | -2.4 dB |
| Peaking | 62 Hz   | 4.74 | 1.4 dB  |
| Peaking | 574 Hz  | 2.08 | 1.0 dB  |
| Peaking | 1992 Hz | 4.59 | -2.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Sennheiser%20HD25-1/Sennheiser%20HD25-1.png)