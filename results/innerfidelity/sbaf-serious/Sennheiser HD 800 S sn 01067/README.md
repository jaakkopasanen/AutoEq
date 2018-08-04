# Sennheiser HD 800 S sn 01067

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.3dB
GraphicEQ: 10 -84; 20 4.8; 22 4.3; 23 4.0; 25 3.7; 26 3.5; 28 3.2; 30 3.0; 32 2.7; 35 2.4; 37 2.3; 40 2.1; 42 2.0; 45 1.8; 49 1.7; 52 1.7; 56 1.6; 59 1.5; 64 1.6; 68 1.7; 73 1.5; 78 1.1; 83 0.9; 89 0.7; 95 0.1; 102 -0.5; 109 -0.9; 117 -1.3; 125 -1.9; 134 -2.1; 143 -2.4; 153 -2.5; 164 -2.5; 175 -2.7; 188 -2.7; 201 -2.8; 215 -2.8; 230 -2.7; 246 -2.8; 263 -2.8; 282 -2.6; 301 -2.5; 323 -2.4; 345 -2.4; 369 -2.2; 395 -2.1; 423 -1.9; 452 -1.8; 484 -1.7; 518 -1.7; 554 -1.4; 593 -1.1; 635 -1.1; 679 -1.0; 726 -0.9; 777 -0.5; 832 -0.4; 890 -0.2; 952 -0.1; 1019 0.1; 1090 0.4; 1167 0.4; 1248 0.9; 1336 1.1; 1429 1.3; 1529 1.7; 1636 1.5; 1751 1.4; 1873 1.3; 2004 1.6; 2145 1.6; 2295 1.6; 2455 2.1; 2627 2.6; 2811 2.0; 3008 1.9; 3219 2.2; 3444 2.0; 3685 0.4; 3943 -0.3; 4219 -0.4; 4514 -0.0; 4830 0.4; 5168 -0.0; 5530 -1.3; 5917 -1.8; 6331 -3.7; 6775 -3.7; 7249 -2.3; 7756 -1.1; 8299 -0.8; 8880 -0.9; 9502 -0.2; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 -0.3; 14260 -1.3; 15258 -0.7; 16326 -0.0; 17469 0.0; 18692 0.0; 20000 -0.3
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.3dB` and instead set Global volume in the UI for both channels to **-53**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 800 S sn 01067 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 14 Hz    | 0.45 | 5.2 dB  |
| Peaking | 76 Hz    | 1.17 | 3.0 dB  |
| Peaking | 168 Hz   | 0.35 | -3.4 dB |
| Peaking | 2248 Hz  | 0.82 | 2.2 dB  |
| Peaking | 6566 Hz  | 3.44 | -4.3 dB |
| Peaking | 2150 Hz  | 2.49 | -1.4 dB |
| Peaking | 2716 Hz  | 0.98 | 1.2 dB  |
| Peaking | 4020 Hz  | 5.45 | -1.9 dB |
| Peaking | 33571 Hz | 5.38 | -1.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20800%20S%20sn%2001067/Sennheiser%20HD%20800%20S%20sn%2001067.png)