# Sennheiser Urbanite XL

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.2dB
GraphicEQ: 10 -84; 20 1.0; 22 0.3; 23 -0.0; 25 -0.6; 26 -0.8; 28 -1.2; 30 -1.6; 32 -1.9; 35 -2.3; 37 -2.6; 40 -3.0; 42 -3.2; 45 -3.5; 49 -3.8; 52 -4.0; 56 -4.3; 59 -4.5; 64 -4.8; 68 -5.0; 73 -5.3; 78 -5.6; 83 -5.9; 89 -6.2; 95 -6.4; 102 -6.6; 109 -6.4; 117 -6.2; 125 -6.1; 134 -6.2; 143 -6.8; 153 -7.2; 164 -6.4; 175 -5.9; 188 -6.2; 201 -6.1; 215 -5.7; 230 -5.1; 246 -4.8; 263 -4.7; 282 -5.1; 301 -5.4; 323 -5.5; 345 -5.3; 369 -4.9; 395 -4.2; 423 -3.4; 452 -3.2; 484 -3.1; 518 -2.6; 554 -2.0; 593 -1.4; 635 -1.2; 679 -1.2; 726 -1.1; 777 -0.8; 832 -0.6; 890 -0.5; 952 -0.2; 1019 0.1; 1090 0.0; 1167 -0.2; 1248 -0.4; 1336 -0.7; 1429 -1.1; 1529 -1.5; 1636 -1.8; 1751 -2.1; 1873 -2.2; 2004 -2.2; 2145 -1.7; 2295 -0.7; 2455 0.4; 2627 0.8; 2811 1.5; 3008 2.5; 3219 2.6; 3444 3.2; 3685 4.1; 3943 5.4; 4219 6.0; 4514 5.6; 4830 0.1; 5168 -1.2; 5530 2.3; 5917 4.6; 6331 5.0; 6775 3.7; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.185882491425293dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Urbanite XL ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.9dB.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 73 Hz    |  0.7  | -1.9 dB |
| Peaking | 154 Hz   |  0.44 | -5.5 dB |
| Peaking | 349 Hz   |  3.05 | -1.9 dB |
| Peaking | 4072 Hz  |  2.61 | 5.8 dB  |
| Peaking | 22809 Hz |  2.41 | 2.3 dB  |
| Peaking | 20 Hz    |  2.33 | 1.6 dB  |
| Peaking | 1880 Hz  |  1.7  | -5.2 dB |
| Peaking | 1884 Hz  |  0.82 | 2.7 dB  |
| Peaking | 5046 Hz  | 10.53 | -5.6 dB |
| Peaking | 6238 Hz  |  5.21 | 4.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20Urbanite%20XL/Sennheiser%20Urbanite%20XL.png)