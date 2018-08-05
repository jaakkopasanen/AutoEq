# AKG K3003 Bass Boost Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.8dB
GraphicEQ: 10 -84; 20 -0.4; 22 -0.9; 23 -1.1; 25 -1.5; 26 -1.7; 28 -2.1; 30 -2.4; 32 -2.6; 35 -3.0; 37 -3.2; 40 -3.5; 42 -3.6; 45 -3.8; 49 -4.0; 52 -4.1; 56 -4.3; 59 -4.4; 64 -4.6; 68 -4.8; 73 -5.0; 78 -5.2; 83 -5.5; 89 -5.9; 95 -6.4; 102 -7.0; 109 -7.4; 117 -7.8; 125 -8.4; 134 -8.8; 143 -9.1; 153 -9.2; 164 -9.2; 175 -9.1; 188 -9.0; 201 -8.9; 215 -8.6; 230 -8.3; 246 -8.1; 263 -7.8; 282 -7.4; 301 -7.1; 323 -6.6; 345 -6.2; 369 -5.7; 395 -5.3; 423 -4.6; 452 -4.2; 484 -3.8; 518 -3.3; 554 -2.7; 593 -2.0; 635 -1.5; 679 -1.2; 726 -0.8; 777 -0.3; 832 -0.2; 890 -0.1; 952 -0.1; 1019 0.0; 1090 -0.1; 1167 -0.1; 1248 -0.2; 1336 -0.3; 1429 -0.1; 1529 -0.4; 1636 -1.0; 1751 -1.6; 1873 -1.8; 2004 -2.0; 2145 -2.2; 2295 -2.3; 2455 -1.7; 2627 -0.7; 2811 0.7; 3008 2.7; 3219 4.2; 3444 5.2; 3685 4.9; 3943 3.7; 4219 1.2; 4514 -1.3; 4830 -3.2; 5168 -4.6; 5530 -3.7; 5917 -0.9; 6331 1.5; 6775 2.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -0.7; 9502 -2.4; 10167 -1.6; 10879 -0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.8dB` and instead set Global volume in the UI for both channels to **-58**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `AKG K3003 Bass Boost Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 90 Hz   |  0.32 | -3.2 dB |
| Peaking | 197 Hz  |  0.64 | -6.9 dB |
| Peaking | 2421 Hz |  1.71 | -7.8 dB |
| Peaking | 3301 Hz |  1.05 | 9.0 dB  |
| Peaking | 5015 Hz |  3.45 | -8.6 dB |
| Peaking | 3 Hz    |  2.29 | 0.6 dB  |
| Peaking | 838 Hz  |  2.95 | 1.1 dB  |
| Peaking | 5574 Hz | 10.27 | -1.5 dB |
| Peaking | 6678 Hz |  6.74 | 2.8 dB  |
| Peaking | 9588 Hz |  5.38 | -3.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/AKG%20K3003%20Bass%20Boost%20Filter/AKG%20K3003%20Bass%20Boost%20Filter.png)