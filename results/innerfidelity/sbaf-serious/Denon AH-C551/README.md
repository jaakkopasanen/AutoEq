# Denon AH-C551

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.3dB
GraphicEQ: 10 -84; 20 -5.5; 22 -5.8; 23 -6.0; 25 -6.3; 26 -6.4; 28 -6.6; 30 -6.8; 32 -6.9; 35 -7.1; 37 -7.2; 40 -7.3; 42 -7.4; 45 -7.4; 49 -7.5; 52 -7.4; 56 -7.4; 59 -7.4; 64 -7.5; 68 -7.5; 73 -7.5; 78 -7.6; 83 -7.8; 89 -8.0; 95 -8.3; 102 -8.7; 109 -8.9; 117 -9.3; 125 -9.6; 134 -9.9; 143 -9.9; 153 -9.8; 164 -9.7; 175 -9.4; 188 -9.1; 201 -8.8; 215 -8.3; 230 -7.9; 246 -7.4; 263 -7.1; 282 -6.5; 301 -6.0; 323 -5.5; 345 -4.9; 369 -4.4; 395 -3.9; 423 -3.2; 452 -2.7; 484 -2.2; 518 -1.7; 554 -1.1; 593 -0.5; 635 -0.1; 679 0.1; 726 0.4; 777 0.7; 832 0.7; 890 0.5; 952 0.3; 1019 -0.1; 1090 -0.4; 1167 -0.8; 1248 -1.3; 1336 -1.7; 1429 -2.3; 1529 -3.1; 1636 -3.8; 1751 -4.4; 1873 -4.8; 2004 -5.2; 2145 -5.8; 2295 -6.7; 2455 -7.7; 2627 -8.9; 2811 -9.9; 3008 -9.5; 3219 -7.1; 3444 -4.7; 3685 -3.8; 3943 -3.9; 4219 -5.4; 4514 -7.0; 4830 -8.3; 5168 -9.7; 5530 -11.2; 5917 -10.3; 6331 -7.6; 6775 -5.6; 7249 -4.3; 7756 -4.3; 8299 -5.7; 8880 -7.2; 9502 -6.7; 10167 -3.2; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 -2.2; 16326 -2.5; 17469 -0.1; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-1.3dB` and instead set Global volume in the UI for both channels to **-13**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Denon AH-C551 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 41 Hz    | 0.28 | -6.6 dB |
| Peaking | 178 Hz   | 0.81 | -6.9 dB |
| Peaking | 2601 Hz  | 1.98 | -8.1 dB |
| Peaking | 5763 Hz  | 1.5  | -9.3 dB |
| Peaking | 15996 Hz | 3.72 | -2.2 dB |
| Peaking | 779 Hz   | 2.87 | 2.1 dB  |
| Peaking | 6742 Hz  | 1.44 | 4.3 dB  |
| Peaking | 5618 Hz  | 3.82 | -4.1 dB |
| Peaking | 9244 Hz  | 2.81 | -8.5 dB |
| Peaking | 10779 Hz | 2.32 | 3.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Denon%20AH-C551/Denon%20AH-C551.png)