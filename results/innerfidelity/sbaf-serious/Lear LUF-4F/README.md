# Lear LUF-4F

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 1.4; 22 1.2; 23 1.1; 25 0.9; 26 0.8; 28 0.6; 30 0.5; 32 0.4; 35 0.2; 37 0.1; 40 -0.0; 42 -0.1; 45 -0.2; 49 -0.3; 52 -0.3; 56 -0.4; 59 -0.5; 64 -0.6; 68 -0.7; 73 -0.8; 78 -0.9; 83 -1.1; 89 -1.4; 95 -1.8; 102 -2.2; 109 -2.5; 117 -2.8; 125 -3.2; 134 -3.4; 143 -3.3; 153 -3.2; 164 -2.9; 175 -2.4; 188 -1.9; 201 -1.4; 215 -0.8; 230 -0.3; 246 0.1; 263 0.5; 282 0.9; 301 1.2; 323 1.4; 345 1.6; 369 1.7; 395 1.7; 423 1.8; 452 1.9; 484 1.8; 518 1.7; 554 1.8; 593 1.9; 635 1.9; 679 1.7; 726 1.6; 777 1.6; 832 1.3; 890 0.9; 952 0.5; 1019 -0.1; 1090 -0.6; 1167 -1.2; 1248 -1.9; 1336 -2.7; 1429 -3.8; 1529 -4.8; 1636 -5.6; 1751 -6.2; 1873 -6.5; 2004 -6.6; 2145 -6.6; 2295 -6.3; 2455 -5.4; 2627 -4.0; 2811 -2.4; 3008 -0.4; 3219 0.3; 3444 -0.1; 3685 -0.1; 3943 0.9; 4219 3.9; 4514 6.0; 4830 6.0; 5168 2.3; 5530 -0.3; 5917 0.6; 6331 1.8; 6775 1.8; 7249 0.4; 7756 -2.7; 8299 -4.0; 8880 -2.0; 9502 -0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Lear LUF-4F ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 142 Hz  |  0.89 | -5.9 dB  |
| Peaking | 737 Hz  |  0.11 | 3.4 dB   |
| Peaking | 1928 Hz |  1.13 | -10.2 dB |
| Peaking | 4589 Hz |  5.64 | 6.4 dB   |
| Peaking | 8279 Hz |  6.13 | -5.4 dB  |
| Peaking | 20 Hz   |  1.85 | 1.3 dB   |
| Peaking | 2436 Hz |  6.71 | -1.1 dB  |
| Peaking | 3084 Hz |  8.48 | 1.8 dB   |
| Peaking | 5553 Hz | 11.56 | -2.3 dB  |
| Peaking | 6639 Hz |  8.02 | 1.6 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Lear%20LUF-4F/Lear%20LUF-4F.png)