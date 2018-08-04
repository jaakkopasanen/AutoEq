# Sennheiser HD 449

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 1.3; 22 0.8; 23 0.6; 25 0.2; 26 0.0; 28 -0.3; 30 -0.6; 32 -0.8; 35 -1.1; 37 -1.3; 40 -1.5; 42 -1.6; 45 -1.7; 49 -1.8; 52 -1.8; 56 -1.8; 59 -1.8; 64 -1.8; 68 -1.8; 73 -1.6; 78 -1.4; 83 -1.2; 89 -0.9; 95 -0.4; 102 0.5; 109 1.0; 117 0.2; 125 -1.7; 134 -3.4; 143 -3.6; 153 -2.8; 164 -1.6; 175 -2.4; 188 -3.2; 201 -3.0; 215 -2.6; 230 -2.1; 246 -1.8; 263 -1.3; 282 -0.9; 301 -0.5; 323 0.0; 345 0.7; 369 1.0; 395 0.9; 423 0.9; 452 0.9; 484 0.9; 518 0.8; 554 0.6; 593 0.5; 635 0.1; 679 -0.2; 726 -0.3; 777 0.0; 832 0.1; 890 -0.1; 952 -0.3; 1019 -0.0; 1090 0.0; 1167 -0.1; 1248 -0.6; 1336 -1.5; 1429 -1.8; 1529 -2.1; 1636 -2.1; 1751 -2.0; 1873 -1.4; 2004 -0.5; 2145 0.5; 2295 2.1; 2455 2.9; 2627 2.8; 2811 3.3; 3008 3.8; 3219 3.8; 3444 4.0; 3685 4.5; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 449 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 5 Hz    | 2.08 | -0.3 dB |
| Peaking | 53 Hz   | 1.63 | -2.0 dB |
| Peaking | 180 Hz  | 1.88 | -3.1 dB |
| Peaking | 1623 Hz | 2.99 | -3.3 dB |
| Peaking | 4483 Hz | 1.14 | 6.6 dB  |
| Peaking | 110 Hz  | 6.41 | 2.2 dB  |
| Peaking | 135 Hz  | 7.77 | -2.4 dB |
| Peaking | 423 Hz  | 2.52 | 1.4 dB  |
| Peaking | 6355 Hz | 3.44 | 4.3 dB  |
| Peaking | 7374 Hz | 1.59 | -3.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20449/Sennheiser%20HD%20449.png)