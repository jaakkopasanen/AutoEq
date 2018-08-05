# Audeo PFE 232

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.7dB
GraphicEQ: 10 -84; 20 -3.8; 22 -3.9; 23 -4.0; 25 -4.0; 26 -4.0; 28 -4.1; 30 -4.1; 32 -4.2; 35 -4.2; 37 -4.2; 40 -4.2; 42 -4.2; 45 -4.2; 49 -4.2; 52 -4.2; 56 -4.2; 59 -4.3; 64 -4.3; 68 -4.3; 73 -4.4; 78 -4.5; 83 -4.8; 89 -5.1; 95 -5.4; 102 -6.0; 109 -6.4; 117 -6.8; 125 -7.4; 134 -7.7; 143 -7.9; 153 -8.0; 164 -8.0; 175 -7.8; 188 -7.7; 201 -7.5; 215 -7.3; 230 -6.9; 246 -6.7; 263 -6.4; 282 -6.0; 301 -5.7; 323 -5.3; 345 -4.9; 369 -4.5; 395 -4.1; 423 -3.6; 452 -3.2; 484 -2.9; 518 -2.5; 554 -1.9; 593 -1.3; 635 -1.0; 679 -0.8; 726 -0.6; 777 -0.2; 832 0.0; 890 0.1; 952 0.1; 1019 -0.0; 1090 -0.1; 1167 -0.2; 1248 -0.3; 1336 -0.6; 1429 -0.9; 1529 -1.1; 1636 -1.3; 1751 -1.3; 1873 -1.2; 2004 -0.9; 2145 -0.7; 2295 -0.3; 2455 0.7; 2627 1.8; 2811 2.6; 3008 3.2; 3219 3.1; 3444 2.9; 3685 2.7; 3943 2.7; 4219 2.4; 4514 2.4; 4830 2.6; 5168 2.7; 5530 2.5; 5917 2.4; 6331 0.1; 6775 0.1; 7249 1.2; 7756 -0.0; 8299 -2.5; 8880 -5.1; 9502 -5.7; 10167 -4.1; 10879 -1.4; 11640 -0.0; 12455 -0.6; 13327 -5.2; 14260 -10.5; 15258 -9.9; 16326 -1.7; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.7dB` and instead set Global volume in the UI for both channels to **-37**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeo PFE 232 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 27 Hz    | 0.55 | -3.6 dB  |
| Peaking | 176 Hz   | 0.6  | -7.8 dB  |
| Peaking | 3825 Hz  | 1.64 | 3.4 dB   |
| Peaking | 14609 Hz | 3.33 | -12.1 dB |
| Peaking | 24000 Hz | 1.71 | -6.8 dB  |
| Peaking | 1820 Hz  | 3.47 | -1.7 dB  |
| Peaking | 7205 Hz  | 1.19 | 1.7 dB   |
| Peaking | 9394 Hz  | 3.09 | -7.0 dB  |
| Peaking | 16935 Hz | 5.21 | 2.2 dB   |
| Peaking | 12011 Hz | 4.74 | 3.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeo%20PFE%20232/Audeo%20PFE%20232.png)