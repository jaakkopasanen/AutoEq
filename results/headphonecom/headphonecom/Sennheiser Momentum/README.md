# Sennheiser Momentum

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -0.8; 22 -1.1; 23 -1.2; 25 -1.4; 26 -1.5; 28 -1.7; 30 -1.8; 32 -2.0; 35 -2.1; 37 -2.2; 40 -2.3; 42 -2.4; 45 -2.5; 49 -2.6; 52 -2.6; 56 -2.7; 59 -2.8; 64 -2.8; 68 -2.8; 73 -3.0; 78 -3.1; 83 -3.0; 89 -3.0; 95 -3.0; 102 -3.0; 109 -3.0; 117 -2.8; 125 -2.6; 134 -2.4; 143 -2.5; 153 -2.8; 164 -2.9; 175 -2.4; 188 -2.7; 201 -2.9; 215 -2.8; 230 -2.6; 246 -2.5; 263 -2.2; 282 -1.7; 301 -1.7; 323 -1.2; 345 -0.7; 369 -0.2; 395 0.1; 423 0.4; 452 0.6; 484 0.9; 518 1.0; 554 1.1; 593 1.2; 635 1.1; 679 0.8; 726 0.6; 777 0.4; 832 0.3; 890 0.1; 952 0.1; 1019 0.0; 1090 0.2; 1167 0.5; 1248 0.5; 1336 0.7; 1429 0.9; 1529 1.2; 1636 1.6; 1751 1.5; 1873 1.8; 2004 2.5; 2145 3.5; 2295 4.8; 2455 5.9; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 50 Hz   | 0.53 | -1.2 dB |
| Peaking | 258 Hz  | 0.17 | -2.5 dB |
| Peaking | 231 Hz  | 2.26 | -0.8 dB |
| Peaking | 520 Hz  | 1.05 | 3.3 dB  |
| Peaking | 3579 Hz | 0.78 | 7.2 dB  |
| Peaking | 1926 Hz | 4.24 | -0.9 dB |
| Peaking | 2454 Hz | 3.92 | 1.7 dB  |
| Peaking | 3595 Hz | 2.7  | -1.1 dB |
| Peaking | 6246 Hz | 2.32 | 5.3 dB  |
| Peaking | 7423 Hz | 1.48 | -4.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Sennheiser%20Momentum/Sennheiser%20Momentum.png)