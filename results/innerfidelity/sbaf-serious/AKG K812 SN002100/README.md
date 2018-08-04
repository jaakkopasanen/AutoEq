# AKG K812 SN002100

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.3dB
GraphicEQ: 10 -84; 20 0.2; 22 -0.1; 23 -0.3; 25 -0.6; 26 -0.7; 28 -0.9; 30 -1.0; 32 -1.1; 35 -1.3; 37 -1.4; 40 -1.5; 42 -1.6; 45 -1.7; 49 -1.7; 52 -1.8; 56 -1.9; 59 -1.9; 64 -2.0; 68 -2.0; 73 -2.0; 78 -2.0; 83 -2.2; 89 -2.6; 95 -2.9; 102 -3.3; 109 -3.6; 117 -4.0; 125 -4.5; 134 -4.7; 143 -4.8; 153 -5.0; 164 -5.1; 175 -5.0; 188 -5.0; 201 -5.1; 215 -5.0; 230 -4.8; 246 -4.7; 263 -4.7; 282 -4.5; 301 -4.4; 323 -4.3; 345 -4.1; 369 -4.0; 395 -3.9; 423 -3.5; 452 -3.3; 484 -3.2; 518 -3.0; 554 -2.6; 593 -2.2; 635 -2.0; 679 -1.8; 726 -1.4; 777 -0.8; 832 -0.4; 890 -0.3; 952 -0.3; 1019 0.1; 1090 0.7; 1167 0.8; 1248 0.9; 1336 1.1; 1429 0.5; 1529 -0.1; 1636 0.3; 1751 1.1; 1873 1.5; 2004 1.0; 2145 1.0; 2295 1.0; 2455 2.5; 2627 4.4; 2811 1.7; 3008 -1.2; 3219 -2.0; 3444 -1.5; 3685 0.1; 3943 2.5; 4219 4.7; 4514 2.5; 4830 -1.4; 5168 -4.2; 5530 -6.9; 5917 -8.7; 6331 -5.6; 6775 -0.5; 7249 -0.5; 7756 -1.5; 8299 -2.7; 8880 -3.1; 9502 -2.4; 10167 -0.6; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -2.0; 20000 -8.7
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.3dB` and instead set Global volume in the UI for both channels to **-53**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K812 SN002100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 201 Hz   | 0.49 | -5.2 dB |
| Peaking | 4244 Hz  | 6.16 | 6.3 dB  |
| Peaking | 2780 Hz  | 2.17 | 6.3 dB  |
| Peaking | 5774 Hz  | 3.95 | -9.2 dB |
| Peaking | 3127 Hz  | 3.46 | -6.9 dB |
| Peaking | 38 Hz    | 2.1  | -0.8 dB |
| Peaking | 1174 Hz  | 3.2  | 1.4 dB  |
| Peaking | 7021 Hz  | 6.45 | 3.6 dB  |
| Peaking | 9288 Hz  | 1.84 | -4.0 dB |
| Peaking | 10487 Hz | 2.57 | 2.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K812%20SN002100/AKG%20K812%20SN002100.png)