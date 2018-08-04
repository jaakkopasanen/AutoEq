# Sennheiser RS 220

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 3.9; 22 3.2; 23 2.9; 25 2.3; 26 2.0; 28 1.6; 30 1.2; 32 0.8; 35 0.4; 37 0.1; 40 -0.2; 42 -0.4; 45 -0.7; 49 -1.0; 52 -1.2; 56 -1.5; 59 -1.7; 64 -1.7; 68 -1.1; 73 -0.9; 78 -1.8; 83 -2.2; 89 -2.4; 95 -2.5; 102 -2.5; 109 -2.5; 117 -2.4; 125 -2.4; 134 -2.4; 143 -2.3; 153 -2.2; 164 -1.9; 175 -2.0; 188 -2.0; 201 -1.9; 215 -1.7; 230 -1.3; 246 -1.2; 263 -1.0; 282 -0.9; 301 -0.8; 323 -0.8; 345 -0.6; 369 -0.4; 395 -0.5; 423 -0.4; 452 -0.3; 484 -0.2; 518 0.0; 554 0.3; 593 0.4; 635 0.5; 679 0.3; 726 0.3; 777 0.5; 832 0.4; 890 0.3; 952 0.2; 1019 -0.1; 1090 0.2; 1167 -0.2; 1248 -0.3; 1336 0.3; 1429 2.1; 1529 3.8; 1636 4.3; 1751 4.2; 1873 4.0; 2004 2.4; 2145 -0.3; 2295 -2.8; 2455 -3.8; 2627 -3.3; 2811 -1.7; 3008 -0.5; 3219 0.1; 3444 1.2; 3685 3.6; 3943 5.8; 4219 6.0; 4514 6.0; 4830 6.0; 5168 5.2; 5530 2.2; 5917 2.9; 6331 5.5; 6775 2.2; 7249 -0.6; 7756 -0.5; 8299 0.0; 8880 0.0; 9502 -0.3; 10167 -1.2; 10879 -0.4; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser RS 220 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 1.59 | 3.8 dB  |
| Peaking | 111 Hz  | 0.62 | -2.6 dB |
| Peaking | 1806 Hz | 2.65 | 6.6 dB  |
| Peaking | 2456 Hz | 2.17 | -6.4 dB |
| Peaking | 4427 Hz | 1.95 | 7.2 dB  |
| Peaking | 667 Hz  | 2.13 | 0.6 dB  |
| Peaking | 1284 Hz | 4.05 | -1.4 dB |
| Peaking | 1514 Hz | 8.29 | 1.7 dB  |
| Peaking | 6389 Hz | 8.37 | 6.0 dB  |
| Peaking | 6971 Hz | 2.22 | -2.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20RS%20220/Sennheiser%20RS%20220.png)