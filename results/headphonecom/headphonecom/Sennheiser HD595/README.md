# Sennheiser HD595

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -7.4dB
GraphicEQ: 10 -84; 20 6.9; 22 5.9; 23 5.4; 25 4.6; 26 4.3; 28 3.7; 30 3.1; 32 2.6; 35 1.9; 37 1.5; 40 1.0; 42 0.7; 45 0.3; 49 -0.2; 52 -0.3; 56 -0.1; 59 -0.3; 64 -0.7; 68 -0.1; 73 0.5; 78 -0.7; 83 -1.5; 89 -1.9; 95 -2.2; 102 -2.4; 109 -2.5; 117 -2.5; 125 -2.7; 134 -2.8; 143 -3.0; 153 -2.9; 164 -2.7; 175 -2.8; 188 -2.9; 201 -2.8; 215 -2.8; 230 -2.7; 246 -2.9; 263 -2.9; 282 -2.8; 301 -2.7; 323 -2.6; 345 -2.3; 369 -2.0; 395 -1.8; 423 -1.3; 452 -1.0; 484 -1.0; 518 -0.9; 554 -0.8; 593 -0.7; 635 -0.6; 679 0.7; 726 0.3; 777 0.2; 832 0.2; 890 0.2; 952 0.0; 1019 0.0; 1090 0.3; 1167 0.8; 1248 1.4; 1336 2.4; 1429 3.4; 1529 4.1; 1636 4.6; 1751 4.7; 1873 4.4; 2004 3.9; 2145 3.6; 2295 3.5; 2455 4.0; 2627 4.7; 2811 4.7; 3008 4.0; 3219 3.3; 3444 3.3; 3685 3.9; 3943 5.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 2.3; 7249 1.2; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-7.4dB` and instead set Global volume in the UI for both channels to **-74**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD595 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 19 Hz   | 1.14 | 7.0 dB  |
| Peaking | 178 Hz  | 0.54 | -3.2 dB |
| Peaking | 1656 Hz | 2.38 | 4.2 dB  |
| Peaking | 2726 Hz | 2.12 | 3.0 dB  |
| Peaking | 5009 Hz | 1.83 | 6.4 dB  |
| Peaking | 72 Hz   | 8.1  | 1.2 dB  |
| Peaking | 710 Hz  | 4.55 | 1.3 dB  |
| Peaking | 746 Hz  | 1.22 | -0.4 dB |
| Peaking | 6267 Hz | 6.77 | 3.1 dB  |
| Peaking | 7578 Hz | 1.7  | -1.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Sennheiser%20HD595/Sennheiser%20HD595.png)