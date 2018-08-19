# Sennheiser IE 800 sample B

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 5.9; 30 5.7; 32 5.4; 35 4.9; 37 4.5; 40 4.0; 42 3.7; 45 3.3; 49 2.8; 52 2.5; 56 2.0; 59 1.7; 64 1.3; 68 0.9; 73 0.5; 78 0.1; 83 -0.3; 89 -0.7; 95 -1.0; 102 -1.3; 109 -1.6; 117 -1.7; 125 -2.1; 134 -2.4; 143 -2.5; 153 -2.7; 164 -2.8; 175 -2.9; 188 -2.9; 201 -3.0; 215 -2.9; 230 -2.8; 246 -2.8; 263 -2.7; 282 -2.5; 301 -2.4; 323 -2.3; 345 -2.1; 369 -1.9; 395 -1.7; 423 -1.4; 452 -1.1; 484 -1.0; 518 -0.9; 554 -0.5; 593 -0.1; 635 0.1; 679 0.2; 726 0.4; 777 0.6; 832 0.5; 890 0.3; 952 0.2; 1019 -0.0; 1090 -0.2; 1167 -0.4; 1248 -0.5; 1336 -0.7; 1429 -0.9; 1529 -1.0; 1636 -0.9; 1751 -0.4; 1873 0.3; 2004 1.2; 2145 2.2; 2295 3.4; 2455 5.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 5.9; 4830 5.0; 5168 4.2; 5530 3.0; 5917 1.6; 6331 3.4; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.8; 9502 -2.3; 10167 -3.3; 10879 -4.5; 11640 -5.4; 12455 -4.9; 13327 -3.6; 14260 -2.6; 15258 -2.0; 16326 -0.4; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE 800 sample B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 20 Hz    |  0.53 | 0.7 dB  |
| Peaking | 25 Hz    |  0.59 | 5.6 dB  |
| Peaking | 180 Hz   |  0.57 | -3.4 dB |
| Peaking | 3758 Hz  |  1.09 | 6.9 dB  |
| Peaking | 11787 Hz |  1.84 | -6.1 dB |
| Peaking | 760 Hz   |  1.44 | 1.7 dB  |
| Peaking | 1557 Hz  |  0.37 | -1.1 dB |
| Peaking | 1604 Hz  |  2.37 | -1.6 dB |
| Peaking | 2594 Hz  |  3.6  | 3.2 dB  |
| Peaking | 6650 Hz  | 10.91 | 3.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20IE%20800%20sample%20B/Sennheiser%20IE%20800%20sample%20B.png)