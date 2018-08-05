# FLC Technologies FLC8 GGBl

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -1.7; 22 -1.8; 23 -1.9; 25 -1.9; 26 -1.9; 28 -2.0; 30 -2.0; 32 -1.9; 35 -1.9; 37 -1.8; 40 -1.7; 42 -1.7; 45 -1.6; 49 -1.4; 52 -1.3; 56 -1.2; 59 -1.1; 64 -0.9; 68 -0.9; 73 -0.8; 78 -0.8; 83 -0.9; 89 -1.0; 95 -1.3; 102 -1.7; 109 -2.0; 117 -2.3; 125 -2.7; 134 -3.0; 143 -3.2; 153 -3.3; 164 -3.3; 175 -3.1; 188 -3.0; 201 -2.9; 215 -2.7; 230 -2.5; 246 -2.3; 263 -2.2; 282 -1.9; 301 -1.7; 323 -1.5; 345 -1.3; 369 -1.0; 395 -0.8; 423 -0.5; 452 -0.2; 484 -0.1; 518 0.0; 554 0.4; 593 0.7; 635 0.8; 679 0.8; 726 0.8; 777 1.0; 832 1.2; 890 0.8; 952 0.4; 1019 -0.1; 1090 -0.5; 1167 -0.7; 1248 -0.8; 1336 -0.7; 1429 -0.4; 1529 0.2; 1636 0.8; 1751 1.8; 1873 2.8; 2004 3.9; 2145 4.6; 2295 5.3; 2455 5.9; 2627 5.9; 2811 5.6; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `FLC Technologies FLC8 GGBl ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 28 Hz   | 1.04 | -2.0 dB |
| Peaking | 178 Hz  | 0.88 | -3.3 dB |
| Peaking | 725 Hz  | 1.68 | 1.1 dB  |
| Peaking | 1317 Hz | 2.02 | -3.1 dB |
| Peaking | 3431 Hz | 0.71 | 6.9 dB  |
| Peaking | 81 Hz   | 4.38 | 0.5 dB  |
| Peaking | 2384 Hz | 3    | 1.8 dB  |
| Peaking | 2941 Hz | 1.2  | -1.2 dB |
| Peaking | 6188 Hz | 2.08 | 5.8 dB  |
| Peaking | 7471 Hz | 1.46 | -4.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/FLC%20Technologies%20FLC8%20GGBl/FLC%20Technologies%20FLC8%20GGBl.png)