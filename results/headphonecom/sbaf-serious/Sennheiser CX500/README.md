# Sennheiser CX500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -7.0; 22 -7.1; 23 -7.1; 25 -7.1; 26 -7.1; 28 -7.0; 30 -7.0; 32 -7.0; 35 -7.0; 37 -7.0; 40 -6.9; 42 -7.0; 45 -7.0; 49 -7.0; 52 -7.0; 56 -7.0; 59 -7.0; 64 -6.9; 68 -7.0; 73 -7.1; 78 -7.2; 83 -7.3; 89 -7.4; 95 -7.8; 102 -8.2; 109 -8.6; 117 -9.0; 125 -9.5; 134 -9.8; 143 -9.9; 153 -10.1; 164 -10.0; 175 -9.8; 188 -9.7; 201 -9.5; 215 -9.2; 230 -8.8; 246 -8.5; 263 -8.2; 282 -7.8; 301 -7.4; 323 -6.9; 345 -6.4; 369 -5.8; 395 -5.4; 423 -4.9; 452 -4.6; 484 -4.3; 518 -3.8; 554 -3.1; 593 -2.5; 635 -2.0; 679 -1.7; 726 -1.2; 777 -0.6; 832 -0.4; 890 -0.2; 952 -0.1; 1019 0.0; 1090 0.1; 1167 0.1; 1248 0.2; 1336 0.2; 1429 0.0; 1529 -0.2; 1636 -0.4; 1751 -0.3; 1873 -0.0; 2004 0.3; 2145 0.7; 2295 1.4; 2455 2.2; 2627 2.9; 2811 3.8; 3008 5.0; 3219 5.8; 3444 6.0; 3685 6.0; 3943 5.4; 4219 3.3; 4514 1.5; 4830 0.1; 5168 -1.0; 5530 -3.8; 5917 -7.6; 6331 -5.2; 6775 -0.9; 7249 0.9; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.1; 10167 -0.9; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser CX500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 18 Hz   | 0.23 | -6.7 dB |
| Peaking | 186 Hz  | 0.58 | -9.0 dB |
| Peaking | 3485 Hz | 1.94 | 6.9 dB  |
| Peaking | 6012 Hz | 4.14 | -9.6 dB |
| Peaking | 6978 Hz | 4.79 | 3.2 dB  |
| Peaking | 82 Hz   | 3.49 | 0.4 dB  |
| Peaking | 211 Hz  | 3.1  | 0.7 dB  |
| Peaking | 546 Hz  | 0.78 | -1.7 dB |
| Peaking | 802 Hz  | 0.86 | 2.2 dB  |
| Peaking | 1749 Hz | 2.91 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20CX500/Sennheiser%20CX500.png)