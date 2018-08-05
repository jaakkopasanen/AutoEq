# Sennheiser Momentum In-Ear

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -6.8; 22 -6.8; 23 -6.8; 25 -6.8; 26 -6.8; 28 -6.9; 30 -6.9; 32 -6.9; 35 -6.9; 37 -6.9; 40 -6.8; 42 -6.8; 45 -6.8; 49 -6.7; 52 -6.7; 56 -6.6; 59 -6.5; 64 -6.5; 68 -6.4; 73 -6.4; 78 -6.5; 83 -6.6; 89 -6.8; 95 -7.1; 102 -7.4; 109 -7.6; 117 -7.9; 125 -8.3; 134 -8.5; 143 -8.5; 153 -8.5; 164 -8.4; 175 -8.1; 188 -7.8; 201 -7.5; 215 -7.1; 230 -6.7; 246 -6.3; 263 -6.0; 282 -5.5; 301 -5.1; 323 -4.6; 345 -4.2; 369 -3.8; 395 -3.4; 423 -2.8; 452 -2.3; 484 -2.1; 518 -1.7; 554 -1.2; 593 -0.7; 635 -0.3; 679 -0.2; 726 0.1; 777 0.4; 832 0.4; 890 0.3; 952 0.2; 1019 -0.1; 1090 -0.2; 1167 -0.4; 1248 -0.6; 1336 -1.0; 1429 -1.3; 1529 -1.7; 1636 -1.8; 1751 -1.8; 1873 -1.5; 2004 -1.1; 2145 -0.7; 2295 -0.0; 2455 1.1; 2627 2.0; 2811 3.1; 3008 4.6; 3219 5.6; 3444 6.0; 3685 6.0; 3943 5.3; 4219 3.5; 4514 2.0; 4830 1.2; 5168 0.9; 5530 -0.3; 5917 -2.5; 6331 -5.1; 6775 -4.9; 7249 -3.1; 7756 -1.4; 8299 -0.2; 8880 0.0; 9502 0.0; 10167 -0.3; 10879 -1.9; 11640 -3.0; 12455 -3.4; 13327 -3.5; 14260 -1.9; 15258 -0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum In-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 24 Hz    | 0.32 | -6.5 dB |
| Peaking | 169 Hz   | 0.68 | -7.2 dB |
| Peaking | 3549 Hz  | 2.69 | 7.0 dB  |
| Peaking | 6553 Hz  | 4.92 | -6.2 dB |
| Peaking | 12682 Hz | 3.02 | -3.9 dB |
| Peaking | 361 Hz   | 2.15 | -0.6 dB |
| Peaking | 787 Hz   | 1.45 | 1.4 dB  |
| Peaking | 1723 Hz  | 1.83 | -2.3 dB |
| Peaking | 2895 Hz  | 5.03 | 1.4 dB  |
| Peaking | 15536 Hz | 5.1  | 0.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20Momentum%20In-Ear/Sennheiser%20Momentum%20In-Ear.png)