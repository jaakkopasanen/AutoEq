# Aurex HR V9

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 5.9; 49 5.7; 52 5.5; 56 5.3; 59 5.2; 64 5.1; 68 5.0; 73 4.9; 78 4.7; 83 4.5; 89 4.3; 95 4.1; 102 3.6; 109 2.9; 117 2.5; 125 2.0; 134 1.7; 143 1.5; 153 1.4; 164 1.3; 175 1.2; 188 1.1; 201 1.1; 215 1.2; 230 1.2; 246 1.1; 263 1.2; 282 1.4; 301 1.4; 323 1.3; 345 1.4; 369 1.3; 395 1.2; 423 1.4; 452 1.4; 484 1.2; 518 1.1; 554 1.2; 593 1.4; 635 1.3; 679 1.1; 726 1.0; 777 1.0; 832 0.5; 890 0.1; 952 -0.1; 1019 0.1; 1090 0.1; 1167 0.4; 1248 1.0; 1336 1.3; 1429 1.7; 1529 2.2; 1636 2.5; 1751 3.1; 1873 2.8; 2004 1.6; 2145 0.5; 2295 0.1; 2455 0.8; 2627 1.6; 2811 2.2; 3008 3.3; 3219 3.7; 3444 4.0; 3685 4.4; 3943 4.3; 4219 3.7; 4514 3.4; 4830 3.9; 5168 5.2; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Aurex HR V9 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 35 Hz   | 0.39 | 6.3 dB  |
| Peaking | 475 Hz  | 1.19 | 1.2 dB  |
| Peaking | 1696 Hz | 3.91 | 2.7 dB  |
| Peaking | 3603 Hz | 2.38 | 4.0 dB  |
| Peaking | 5786 Hz | 3.15 | 6.1 dB  |
| Peaking | 90 Hz   | 1.63 | 2.0 dB  |
| Peaking | 107 Hz  | 0.76 | -1.5 dB |
| Peaking | 272 Hz  | 1.81 | 0.5 dB  |
| Peaking | 6653 Hz | 6.51 | 2.1 dB  |
| Peaking | 7576 Hz | 2.42 | -1.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Aurex%20HR%20V9/Aurex%20HR%20V9.png)