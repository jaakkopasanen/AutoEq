# Sennheiser HD238

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 0.1; 22 -0.7; 23 -1.1; 25 -1.7; 26 -2.0; 28 -2.6; 30 -3.0; 32 -3.5; 35 -4.0; 37 -4.3; 40 -4.6; 42 -4.8; 45 -4.9; 49 -5.3; 52 -5.6; 56 -5.9; 59 -6.0; 64 -5.9; 68 -5.9; 73 -6.2; 78 -6.4; 83 -6.5; 89 -6.7; 95 -6.7; 102 -6.9; 109 -6.9; 117 -6.9; 125 -6.9; 134 -6.7; 143 -6.5; 153 -6.4; 164 -6.3; 175 -6.3; 188 -6.1; 201 -6.0; 215 -5.8; 230 -5.6; 246 -5.4; 263 -5.2; 282 -5.0; 301 -4.7; 323 -4.4; 345 -4.1; 369 -3.8; 395 -3.4; 423 -3.0; 452 -2.8; 484 -2.3; 518 -2.0; 554 -1.5; 593 -1.2; 635 -0.7; 679 -0.4; 726 -0.2; 777 -0.1; 832 -0.0; 890 0.1; 952 0.0; 1019 -0.0; 1090 -0.0; 1167 0.1; 1248 0.1; 1336 0.4; 1429 0.5; 1529 0.7; 1636 1.6; 1751 1.5; 1873 1.7; 2004 2.5; 2145 3.7; 2295 4.7; 2455 5.2; 2627 4.1; 2811 2.3; 3008 0.4; 3219 -1.3; 3444 -0.1; 3685 3.0; 3943 3.8; 4219 1.3; 4514 0.5; 4830 3.3; 5168 5.5; 5530 4.7; 5917 2.1; 6331 0.4; 6775 0.1; 7249 0.4; 7756 0.2; 8299 -0.1; 8880 -0.9; 9502 -0.1; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser HD238 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 90 Hz    |  0.43 | -6.6 dB |
| Peaking | 268 Hz   |  1.01 | -2.4 dB |
| Peaking | 2346 Hz  |  3.01 | 5.2 dB  |
| Peaking | 5258 Hz  |  5.52 | 5.7 dB  |
| Peaking | 24000 Hz |  2.37 | 2.1 dB  |
| Peaking | 14 Hz    |  0.65 | 2.3 dB  |
| Peaking | 33 Hz    |  1.6  | -1.3 dB |
| Peaking | 814 Hz   |  2.41 | 0.7 dB  |
| Peaking | 3248 Hz  |  8.19 | -3.0 dB |
| Peaking | 3832 Hz  | 10.04 | 3.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Sennheiser%20HD238/Sennheiser%20HD238.png)