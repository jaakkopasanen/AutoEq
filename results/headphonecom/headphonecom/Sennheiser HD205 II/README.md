# Sennheiser HD205 II

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -4.8; 22 -5.0; 23 -5.1; 25 -5.2; 26 -5.2; 28 -5.2; 30 -5.2; 32 -5.2; 35 -5.5; 37 -5.7; 40 -5.8; 42 -5.9; 45 -6.0; 49 -6.1; 52 -6.1; 56 -6.0; 59 -5.8; 64 -5.2; 68 -5.3; 73 -5.9; 78 -6.4; 83 -6.7; 89 -6.7; 95 -6.8; 102 -6.7; 109 -6.7; 117 -6.5; 125 -6.1; 134 -5.5; 143 -4.6; 153 -4.8; 164 -4.7; 175 -4.7; 188 -4.6; 201 -4.3; 215 -4.2; 230 -4.3; 246 -3.9; 263 -3.8; 282 -3.5; 301 -3.1; 323 -2.2; 345 -1.2; 369 -0.2; 395 0.8; 423 1.4; 452 1.3; 484 0.7; 518 -0.1; 554 -0.5; 593 -0.2; 635 1.1; 679 3.2; 726 4.3; 777 4.1; 832 2.8; 890 1.5; 952 0.5; 1019 -0.2; 1090 -0.7; 1167 -1.1; 1248 -0.9; 1336 -0.6; 1429 0.1; 1529 0.3; 1636 0.4; 1751 0.9; 1873 1.3; 2004 1.7; 2145 2.3; 2295 3.4; 2455 4.5; 2627 5.7; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD205 II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 5 Hz    | 1.56 | -4.3 dB |
| Peaking | 28 Hz   | 0.41 | -4.5 dB |
| Peaking | 119 Hz  | 0.58 | -5.0 dB |
| Peaking | 747 Hz  | 4.81 | 5.0 dB  |
| Peaking | 3988 Hz | 1    | 7.0 dB  |
| Peaking | 429 Hz  | 4.93 | 2.9 dB  |
| Peaking | 3536 Hz | 0.41 | -2.9 dB |
| Peaking | 2696 Hz | 2.04 | 4.2 dB  |
| Peaking | 6200 Hz | 1.97 | 5.4 dB  |
| Peaking | 7633 Hz | 2.7  | -3.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Sennheiser%20HD205%20II/Sennheiser%20HD205%20II.png)