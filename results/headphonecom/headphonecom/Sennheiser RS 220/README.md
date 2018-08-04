# Sennheiser RS 220

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 3.4; 22 2.7; 23 2.4; 25 1.8; 26 1.5; 28 1.0; 30 0.6; 32 0.3; 35 -0.2; 37 -0.5; 40 -0.8; 42 -1.0; 45 -1.3; 49 -1.6; 52 -1.8; 56 -2.1; 59 -2.3; 64 -2.3; 68 -1.7; 73 -1.5; 78 -2.4; 83 -2.9; 89 -3.2; 95 -3.4; 102 -3.5; 109 -3.7; 117 -3.7; 125 -3.7; 134 -3.7; 143 -3.7; 153 -3.5; 164 -3.3; 175 -3.4; 188 -3.3; 201 -3.3; 215 -3.1; 230 -2.7; 246 -2.5; 263 -2.4; 282 -2.3; 301 -2.2; 323 -2.2; 345 -2.0; 369 -1.8; 395 -1.8; 423 -1.7; 452 -1.4; 484 -0.9; 518 -0.5; 554 -0.2; 593 -0.1; 635 0.1; 679 0.3; 726 0.4; 777 0.4; 832 0.3; 890 0.3; 952 0.2; 1019 -0.1; 1090 0.3; 1167 0.1; 1248 0.4; 1336 1.7; 1429 4.2; 1529 5.9; 1636 6.0; 1751 6.0; 1873 6.0; 2004 5.3; 2145 2.7; 2295 0.2; 2455 -0.8; 2627 -0.3; 2811 1.2; 3008 2.1; 3219 2.4; 3444 3.3; 3685 5.5; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.3; 7249 0.4; 7756 0.2; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser RS 220 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 16 Hz   | 1.08 | 4.3 dB  |
| Peaking | 45 Hz   | 1.78 | -0.8 dB |
| Peaking | 140 Hz  | 0.53 | -3.7 dB |
| Peaking | 1689 Hz | 3.28 | 6.8 dB  |
| Peaking | 4832 Hz | 1.7  | 6.9 dB  |
| Peaking | 1210 Hz | 4.12 | -1.8 dB |
| Peaking | 2501 Hz | 4.01 | -4.6 dB |
| Peaking | 3453 Hz | 0.54 | 2.6 dB  |
| Peaking | 6190 Hz | 4    | 6.1 dB  |
| Peaking | 6272 Hz | 1.22 | -5.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Sennheiser%20RS%20220/Sennheiser%20RS%20220.png)