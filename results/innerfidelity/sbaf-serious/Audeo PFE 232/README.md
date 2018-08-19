# Audeo PFE 232

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.3dB
GraphicEQ: 10 -84; 20 -3.9; 22 -4.0; 23 -4.0; 25 -4.1; 26 -4.2; 28 -4.2; 30 -4.3; 32 -4.4; 35 -4.5; 37 -4.6; 40 -4.6; 42 -4.7; 45 -4.8; 49 -4.9; 52 -5.0; 56 -5.2; 59 -5.4; 64 -5.6; 68 -5.7; 73 -5.9; 78 -6.2; 83 -6.4; 89 -6.7; 95 -6.8; 102 -7.1; 109 -7.2; 117 -7.2; 125 -7.4; 134 -7.4; 143 -7.5; 153 -7.4; 164 -7.4; 175 -7.3; 188 -7.2; 201 -7.1; 215 -6.9; 230 -6.6; 246 -6.4; 263 -6.2; 282 -5.8; 301 -5.5; 323 -5.2; 345 -4.8; 369 -4.4; 395 -4.0; 423 -3.5; 452 -3.1; 484 -2.8; 518 -2.4; 554 -1.9; 593 -1.3; 635 -1.0; 679 -0.8; 726 -0.6; 777 -0.2; 832 0.0; 890 0.1; 952 0.1; 1019 -0.0; 1090 -0.1; 1167 -0.2; 1248 -0.3; 1336 -0.6; 1429 -0.9; 1529 -1.1; 1636 -1.3; 1751 -1.3; 1873 -1.2; 2004 -0.9; 2145 -0.7; 2295 -0.3; 2455 0.7; 2627 1.8; 2811 2.6; 3008 3.2; 3219 3.1; 3444 2.9; 3685 2.7; 3943 2.7; 4219 2.4; 4514 2.4; 4830 2.6; 5168 2.7; 5530 2.5; 5917 2.4; 6331 0.1; 6775 0.1; 7249 1.2; 7756 -0.0; 8299 -2.5; 8880 -5.1; 9502 -5.7; 10167 -4.1; 10879 -1.4; 11640 -0.0; 12455 -0.6; 13327 -5.2; 14260 -10.5; 15258 -9.9; 16326 -1.7; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.285498588008806dB` and instead set Global volume in the UI for both channels to **-32**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeo PFE 232 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -0.0dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 37 Hz    | 0.25 | -3.9 dB  |
| Peaking | 146 Hz   | 0.7  | -4.9 dB  |
| Peaking | 300 Hz   | 1.19 | -2.7 dB  |
| Peaking | 14642 Hz | 3.6  | -12.3 dB |
| Peaking | 24000 Hz | 1.89 | -6.6 dB  |
| Peaking | 1934 Hz  | 2.17 | -2.0 dB  |
| Peaking | 3018 Hz  | 2.52 | 2.5 dB   |
| Peaking | 4962 Hz  | 0.99 | 2.6 dB   |
| Peaking | 9345 Hz  | 3.51 | -6.6 dB  |
| Peaking | 11862 Hz | 5.12 | 2.8 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeo%20PFE%20232/Audeo%20PFE%20232.png)