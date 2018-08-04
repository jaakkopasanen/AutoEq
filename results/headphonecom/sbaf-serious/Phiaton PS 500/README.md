# Phiaton PS 500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 5.9; 30 5.5; 32 4.9; 35 4.1; 37 3.9; 40 3.8; 42 3.6; 45 2.8; 49 1.8; 52 1.9; 56 2.4; 59 2.6; 64 1.8; 68 1.0; 73 0.3; 78 -0.2; 83 -0.6; 89 -1.0; 95 -1.5; 102 -1.8; 109 -2.2; 117 -2.7; 125 -3.1; 134 -3.4; 143 -3.6; 153 -3.7; 164 -3.3; 175 -3.6; 188 -3.6; 201 -3.3; 215 -3.2; 230 -2.8; 246 -2.2; 263 -1.5; 282 -0.4; 301 0.8; 323 1.8; 345 2.5; 369 2.8; 395 2.8; 423 2.8; 452 2.6; 484 2.3; 518 2.1; 554 2.1; 593 2.2; 635 1.9; 679 1.6; 726 1.2; 777 1.0; 832 1.4; 890 1.3; 952 0.4; 1019 -0.1; 1090 -0.4; 1167 -0.7; 1248 -0.7; 1336 -0.7; 1429 -0.5; 1529 -0.5; 1636 -1.0; 1751 -1.7; 1873 -2.1; 2004 -1.2; 2145 0.2; 2295 2.1; 2455 4.6; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 4.8; 4514 5.7; 4830 6.0; 5168 6.0; 5530 5.9; 5917 4.4; 6331 3.0; 6775 2.6; 7249 1.3; 7756 0.2; 8299 -0.8; 8880 -1.2; 9502 -0.3; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 -1.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton PS 500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 31 Hz   | 0.37 | 7.7 dB   |
| Peaking | 368 Hz  | 0.16 | -11.1 dB |
| Peaking | 501 Hz  | 0.49 | 13.6 dB  |
| Peaking | 2998 Hz | 1.72 | 8.3 dB   |
| Peaking | 5077 Hz | 2.15 | 6.0 dB   |
| Peaking | 380 Hz  | 0.88 | -3.7 dB  |
| Peaking | 352 Hz  | 2.04 | 4.8 dB   |
| Peaking | 1905 Hz | 5.21 | -2.8 dB  |
| Peaking | 1095 Hz | 0.46 | 1.1 dB   |
| Peaking | 8664 Hz | 5.33 | -2.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Phiaton%20PS%20500/Phiaton%20PS%20500.png)