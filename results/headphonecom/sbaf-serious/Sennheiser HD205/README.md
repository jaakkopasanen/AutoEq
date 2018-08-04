# Sennheiser HD205

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 6.0; 22 5.9; 23 5.8; 25 5.6; 26 5.4; 28 5.2; 30 4.9; 32 4.7; 35 4.3; 37 4.0; 40 3.8; 42 3.7; 45 3.6; 49 3.3; 52 2.9; 56 2.4; 59 2.3; 64 2.4; 68 2.5; 73 2.5; 78 1.9; 83 1.5; 89 1.1; 95 0.6; 102 0.2; 109 -0.1; 117 -0.4; 125 -0.8; 134 -0.8; 143 -0.2; 153 0.5; 164 0.1; 175 -0.3; 188 -0.3; 201 -0.1; 215 0.7; 230 0.9; 246 0.6; 263 0.6; 282 0.9; 301 1.2; 323 1.6; 345 2.2; 369 3.0; 395 3.8; 423 4.3; 452 3.9; 484 2.5; 518 1.2; 554 0.5; 593 0.8; 635 1.8; 679 3.5; 726 4.4; 777 3.9; 832 2.6; 890 1.3; 952 0.4; 1019 -0.2; 1090 -0.7; 1167 -1.0; 1248 -1.2; 1336 -1.6; 1429 -1.9; 1529 -2.2; 1636 -2.3; 1751 -2.2; 1873 -1.7; 2004 -1.3; 2145 -0.6; 2295 0.2; 2455 1.3; 2627 2.5; 2811 3.3; 3008 3.7; 3219 4.0; 3444 5.1; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 2.3; 5168 0.0; 5530 2.7; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD205 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 0.64 | 5.7 dB  |
| Peaking | 413 Hz   | 3.52 | 4.4 dB  |
| Peaking | 736 Hz   | 5.7  | 4.5 dB  |
| Peaking | 4015 Hz  | 1.85 | 6.3 dB  |
| Peaking | 24000 Hz | 2.37 | 3.0 dB  |
| Peaking | 126 Hz   | 4.55 | -1.4 dB |
| Peaking | 1673 Hz  | 1.79 | -3.1 dB |
| Peaking | 2809 Hz  | 3.72 | 1.7 dB  |
| Peaking | 5165 Hz  | 8.96 | -4.6 dB |
| Peaking | 6149 Hz  | 5.25 | 5.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20HD205/Sennheiser%20HD205.png)