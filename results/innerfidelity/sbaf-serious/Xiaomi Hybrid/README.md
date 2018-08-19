# Xiaomi Hybrid

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -5.2; 22 -5.6; 23 -5.8; 25 -6.1; 26 -6.2; 28 -6.4; 30 -6.6; 32 -6.7; 35 -6.9; 37 -7.0; 40 -7.1; 42 -7.2; 45 -7.3; 49 -7.4; 52 -7.5; 56 -7.6; 59 -7.7; 64 -7.7; 68 -7.8; 73 -7.9; 78 -7.9; 83 -8.0; 89 -8.1; 95 -8.3; 102 -8.1; 109 -8.0; 117 -7.9; 125 -7.8; 134 -7.7; 143 -7.5; 153 -7.3; 164 -7.1; 175 -6.8; 188 -6.5; 201 -6.3; 215 -6.0; 230 -5.7; 246 -5.3; 263 -4.9; 282 -4.4; 301 -4.0; 323 -3.6; 345 -3.2; 369 -2.8; 395 -2.4; 423 -1.9; 452 -1.5; 484 -1.2; 518 -0.8; 554 -0.3; 593 0.1; 635 0.3; 679 0.4; 726 0.6; 777 0.8; 832 0.7; 890 0.5; 952 0.3; 1019 -0.1; 1090 -0.5; 1167 -0.8; 1248 -1.1; 1336 -1.8; 1429 -2.7; 1529 -3.5; 1636 -4.4; 1751 -5.2; 1873 -5.7; 2004 -6.0; 2145 -6.1; 2295 -5.7; 2455 -4.1; 2627 -2.5; 2811 -1.0; 3008 0.5; 3219 1.3; 3444 1.2; 3685 -0.1; 3943 -1.3; 4219 -0.9; 4514 1.0; 4830 3.6; 5168 5.7; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -1.4; 15258 -1.9; 16326 -0.3; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.094765865819561dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Xiaomi Hybrid ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 40 Hz    | 0.39 | -6.5 dB |
| Peaking | 121 Hz   | 0.85 | -4.4 dB |
| Peaking | 236 Hz   | 1.43 | -2.8 dB |
| Peaking | 1997 Hz  | 2.35 | -6.8 dB |
| Peaking | 5723 Hz  | 3.08 | 7.1 dB  |
| Peaking | 783 Hz   | 1.39 | 2.3 dB  |
| Peaking | 1267 Hz  | 0.26 | -0.8 dB |
| Peaking | 3162 Hz  | 6.2  | 2.9 dB  |
| Peaking | 14824 Hz | 5.78 | -1.7 dB |
| Peaking | 15398 Hz | 4.69 | -0.7 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Xiaomi%20Hybrid/Xiaomi%20Hybrid.png)