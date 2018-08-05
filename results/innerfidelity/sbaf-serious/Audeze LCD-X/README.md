# Audeze LCD-X

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 4.0; 22 4.0; 23 4.0; 25 3.9; 26 3.8; 28 3.6; 30 3.3; 32 2.8; 35 2.1; 37 1.7; 40 1.4; 42 1.3; 45 1.2; 49 1.2; 52 1.2; 56 1.3; 59 1.3; 64 1.3; 68 1.3; 73 1.3; 78 1.2; 83 1.1; 89 0.8; 95 0.5; 102 0.2; 109 -0.1; 117 -0.4; 125 -0.9; 134 -1.2; 143 -1.4; 153 -1.6; 164 -1.6; 175 -1.8; 188 -1.9; 201 -1.9; 215 -1.9; 230 -1.8; 246 -1.8; 263 -1.8; 282 -1.7; 301 -1.6; 323 -1.5; 345 -1.3; 369 -1.2; 395 -1.1; 423 -0.8; 452 -0.8; 484 -1.2; 518 -1.3; 554 -0.9; 593 -0.6; 635 -0.6; 679 -0.7; 726 -0.7; 777 -0.4; 832 -0.3; 890 -0.1; 952 0.0; 1019 0.1; 1090 0.3; 1167 0.1; 1248 0.1; 1336 -0.4; 1429 -0.6; 1529 -0.8; 1636 -0.9; 1751 -0.7; 1873 -0.8; 2004 -0.9; 2145 -0.9; 2295 -0.3; 2455 0.7; 2627 1.9; 2811 3.1; 3008 4.3; 3219 5.1; 3444 5.6; 3685 5.0; 3943 3.5; 4219 3.3; 4514 2.5; 4830 2.8; 5168 5.2; 5530 6.0; 5917 5.2; 6331 3.7; 6775 3.0; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 -0.2; 16326 -1.4; 17469 -2.6; 18692 -3.8; 20000 -5.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 23 Hz    | 1.08 | 4.3 dB  |
| Peaking | 80 Hz    | 1.03 | 3.0 dB  |
| Peaking | 144 Hz   | 0.38 | -2.6 dB |
| Peaking | 3383 Hz  | 3.34 | 5.7 dB  |
| Peaking | 5630 Hz  | 3.49 | 5.9 dB  |
| Peaking | 1076 Hz  | 3.25 | 0.7 dB  |
| Peaking | 2054 Hz  | 1.71 | -1.6 dB |
| Peaking | 2778 Hz  | 4.34 | 1.6 dB  |
| Peaking | 19650 Hz | 1.35 | -4.8 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-X/Audeze%20LCD-X.png)