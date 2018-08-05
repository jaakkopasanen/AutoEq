# Sennheiser IE 6

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 10 -84; 20 -3.1; 22 -3.5; 23 -3.7; 25 -4.0; 26 -4.1; 28 -4.3; 30 -4.5; 32 -4.6; 35 -4.9; 37 -5.0; 40 -5.2; 42 -5.3; 45 -5.4; 49 -5.5; 52 -5.6; 56 -5.7; 59 -5.7; 64 -5.7; 68 -5.9; 73 -6.0; 78 -6.1; 83 -6.4; 89 -6.7; 95 -7.0; 102 -7.5; 109 -7.8; 117 -8.2; 125 -8.7; 134 -9.0; 143 -9.2; 153 -9.2; 164 -9.2; 175 -9.0; 188 -8.8; 201 -8.6; 215 -8.2; 230 -7.8; 246 -7.5; 263 -7.2; 282 -6.7; 301 -6.3; 323 -5.9; 345 -5.4; 369 -5.0; 395 -4.5; 423 -4.0; 452 -3.5; 484 -3.1; 518 -2.7; 554 -2.1; 593 -1.5; 635 -1.0; 679 -0.8; 726 -0.4; 777 0.0; 832 0.1; 890 0.2; 952 0.1; 1019 0.0; 1090 -0.0; 1167 0.0; 1248 -0.2; 1336 -0.5; 1429 -0.7; 1529 -0.7; 1636 -1.0; 1751 -1.2; 1873 -1.2; 2004 -1.1; 2145 -1.2; 2295 -1.3; 2455 -1.1; 2627 -1.3; 2811 -1.1; 3008 -0.5; 3219 -0.1; 3444 0.3; 3685 -0.4; 3943 -2.3; 4219 -5.8; 4514 -9.1; 4830 -9.0; 5168 -4.1; 5530 0.3; 5917 3.8; 6331 5.4; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.0dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE 6 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 3 Hz    | 1.94 | -2.2 dB  |
| Peaking | 50 Hz   | 0.24 | -4.3 dB  |
| Peaking | 188 Hz  | 0.68 | -6.6 dB  |
| Peaking | 4694 Hz | 4.86 | -11.2 dB |
| Peaking | 6264 Hz | 4.46 | 7.0 dB   |
| Peaking | 441 Hz  | 1.08 | -2.2 dB  |
| Peaking | 726 Hz  | 0.51 | 2.4 dB   |
| Peaking | 1875 Hz | 0.85 | -1.9 dB  |
| Peaking | 3477 Hz | 5.81 | 2.0 dB   |
| Peaking | 7888 Hz | 8.17 | -0.6 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20IE%206/Sennheiser%20IE%206.png)