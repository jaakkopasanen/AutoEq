# HiFiMAN HE-500

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -1.5; 22 -1.9; 23 -2.1; 25 -2.5; 26 -2.6; 28 -2.8; 30 -3.0; 32 -3.2; 35 -3.4; 37 -3.4; 40 -3.4; 42 -3.4; 45 -3.3; 49 -3.2; 52 -3.1; 56 -3.2; 59 -3.4; 64 -3.5; 68 -3.4; 73 -3.3; 78 -3.1; 83 -3.0; 89 -3.2; 95 -3.1; 102 -3.0; 109 -3.0; 117 -2.9; 125 -2.8; 134 -2.8; 143 -2.7; 153 -2.5; 164 -2.6; 175 -2.5; 188 -2.5; 201 -2.4; 215 -2.4; 230 -2.5; 246 -2.5; 263 -2.7; 282 -2.6; 301 -2.5; 323 -2.4; 345 -2.4; 369 -2.5; 395 -2.1; 423 -1.9; 452 -2.0; 484 -2.0; 518 -1.4; 554 -1.4; 593 -1.3; 635 -0.9; 679 -0.8; 726 0.1; 777 0.6; 832 0.2; 890 -0.3; 952 0.1; 1019 -0.2; 1090 -0.2; 1167 0.5; 1248 1.0; 1336 2.3; 1429 3.1; 1529 3.3; 1636 3.8; 1751 4.8; 1873 5.4; 2004 5.7; 2145 4.7; 2295 4.0; 2455 5.6; 2627 5.6; 2811 4.7; 3008 3.4; 3219 2.8; 3444 2.2; 3685 2.7; 3943 2.7; 4219 2.4; 4514 3.0; 4830 4.3; 5168 5.9; 5530 6.0; 5917 5.4; 6331 2.8; 6775 1.2; 7249 1.0; 7756 0.2; 8299 -1.6; 8880 -3.7; 9502 -2.9; 10167 -0.1; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN HE-500 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 51 Hz   |  0.38 | -3.3 dB |
| Peaking | 338 Hz  |  0.56 | -2.0 dB |
| Peaking | 2140 Hz |  1.16 | 5.6 dB  |
| Peaking | 5466 Hz |  3.37 | 5.9 dB  |
| Peaking | 8987 Hz |  5.53 | -4.7 dB |
| Peaking | 766 Hz  |  7.54 | 1.3 dB  |
| Peaking | 1150 Hz |  2.51 | -1.9 dB |
| Peaking | 1355 Hz |  2.02 | 1.3 dB  |
| Peaking | 2257 Hz | 11.4  | -2.1 dB |
| Peaking | 2599 Hz |  7.98 | 1.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/headphonecom/HiFiMAN%20HE-500/HiFiMAN%20HE-500.png)