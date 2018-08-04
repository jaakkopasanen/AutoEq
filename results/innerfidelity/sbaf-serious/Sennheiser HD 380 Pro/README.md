# Sennheiser HD 380 Pro

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.1dB
GraphicEQ: 10 -84; 20 -9.6; 22 -9.7; 23 -9.8; 25 -9.8; 26 -9.9; 28 -9.9; 30 -9.9; 32 -9.8; 35 -9.7; 37 -9.6; 40 -9.4; 42 -9.2; 45 -8.9; 49 -8.4; 52 -7.9; 56 -7.4; 59 -6.9; 64 -5.9; 68 -5.1; 73 -4.3; 78 -3.0; 83 -1.3; 89 0.6; 95 1.7; 102 -0.0; 109 -2.6; 117 -2.9; 125 -2.6; 134 -4.0; 143 -4.8; 153 -3.6; 164 -1.2; 175 -2.0; 188 -1.4; 201 -0.1; 215 1.0; 230 1.6; 246 1.7; 263 1.6; 282 1.2; 301 0.7; 323 -0.3; 345 -0.9; 369 -1.5; 395 -2.0; 423 -2.2; 452 -2.3; 484 -2.4; 518 -2.4; 554 -2.1; 593 -1.6; 635 -1.3; 679 -1.1; 726 -0.9; 777 -0.5; 832 -0.4; 890 -0.1; 952 -0.1; 1019 0.0; 1090 0.1; 1167 0.4; 1248 0.4; 1336 0.4; 1429 0.3; 1529 0.0; 1636 -0.5; 1751 -1.6; 1873 -3.2; 2004 -4.0; 2145 -4.5; 2295 -4.0; 2455 -3.9; 2627 -2.5; 2811 -0.8; 3008 0.9; 3219 1.9; 3444 1.2; 3685 -1.0; 3943 -1.9; 4219 -2.8; 4514 -1.6; 4830 1.0; 5168 3.6; 5530 4.5; 5917 3.5; 6331 2.8; 6775 1.2; 7249 0.7; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.2; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -0.2; 20000 -0.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.1dB` and instead set Global volume in the UI for both channels to **-51**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 380 Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 31 Hz   | 0.8  | -11.0 dB |
| Peaking | 142 Hz  | 6.7  | -4.1 dB  |
| Peaking | 494 Hz  | 2.9  | -2.7 dB  |
| Peaking | 2179 Hz | 3.53 | -5.0 dB  |
| Peaking | 5652 Hz | 5.2  | 5.0 dB   |
| Peaking | 84 Hz   | 0.95 | -2.6 dB  |
| Peaking | 91 Hz   | 4.05 | 6.6 dB   |
| Peaking | 245 Hz  | 3.46 | 2.8 dB   |
| Peaking | 3224 Hz | 7.78 | 3.0 dB   |
| Peaking | 4167 Hz | 6.49 | -3.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20380%20Pro/Sennheiser%20HD%20380%20Pro.png)