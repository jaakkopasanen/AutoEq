# Sennheiser HD 800 S

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.3dB
GraphicEQ: 10 -84; 20 6.2; 22 5.7; 23 5.6; 25 5.2; 26 5.1; 28 4.8; 30 4.6; 32 4.4; 35 4.2; 37 4.0; 40 3.8; 42 3.8; 45 3.7; 49 3.6; 52 3.5; 56 3.5; 59 3.5; 64 3.3; 68 3.0; 73 2.6; 78 2.1; 83 1.6; 89 1.2; 95 0.8; 102 0.3; 109 -0.0; 117 -0.3; 125 -0.6; 134 -0.8; 143 -1.0; 153 -1.2; 164 -1.4; 175 -1.5; 188 -1.6; 201 -1.7; 215 -1.7; 230 -1.7; 246 -1.7; 263 -1.6; 282 -1.5; 301 -1.3; 323 -1.1; 345 -1.0; 369 -0.9; 395 -0.8; 423 -0.7; 452 -0.7; 484 -0.6; 518 -0.5; 554 -0.4; 593 -0.3; 635 -0.2; 679 -0.2; 726 -0.1; 777 -0.1; 832 -0.2; 890 -0.1; 952 -0.0; 1019 0.1; 1090 0.3; 1167 0.7; 1248 1.3; 1336 1.9; 1429 2.3; 1529 2.4; 1636 2.4; 1751 2.3; 1873 2.2; 2004 2.3; 2145 2.3; 2295 2.0; 2455 1.5; 2627 1.1; 2811 1.0; 3008 1.4; 3219 2.1; 3444 2.3; 3685 1.6; 3943 0.7; 4219 0.8; 4514 0.7; 4830 -0.5; 5168 -2.9; 5530 -4.6; 5917 -3.5; 6331 -2.4; 6775 -1.0; 7249 -1.3; 7756 -0.4; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 -3.3; 11640 -6.4; 12455 -7.2; 13327 -6.2; 14260 -4.7; 15258 -4.1; 16326 -5.0; 17469 -6.6; 18692 -7.4; 20000 -7.2
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.261415938776109dB` and instead set Global volume in the UI for both channels to **-62**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 800 S ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.1dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 1.08 | 5.7 dB  |
| Peaking | 58 Hz    | 2.38 | 2.9 dB  |
| Peaking | 5627 Hz  | 6.91 | -4.8 dB |
| Peaking | 12467 Hz | 3.58 | -6.5 dB |
| Peaking | 18847 Hz | 0.98 | -7.9 dB |
| Peaking | 213 Hz   | 1.16 | -1.9 dB |
| Peaking | 1711 Hz  | 1.17 | 3.8 dB  |
| Peaking | 3449 Hz  | 0.22 | -1.7 dB |
| Peaking | 3600 Hz  | 1.69 | 2.9 dB  |
| Peaking | 9350 Hz  | 2.51 | 2.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sennheiser%20HD%20800%20S/Sennheiser%20HD%20800%20S.png)