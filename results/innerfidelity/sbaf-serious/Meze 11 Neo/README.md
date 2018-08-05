# Meze 11 Neo

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.2dB
GraphicEQ: 10 -84; 20 3.2; 22 2.6; 23 2.3; 25 1.8; 26 1.6; 28 1.1; 30 0.8; 32 0.5; 35 0.1; 37 -0.2; 40 -0.5; 42 -0.7; 45 -1.0; 49 -1.2; 52 -1.4; 56 -1.7; 59 -1.8; 64 -2.0; 68 -2.2; 73 -2.5; 78 -2.7; 83 -3.0; 89 -3.5; 95 -4.0; 102 -4.6; 109 -5.1; 117 -5.6; 125 -6.2; 134 -6.7; 143 -6.9; 153 -7.1; 164 -7.1; 175 -7.1; 188 -7.0; 201 -6.9; 215 -6.7; 230 -6.5; 246 -6.3; 263 -6.0; 282 -5.7; 301 -5.4; 323 -5.0; 345 -4.6; 369 -4.3; 395 -3.9; 423 -3.4; 452 -3.0; 484 -2.6; 518 -2.3; 554 -1.7; 593 -1.0; 635 -0.6; 679 -0.4; 726 -0.0; 777 0.2; 832 0.3; 890 0.2; 952 0.1; 1019 -0.1; 1090 -0.3; 1167 -0.4; 1248 -0.7; 1336 -1.1; 1429 -1.6; 1529 -2.1; 1636 -2.5; 1751 -2.8; 1873 -3.1; 2004 -3.2; 2145 -3.4; 2295 -3.4; 2455 -2.8; 2627 -2.1; 2811 -1.0; 3008 0.8; 3219 2.1; 3444 3.3; 3685 3.4; 3943 2.9; 4219 1.3; 4514 0.1; 4830 0.0; 5168 0.9; 5530 2.0; 5917 3.2; 6331 4.4; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.2dB` and instead set Global volume in the UI for both channels to **-52**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Meze 11 Neo ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 21 Hz   | 1.62 | 3.3 dB  |
| Peaking | 180 Hz  | 0.65 | -7.4 dB |
| Peaking | 2157 Hz | 1.96 | -3.9 dB |
| Peaking | 3534 Hz | 3.68 | 4.5 dB  |
| Peaking | 6394 Hz | 5.11 | 4.8 dB  |
| Peaking | 480 Hz  | 0.63 | -1.4 dB |
| Peaking | 747 Hz  | 1.13 | 2.4 dB  |
| Peaking | 1552 Hz | 4.15 | -0.9 dB |
| Peaking | 208 Hz  | 2.26 | 0.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Meze%2011%20Neo/Meze%2011%20Neo.png)