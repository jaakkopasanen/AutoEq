# Sennheiser HD25-SP

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.7dB
GraphicEQ: 10 -84; 20 -1.7; 22 -2.5; 23 -2.8; 25 -3.4; 26 -3.7; 28 -4.3; 30 -4.8; 32 -5.1; 35 -5.3; 37 -5.4; 40 -5.7; 42 -6.2; 45 -7.0; 49 -7.7; 52 -7.8; 56 -8.0; 59 -8.1; 64 -8.1; 68 -8.2; 73 -8.2; 78 -7.9; 83 -7.4; 89 -7.3; 95 -8.4; 102 -9.5; 109 -9.8; 117 -9.7; 125 -9.3; 134 -8.6; 143 -8.0; 153 -7.2; 164 -6.9; 175 -7.7; 188 -8.2; 201 -8.2; 215 -7.8; 230 -7.4; 246 -6.5; 263 -5.8; 282 -5.1; 301 -4.3; 323 -3.1; 345 -2.1; 369 -1.3; 395 -0.5; 423 -0.0; 452 0.2; 484 0.4; 518 0.7; 554 0.9; 593 1.0; 635 1.1; 679 1.0; 726 1.0; 777 0.8; 832 0.7; 890 0.4; 952 0.2; 1019 -0.1; 1090 -0.3; 1167 -0.5; 1248 -0.7; 1336 -0.7; 1429 -0.6; 1529 -0.6; 1636 -1.1; 1751 -1.5; 1873 -1.8; 2004 -1.7; 2145 -1.3; 2295 -0.8; 2455 -0.5; 2627 -0.1; 2811 1.1; 3008 2.5; 3219 2.9; 3444 3.2; 3685 3.5; 3943 3.0; 4219 4.3; 4514 5.6; 4830 6.2; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -2.9; 8880 -7.1; 9502 -5.7; 10167 -1.3; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.7dB` and instead set Global volume in the UI for both channels to **-67**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD25-SP ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 9 Hz    | 1.5  | -7.2 dB |
| Peaking | 81 Hz   | 0.53 | -8.8 dB |
| Peaking | 210 Hz  | 2.04 | -4.6 dB |
| Peaking | 5373 Hz | 1.5  | 7.0 dB  |
| Peaking | 8992 Hz | 4.89 | -9.4 dB |
| Peaking | 87 Hz   | 4.43 | 2.5 dB  |
| Peaking | 114 Hz  | 3    | -2.1 dB |
| Peaking | 582 Hz  | 1.46 | 2.1 dB  |
| Peaking | 2027 Hz | 1.45 | -2.3 dB |
| Peaking | 3145 Hz | 3.49 | 2.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Sennheiser%20HD25-SP/Sennheiser%20HD25-SP.png)