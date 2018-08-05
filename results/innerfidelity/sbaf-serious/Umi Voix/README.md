# Umi Voix

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -3.5; 22 -3.6; 23 -3.6; 25 -3.6; 26 -3.6; 28 -3.6; 30 -3.7; 32 -3.7; 35 -3.7; 37 -3.6; 40 -3.6; 42 -3.6; 45 -3.5; 49 -3.5; 52 -3.4; 56 -3.3; 59 -3.2; 64 -3.2; 68 -3.2; 73 -3.2; 78 -3.2; 83 -3.3; 89 -3.6; 95 -3.9; 102 -4.2; 109 -4.5; 117 -4.9; 125 -5.3; 134 -5.4; 143 -5.5; 153 -5.5; 164 -5.5; 175 -5.2; 188 -4.8; 201 -4.6; 215 -4.1; 230 -3.8; 246 -3.3; 263 -2.9; 282 -2.3; 301 -1.7; 323 -1.2; 345 -0.5; 369 0.1; 395 0.7; 423 1.3; 452 2.2; 484 2.4; 518 2.6; 554 2.8; 593 3.3; 635 3.2; 679 2.9; 726 2.6; 777 2.4; 832 1.8; 890 1.2; 952 0.6; 1019 -0.2; 1090 -0.8; 1167 -1.3; 1248 -1.8; 1336 -2.2; 1429 -2.6; 1529 -2.7; 1636 -2.4; 1751 -1.6; 1873 -0.5; 2004 1.0; 2145 2.6; 2295 4.1; 2455 5.8; 2627 6.0; 2811 6.0; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 5.5; 4219 2.9; 4514 3.3; 4830 5.7; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Umi Voix ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-8.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 0.51 | -3.5 dB |
| Peaking | 158 Hz  | 0.84 | -5.3 dB |
| Peaking | 554 Hz  | 1.86 | 4.2 dB  |
| Peaking | 3045 Hz | 2.28 | 6.6 dB  |
| Peaking | 5582 Hz | 2.62 | 6.1 dB  |
| Peaking | 786 Hz  | 3.27 | 1.5 dB  |
| Peaking | 1507 Hz | 1.86 | -3.8 dB |
| Peaking | 2375 Hz | 4.64 | 3.1 dB  |
| Peaking | 6575 Hz | 6.66 | 2.3 dB  |
| Peaking | 7745 Hz | 2.42 | -1.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Umi%20Voix/Umi%20Voix.png)