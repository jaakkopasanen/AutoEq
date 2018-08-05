# HiFiMAN Edition X V2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.4dB
GraphicEQ: 10 -84; 20 4.9; 22 4.4; 23 4.2; 25 3.9; 26 3.8; 28 3.6; 30 3.4; 32 3.3; 35 3.2; 37 3.2; 40 3.2; 42 3.3; 45 3.4; 49 3.5; 52 3.4; 56 3.0; 59 2.5; 64 2.0; 68 1.9; 73 1.7; 78 1.8; 83 1.7; 89 1.5; 95 1.2; 102 0.8; 109 0.7; 117 0.2; 125 -0.2; 134 -0.3; 143 -0.6; 153 -0.8; 164 -1.0; 175 -1.0; 188 -1.1; 201 -1.2; 215 -1.3; 230 -1.4; 246 -1.5; 263 -1.8; 282 -2.0; 301 -1.7; 323 0.1; 345 -1.3; 369 0.5; 395 0.1; 423 -0.3; 452 -0.9; 484 -1.7; 518 -2.5; 554 -1.6; 593 0.5; 635 -1.6; 679 -0.6; 726 1.8; 777 0.6; 832 1.7; 890 1.1; 952 -0.1; 1019 1.8; 1090 4.7; 1167 3.4; 1248 3.2; 1336 3.6; 1429 5.8; 1529 4.5; 1636 5.2; 1751 4.7; 1873 4.5; 2004 3.5; 2145 3.2; 2295 2.2; 2455 1.6; 2627 1.1; 2811 0.5; 3008 1.1; 3219 1.0; 3444 1.3; 3685 1.8; 3943 1.7; 4219 0.7; 4514 0.7; 4830 1.1; 5168 2.1; 5530 4.0; 5917 3.5; 6331 0.4; 6775 -0.4; 7249 1.0; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -0.2; 18692 -2.9; 20000 -3.5
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.4dB` and instead set Global volume in the UI for both channels to **-64**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN Edition X V2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 15 Hz   | 1    | 4.8 dB  |
| Peaking | 54 Hz   | 0.57 | 3.3 dB  |
| Peaking | 207 Hz  | 0.31 | -1.9 dB |
| Peaking | 1523 Hz | 1.26 | 5.4 dB  |
| Peaking | 5623 Hz | 6.84 | 4.3 dB  |
| Peaking | 395 Hz  | 3.13 | 3.8 dB  |
| Peaking | 435 Hz  | 1.53 | -2.5 dB |
| Peaking | 729 Hz  | 8.93 | 1.8 dB  |
| Peaking | 3507 Hz | 1.88 | -1.0 dB |
| Peaking | 3710 Hz | 4.53 | 2.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20Edition%20X%20V2/HiFiMAN%20Edition%20X%20V2.png)