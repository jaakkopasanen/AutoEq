# Sennheiser RS 220

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 5.9; 26 5.8; 28 5.5; 30 5.2; 32 4.8; 35 4.4; 37 4.1; 40 3.8; 42 3.5; 45 3.3; 49 3.0; 52 2.8; 56 2.5; 59 2.2; 64 2.2; 68 2.8; 73 2.9; 78 1.9; 83 1.2; 89 0.8; 95 0.3; 102 -0.1; 109 -0.5; 117 -0.8; 125 -1.2; 134 -1.5; 143 -1.8; 153 -1.8; 164 -1.7; 175 -1.8; 188 -1.9; 201 -1.9; 215 -1.7; 230 -1.3; 246 -1.1; 263 -1.0; 282 -0.9; 301 -0.8; 323 -0.8; 345 -0.6; 369 -0.4; 395 -0.5; 423 -0.4; 452 -0.3; 484 -0.2; 518 0.0; 554 0.3; 593 0.4; 635 0.5; 679 0.3; 726 0.3; 777 0.5; 832 0.4; 890 0.3; 952 0.2; 1019 -0.1; 1090 0.2; 1167 -0.2; 1248 -0.3; 1336 0.3; 1429 2.1; 1529 3.8; 1636 4.3; 1751 4.2; 1873 4.0; 2004 2.4; 2145 -0.3; 2295 -2.8; 2455 -3.8; 2627 -3.3; 2811 -1.7; 3008 -0.5; 3219 0.1; 3444 1.2; 3685 3.6; 3943 5.8; 4219 6.0; 4514 6.0; 4830 6.0; 5168 5.2; 5530 2.2; 5917 2.9; 6331 5.5; 6775 2.2; 7249 -0.6; 7756 -0.5; 8299 0.0; 8880 0.0; 9502 -0.3; 10167 -1.2; 10879 -0.4; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser RS 220 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 1.11 | 6.3 dB  |
| Peaking | 70 Hz   | 5.36 | 2.3 dB  |
| Peaking | 1807 Hz | 2.73 | 6.9 dB  |
| Peaking | 2445 Hz | 1.95 | -6.4 dB |
| Peaking | 4405 Hz | 1.91 | 7.3 dB  |
| Peaking | 84 Hz   | 0.74 | 1.6 dB  |
| Peaking | 150 Hz  | 0.79 | -2.8 dB |
| Peaking | 630 Hz  | 3.03 | 0.6 dB  |
| Peaking | 6428 Hz | 8.35 | 5.9 dB  |
| Peaking | 6950 Hz | 2.23 | -2.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20RS%20220/Sennheiser%20RS%20220.png)