# Sennheiser HD 218

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 5.8; 23 5.7; 25 5.3; 26 5.1; 28 4.5; 30 4.1; 32 3.7; 35 3.1; 37 2.8; 40 2.3; 42 2.0; 45 1.5; 49 0.9; 52 0.5; 56 0.1; 59 -0.3; 64 -0.9; 68 -1.3; 73 -1.9; 78 -2.4; 83 -2.8; 89 -3.3; 95 -3.8; 102 -3.9; 109 -3.5; 117 -3.3; 125 -3.7; 134 -4.7; 143 -5.6; 153 -6.3; 164 -6.1; 175 -6.5; 188 -6.4; 201 -6.1; 215 -5.8; 230 -5.1; 246 -4.4; 263 -3.7; 282 -3.1; 301 -3.0; 323 -3.5; 345 -3.1; 369 -2.4; 395 -2.0; 423 -0.9; 452 -0.4; 484 -0.3; 518 -0.5; 554 -0.2; 593 0.8; 635 1.1; 679 1.0; 726 0.9; 777 0.9; 832 0.6; 890 0.3; 952 0.1; 1019 0.0; 1090 -0.0; 1167 0.1; 1248 0.3; 1336 0.5; 1429 0.8; 1529 1.1; 1636 0.8; 1751 0.3; 1873 0.4; 2004 1.0; 2145 1.7; 2295 2.3; 2455 2.9; 2627 3.5; 2811 3.5; 3008 4.2; 3219 4.9; 3444 5.7; 3685 6.0; 3943 6.0; 4219 4.2; 4514 2.4; 4830 -1.6; 5168 0.5; 5530 1.3; 5917 0.3; 6331 2.0; 6775 3.3; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.1; 17469 -2.1; 18692 -2.2; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999999999dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD 218 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.2dB.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 21 Hz    |  0.82 | 6.0 dB  |
| Peaking | 88 Hz    |  1.78 | -2.4 dB |
| Peaking | 183 Hz   |  1.17 | -6.5 dB |
| Peaking | 3426 Hz  |  1.85 | 6.0 dB  |
| Peaking | 24000 Hz |  2.3  | 0.4 dB  |
| Peaking | 340 Hz   |  5.8  | -1.5 dB |
| Peaking | 663 Hz   |  2.47 | 1.5 dB  |
| Peaking | 4839 Hz  | 12.96 | -4.1 dB |
| Peaking | 6731 Hz  | 10.23 | 2.9 dB  |
| Peaking | 18213 Hz |  3.21 | -2.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20HD%20218/Sennheiser%20HD%20218.png)