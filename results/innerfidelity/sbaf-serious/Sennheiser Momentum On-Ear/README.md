# Sennheiser Momentum On-Ear

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -3.4; 22 -3.6; 23 -3.7; 25 -3.8; 26 -3.8; 28 -3.9; 30 -4.0; 32 -4.1; 35 -4.2; 37 -4.2; 40 -4.2; 42 -4.2; 45 -4.2; 49 -4.3; 52 -4.2; 56 -4.2; 59 -4.1; 64 -4.0; 68 -3.8; 73 -3.7; 78 -3.7; 83 -3.7; 89 -3.8; 95 -3.8; 102 -4.0; 109 -4.1; 117 -4.3; 125 -4.5; 134 -4.7; 143 -4.6; 153 -4.5; 164 -4.1; 175 -3.8; 188 -3.5; 201 -3.1; 215 -2.6; 230 -2.0; 246 -1.3; 263 -0.7; 282 0.0; 301 0.6; 323 1.0; 345 1.3; 369 1.5; 395 1.6; 423 1.8; 452 1.9; 484 1.6; 518 1.4; 554 1.2; 593 1.0; 635 0.5; 679 0.1; 726 -0.2; 777 -0.1; 832 -0.0; 890 0.2; 952 0.2; 1019 -0.0; 1090 -0.6; 1167 -1.2; 1248 -1.9; 1336 -2.8; 1429 -3.7; 1529 -4.4; 1636 -5.1; 1751 -5.4; 1873 -5.3; 2004 -4.6; 2145 -3.8; 2295 -2.9; 2455 -1.4; 2627 0.1; 2811 1.2; 3008 2.3; 3219 3.1; 3444 4.2; 3685 5.3; 3943 6.0; 4219 6.0; 4514 5.1; 4830 0.9; 5168 1.1; 5530 2.4; 5917 2.7; 6331 1.4; 6775 -0.1; 7249 -0.9; 7756 -1.0; 8299 -1.6; 8880 -2.5; 9502 -1.9; 10167 -0.1; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sennheiser Momentum On-Ear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 39 Hz   | 0.57 | -4.5 dB |
| Peaking | 126 Hz  | 2    | -3.3 dB |
| Peaking | 180 Hz  | 3.5  | -2.3 dB |
| Peaking | 1798 Hz | 2.18 | -6.3 dB |
| Peaking | 3879 Hz | 2.44 | 6.8 dB  |
| Peaking | 430 Hz  | 1.19 | 3.5 dB  |
| Peaking | 970 Hz  | 3.76 | 1.3 dB  |
| Peaking | 2661 Hz | 0.08 | -1.7 dB |
| Peaking | 6248 Hz | 0.23 | 2.0 dB  |
| Peaking | 8750 Hz | 3.36 | -3.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sennheiser%20Momentum%20On-Ear/Sennheiser%20Momentum%20On-Ear.png)