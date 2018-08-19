# Sennheiser HD 650

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 5.9; 37 5.7; 40 5.3; 42 5.1; 45 5.0; 49 4.8; 52 4.6; 56 4.3; 59 4.1; 64 3.8; 68 3.2; 73 2.5; 78 1.9; 83 1.5; 89 0.9; 95 0.4; 102 -0.0; 109 -0.4; 117 -0.7; 125 -0.9; 134 -1.2; 143 -1.5; 153 -1.6; 164 -1.7; 175 -1.7; 188 -1.8; 201 -1.9; 215 -1.8; 230 -1.8; 246 -1.6; 263 -1.5; 282 -1.3; 301 -1.2; 323 -1.0; 345 -0.9; 369 -0.7; 395 -0.6; 423 -0.4; 452 -0.4; 484 -0.3; 518 -0.1; 554 0.1; 593 0.2; 635 0.2; 679 0.2; 726 0.2; 777 0.1; 832 0.1; 890 0.1; 952 0.2; 1019 -0.0; 1090 -0.1; 1167 0.0; 1248 0.2; 1336 0.4; 1429 0.7; 1529 1.0; 1636 1.2; 1751 1.5; 1873 1.8; 2004 2.0; 2145 2.3; 2295 2.1; 2455 1.6; 2627 1.0; 2811 0.5; 3008 0.2; 3219 0.3; 3444 1.0; 3685 1.8; 3943 2.9; 4219 4.2; 4514 3.7; 4830 2.1; 5168 1.7; 5530 3.3; 5917 3.8; 6331 3.0; 6775 3.0; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 -0.2; 14260 -1.6; 15258 -2.7; 16326 -4.6; 17469 -6.5; 18692 -7.1; 20000 -5.8
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 650 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 31 Hz    |  0.92 | 6.8 dB  |
| Peaking | 2021 Hz  |  3.03 | 2.0 dB  |
| Peaking | 5266 Hz  |  1.32 | 3.4 dB  |
| Peaking | 18571 Hz |  1.18 | -7.8 dB |
| Peaking | 24000 Hz |  1.76 | 2.0 dB  |
| Peaking | 63 Hz    |  2.36 | 2.0 dB  |
| Peaking | 180 Hz   |  0.89 | -2.3 dB |
| Peaking | 3118 Hz  |  5.69 | -1.2 dB |
| Peaking | 4185 Hz  | 10.68 | 2.1 dB  |
| Peaking | 12954 Hz |  5.34 | 1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/oratory1990/harman_over-ear_2018/Sennheiser%20HD%20650/Sennheiser%20HD%20650.png)