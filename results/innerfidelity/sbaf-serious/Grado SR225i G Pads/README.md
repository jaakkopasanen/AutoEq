# Grado SR225i G Pads

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 5.9; 35 5.4; 37 5.0; 40 4.2; 42 3.7; 45 3.3; 49 3.0; 52 2.4; 56 1.4; 59 0.8; 64 0.0; 68 -0.4; 73 -0.8; 78 -1.2; 83 -1.5; 89 -1.8; 95 -2.2; 102 -2.7; 109 -2.9; 117 -3.1; 125 -3.3; 134 -3.5; 143 -3.5; 153 -3.5; 164 -3.3; 175 -3.0; 188 -2.8; 201 -2.6; 215 -2.4; 230 -2.1; 246 -1.8; 263 -1.6; 282 -1.3; 301 -1.2; 323 -1.0; 345 -0.8; 369 -0.8; 395 -0.8; 423 -0.7; 452 -0.4; 484 -0.5; 518 -0.5; 554 -0.4; 593 -0.2; 635 -0.0; 679 -0.1; 726 -0.0; 777 0.2; 832 0.1; 890 -0.1; 952 -0.1; 1019 -0.1; 1090 -0.2; 1167 -0.6; 1248 -0.9; 1336 -1.1; 1429 -1.7; 1529 -1.7; 1636 -1.8; 1751 -2.2; 1873 -1.5; 2004 -1.8; 2145 -1.4; 2295 -1.5; 2455 -1.9; 2627 -2.2; 2811 -2.4; 3008 -3.2; 3219 -2.9; 3444 -3.9; 3685 -4.8; 3943 -4.4; 4219 -3.7; 4514 -3.1; 4830 -4.9; 5168 -7.6; 5530 -8.6; 5917 -10.0; 6331 -10.5; 6775 -9.4; 7249 -8.1; 7756 -7.6; 8299 -8.4; 8880 -10.0; 9502 -9.9; 10167 -7.1; 10879 -2.8; 11640 -0.1; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR225i G Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 27 Hz    | 0.7  | 6.7 dB   |
| Peaking | 127 Hz   | 0.72 | -4.1 dB  |
| Peaking | 5941 Hz  | 3.82 | -1.7 dB  |
| Peaking | 6981 Hz  | 0.93 | -9.2 dB  |
| Peaking | 24000 Hz | 2.21 | -7.9 dB  |
| Peaking | 1626 Hz  | 3.61 | -1.3 dB  |
| Peaking | 4606 Hz  | 1.44 | -3.4 dB  |
| Peaking | 4536 Hz  | 5.05 | 4.8 dB   |
| Peaking | 9502 Hz  | 3.3  | -10.0 dB |
| Peaking | 10073 Hz | 1    | 6.0 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20SR225i%20G%20Pads/Grado%20SR225i%20G%20Pads.png)