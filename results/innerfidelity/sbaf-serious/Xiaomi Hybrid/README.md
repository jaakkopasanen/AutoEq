# Xiaomi Hybrid

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -5.2; 22 -5.5; 23 -5.7; 25 -6.0; 26 -6.1; 28 -6.3; 30 -6.4; 32 -6.5; 35 -6.6; 37 -6.7; 40 -6.7; 42 -6.7; 45 -6.7; 49 -6.7; 52 -6.7; 56 -6.7; 59 -6.6; 64 -6.5; 68 -6.4; 73 -6.4; 78 -6.3; 83 -6.4; 89 -6.6; 95 -6.9; 102 -7.1; 109 -7.2; 117 -7.5; 125 -7.8; 134 -7.9; 143 -7.9; 153 -7.9; 164 -7.7; 175 -7.4; 188 -7.0; 201 -6.8; 215 -6.3; 230 -6.0; 246 -5.5; 263 -5.1; 282 -4.6; 301 -4.1; 323 -3.7; 345 -3.3; 369 -2.8; 395 -2.5; 423 -1.9; 452 -1.5; 484 -1.2; 518 -0.9; 554 -0.4; 593 0.1; 635 0.3; 679 0.4; 726 0.6; 777 0.8; 832 0.7; 890 0.5; 952 0.3; 1019 -0.1; 1090 -0.5; 1167 -0.8; 1248 -1.1; 1336 -1.8; 1429 -2.7; 1529 -3.5; 1636 -4.4; 1751 -5.2; 1873 -5.7; 2004 -6.0; 2145 -6.1; 2295 -5.7; 2455 -4.1; 2627 -2.5; 2811 -1.0; 3008 0.5; 3219 1.3; 3444 1.2; 3685 -0.1; 3943 -1.3; 4219 -0.9; 4514 1.0; 4830 3.6; 5168 5.7; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -1.4; 15258 -1.9; 16326 -0.3; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Xiaomi Hybrid ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 6 Hz     | 1.53 | -4.6 dB |
| Peaking | 37 Hz    | 0.34 | -6.1 dB |
| Peaking | 169 Hz   | 0.87 | -5.9 dB |
| Peaking | 2001 Hz  | 2.37 | -6.8 dB |
| Peaking | 5723 Hz  | 3.09 | 7.1 dB  |
| Peaking | 765 Hz   | 1.02 | 4.2 dB  |
| Peaking | 795 Hz   | 0.53 | -2.6 dB |
| Peaking | 3228 Hz  | 4.88 | 2.6 dB  |
| Peaking | 4058 Hz  | 8.27 | -2.6 dB |
| Peaking | 14934 Hz | 4.81 | -2.3 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Xiaomi%20Hybrid/Xiaomi%20Hybrid.png)