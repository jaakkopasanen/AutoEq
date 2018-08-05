# Sennheiser CX 200

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -1.3; 22 -1.6; 23 -1.7; 25 -2.0; 26 -2.1; 28 -2.3; 30 -2.5; 32 -2.6; 35 -2.7; 37 -2.8; 40 -2.8; 42 -2.8; 45 -2.9; 49 -3.0; 52 -3.0; 56 -2.9; 59 -2.9; 64 -2.9; 68 -2.9; 73 -2.9; 78 -3.0; 83 -3.1; 89 -3.3; 95 -3.5; 102 -3.9; 109 -4.2; 117 -4.5; 125 -4.9; 134 -5.1; 143 -5.2; 153 -5.1; 164 -5.1; 175 -4.8; 188 -4.6; 201 -4.4; 215 -4.0; 230 -3.7; 246 -3.4; 263 -3.2; 282 -2.8; 301 -2.5; 323 -2.2; 345 -1.9; 369 -1.6; 395 -1.3; 423 -0.9; 452 -0.7; 484 -0.6; 518 -0.4; 554 -0.0; 593 0.3; 635 0.5; 679 0.4; 726 0.6; 777 0.8; 832 0.6; 890 0.4; 952 0.1; 1019 -0.1; 1090 -0.5; 1167 -0.8; 1248 -0.9; 1336 -1.4; 1429 -1.8; 1529 -2.1; 1636 -2.2; 1751 -2.1; 1873 -1.6; 2004 -1.0; 2145 -0.2; 2295 0.8; 2455 2.3; 2627 3.3; 2811 4.5; 3008 5.9; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 4.6; 4514 3.1; 4830 2.3; 5168 2.1; 5530 1.6; 5917 0.8; 6331 -0.0; 6775 -0.3; 7249 0.3; 7756 0.2; 8299 0.0; 8880 0.0; 9502 0.0; 10167 -0.4; 10879 -1.6; 11640 -0.6; 12455 0.0; 13327 -0.1; 14260 -2.1; 15258 -2.0; 16326 -0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser CX 200 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 4 Hz     |  1.55 | -0.6 dB |
| Peaking | 39 Hz    |  0.63 | -2.4 dB |
| Peaking | 159 Hz   |  0.89 | -4.9 dB |
| Peaking | 1718 Hz  |  2.28 | -3.3 dB |
| Peaking | 3385 Hz  |  1.77 | 7.0 dB  |
| Peaking | 311 Hz   |  2.28 | -0.6 dB |
| Peaking | 744 Hz   |  1.47 | 1.2 dB  |
| Peaking | 1224 Hz  |  2.53 | -0.7 dB |
| Peaking | 4074 Hz  | 12.26 | 1.2 dB  |
| Peaking | 13458 Hz |  0.81 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20CX%20200/Sennheiser%20CX%20200.png)