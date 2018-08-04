# Sennheiser Urbanite XL

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 1.0; 22 0.3; 23 0.0; 25 -0.5; 26 -0.8; 28 -1.2; 30 -1.5; 32 -1.8; 35 -2.2; 37 -2.5; 40 -2.8; 42 -3.0; 45 -3.3; 49 -3.6; 52 -3.7; 56 -4.0; 59 -4.1; 64 -4.3; 68 -4.4; 73 -4.6; 78 -4.8; 83 -5.1; 89 -5.4; 95 -5.7; 102 -6.0; 109 -6.0; 117 -6.0; 125 -6.1; 134 -6.4; 143 -7.0; 153 -7.4; 164 -6.6; 175 -6.1; 188 -6.5; 201 -6.3; 215 -5.8; 230 -5.2; 246 -4.9; 263 -4.8; 282 -5.1; 301 -5.4; 323 -5.5; 345 -5.4; 369 -4.9; 395 -4.2; 423 -3.4; 452 -3.2; 484 -3.1; 518 -2.6; 554 -2.0; 593 -1.4; 635 -1.2; 679 -1.2; 726 -1.1; 777 -0.8; 832 -0.6; 890 -0.5; 952 -0.2; 1019 0.1; 1090 0.0; 1167 -0.2; 1248 -0.4; 1336 -0.7; 1429 -1.1; 1529 -1.5; 1636 -1.8; 1751 -2.1; 1873 -2.2; 2004 -2.2; 2145 -1.7; 2295 -0.7; 2455 0.4; 2627 0.8; 2811 1.5; 3008 2.5; 3219 2.6; 3444 3.2; 3685 4.1; 3943 5.4; 4219 6.0; 4514 5.6; 4830 0.1; 5168 -1.2; 5530 2.3; 5917 4.6; 6331 5.0; 6775 3.7; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Urbanite XL ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 49 Hz    |  1.41 | -1.3 dB |
| Peaking | 146 Hz   |  0.52 | -6.4 dB |
| Peaking | 356 Hz   |  2.12 | -2.1 dB |
| Peaking | 4073 Hz  |  2.65 | 5.8 dB  |
| Peaking | 25210 Hz |  2.41 | 2.3 dB  |
| Peaking | 1064 Hz  |  2.24 | 1.0 dB  |
| Peaking | 1991 Hz  |  1.59 | -3.3 dB |
| Peaking | 2665 Hz  |  1.93 | 2.0 dB  |
| Peaking | 5038 Hz  | 11.17 | -5.4 dB |
| Peaking | 6226 Hz  |  4.95 | 4.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20Urbanite%20XL/Sennheiser%20Urbanite%20XL.png)