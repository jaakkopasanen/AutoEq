# Sennheiser HD 4

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 5.9; 26 5.8; 28 5.5; 30 5.1; 32 4.6; 35 4.0; 37 3.6; 40 3.2; 42 3.0; 45 2.7; 49 2.4; 52 2.1; 56 1.9; 59 1.7; 64 1.3; 68 1.1; 73 0.9; 78 0.6; 83 0.3; 89 0.1; 95 -0.0; 102 -0.3; 109 -0.6; 117 -0.5; 125 -0.5; 134 -0.6; 143 -0.9; 153 -1.4; 164 -1.0; 175 -0.5; 188 -1.1; 201 -1.4; 215 -1.3; 230 -1.1; 246 -0.9; 263 -0.7; 282 -0.4; 301 -0.1; 323 0.2; 345 0.6; 369 0.8; 395 1.0; 423 0.9; 452 0.7; 484 0.3; 518 0.2; 554 0.4; 593 0.6; 635 0.6; 679 0.4; 726 0.4; 777 0.5; 832 0.4; 890 0.2; 952 0.2; 1019 0.0; 1090 -0.0; 1167 -0.1; 1248 -0.4; 1336 -0.7; 1429 -1.1; 1529 -1.4; 1636 -1.9; 1751 -2.0; 1873 -1.7; 2004 -1.2; 2145 -1.0; 2295 -0.3; 2455 0.8; 2627 2.1; 2811 3.3; 3008 4.5; 3219 5.7; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 5.9; 4830 0.9; 5168 0.3; 5530 2.7; 5917 4.1; 6331 5.4; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 4 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.8dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 22 Hz   |  1.49 | 6.0 dB  |
| Peaking | 39 Hz   |  1.74 | 2.1 dB  |
| Peaking | 1837 Hz |  2.19 | -2.9 dB |
| Peaking | 3597 Hz |  1.94 | 6.9 dB  |
| Peaking | 6354 Hz |  6.98 | 4.9 dB  |
| Peaking | 228 Hz  |  0.97 | -2.4 dB |
| Peaking | 343 Hz  |  0.92 | 1.9 dB  |
| Peaking | 4494 Hz |  8.85 | 2.8 dB  |
| Peaking | 4971 Hz | 11.15 | -4.0 dB |
| Peaking | 8429 Hz |  4.44 | -0.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%204/Sennheiser%20HD%204.png)