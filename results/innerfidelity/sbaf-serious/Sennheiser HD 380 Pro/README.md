# Sennheiser HD 380 Pro

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.6dB
GraphicEQ: 10 -84; 20 -9.6; 22 -9.7; 23 -9.8; 25 -9.9; 26 -9.9; 28 -9.9; 30 -9.9; 32 -9.9; 35 -9.8; 37 -9.7; 40 -9.5; 42 -9.3; 45 -9.1; 49 -8.6; 52 -8.2; 56 -7.7; 59 -7.3; 64 -6.4; 68 -5.7; 73 -5.0; 78 -3.8; 83 -2.1; 89 -0.2; 95 1.0; 102 -0.6; 109 -3.0; 117 -3.1; 125 -2.6; 134 -3.8; 143 -4.6; 153 -3.4; 164 -1.0; 175 -1.8; 188 -1.2; 201 0.1; 215 1.1; 230 1.7; 246 1.8; 263 1.6; 282 1.3; 301 0.7; 323 -0.2; 345 -0.8; 369 -1.5; 395 -2.0; 423 -2.2; 452 -2.2; 484 -2.4; 518 -2.4; 554 -2.1; 593 -1.6; 635 -1.3; 679 -1.1; 726 -0.9; 777 -0.5; 832 -0.4; 890 -0.1; 952 -0.1; 1019 0.0; 1090 0.1; 1167 0.4; 1248 0.4; 1336 0.4; 1429 0.3; 1529 0.0; 1636 -0.5; 1751 -1.6; 1873 -3.2; 2004 -4.0; 2145 -4.5; 2295 -4.0; 2455 -3.9; 2627 -2.5; 2811 -0.8; 3008 0.9; 3219 1.9; 3444 1.2; 3685 -1.0; 3943 -1.9; 4219 -2.8; 4514 -1.6; 4830 1.0; 5168 3.6; 5530 4.5; 5917 3.5; 6331 2.8; 6775 1.2; 7249 0.7; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.2; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -0.2; 20000 -0.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.602027532836769dB` and instead set Global volume in the UI for both channels to **-46**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 380 Pro ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.0dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 26 Hz   | 0.64 | -9.9 dB |
| Peaking | 51 Hz   | 1.92 | -3.5 dB |
| Peaking | 494 Hz  | 2.8  | -2.6 dB |
| Peaking | 2179 Hz | 3.53 | -5.0 dB |
| Peaking | 5653 Hz | 5.2  | 5.0 dB  |
| Peaking | 94 Hz   | 4.52 | 5.7 dB  |
| Peaking | 128 Hz  | 0.94 | -3.3 dB |
| Peaking | 237 Hz  | 2.4  | 3.8 dB  |
| Peaking | 3233 Hz | 7.86 | 3.0 dB  |
| Peaking | 4180 Hz | 6.56 | -3.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20380%20Pro/Sennheiser%20HD%20380%20Pro.png)