# Stax 4070

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.7dB
GraphicEQ: 10 -84; 20 3.1; 22 1.6; 23 1.0; 25 0.1; 26 -0.2; 28 -0.5; 30 -0.6; 32 -0.5; 35 -0.3; 37 -0.1; 40 0.3; 42 0.5; 45 0.8; 49 1.1; 52 1.3; 56 1.5; 59 1.6; 64 1.7; 68 1.7; 73 1.6; 78 1.6; 83 1.5; 89 1.3; 95 1.1; 102 0.8; 109 0.7; 117 0.4; 125 -0.0; 134 -0.2; 143 -0.4; 153 -0.6; 164 -0.6; 175 -0.6; 188 -0.8; 201 -0.9; 215 -0.8; 230 -0.8; 246 -0.9; 263 -1.0; 282 -1.1; 301 -1.1; 323 -1.1; 345 -0.8; 369 0.1; 395 1.3; 423 2.1; 452 1.9; 484 1.4; 518 1.3; 554 1.5; 593 1.9; 635 2.0; 679 1.7; 726 1.4; 777 1.3; 832 0.8; 890 0.3; 952 0.1; 1019 -0.1; 1090 -0.4; 1167 -0.6; 1248 -1.0; 1336 -1.4; 1429 -2.2; 1529 -3.2; 1636 -3.9; 1751 -4.2; 1873 -4.0; 2004 -3.6; 2145 -3.0; 2295 -2.4; 2455 -2.0; 2627 -2.3; 2811 -3.0; 3008 -3.8; 3219 -4.0; 3444 -4.4; 3685 -5.5; 3943 -6.3; 4219 -7.1; 4514 -6.4; 4830 -4.2; 5168 -1.9; 5530 -1.1; 5917 -1.5; 6331 -0.8; 6775 2.4; 7249 1.3; 7756 0.3; 8299 -0.6; 8880 -2.8; 9502 -2.8; 10167 -1.4; 10879 -0.6; 11640 -0.6; 12455 -0.6; 13327 -0.4; 14260 -0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -0.5; 20000 -3.2
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.7dB` and instead set Global volume in the UI for both channels to **-37**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax 4070 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 68 Hz    |  1.98 | 2.0 dB  |
| Peaking | 625 Hz   |  1.84 | 2.3 dB  |
| Peaking | 1786 Hz  |  1.86 | -3.9 dB |
| Peaking | 4038 Hz  |  2.43 | -6.5 dB |
| Peaking | 37269 Hz |  2.68 | -1.4 dB |
| Peaking | 289 Hz   |  1.19 | -1.5 dB |
| Peaking | 425 Hz   |  5.07 | 2.4 dB  |
| Peaking | 4507 Hz  | 10.65 | -1.5 dB |
| Peaking | 6957 Hz  |  6.92 | 3.6 dB  |
| Peaking | 9113 Hz  |  8.97 | -2.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%204070/Stax%204070.png)