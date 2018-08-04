# Noontech Zoro

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -5.1; 22 -5.3; 23 -5.5; 25 -5.7; 26 -5.8; 28 -6.0; 30 -6.2; 32 -6.3; 35 -6.4; 37 -6.5; 40 -6.6; 42 -6.7; 45 -6.8; 49 -6.8; 52 -6.8; 56 -6.8; 59 -6.9; 64 -7.0; 68 -7.0; 73 -7.0; 78 -6.9; 83 -6.8; 89 -6.6; 95 -6.6; 102 -6.6; 109 -6.3; 117 -6.1; 125 -5.9; 134 -5.8; 143 -5.8; 153 -6.0; 164 -5.7; 175 -5.6; 188 -5.6; 201 -5.6; 215 -5.4; 230 -5.2; 246 -5.1; 263 -4.8; 282 -4.3; 301 -4.0; 323 -4.1; 345 -4.0; 369 -3.9; 395 -3.6; 423 -3.4; 452 -3.3; 484 -3.4; 518 -3.3; 554 -3.0; 593 -2.5; 635 -2.1; 679 -1.9; 726 -1.4; 777 -0.8; 832 -0.5; 890 -0.2; 952 -0.0; 1019 -0.0; 1090 -0.1; 1167 -0.2; 1248 -0.2; 1336 -0.6; 1429 -1.3; 1529 -1.6; 1636 -1.7; 1751 -1.2; 1873 -0.1; 2004 1.1; 2145 2.5; 2295 4.2; 2455 5.8; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.2; 6331 4.3; 6775 3.6; 7249 1.3; 7756 -1.3; 8299 -4.2; 8880 -5.1; 9502 -4.0; 10167 -1.2; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Noontech Zoro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 27 Hz    | 0.28 | -3.4 dB |
| Peaking | 147 Hz   | 0.19 | -4.9 dB |
| Peaking | 1668 Hz  | 2.03 | -6.1 dB |
| Peaking | 3389 Hz  | 0.41 | 7.6 dB  |
| Peaking | 8792 Hz  | 2.85 | -9.1 dB |
| Peaking | 299 Hz   | 7.59 | 0.5 dB  |
| Peaking | 2525 Hz  | 6.35 | 1.5 dB  |
| Peaking | 4149 Hz  | 0.96 | -0.9 dB |
| Peaking | 5702 Hz  | 2.32 | 1.6 dB  |
| Peaking | 14444 Hz | 1.56 | -0.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Noontech%20Zoro/Noontech%20Zoro.png)