# Klipsch X12i

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -0.7; 22 -0.9; 23 -0.9; 25 -1.0; 26 -1.1; 28 -1.1; 30 -1.2; 32 -1.3; 35 -1.3; 37 -1.3; 40 -1.4; 42 -1.4; 45 -1.4; 49 -1.5; 52 -1.5; 56 -1.5; 59 -1.6; 64 -1.6; 68 -1.7; 73 -1.8; 78 -1.9; 83 -2.2; 89 -2.5; 95 -2.9; 102 -3.5; 109 -3.9; 117 -4.4; 125 -4.9; 134 -5.3; 143 -5.6; 153 -5.7; 164 -5.8; 175 -5.8; 188 -5.7; 201 -5.6; 215 -5.5; 230 -5.2; 246 -5.1; 263 -4.9; 282 -4.7; 301 -4.4; 323 -4.2; 345 -3.9; 369 -3.6; 395 -3.4; 423 -3.0; 452 -2.7; 484 -2.4; 518 -2.1; 554 -1.7; 593 -1.2; 635 -0.8; 679 -0.7; 726 -0.4; 777 0.0; 832 0.2; 890 0.2; 952 0.1; 1019 -0.0; 1090 -0.1; 1167 -0.2; 1248 -0.2; 1336 -0.4; 1429 -0.7; 1529 -0.8; 1636 -0.8; 1751 -0.6; 1873 -0.2; 2004 0.1; 2145 0.4; 2295 0.6; 2455 0.9; 2627 1.0; 2811 0.7; 3008 0.8; 3219 1.5; 3444 3.2; 3685 5.1; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Klipsch X12i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 31 Hz   | 1.28 | -0.9 dB |
| Peaking | 189 Hz  | 0.65 | -6.0 dB |
| Peaking | 1620 Hz | 4.93 | -1.0 dB |
| Peaking | 4227 Hz | 2.47 | 5.9 dB  |
| Peaking | 5870 Hz | 3.39 | 5.1 dB  |
| Peaking | 77 Hz   | 4.07 | 0.5 dB  |
| Peaking | 429 Hz  | 2.15 | -0.6 dB |
| Peaking | 840 Hz  | 3.16 | 0.9 dB  |
| Peaking | 648 Hz  | 2.91 | 0.3 dB  |
| Peaking | 8250 Hz | 4.37 | -1.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Klipsch%20X12i/Klipsch%20X12i.png)