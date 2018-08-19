# Phiaton PS 320

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 2.5; 22 2.3; 23 2.2; 25 2.0; 26 2.0; 28 1.9; 30 1.8; 32 1.7; 35 1.6; 37 1.6; 40 1.5; 42 1.5; 45 1.3; 49 1.0; 52 0.9; 56 0.7; 59 0.6; 64 0.4; 68 0.5; 73 0.7; 78 0.7; 83 0.3; 89 -0.4; 95 -1.1; 102 -1.9; 109 -2.3; 117 -2.4; 125 -2.7; 134 -3.0; 143 -3.3; 153 -3.5; 164 -3.5; 175 -3.5; 188 -3.4; 201 -3.2; 215 -2.7; 230 -2.0; 246 -2.2; 263 -3.0; 282 -3.2; 301 -3.1; 323 -2.7; 345 -1.9; 369 -1.1; 395 -0.2; 423 1.0; 452 2.0; 484 2.8; 518 3.3; 554 3.8; 593 4.3; 635 4.3; 679 3.8; 726 2.9; 777 2.3; 832 1.5; 890 0.9; 952 0.3; 1019 -0.1; 1090 -0.4; 1167 -0.7; 1248 -0.9; 1336 -1.6; 1429 -2.5; 1529 -2.7; 1636 -2.9; 1751 -3.3; 1873 -3.1; 2004 -3.1; 2145 -3.7; 2295 -3.5; 2455 -2.3; 2627 -0.9; 2811 0.4; 3008 1.7; 3219 2.6; 3444 3.8; 3685 5.7; 3943 5.5; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 4.8; 6331 1.3; 6775 0.6; 7249 1.2; 7756 0.3; 8299 -0.4; 8880 -1.9; 9502 -1.5; 10167 -0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 -0.1; 16326 -1.9; 17469 -3.2; 18692 -3.5; 20000 -2.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099993182728349dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Phiaton PS 320 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.9dB.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 226 Hz   |  0.73 | -3.9 dB |
| Peaking | 589 Hz   |  1.57 | 5.8 dB  |
| Peaking | 1997 Hz  |  1.23 | -4.9 dB |
| Peaking | 4291 Hz  |  1.51 | 7.7 dB  |
| Peaking | 18633 Hz |  1.25 | -3.8 dB |
| Peaking | 25 Hz    |  0.96 | 2.3 dB  |
| Peaking | 74 Hz    |  5.45 | 1.4 dB  |
| Peaking | 1420 Hz  |  2.72 | -0.1 dB |
| Peaking | 5609 Hz  | 10.85 | 2.7 dB  |
| Peaking | 8898 Hz  |  4.55 | -2.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Phiaton%20PS%20320/Phiaton%20PS%20320.png)