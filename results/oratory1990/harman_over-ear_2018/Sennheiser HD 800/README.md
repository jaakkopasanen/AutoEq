# Sennheiser HD 800

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 5.9; 26 5.8; 28 5.5; 30 5.3; 32 5.0; 35 4.7; 37 4.5; 40 4.2; 42 4.0; 45 3.8; 49 3.7; 52 3.7; 56 3.9; 59 3.9; 64 3.7; 68 3.3; 73 2.6; 78 2.1; 83 1.7; 89 1.3; 95 0.9; 102 0.5; 109 0.1; 117 -0.2; 125 -0.5; 134 -0.7; 143 -1.0; 153 -1.2; 164 -1.3; 175 -1.4; 188 -1.6; 201 -1.7; 215 -1.7; 230 -1.8; 246 -1.7; 263 -1.7; 282 -1.5; 301 -1.4; 323 -1.3; 345 -1.1; 369 -1.0; 395 -0.9; 423 -0.9; 452 -0.9; 484 -0.8; 518 -0.7; 554 -0.6; 593 -0.6; 635 -0.5; 679 -0.4; 726 -0.4; 777 -0.3; 832 -0.3; 890 -0.2; 952 -0.1; 1019 0.0; 1090 0.1; 1167 0.4; 1248 0.8; 1336 1.4; 1429 1.9; 1529 2.2; 1636 2.5; 1751 2.5; 1873 2.5; 2004 2.7; 2145 2.6; 2295 2.1; 2455 1.1; 2627 0.4; 2811 0.2; 3008 0.1; 3219 0.7; 3444 1.2; 3685 1.1; 3943 0.5; 4219 -0.3; 4514 -1.4; 4830 -2.6; 5168 -4.8; 5530 -7.6; 5917 -7.8; 6331 -4.7; 6775 -2.2; 7249 -2.9; 7756 -3.4; 8299 -1.1; 8880 0.0; 9502 0.0; 10167 0.0; 10879 -3.0; 11640 -5.8; 12455 -6.7; 13327 -6.3; 14260 -5.1; 15258 -3.7; 16326 -3.1; 17469 -3.7; 18692 -5.4; 20000 -8.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 800 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.9dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 1.12 | 6.2 dB  |
| Peaking | 60 Hz    | 2.61 | 3.1 dB  |
| Peaking | 1910 Hz  | 1.77 | 3.0 dB  |
| Peaking | 5722 Hz  | 5.13 | -8.0 dB |
| Peaking | 21242 Hz | 0.17 | -6.2 dB |
| Peaking | 241 Hz   | 0.85 | -1.9 dB |
| Peaking | 3692 Hz  | 5.38 | 1.8 dB  |
| Peaking | 9894 Hz  | 2.7  | 6.4 dB  |
| Peaking | 11949 Hz | 1.28 | -5.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sennheiser%20HD%20800/Sennheiser%20HD%20800.png)