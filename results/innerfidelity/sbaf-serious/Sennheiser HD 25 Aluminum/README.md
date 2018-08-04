# Sennheiser HD 25 Aluminum

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -3.3; 22 -3.6; 23 -3.8; 25 -4.0; 26 -4.1; 28 -4.3; 30 -4.4; 32 -4.5; 35 -4.6; 37 -4.7; 40 -4.7; 42 -4.7; 45 -4.7; 49 -4.6; 52 -4.5; 56 -4.4; 59 -4.3; 64 -4.2; 68 -4.1; 73 -3.8; 78 -3.4; 83 -3.1; 89 -3.4; 95 -4.4; 102 -5.7; 109 -6.4; 117 -7.1; 125 -7.3; 134 -7.0; 143 -6.8; 153 -6.3; 164 -5.5; 175 -5.6; 188 -4.7; 201 -4.0; 215 -3.4; 230 -2.6; 246 -1.7; 263 -0.6; 282 0.3; 301 0.9; 323 1.5; 345 1.9; 369 2.3; 395 2.4; 423 2.6; 452 2.4; 484 2.0; 518 1.8; 554 1.7; 593 1.7; 635 1.5; 679 1.2; 726 1.0; 777 1.0; 832 0.7; 890 0.4; 952 0.1; 1019 -0.1; 1090 -0.3; 1167 -0.5; 1248 -0.8; 1336 -1.4; 1429 -2.1; 1529 -2.9; 1636 -3.6; 1751 -4.1; 1873 -4.4; 2004 -4.5; 2145 -4.2; 2295 -3.5; 2455 -2.4; 2627 -1.3; 2811 -0.4; 3008 0.5; 3219 0.7; 3444 0.6; 3685 0.4; 3943 0.5; 4219 1.0; 4514 3.6; 4830 5.7; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 -2.3; 8299 -5.7; 8880 -6.4; 9502 -4.1; 10167 -0.4; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 25 Aluminum ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 37 Hz    | 0.66 | -4.7 dB |
| Peaking | 135 Hz   | 1.74 | -6.9 dB |
| Peaking | 1958 Hz  | 2.3  | -5.3 dB |
| Peaking | 5817 Hz  | 1.82 | 7.4 dB  |
| Peaking | 8682 Hz  | 3.91 | -9.0 dB |
| Peaking | 209 Hz   | 2.23 | -2.7 dB |
| Peaking | 391 Hz   | 0.92 | 3.2 dB  |
| Peaking | 1508 Hz  | 4.35 | -1.0 dB |
| Peaking | 7899 Hz  | 7.56 | -1.1 dB |
| Peaking | 10466 Hz | 6.72 | 1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%2025%20Aluminum/Sennheiser%20HD%2025%20Aluminum.png)