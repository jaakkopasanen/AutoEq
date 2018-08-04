# HiFiMAN Sundara

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.4dB
GraphicEQ: 10 -84; 20 4.9; 22 4.6; 23 4.4; 25 4.2; 26 4.1; 28 3.9; 30 3.8; 32 3.7; 35 3.7; 37 3.7; 40 3.6; 42 3.7; 45 3.7; 49 3.7; 52 3.6; 56 3.5; 59 3.3; 64 2.9; 68 2.7; 73 2.5; 78 2.5; 83 2.4; 89 2.2; 95 2.0; 102 1.6; 109 1.4; 117 1.1; 125 0.7; 134 0.4; 143 0.2; 153 0.1; 164 -0.0; 175 -0.0; 188 -0.1; 201 -0.3; 215 -0.2; 230 -0.3; 246 -0.3; 263 -0.4; 282 -0.4; 301 -0.4; 323 -0.5; 345 -0.5; 369 -0.5; 395 -0.6; 423 -0.5; 452 -0.2; 484 0.3; 518 0.6; 554 0.5; 593 0.4; 635 -0.1; 679 -0.6; 726 -0.5; 777 -0.3; 832 -0.5; 890 -0.7; 952 -0.7; 1019 0.7; 1090 1.7; 1167 1.2; 1248 1.4; 1336 1.3; 1429 1.3; 1529 1.3; 1636 1.9; 1751 2.0; 1873 2.2; 2004 2.2; 2145 1.6; 2295 2.2; 2455 1.8; 2627 0.5; 2811 -0.2; 3008 -0.2; 3219 -1.3; 3444 -0.7; 3685 -0.2; 3943 -0.9; 4219 -2.1; 4514 -2.4; 4830 -2.2; 5168 -1.9; 5530 -0.3; 5917 -1.7; 6331 2.1; 6775 -0.9; 7249 -1.0; 7756 -1.2; 8299 -2.2; 8880 -2.4; 9502 -0.4; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.4dB` and instead set Global volume in the UI for both channels to **-54**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN Sundara ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 20 Hz   |  0.7  | 4.3 dB  |
| Peaking | 58 Hz   |  1.12 | 2.5 dB  |
| Peaking | 1864 Hz |  1.72 | 2.4 dB  |
| Peaking | 4533 Hz |  2.98 | -2.6 dB |
| Peaking | 8529 Hz |  6.09 | -2.7 dB |
| Peaking | 274 Hz  |  1.25 | -0.6 dB |
| Peaking | 956 Hz  |  3.5  | -2.3 dB |
| Peaking | 1065 Hz |  4.11 | 2.5 dB  |
| Peaking | 3202 Hz | 10.58 | -1.4 dB |
| Peaking | 6342 Hz | 19.45 | 2.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20Sundara/HiFiMAN%20Sundara.png)