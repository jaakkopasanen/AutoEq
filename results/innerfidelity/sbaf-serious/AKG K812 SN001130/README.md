# AKG K812 SN001130

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.3dB
GraphicEQ: 10 -84; 20 1.7; 22 1.4; 23 1.2; 25 1.0; 26 0.9; 28 0.7; 30 0.5; 32 0.4; 35 0.2; 37 0.1; 40 -0.0; 42 -0.1; 45 -0.1; 49 -0.2; 52 -0.2; 56 -0.2; 59 -0.3; 64 -0.5; 68 -0.6; 73 -0.6; 78 -0.8; 83 -1.1; 89 -1.4; 95 -1.8; 102 -2.3; 109 -2.6; 117 -2.9; 125 -3.5; 134 -3.8; 143 -4.0; 153 -4.2; 164 -4.1; 175 -4.1; 188 -4.3; 201 -4.2; 215 -4.2; 230 -4.2; 246 -4.0; 263 -4.1; 282 -3.9; 301 -3.9; 323 -3.9; 345 -3.6; 369 -3.6; 395 -3.5; 423 -3.3; 452 -3.1; 484 -3.0; 518 -2.8; 554 -2.5; 593 -2.2; 635 -2.0; 679 -1.9; 726 -1.6; 777 -1.1; 832 -0.9; 890 -0.7; 952 -0.2; 1019 -0.0; 1090 0.0; 1167 0.2; 1248 0.5; 1336 0.2; 1429 -0.4; 1529 -0.4; 1636 -1.0; 1751 -0.6; 1873 0.3; 2004 0.8; 2145 0.3; 2295 0.2; 2455 2.2; 2627 2.0; 2811 -0.8; 3008 -2.0; 3219 -2.9; 3444 -3.8; 3685 -4.4; 3943 -3.3; 4219 -1.3; 4514 1.2; 4830 0.3; 5168 -3.2; 5530 -5.8; 5917 -8.9; 6331 -6.9; 6775 -1.6; 7249 -1.8; 7756 -2.8; 8299 -4.0; 8880 -4.4; 9502 -3.4; 10167 -1.1; 10879 -0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 -0.0; 16326 -1.3; 17469 -2.7; 18692 -4.4; 20000 -6.7
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.3dB` and instead set Global volume in the UI for both channels to **-33**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K812 SN001130 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 14 Hz    |  0.12 | 1.1 dB  |
| Peaking | 210 Hz   |  0.5  | -4.7 dB |
| Peaking | 3572 Hz  |  6.01 | -4.5 dB |
| Peaking | 6004 Hz  |  5.19 | -9.2 dB |
| Peaking | 28140 Hz |  1.26 | -6.4 dB |
| Peaking | 2505 Hz  | 11.1  | 3.4 dB  |
| Peaking | 10512 Hz |  3.87 | 1.8 dB  |
| Peaking | 6840 Hz  |  8.62 | 2.4 dB  |
| Peaking | 8937 Hz  |  2.08 | -6.4 dB |
| Peaking | 9858 Hz  |  0.72 | 2.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K812%20SN001130/AKG%20K812%20SN001130.png)