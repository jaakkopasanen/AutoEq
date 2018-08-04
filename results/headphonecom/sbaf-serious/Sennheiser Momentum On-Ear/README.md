# Sennheiser Momentum On-Ear

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -6.3; 22 -6.5; 23 -6.6; 25 -6.8; 26 -6.8; 28 -6.9; 30 -7.0; 32 -7.1; 35 -7.2; 37 -7.2; 40 -7.3; 42 -7.3; 45 -7.3; 49 -7.3; 52 -7.3; 56 -7.3; 59 -7.3; 64 -7.3; 68 -7.2; 73 -6.9; 78 -6.5; 83 -6.2; 89 -6.1; 95 -6.2; 102 -6.1; 109 -6.0; 117 -5.6; 125 -5.4; 134 -5.2; 143 -4.8; 153 -4.5; 164 -4.1; 175 -3.8; 188 -3.4; 201 -2.9; 215 -2.4; 230 -1.7; 246 -1.0; 263 -0.2; 282 0.5; 301 0.7; 323 1.2; 345 1.7; 369 1.9; 395 2.1; 423 2.1; 452 2.1; 484 1.8; 518 1.5; 554 1.4; 593 1.3; 635 0.9; 679 0.5; 726 0.3; 777 0.5; 832 0.3; 890 0.3; 952 0.3; 1019 -0.0; 1090 -0.5; 1167 -1.1; 1248 -1.9; 1336 -2.9; 1429 -3.6; 1529 -4.5; 1636 -5.4; 1751 -5.7; 1873 -5.4; 2004 -4.9; 2145 -4.2; 2295 -3.3; 2455 -1.8; 2627 -0.4; 2811 0.7; 3008 2.0; 3219 2.8; 3444 3.8; 3685 5.1; 3943 6.0; 4219 6.0; 4514 5.1; 4830 0.5; 5168 0.9; 5530 2.4; 5917 2.6; 6331 1.0; 6775 -1.8; 7249 -3.6; 7756 -3.4; 8299 -2.9; 8880 -2.9; 9502 -1.9; 10167 -0.1; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
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
| Peaking | 38 Hz   |  0.52 | -7.7 dB |
| Peaking | 118 Hz  |  1.4  | -3.6 dB |
| Peaking | 1827 Hz |  2.15 | -6.6 dB |
| Peaking | 3938 Hz |  2.16 | 6.7 dB  |
| Peaking | 7885 Hz |  3.13 | -4.3 dB |
| Peaking | 194 Hz  |  2.24 | -1.7 dB |
| Peaking | 395 Hz  |  1.14 | 2.8 dB  |
| Peaking | 979 Hz  |  3.39 | 0.6 dB  |
| Peaking | 1386 Hz |  3.91 | -1.1 dB |
| Peaking | 5905 Hz | 11.09 | 2.4 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Sennheiser%20Momentum%20On-Ear/Sennheiser%20Momentum%20On-Ear.png)