# Sennheiser Momentum On-Ear

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -2.3; 22 -2.5; 23 -2.6; 25 -2.8; 26 -2.8; 28 -2.9; 30 -3.0; 32 -3.1; 35 -3.2; 37 -3.2; 40 -3.3; 42 -3.3; 45 -3.3; 49 -3.3; 52 -3.3; 56 -3.3; 59 -3.4; 64 -3.4; 68 -3.3; 73 -3.1; 78 -2.9; 83 -2.7; 89 -2.9; 95 -3.3; 102 -3.7; 109 -3.9; 117 -4.0; 125 -4.3; 134 -4.4; 143 -4.3; 153 -4.1; 164 -3.8; 175 -3.6; 188 -3.3; 201 -2.8; 215 -2.3; 230 -1.7; 246 -1.0; 263 -0.2; 282 0.5; 301 0.8; 323 1.2; 345 1.7; 369 1.9; 395 2.1; 423 2.1; 452 2.1; 484 1.8; 518 1.5; 554 1.4; 593 1.3; 635 0.9; 679 0.5; 726 0.3; 777 0.5; 832 0.3; 890 0.3; 952 0.3; 1019 -0.0; 1090 -0.5; 1167 -1.1; 1248 -1.9; 1336 -2.9; 1429 -3.6; 1529 -4.5; 1636 -5.4; 1751 -5.7; 1873 -5.4; 2004 -4.9; 2145 -4.2; 2295 -3.3; 2455 -1.8; 2627 -0.4; 2811 0.7; 3008 2.0; 3219 2.8; 3444 3.8; 3685 5.1; 3943 6.0; 4219 6.0; 4514 5.1; 4830 0.5; 5168 0.9; 5530 2.4; 5917 2.6; 6331 1.0; 6775 -1.8; 7249 -3.6; 7756 -3.4; 8299 -2.9; 8880 -2.9; 9502 -1.9; 10167 -0.1; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum On-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 42 Hz   |  0.6  | -3.5 dB |
| Peaking | 140 Hz  |  1.81 | -3.9 dB |
| Peaking | 1827 Hz |  2.13 | -6.6 dB |
| Peaking | 3937 Hz |  2.15 | 6.7 dB  |
| Peaking | 7885 Hz |  3.12 | -4.3 dB |
| Peaking | 204 Hz  |  2.83 | -1.7 dB |
| Peaking | 404 Hz  |  1.22 | 2.6 dB  |
| Peaking | 977 Hz  |  3.32 | 0.7 dB  |
| Peaking | 1388 Hz |  4    | -1.1 dB |
| Peaking | 5920 Hz | 11.1  | 2.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20Momentum%20On-Ear/Sennheiser%20Momentum%20On-Ear.png)