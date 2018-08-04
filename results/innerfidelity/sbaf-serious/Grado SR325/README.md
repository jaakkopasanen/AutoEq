# Grado SR325

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 5.9; 42 5.7; 45 5.1; 49 4.4; 52 3.9; 56 3.2; 59 2.8; 64 2.3; 68 2.0; 73 1.6; 78 1.4; 83 1.2; 89 0.8; 95 0.5; 102 0.2; 109 0.1; 117 -0.1; 125 -0.3; 134 -0.5; 143 -0.5; 153 -0.5; 164 -0.4; 175 -0.3; 188 -0.1; 201 -0.2; 215 -0.1; 230 0.0; 246 0.1; 263 0.2; 282 0.3; 301 0.5; 323 0.7; 345 1.0; 369 1.1; 395 0.5; 423 0.4; 452 0.5; 484 0.5; 518 0.3; 554 0.5; 593 0.7; 635 0.7; 679 0.5; 726 0.6; 777 0.6; 832 0.5; 890 0.3; 952 0.0; 1019 -0.1; 1090 -0.2; 1167 -0.4; 1248 -1.0; 1336 -1.8; 1429 -2.7; 1529 -3.6; 1636 -4.1; 1751 -4.4; 1873 -6.1; 2004 -9.3; 2145 -8.1; 2295 -7.1; 2455 -5.5; 2627 -4.6; 2811 -3.1; 3008 -2.1; 3219 -1.3; 3444 -0.4; 3685 3.3; 3943 -3.3; 4219 -6.7; 4514 -8.1; 4830 -8.8; 5168 -6.5; 5530 -4.8; 5917 -2.9; 6331 -2.8; 6775 -5.2; 7249 -5.6; 7756 -6.0; 8299 -8.0; 8880 -10.4; 9502 -10.8; 10167 -8.6; 10879 -5.3; 11640 -2.4; 12455 -0.3; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.2; 17469 -1.5; 18692 -0.8; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR325 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 30 Hz    | 0.89 | 6.8 dB   |
| Peaking | 2058 Hz  | 3.21 | -8.2 dB  |
| Peaking | 9868 Hz  | 1    | -22.1 dB |
| Peaking | 24000 Hz | 2.25 | -8.3 dB  |
| Peaking | 11422 Hz | 0.9  | 14.3 dB  |
| Peaking | 134 Hz   | 2.48 | -1.1 dB  |
| Peaking | 2506 Hz  | 6.67 | -0.5 dB  |
| Peaking | 3684 Hz  | 6.19 | 8.5 dB   |
| Peaking | 4526 Hz  | 2.82 | -6.7 dB  |
| Peaking | 6132 Hz  | 4.38 | 3.9 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20SR325/Grado%20SR325.png)