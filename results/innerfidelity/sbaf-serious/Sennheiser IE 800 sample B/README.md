# Sennheiser IE 800 sample B

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 5.8; 32 5.6; 35 5.2; 37 4.8; 40 4.4; 42 4.2; 45 3.9; 49 3.5; 52 3.3; 56 3.0; 59 2.8; 64 2.5; 68 2.3; 73 2.1; 78 1.7; 83 1.3; 89 0.9; 95 0.4; 102 -0.3; 109 -0.8; 117 -1.4; 125 -2.1; 134 -2.7; 143 -2.9; 153 -3.2; 164 -3.4; 175 -3.4; 188 -3.4; 201 -3.4; 215 -3.3; 230 -3.1; 246 -3.1; 263 -3.0; 282 -2.7; 301 -2.6; 323 -2.4; 345 -2.2; 369 -2.0; 395 -1.8; 423 -1.4; 452 -1.2; 484 -1.1; 518 -0.9; 554 -0.5; 593 -0.1; 635 0.1; 679 0.2; 726 0.3; 777 0.6; 832 0.5; 890 0.3; 952 0.2; 1019 -0.0; 1090 -0.2; 1167 -0.4; 1248 -0.5; 1336 -0.7; 1429 -0.9; 1529 -1.0; 1636 -0.9; 1751 -0.4; 1873 0.3; 2004 1.2; 2145 2.2; 2295 3.4; 2455 5.0; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 5.9; 4830 5.0; 5168 4.2; 5530 3.0; 5917 1.6; 6331 3.4; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.8; 9502 -2.3; 10167 -3.3; 10879 -4.5; 11640 -5.4; 12455 -4.9; 13327 -3.6; 14260 -2.6; 15258 -2.0; 16326 -0.4; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser IE 800 sample B ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 25 Hz    |  0.54 | 6.2 dB  |
| Peaking | 83 Hz    |  1.09 | 2.4 dB  |
| Peaking | 162 Hz   |  0.59 | -4.5 dB |
| Peaking | 3758 Hz  |  1.09 | 6.9 dB  |
| Peaking | 11787 Hz |  1.84 | -6.1 dB |
| Peaking | 761 Hz   |  1.43 | 1.7 dB  |
| Peaking | 1603 Hz  |  2.37 | -1.6 dB |
| Peaking | 2572 Hz  |  3.6  | 3.1 dB  |
| Peaking | 1540 Hz  |  0.36 | -1.1 dB |
| Peaking | 6659 Hz  | 10.94 | 3.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20IE%20800%20sample%20B/Sennheiser%20IE%20800%20sample%20B.png)