# JVC HA-FXT90

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.5dB
GraphicEQ: 10 -84; 20 1.9; 22 1.4; 23 1.2; 25 0.7; 26 0.5; 28 0.0; 30 -0.4; 32 -0.9; 35 -1.3; 37 -1.6; 40 -1.9; 42 -2.1; 45 -2.4; 49 -2.7; 52 -2.9; 56 -3.1; 59 -3.3; 64 -3.6; 68 -3.7; 73 -3.9; 78 -4.1; 83 -4.4; 89 -4.9; 95 -5.4; 102 -6.0; 109 -6.3; 117 -6.8; 125 -7.3; 134 -7.7; 143 -7.9; 153 -7.9; 164 -7.9; 175 -7.8; 188 -7.6; 201 -7.5; 215 -7.1; 230 -6.8; 246 -6.5; 263 -6.1; 282 -5.7; 301 -5.3; 323 -5.0; 345 -4.6; 369 -4.2; 395 -3.9; 423 -3.2; 452 -2.8; 484 -2.5; 518 -2.1; 554 -1.6; 593 -1.0; 635 -0.7; 679 -0.5; 726 -0.2; 777 0.2; 832 0.2; 890 0.0; 952 0.1; 1019 -0.0; 1090 -0.4; 1167 -0.7; 1248 -0.7; 1336 -1.2; 1429 -1.3; 1529 -0.4; 1636 -0.1; 1751 -0.7; 1873 -1.1; 2004 -1.5; 2145 -1.8; 2295 -2.0; 2455 -2.0; 2627 -2.1; 2811 -1.8; 3008 -0.8; 3219 0.3; 3444 1.1; 3685 0.9; 3943 -0.2; 4219 -2.5; 4514 -4.7; 4830 -6.1; 5168 -6.5; 5530 -5.5; 5917 -3.3; 6331 -1.9; 6775 -1.8; 7249 -3.3; 7756 -5.4; 8299 -6.4; 8880 -4.6; 9502 -0.7; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.5dB` and instead set Global volume in the UI for both channels to **-25**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JVC HA-FXT90 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 131 Hz   | 0.66 | -5.8 dB |
| Peaking | 238 Hz   | 0.89 | -3.6 dB |
| Peaking | 2287 Hz  | 4.53 | -1.6 dB |
| Peaking | 6046 Hz  | 1.16 | -4.6 dB |
| Peaking | 24000 Hz | 2.12 | -3.9 dB |
| Peaking | 21 Hz    | 2.75 | 2.3 dB  |
| Peaking | 3700 Hz  | 4.8  | 3.5 dB  |
| Peaking | 5012 Hz  | 2.48 | -5.9 dB |
| Peaking | 7132 Hz  | 1.24 | 6.8 dB  |
| Peaking | 8132 Hz  | 3.61 | -9.4 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/JVC%20HA-FXT90/JVC%20HA-FXT90.png)