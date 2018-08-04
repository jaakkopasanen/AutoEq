# Sennheiser HD 228

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 5.2; 22 4.5; 23 4.2; 25 3.5; 26 3.2; 28 2.6; 30 2.1; 32 1.6; 35 1.0; 37 0.6; 40 0.3; 42 -0.0; 45 -0.4; 49 -0.9; 52 -1.2; 56 -1.6; 59 -1.9; 64 -2.3; 68 -2.5; 73 -2.9; 78 -3.2; 83 -3.5; 89 -3.8; 95 -4.3; 102 -4.5; 109 -4.6; 117 -4.5; 125 -4.7; 134 -5.4; 143 -6.4; 153 -7.0; 164 -6.8; 175 -7.0; 188 -7.1; 201 -6.8; 215 -6.5; 230 -6.1; 246 -6.3; 263 -5.6; 282 -4.2; 301 -3.4; 323 -3.5; 345 -3.3; 369 -2.8; 395 -2.0; 423 -1.3; 452 -1.1; 484 -0.7; 518 -0.2; 554 0.2; 593 0.7; 635 0.8; 679 0.7; 726 0.7; 777 0.7; 832 0.4; 890 0.2; 952 0.1; 1019 0.0; 1090 0.2; 1167 0.5; 1248 0.9; 1336 1.2; 1429 1.7; 1529 1.3; 1636 0.0; 1751 0.6; 1873 1.1; 2004 1.4; 2145 1.8; 2295 2.6; 2455 3.3; 2627 3.7; 2811 4.1; 3008 5.5; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 3.1; 4830 -1.6; 5168 -2.8; 5530 -0.6; 5917 1.9; 6331 2.2; 6775 3.3; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.1; 17469 -2.9; 18692 -4.3; 20000 -1.3
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 228 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 22 Hz    | 1.77 | 5.0 dB  |
| Peaking | 167 Hz   | 0.82 | -7.2 dB |
| Peaking | 3339 Hz  | 1.78 | 6.6 dB  |
| Peaking | 16302 Hz | 2.17 | 1.9 dB  |
| Peaking | 18325 Hz | 1.68 | -5.1 dB |
| Peaking | 647 Hz   | 2.29 | 1.6 dB  |
| Peaking | 7803 Hz  | 3.1  | -1.6 dB |
| Peaking | 4255 Hz  | 6.56 | 4.0 dB  |
| Peaking | 4991 Hz  | 4.92 | -6.2 dB |
| Peaking | 6630 Hz  | 3.28 | 3.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20228/Sennheiser%20HD%20228.png)