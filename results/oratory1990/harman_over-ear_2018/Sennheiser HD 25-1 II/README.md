# Sennheiser HD 25-1 II

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 5.2; 78 4.1; 83 3.4; 89 2.7; 95 1.9; 102 1.1; 109 0.6; 117 0.2; 125 0.2; 134 0.4; 143 0.2; 153 -0.1; 164 -0.0; 175 -0.1; 188 -0.3; 201 -0.3; 215 -0.5; 230 -0.6; 246 -0.6; 263 -0.6; 282 -0.5; 301 -0.3; 323 -0.1; 345 0.2; 369 0.6; 395 1.1; 423 1.4; 452 1.4; 484 1.6; 518 1.9; 554 2.1; 593 2.1; 635 2.1; 679 2.0; 726 1.7; 777 1.3; 832 0.8; 890 0.4; 952 0.2; 1019 -0.1; 1090 -0.6; 1167 0.1; 1248 0.9; 1336 0.6; 1429 0.4; 1529 0.3; 1636 0.0; 1751 -0.2; 1873 -0.6; 2004 -0.8; 2145 -1.0; 2295 -1.2; 2455 -1.3; 2627 -1.3; 2811 -1.2; 3008 -0.9; 3219 -0.1; 3444 0.7; 3685 1.2; 3943 1.6; 4219 5.4; 4514 5.6; 4830 3.9; 5168 2.9; 5530 3.5; 5917 4.5; 6331 0.2; 6775 -2.6; 7249 -3.0; 7756 -4.5; 8299 -5.9; 8880 -6.1; 9502 -3.8; 10167 -0.3; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 25-1 II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.2dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 37 Hz    | 0.7  | 7.1 dB  |
| Peaking | 601 Hz   | 2.2  | 2.4 dB  |
| Peaking | 3102 Hz  | 1.3  | -4.0 dB |
| Peaking | 4562 Hz  | 1.28 | 7.1 dB  |
| Peaking | 8193 Hz  | 2.63 | -7.8 dB |
| Peaking | 39 Hz    | 2.95 | -1.1 dB |
| Peaking | 68 Hz    | 2.39 | 2.8 dB  |
| Peaking | 136 Hz   | 0.76 | -1.3 dB |
| Peaking | 1335 Hz  | 6.6  | 0.8 dB  |
| Peaking | 10564 Hz | 7.42 | 1.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sennheiser%20HD%2025-1%20II/Sennheiser%20HD%2025-1%20II.png)