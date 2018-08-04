# HiFiMAN Edition X

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 5.9; 26 5.8; 28 5.5; 30 5.2; 32 4.9; 35 4.5; 37 4.4; 40 4.2; 42 4.1; 45 4.1; 49 4.0; 52 4.0; 56 3.9; 59 3.9; 64 3.9; 68 3.9; 73 3.9; 78 3.7; 83 3.4; 89 3.0; 95 2.6; 102 2.3; 109 2.1; 117 1.9; 125 1.5; 134 1.3; 143 1.2; 153 1.1; 164 1.0; 175 0.9; 188 0.9; 201 0.9; 215 0.9; 230 0.8; 246 0.7; 263 0.6; 282 0.6; 301 0.5; 323 0.5; 345 1.2; 369 1.4; 395 1.6; 423 1.5; 452 1.1; 484 0.6; 518 0.3; 554 0.1; 593 0.5; 635 0.2; 679 0.3; 726 1.1; 777 2.7; 832 2.4; 890 1.1; 952 0.4; 1019 0.8; 1090 2.7; 1167 3.9; 1248 3.8; 1336 2.2; 1429 2.9; 1529 2.8; 1636 2.5; 1751 1.6; 1873 2.1; 2004 2.4; 2145 2.0; 2295 2.1; 2455 2.2; 2627 2.0; 2811 1.8; 3008 1.5; 3219 1.8; 3444 2.8; 3685 2.6; 3943 2.1; 4219 0.7; 4514 0.1; 4830 1.2; 5168 3.3; 5530 4.5; 5917 4.0; 6331 2.2; 6775 2.3; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 -0.4; 20000 -5.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN Edition X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 22 Hz   |  0.95 | 5.5 dB  |
| Peaking | 66 Hz   |  0.76 | 3.1 dB  |
| Peaking | 1427 Hz |  0.81 | 2.8 dB  |
| Peaking | 3539 Hz |  5.23 | 2.0 dB  |
| Peaking | 5706 Hz |  4.56 | 4.5 dB  |
| Peaking | 396 Hz  |  4.29 | 1.3 dB  |
| Peaking | 644 Hz  |  2.93 | -1.0 dB |
| Peaking | 962 Hz  | 10.28 | -2.0 dB |
| Peaking | 792 Hz  |  7.65 | 2.0 dB  |
| Peaking | 4501 Hz | 11.98 | -1.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20Edition%20X/HiFiMAN%20Edition%20X.png)