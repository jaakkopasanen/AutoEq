# Enigmatic Audio Paradox

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 4.2; 22 3.9; 23 3.8; 25 3.5; 26 3.4; 28 3.2; 30 3.0; 32 2.8; 35 2.7; 37 2.6; 40 2.6; 42 2.5; 45 2.5; 49 2.5; 52 2.5; 56 2.2; 59 1.9; 64 1.7; 68 1.8; 73 1.8; 78 1.8; 83 1.8; 89 1.5; 95 0.7; 102 -0.7; 109 -1.7; 117 -2.5; 125 -3.2; 134 -3.5; 143 -3.7; 153 -3.6; 164 -3.1; 175 -3.8; 188 -4.1; 201 -4.0; 215 -3.9; 230 -3.8; 246 -3.6; 263 -3.5; 282 -3.1; 301 -2.9; 323 -2.6; 345 -1.6; 369 -0.3; 395 0.2; 423 0.4; 452 0.6; 484 0.7; 518 0.7; 554 0.9; 593 1.2; 635 2.1; 679 2.4; 726 1.8; 777 1.7; 832 1.7; 890 1.1; 952 0.4; 1019 -0.1; 1090 -0.4; 1167 -0.4; 1248 -0.3; 1336 -0.4; 1429 -0.2; 1529 0.0; 1636 0.6; 1751 0.8; 1873 1.4; 2004 2.3; 2145 3.2; 2295 4.1; 2455 4.9; 2627 5.6; 2811 6.0; 3008 6.0; 3219 5.8; 3444 5.1; 3685 4.4; 3943 4.3; 4219 4.2; 4514 4.7; 4830 5.9; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.2; 8880 -2.3; 9502 -1.8; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Enigmatic Audio Paradox ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 36 Hz   | 0.19 | 3.7 dB  |
| Peaking | 175 Hz  | 0.76 | -6.4 dB |
| Peaking | 623 Hz  | 1.82 | 2.5 dB  |
| Peaking | 2911 Hz | 1.93 | 6.0 dB  |
| Peaking | 5463 Hz | 2.56 | 6.1 dB  |
| Peaking | 88 Hz   | 4.63 | 1.3 dB  |
| Peaking | 120 Hz  | 5.01 | -1.2 dB |
| Peaking | 823 Hz  | 4.94 | 0.9 dB  |
| Peaking | 1222 Hz | 2.35 | -1.3 dB |
| Peaking | 9040 Hz | 6.08 | -3.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Enigmatic%20Audio%20Paradox/Enigmatic%20Audio%20Paradox.png)