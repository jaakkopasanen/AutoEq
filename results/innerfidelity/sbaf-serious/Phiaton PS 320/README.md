# Phiaton PS 320

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 2.5; 22 2.3; 23 2.2; 25 2.0; 26 2.0; 28 1.9; 30 1.8; 32 1.8; 35 1.7; 37 1.7; 40 1.6; 42 1.6; 45 1.5; 49 1.3; 52 1.1; 56 1.1; 59 1.0; 64 0.9; 68 1.1; 73 1.4; 78 1.5; 83 1.1; 89 0.4; 95 -0.4; 102 -1.3; 109 -1.9; 117 -2.2; 125 -2.7; 134 -3.1; 143 -3.5; 153 -3.8; 164 -3.7; 175 -3.7; 188 -3.6; 201 -3.4; 215 -2.8; 230 -2.2; 246 -2.3; 263 -3.1; 282 -3.3; 301 -3.2; 323 -2.7; 345 -2.0; 369 -1.1; 395 -0.2; 423 1.0; 452 2.0; 484 2.8; 518 3.3; 554 3.8; 593 4.2; 635 4.3; 679 3.8; 726 2.9; 777 2.3; 832 1.5; 890 0.9; 952 0.3; 1019 -0.1; 1090 -0.4; 1167 -0.7; 1248 -0.9; 1336 -1.6; 1429 -2.5; 1529 -2.7; 1636 -2.9; 1751 -3.3; 1873 -3.1; 2004 -3.1; 2145 -3.7; 2295 -3.5; 2455 -2.3; 2627 -0.9; 2811 0.4; 3008 1.7; 3219 2.6; 3444 3.8; 3685 5.7; 3943 5.5; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 4.8; 6331 1.3; 6775 0.6; 7249 1.2; 7756 0.3; 8299 -0.4; 8880 -1.9; 9502 -1.5; 10167 -0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 -0.1; 16326 -1.9; 17469 -3.2; 18692 -3.5; 20000 -2.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton PS 320 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 220 Hz   |  0.86 | -4.0 dB |
| Peaking | 594 Hz   |  1.67 | 5.5 dB  |
| Peaking | 1998 Hz  |  1.24 | -4.9 dB |
| Peaking | 4294 Hz  |  1.51 | 7.7 dB  |
| Peaking | 18633 Hz |  1.25 | -3.8 dB |
| Peaking | 27 Hz    |  0.87 | 2.4 dB  |
| Peaking | 77 Hz    |  4.67 | 1.9 dB  |
| Peaking | 1421 Hz  |  2.67 | -0.1 dB |
| Peaking | 5622 Hz  | 10.86 | 2.7 dB  |
| Peaking | 8926 Hz  |  4.54 | -2.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Phiaton%20PS%20320/Phiaton%20PS%20320.png)