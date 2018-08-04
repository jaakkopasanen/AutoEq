# Denon AH-D5000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.8dB
GraphicEQ: 10 -84; 20 -2.0; 22 -2.8; 23 -3.1; 25 -3.7; 26 -3.9; 28 -4.3; 30 -4.5; 32 -4.7; 35 -5.0; 37 -5.2; 40 -5.4; 42 -5.3; 45 -5.1; 49 -5.0; 52 -5.1; 56 -5.1; 59 -5.1; 64 -5.1; 68 -5.1; 73 -5.1; 78 -5.1; 83 -5.1; 89 -5.1; 95 -5.1; 102 -4.9; 109 -4.8; 117 -4.8; 125 -4.8; 134 -4.8; 143 -4.6; 153 -4.5; 164 -4.3; 175 -4.2; 188 -3.9; 201 -3.8; 215 -3.8; 230 -3.7; 246 -3.6; 263 -3.5; 282 -3.5; 301 -3.4; 323 -3.1; 345 -2.9; 369 -2.5; 395 -2.2; 423 -1.7; 452 -1.3; 484 -0.8; 518 -0.2; 554 0.4; 593 1.1; 635 1.3; 679 0.9; 726 -0.1; 777 -1.6; 832 -2.0; 890 0.4; 952 1.0; 1019 -0.3; 1090 -0.9; 1167 -1.2; 1248 -1.2; 1336 -0.9; 1429 -0.6; 1529 -0.5; 1636 -0.5; 1751 -0.8; 1873 -0.7; 2004 -0.4; 2145 0.1; 2295 0.7; 2455 1.6; 2627 3.4; 2811 4.2; 3008 3.7; 3219 2.8; 3444 1.9; 3685 1.3; 3943 0.6; 4219 0.1; 4514 0.9; 4830 2.3; 5168 3.5; 5530 3.9; 5917 3.2; 6331 0.4; 6775 -2.3; 7249 -3.4; 7756 -2.8; 8299 -2.1; 8880 -2.7; 9502 -2.2; 10167 -0.1; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 -0.2
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.8dB` and instead set Global volume in the UI for both channels to **-48**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-D5000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 63 Hz    |  0.32 | -5.4 dB |
| Peaking | 274 Hz   |  1.63 | -1.6 dB |
| Peaking | 2883 Hz  |  4.28 | 4.6 dB  |
| Peaking | 5659 Hz  |  3.11 | 6.6 dB  |
| Peaking | 7108 Hz  |  1.93 | -5.0 dB |
| Peaking | 34 Hz    |  2.54 | -0.3 dB |
| Peaking | 627 Hz   |  3.77 | 2.2 dB  |
| Peaking | 799 Hz   | 11.15 | -2.3 dB |
| Peaking | 1467 Hz  |  1.77 | -0.9 dB |
| Peaking | 10969 Hz |  6.02 | 0.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/Denon%20AH-D5000/Denon%20AH-D5000.png)