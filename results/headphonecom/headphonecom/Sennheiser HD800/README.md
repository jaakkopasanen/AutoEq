# Sennheiser HD800

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 0.1; 22 -0.3; 23 -0.5; 25 -0.9; 26 -1.0; 28 -1.3; 30 -1.6; 32 -1.8; 35 -2.0; 37 -2.1; 40 -2.1; 42 -2.0; 45 -1.6; 49 -1.6; 52 -2.0; 56 -2.4; 59 -2.5; 64 -2.8; 68 -3.2; 73 -3.7; 78 -3.9; 83 -4.0; 89 -4.2; 95 -4.2; 102 -4.1; 109 -4.3; 117 -4.4; 125 -4.4; 134 -4.4; 143 -4.6; 153 -4.5; 164 -4.3; 175 -4.4; 188 -4.5; 201 -4.4; 215 -4.4; 230 -4.3; 246 -4.3; 263 -4.2; 282 -3.9; 301 -3.8; 323 -3.7; 345 -3.6; 369 -3.4; 395 -3.2; 423 -3.0; 452 -2.7; 484 -2.3; 518 -2.0; 554 -1.7; 593 -1.4; 635 -1.1; 679 -0.9; 726 -0.7; 777 -0.6; 832 -0.5; 890 -0.4; 952 -0.1; 1019 0.0; 1090 0.6; 1167 1.3; 1248 2.1; 1336 3.2; 1429 4.0; 1529 4.3; 1636 4.4; 1751 4.7; 1873 4.8; 2004 4.8; 2145 4.9; 2295 5.5; 2455 6.0; 2627 6.0; 2811 6.0; 3008 5.5; 3219 4.7; 3444 4.4; 3685 3.2; 3943 2.1; 4219 2.3; 4514 3.5; 4830 4.4; 5168 3.4; 5530 -0.1; 5917 -4.9; 6331 -3.7; 6775 -0.1; 7249 1.0; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD800 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 91 Hz   | 0.51 | -2.4 dB |
| Peaking | 259 Hz  | 0.41 | -3.3 dB |
| Peaking | 2304 Hz | 0.83 | 6.2 dB  |
| Peaking | 4995 Hz | 6.39 | 3.4 dB  |
| Peaking | 6030 Hz | 7.15 | -7.5 dB |
| Peaking | 1071 Hz | 3.3  | -1.1 dB |
| Peaking | 1429 Hz | 2.78 | 1.1 dB  |
| Peaking | 2130 Hz | 2.93 | -1.8 dB |
| Peaking | 2566 Hz | 1.32 | 1.1 dB  |
| Peaking | 3949 Hz | 7.7  | -1.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Sennheiser%20HD800/Sennheiser%20HD800.png)