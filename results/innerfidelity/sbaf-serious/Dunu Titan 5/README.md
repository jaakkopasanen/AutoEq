# Dunu Titan 5

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.6dB
GraphicEQ: 10 -84; 20 -4.1; 22 -4.2; 23 -4.2; 25 -4.2; 26 -4.3; 28 -4.3; 30 -4.2; 32 -4.2; 35 -4.3; 37 -4.3; 40 -4.2; 42 -4.2; 45 -4.1; 49 -4.0; 52 -4.0; 56 -3.9; 59 -3.9; 64 -3.8; 68 -3.8; 73 -3.7; 78 -3.8; 83 -3.9; 89 -4.1; 95 -4.4; 102 -4.7; 109 -5.0; 117 -5.3; 125 -5.7; 134 -5.9; 143 -5.9; 153 -5.9; 164 -5.8; 175 -5.6; 188 -5.3; 201 -5.1; 215 -4.7; 230 -4.4; 246 -4.0; 263 -3.7; 282 -3.3; 301 -3.0; 323 -2.6; 345 -2.2; 369 -1.9; 395 -1.7; 423 -1.3; 452 -1.0; 484 -0.3; 518 -0.4; 554 -0.2; 593 0.4; 635 0.8; 679 0.7; 726 0.7; 777 1.0; 832 0.8; 890 0.5; 952 0.2; 1019 -0.1; 1090 -0.5; 1167 -0.8; 1248 -1.2; 1336 -1.7; 1429 -2.3; 1529 -2.9; 1636 -3.4; 1751 -3.7; 1873 -3.9; 2004 -4.1; 2145 -4.3; 2295 -4.4; 2455 -4.1; 2627 -3.7; 2811 -2.9; 3008 -1.4; 3219 0.2; 3444 1.7; 3685 2.0; 3943 1.4; 4219 -0.4; 4514 -2.2; 4830 -3.7; 5168 -5.3; 5530 -7.9; 5917 -7.8; 6331 -4.4; 6775 -1.1; 7249 0.7; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.2; 10167 -1.6; 10879 -1.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.6dB` and instead set Global volume in the UI for both channels to **-26**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Dunu Titan 5 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |     Q | Gain    |
|:--------|:---------|:------|:--------|
| Peaking | 25 Hz    |  0.33 | -4.1 dB |
| Peaking | 163 Hz   |  0.93 | -5.3 dB |
| Peaking | 2192 Hz  |  1.58 | -4.9 dB |
| Peaking | 3610 Hz  |  4.12 | 4.1 dB  |
| Peaking | 5631 Hz  |  4.53 | -8.7 dB |
| Peaking | 320 Hz   |  2.04 | -0.7 dB |
| Peaking | 739 Hz   |  1.54 | 1.7 dB  |
| Peaking | 1521 Hz  |  3.75 | -1.1 dB |
| Peaking | 7376 Hz  |  7.44 | 2.2 dB  |
| Peaking | 10451 Hz | 10.16 | -1.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Dunu%20Titan%205/Dunu%20Titan%205.png)