# Sennheiser HD 219

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 10 -84; 20 4.3; 22 3.6; 23 3.2; 25 2.6; 26 2.3; 28 1.7; 30 1.2; 32 0.8; 35 0.1; 37 -0.3; 40 -0.8; 42 -1.1; 45 -1.5; 49 -2.0; 52 -2.3; 56 -2.6; 59 -2.8; 64 -3.1; 68 -3.3; 73 -3.5; 78 -3.6; 83 -3.8; 89 -4.0; 95 -4.3; 102 -4.5; 109 -4.7; 117 -4.9; 125 -4.8; 134 -4.7; 143 -4.4; 153 -4.2; 164 -4.4; 175 -3.9; 188 -3.9; 201 -3.3; 215 -2.5; 230 -2.2; 246 -2.1; 263 -1.9; 282 -1.2; 301 -0.2; 323 0.6; 345 1.3; 369 1.7; 395 1.9; 423 2.1; 452 2.2; 484 1.9; 518 1.6; 554 1.6; 593 1.5; 635 1.3; 679 1.3; 726 1.7; 777 1.8; 832 1.2; 890 0.6; 952 0.2; 1019 -0.1; 1090 -0.2; 1167 -0.1; 1248 0.1; 1336 0.2; 1429 0.3; 1529 0.8; 1636 0.2; 1751 -1.2; 1873 -1.1; 2004 -0.8; 2145 -0.4; 2295 -0.1; 2455 0.5; 2627 0.5; 2811 0.5; 3008 0.6; 3219 0.5; 3444 0.6; 3685 0.5; 3943 0.2; 4219 -1.3; 4514 -1.7; 4830 -0.4; 5168 2.2; 5530 3.9; 5917 5.3; 6331 5.4; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -1.3; 8880 -1.6; 9502 -0.1; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -0.2; 20000 -2.2
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.0dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 219 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 18 Hz    | 1    | 5.0 dB  |
| Peaking | 103 Hz   | 0.43 | -2.1 dB |
| Peaking | 188 Hz   | 0.34 | -3.8 dB |
| Peaking | 412 Hz   | 0.83 | 5.5 dB  |
| Peaking | 6127 Hz  | 4.99 | 6.3 dB  |
| Peaking | 268 Hz   | 7.27 | -0.6 dB |
| Peaking | 1880 Hz  | 6.42 | -1.5 dB |
| Peaking | 4415 Hz  | 5.41 | -4.2 dB |
| Peaking | 4379 Hz  | 1.93 | 1.6 dB  |
| Peaking | 20067 Hz | 3.26 | -2.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20219/Sennheiser%20HD%20219.png)