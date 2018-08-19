# AKG K812 sn001130

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.9dB
GraphicEQ: 10 -84; 20 1.7; 22 1.4; 23 1.2; 25 1.0; 26 0.9; 28 0.7; 30 0.5; 32 0.3; 35 0.1; 37 0.0; 40 -0.1; 42 -0.2; 45 -0.3; 49 -0.4; 52 -0.5; 56 -0.6; 59 -0.7; 64 -1.0; 68 -1.2; 73 -1.3; 78 -1.5; 83 -1.9; 89 -2.2; 95 -2.6; 102 -2.9; 109 -3.0; 117 -3.1; 125 -3.5; 134 -3.7; 143 -3.8; 153 -3.9; 164 -3.9; 175 -3.9; 188 -4.1; 201 -4.0; 215 -4.1; 230 -4.1; 246 -3.9; 263 -4.0; 282 -3.8; 301 -3.8; 323 -3.8; 345 -3.6; 369 -3.6; 395 -3.5; 423 -3.3; 452 -3.1; 484 -3.0; 518 -2.8; 554 -2.5; 593 -2.2; 635 -2.0; 679 -1.8; 726 -1.6; 777 -1.1; 832 -0.9; 890 -0.7; 952 -0.2; 1019 -0.0; 1090 0.0; 1167 0.2; 1248 0.5; 1336 0.2; 1429 -0.4; 1529 -0.4; 1636 -1.0; 1751 -0.6; 1873 0.3; 2004 0.8; 2145 0.3; 2295 0.2; 2455 2.2; 2627 2.0; 2811 -0.8; 3008 -2.0; 3219 -2.9; 3444 -3.8; 3685 -4.4; 3943 -3.3; 4219 -1.3; 4514 1.2; 4830 0.3; 5168 -3.2; 5530 -5.8; 5917 -8.9; 6331 -6.9; 6775 -1.6; 7249 -1.8; 7756 -2.8; 8299 -4.0; 8880 -4.4; 9502 -3.4; 10167 -1.1; 10879 -0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 -0.0; 16326 -1.3; 17469 -2.7; 18692 -4.4; 20000 -6.7
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.8641986819750502dB` and instead set Global volume in the UI for both channels to **-28**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K812 sn001130 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -1.5dB.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 11 Hz    |  0.54 | 2.3 dB  |
| Peaking | 215 Hz   |  0.47 | -4.3 dB |
| Peaking | 3573 Hz  |  5.88 | -4.4 dB |
| Peaking | 5991 Hz  |  5.13 | -9.1 dB |
| Peaking | 19908 Hz |  1.27 | -6.4 dB |
| Peaking | 2519 Hz  | 11    | 3.4 dB  |
| Peaking | 6926 Hz  |  8.56 | 2.3 dB  |
| Peaking | 8996 Hz  |  2.06 | -6.5 dB |
| Peaking | 9539 Hz  |  0.73 | 2.1 dB  |
| Peaking | 10389 Hz |  3.53 | 1.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K812%20sn001130/AKG%20K812%20sn001130.png)