# HiFiMAN HE-5LE

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.5dB
GraphicEQ: 10 -84; 20 4.6; 22 3.2; 23 2.6; 25 1.7; 26 1.3; 28 0.9; 30 0.8; 32 0.8; 35 1.0; 37 1.1; 40 1.2; 42 1.3; 45 1.4; 49 1.6; 52 1.7; 56 1.8; 59 1.7; 64 1.4; 68 1.3; 73 1.3; 78 1.3; 83 1.1; 89 0.9; 95 0.7; 102 0.5; 109 0.4; 117 0.1; 125 -0.4; 134 -0.9; 143 -1.4; 153 -2.0; 164 -2.3; 175 -2.5; 188 -2.6; 201 -2.7; 215 -2.7; 230 -2.8; 246 -3.0; 263 -3.0; 282 -3.1; 301 -3.1; 323 -3.0; 345 -3.0; 369 -3.0; 395 -3.0; 423 -2.8; 452 -2.8; 484 -2.9; 518 -2.9; 554 -3.1; 593 -2.7; 635 -1.3; 679 -0.7; 726 0.7; 777 1.5; 832 1.2; 890 0.6; 952 0.1; 1019 -0.1; 1090 0.4; 1167 1.1; 1248 1.8; 1336 2.4; 1429 3.2; 1529 3.7; 1636 3.9; 1751 4.7; 1873 5.3; 2004 4.3; 2145 3.4; 2295 3.1; 2455 4.3; 2627 3.9; 2811 3.1; 3008 2.7; 3219 2.3; 3444 2.4; 3685 2.4; 3943 1.0; 4219 -1.0; 4514 -0.6; 4830 -3.2; 5168 -0.5; 5530 0.7; 5917 -3.0; 6331 -3.7; 6775 -3.5; 7249 -3.1; 7756 -3.7; 8299 -5.5; 8880 -7.3; 9502 -7.0; 10167 -4.3; 10879 -1.1; 11640 -0.0; 12455 0.0; 13327 -0.4; 14260 -0.9; 15258 -1.0; 16326 -1.0; 17469 -1.3; 18692 -1.8; 20000 -2.4
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.467028422996609dB` and instead set Global volume in the UI for both channels to **-54**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE-5LE ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.8dB.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 16 Hz    |  0.08 | 2.1 dB  |
| Peaking | 271 Hz   |  0.6  | -4.2 dB |
| Peaking | 1751 Hz  |  1.5  | 4.6 dB  |
| Peaking | 2816 Hz  |  2.53 | 2.4 dB  |
| Peaking | 8734 Hz  |  2.05 | -6.9 dB |
| Peaking | 32 Hz    |  3.17 | -1.1 dB |
| Peaking | 559 Hz   |  4.65 | -1.6 dB |
| Peaking | 771 Hz   |  5.82 | 2.4 dB  |
| Peaking | 6176 Hz  | 10.37 | -2.6 dB |
| Peaking | 11482 Hz |  6.11 | 2.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20HE-5LE/HiFiMAN%20HE-5LE.png)