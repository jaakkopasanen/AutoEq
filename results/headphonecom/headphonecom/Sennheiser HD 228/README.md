# Sennheiser HD 228

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -6.7; 22 -7.2; 23 -7.4; 25 -7.8; 26 -8.0; 28 -8.3; 30 -8.6; 32 -8.8; 35 -9.2; 37 -9.4; 40 -9.6; 42 -9.8; 45 -10.0; 49 -10.2; 52 -10.3; 56 -10.4; 59 -10.5; 64 -10.7; 68 -10.8; 73 -11.0; 78 -11.0; 83 -11.0; 89 -10.5; 95 -10.0; 102 -9.8; 109 -9.6; 117 -10.4; 125 -11.1; 134 -11.4; 143 -11.4; 153 -11.2; 164 -10.5; 175 -10.0; 188 -9.3; 201 -8.0; 215 -6.5; 230 -5.8; 246 -7.0; 263 -7.4; 282 -6.4; 301 -6.0; 323 -5.5; 345 -4.9; 369 -4.5; 395 -3.9; 423 -3.1; 452 -2.1; 484 -1.4; 518 -0.8; 554 -0.1; 593 0.3; 635 0.7; 679 0.9; 726 0.9; 777 0.7; 832 0.5; 890 0.4; 952 0.2; 1019 0.0; 1090 0.2; 1167 0.7; 1248 1.4; 1336 2.2; 1429 3.3; 1529 3.6; 1636 2.8; 1751 3.3; 1873 3.6; 2004 3.8; 2145 4.4; 2295 4.8; 2455 5.4; 2627 5.8; 2811 5.6; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 5.9; 4219 3.4; 4514 2.2; 4830 1.8; 5168 4.2; 5530 5.9; 5917 5.6; 6331 3.6; 6775 3.2; 7249 1.2; 7756 0.2; 8299 -0.4; 8880 -0.2; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 228 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 29 Hz   | 0.59 | -6.5 dB |
| Peaking | 71 Hz   | 0.81 | -7.0 dB |
| Peaking | 153 Hz  | 1.43 | -7.8 dB |
| Peaking | 303 Hz  | 1.82 | -4.2 dB |
| Peaking | 3036 Hz | 0.72 | 6.0 dB  |
| Peaking | 659 Hz  | 3.62 | 1.3 dB  |
| Peaking | 1043 Hz | 5.06 | -1.3 dB |
| Peaking | 4741 Hz | 4.96 | -5.4 dB |
| Peaking | 5575 Hz | 2    | 5.1 dB  |
| Peaking | 7907 Hz | 1.57 | -2.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Sennheiser%20HD%20228/Sennheiser%20HD%20228.png)