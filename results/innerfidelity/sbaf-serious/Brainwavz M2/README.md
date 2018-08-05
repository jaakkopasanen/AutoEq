# Brainwavz M2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 5.9; 37 5.8; 40 5.4; 42 5.2; 45 5.0; 49 4.6; 52 4.4; 56 4.1; 59 3.9; 64 3.6; 68 3.4; 73 3.1; 78 2.7; 83 2.4; 89 1.9; 95 1.4; 102 0.7; 109 0.2; 117 -0.3; 125 -1.0; 134 -1.5; 143 -1.8; 153 -2.1; 164 -2.2; 175 -2.3; 188 -2.2; 201 -2.2; 215 -2.1; 230 -2.0; 246 -1.8; 263 -1.7; 282 -1.5; 301 -1.3; 323 -1.0; 345 -0.8; 369 -0.6; 395 -0.4; 423 -0.0; 452 0.2; 484 0.3; 518 0.6; 554 0.9; 593 1.2; 635 1.4; 679 1.3; 726 1.3; 777 1.4; 832 1.1; 890 0.8; 952 0.4; 1019 -0.1; 1090 -0.6; 1167 -1.0; 1248 -1.4; 1336 -2.2; 1429 -2.8; 1529 -3.4; 1636 -3.6; 1751 -3.2; 1873 -2.0; 2004 0.1; 2145 2.0; 2295 2.5; 2455 2.5; 2627 3.8; 2811 5.4; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 5.3; 4830 4.4; 5168 4.2; 5530 4.2; 5917 4.8; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Brainwavz M2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 24 Hz   | 0.28 | 6.2 dB  |
| Peaking | 164 Hz  | 1.06 | -3.9 dB |
| Peaking | 1634 Hz | 2.71 | -5.6 dB |
| Peaking | 3446 Hz | 1.11 | 6.7 dB  |
| Peaking | 6217 Hz | 5.86 | 3.7 dB  |
| Peaking | 304 Hz  | 2.21 | -0.7 dB |
| Peaking | 710 Hz  | 1.33 | 1.7 dB  |
| Peaking | 1182 Hz | 2.62 | -1.1 dB |
| Peaking | 6656 Hz | 1.98 | 2.0 dB  |
| Peaking | 7930 Hz | 1.88 | -2.6 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Brainwavz%20M2/Brainwavz%20M2.png)