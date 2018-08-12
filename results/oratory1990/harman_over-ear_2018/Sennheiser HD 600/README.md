# Sennheiser HD 600

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 5.8; 30 5.5; 32 5.1; 35 4.6; 37 4.3; 40 3.9; 42 3.7; 45 3.3; 49 3.0; 52 3.0; 56 2.9; 59 2.7; 64 2.4; 68 2.0; 73 1.4; 78 1.1; 83 0.8; 89 0.5; 95 0.0; 102 -0.4; 109 -0.6; 117 -0.9; 125 -1.1; 134 -1.2; 143 -1.3; 153 -1.4; 164 -1.4; 175 -1.4; 188 -1.3; 201 -1.3; 215 -1.3; 230 -1.2; 246 -1.1; 263 -0.9; 282 -0.7; 301 -0.5; 323 -0.3; 345 -0.1; 369 0.1; 395 0.3; 423 0.4; 452 0.4; 484 0.5; 518 0.6; 554 0.7; 593 0.7; 635 0.8; 679 0.8; 726 0.8; 777 0.9; 832 1.1; 890 0.6; 952 0.2; 1019 -0.1; 1090 -0.2; 1167 -0.4; 1248 -0.6; 1336 -0.7; 1429 -0.5; 1529 -0.3; 1636 -0.0; 1751 -0.1; 1873 -0.3; 2004 -0.0; 2145 0.2; 2295 0.2; 2455 -0.2; 2627 -0.8; 2811 -1.4; 3008 -1.8; 3219 -2.0; 3444 -1.6; 3685 -0.2; 3943 1.6; 4219 3.0; 4514 2.1; 4830 0.5; 5168 0.0; 5530 -1.1; 5917 -2.2; 6331 0.1; 6775 1.8; 7249 1.2; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 -0.9; 12455 -4.5; 13327 -6.1; 14260 -4.6; 15258 -3.1; 16326 -4.5; 17469 -7.4; 18692 -8.5; 20000 -6.3
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.2dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 25 Hz    | 1.27 | 6.5 dB  |
| Peaking | 54 Hz    | 2.8  | 2.0 dB  |
| Peaking | 13216 Hz | 3.06 | -7.6 dB |
| Peaking | 13304 Hz | 0.88 | 3.6 dB  |
| Peaking | 165 Hz   | 1.48 | -1.8 dB |
| Peaking | 3224 Hz  | 3.58 | -2.6 dB |
| Peaking | 4227 Hz  | 5.16 | 3.5 dB  |
| Peaking | 5809 Hz  | 9.62 | -2.6 dB |
| Peaking | 18505 Hz | 1    | -9.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sennheiser%20HD%20600/Sennheiser%20HD%20600.png)