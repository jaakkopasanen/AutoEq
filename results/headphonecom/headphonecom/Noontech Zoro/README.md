# Noontech Zoro

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -5.6; 22 -5.9; 23 -6.0; 25 -6.2; 26 -6.3; 28 -6.5; 30 -6.7; 32 -6.9; 35 -7.0; 37 -7.1; 40 -7.2; 42 -7.3; 45 -7.4; 49 -7.4; 52 -7.4; 56 -7.4; 59 -7.4; 64 -7.6; 68 -7.6; 73 -7.6; 78 -7.6; 83 -7.6; 89 -7.4; 95 -7.5; 102 -7.6; 109 -7.4; 117 -7.3; 125 -7.2; 134 -7.1; 143 -7.1; 153 -7.3; 164 -7.0; 175 -6.9; 188 -7.0; 201 -7.0; 215 -6.8; 230 -6.6; 246 -6.4; 263 -6.1; 282 -5.7; 301 -5.4; 323 -5.5; 345 -5.4; 369 -5.2; 395 -4.9; 423 -4.6; 452 -4.4; 484 -4.1; 518 -3.8; 554 -3.4; 593 -3.0; 635 -2.4; 679 -1.9; 726 -1.4; 777 -0.9; 832 -0.6; 890 -0.2; 952 -0.1; 1019 -0.0; 1090 -0.0; 1167 0.1; 1248 0.5; 1336 0.7; 1429 0.8; 1529 1.1; 1636 1.3; 1751 1.9; 1873 2.8; 2004 4.1; 2145 5.5; 2295 6.0; 2455 6.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 -0.4; 8299 -2.8; 8880 -3.2; 9502 -1.4; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noontech Zoro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 44 Hz   | 0.31 | -6.8 dB |
| Peaking | 254 Hz  | 0.48 | -4.7 dB |
| Peaking | 2630 Hz | 1.24 | 5.3 dB  |
| Peaking | 5683 Hz | 1.06 | 6.1 dB  |
| Peaking | 8535 Hz | 2.82 | -6.6 dB |
| Peaking | 527 Hz  | 2.95 | -0.7 dB |
| Peaking | 863 Hz  | 2.15 | 0.9 dB  |
| Peaking | 1875 Hz | 1.87 | -1.1 dB |
| Peaking | 2158 Hz | 5.56 | 1.8 dB  |
| Peaking | 5280 Hz | 6.97 | -0.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Noontech%20Zoro/Noontech%20Zoro.png)