# Stax SR-404 Ltd SSL-0670

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.3dB
GraphicEQ: 10 -84; 20 5.8; 22 5.6; 23 5.5; 25 5.4; 26 5.3; 28 5.2; 30 5.1; 32 5.1; 35 5.1; 37 5.1; 40 5.1; 42 5.2; 45 5.2; 49 5.2; 52 5.3; 56 5.4; 59 5.3; 64 5.2; 68 4.9; 73 4.7; 78 4.6; 83 4.5; 89 4.3; 95 4.1; 102 3.6; 109 3.2; 117 2.9; 125 2.5; 134 2.2; 143 2.1; 153 1.9; 164 1.9; 175 1.8; 188 1.7; 201 1.7; 215 1.7; 230 1.7; 246 1.7; 263 1.7; 282 1.7; 301 1.8; 323 1.9; 345 1.9; 369 1.9; 395 1.9; 423 2.0; 452 2.0; 484 1.8; 518 1.6; 554 1.7; 593 1.7; 635 1.6; 679 1.4; 726 1.2; 777 1.3; 832 0.9; 890 0.6; 952 0.4; 1019 -0.0; 1090 -0.3; 1167 -0.8; 1248 -1.3; 1336 -1.9; 1429 -2.6; 1529 -3.1; 1636 -3.4; 1751 -3.3; 1873 -1.8; 2004 -0.1; 2145 1.5; 2295 2.1; 2455 2.0; 2627 1.6; 2811 0.7; 3008 1.0; 3219 1.1; 3444 0.9; 3685 1.3; 3943 3.0; 4219 3.2; 4514 2.0; 4830 1.8; 5168 2.6; 5530 2.3; 5917 0.3; 6331 2.1; 6775 3.7; 7249 1.3; 7756 0.3; 8299 -0.6; 8880 -3.1; 9502 -3.6; 10167 -2.4; 10879 -0.5; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -0.8; 18692 -2.9; 20000 -4.3
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.3dB` and instead set Global volume in the UI for both channels to **-63**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Stax SR-404 Ltd SSL-0670 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 17 Hz    |  0.6  | 5.0 dB  |
| Peaking | 64 Hz    |  0.67 | 4.2 dB  |
| Peaking | 1512 Hz  |  1.53 | -6.2 dB |
| Peaking | 1878 Hz  |  0.19 | 3.0 dB  |
| Peaking | 9404 Hz  |  3.83 | -5.4 dB |
| Peaking | 19738 Hz |  1.89 | -4.4 dB |
| Peaking | 2317 Hz  |  3.83 | 3.0 dB  |
| Peaking | 2803 Hz  |  1.13 | -1.7 dB |
| Peaking | 4117 Hz  |  7.76 | 2.2 dB  |
| Peaking | 6700 Hz  | 12.15 | 3.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Stax%20SR-404%20Ltd%20SSL-0670/Stax%20SR-404%20Ltd%20SSL-0670.png)