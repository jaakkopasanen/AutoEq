# Sync by 50

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.4dB
GraphicEQ: 10 -84; 20 -1.2; 22 -2.1; 23 -2.5; 25 -3.2; 26 -3.5; 28 -4.1; 30 -4.6; 32 -5.1; 35 -5.8; 37 -6.1; 40 -6.6; 42 -6.9; 45 -7.2; 49 -7.6; 52 -7.9; 56 -8.1; 59 -8.3; 64 -8.5; 68 -8.7; 73 -8.9; 78 -9.1; 83 -9.3; 89 -9.5; 95 -9.8; 102 -9.9; 109 -9.9; 117 -10.0; 125 -10.1; 134 -10.1; 143 -10.1; 153 -10.1; 164 -9.9; 175 -9.8; 188 -9.7; 201 -9.5; 215 -9.0; 230 -8.7; 246 -8.6; 263 -8.6; 282 -9.1; 301 -9.0; 323 -8.7; 345 -8.6; 369 -8.3; 395 -8.1; 423 -8.1; 452 -7.9; 484 -7.6; 518 -6.8; 554 -5.3; 593 -2.9; 635 -0.7; 679 0.7; 726 1.8; 777 2.3; 832 1.9; 890 1.1; 952 0.4; 1019 -0.2; 1090 -0.7; 1167 -0.8; 1248 -0.5; 1336 0.2; 1429 0.2; 1529 -0.9; 1636 -2.2; 1751 -2.8; 1873 -3.2; 2004 -3.2; 2145 -2.6; 2295 -2.1; 2455 -1.2; 2627 -0.1; 2811 0.7; 3008 1.3; 3219 1.5; 3444 1.1; 3685 0.7; 3943 -0.3; 4219 -0.6; 4514 1.2; 4830 3.2; 5168 4.5; 5530 3.1; 5917 3.3; 6331 5.1; 6775 0.7; 7249 -0.6; 7756 0.2; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.401206033433817dB` and instead set Global volume in the UI for both channels to **-54**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Sync by 50 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.3dB.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 79 Hz   | 0.46 | -8.7 dB |
| Peaking | 218 Hz  | 0.97 | -5.2 dB |
| Peaking | 420 Hz  | 2.47 | -5.6 dB |
| Peaking | 1950 Hz | 4.23 | -3.6 dB |
| Peaking | 5539 Hz | 2.8  | 4.3 dB  |
| Peaking | 534 Hz  | 4.21 | -4.0 dB |
| Peaking | 789 Hz  | 1.16 | 5.8 dB  |
| Peaking | 1026 Hz | 3.03 | -2.4 dB |
| Peaking | 1094 Hz | 0.27 | -1.3 dB |
| Peaking | 3098 Hz | 4.57 | 2.3 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Sync%20by%2050/Sync%20by%2050.png)