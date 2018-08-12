# Sennheiser HD 540 reference-II

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 5.9; 26 5.8; 28 5.3; 30 4.8; 32 4.4; 35 3.8; 37 3.5; 40 3.1; 42 2.8; 45 2.5; 49 2.1; 52 1.8; 56 1.4; 59 1.2; 64 1.1; 68 1.0; 73 0.5; 78 -0.3; 83 -1.1; 89 -1.9; 95 -2.4; 102 -2.9; 109 -3.3; 117 -3.8; 125 -4.2; 134 -4.5; 143 -4.7; 153 -4.9; 164 -5.1; 175 -5.2; 188 -5.3; 201 -5.4; 215 -5.4; 230 -5.4; 246 -5.3; 263 -5.2; 282 -5.0; 301 -4.8; 323 -4.6; 345 -4.4; 369 -4.2; 395 -4.0; 423 -3.8; 452 -3.7; 484 -3.5; 518 -3.3; 554 -3.0; 593 -2.8; 635 -2.6; 679 -2.3; 726 -2.2; 777 -2.0; 832 -1.8; 890 -0.7; 952 0.2; 1019 0.0; 1090 -0.1; 1167 -0.2; 1248 0.0; 1336 0.5; 1429 0.9; 1529 1.4; 1636 1.9; 1751 2.2; 1873 2.2; 2004 2.0; 2145 1.4; 2295 0.7; 2455 0.1; 2627 -0.5; 2811 -1.0; 3008 -1.1; 3219 -0.6; 3444 0.4; 3685 1.0; 3943 -0.8; 4219 -1.3; 4514 -1.7; 4830 -4.2; 5168 -4.1; 5530 -0.5; 5917 -5.1; 6331 -6.0; 6775 -2.4; 7249 -1.3; 7756 -2.4; 8299 -2.6; 8880 -0.4; 9502 0.0; 10167 0.0; 10879 -0.5; 11640 -5.4; 12455 -9.3; 13327 -9.3; 14260 -5.9; 15258 -2.5; 16326 -2.1; 17469 -4.3; 18692 -6.4; 20000 -6.7
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 540 reference-II ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.4dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 15 Hz    | 0.16 | 6.5 dB   |
| Peaking | 172 Hz   | 0.38 | -6.7 dB  |
| Peaking | 1735 Hz  | 2.21 | 2.9 dB   |
| Peaking | 6017 Hz  | 2.62 | -4.4 dB  |
| Peaking | 13043 Hz | 2.94 | -10.2 dB |
| Peaking | 995 Hz   | 4.88 | 1.5 dB   |
| Peaking | 1695 Hz  | 0.38 | -0.4 dB  |
| Peaking | 1998 Hz  | 5.35 | 0.9 dB   |
| Peaking | 10270 Hz | 4.38 | 3.0 dB   |
| Peaking | 19243 Hz | 1.7  | -7.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sennheiser%20HD%20540%20reference-II/Sennheiser%20HD%20540%20reference-II.png)