# PNY Midtown

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.5dB
GraphicEQ: 10 -84; 20 -10.3; 22 -10.3; 23 -10.3; 25 -10.2; 26 -10.2; 28 -10.2; 30 -10.1; 32 -10.1; 35 -10.0; 37 -9.9; 40 -9.8; 42 -9.7; 45 -9.6; 49 -9.5; 52 -9.3; 56 -9.2; 59 -9.1; 64 -8.9; 68 -8.8; 73 -8.7; 78 -8.6; 83 -8.6; 89 -8.8; 95 -8.9; 102 -9.2; 109 -9.4; 117 -9.6; 125 -9.9; 134 -10.0; 143 -10.0; 153 -9.9; 164 -9.7; 175 -9.3; 188 -9.0; 201 -8.7; 215 -8.2; 230 -7.8; 246 -7.4; 263 -6.9; 282 -6.5; 301 -6.1; 323 -5.5; 345 -5.0; 369 -4.6; 395 -4.1; 423 -3.6; 452 -3.1; 484 -2.7; 518 -2.4; 554 -1.8; 593 -1.2; 635 -0.9; 679 -0.7; 726 -0.2; 777 0.2; 832 0.2; 890 0.1; 952 -0.2; 1019 0.2; 1090 0.5; 1167 0.3; 1248 0.1; 1336 -0.4; 1429 -0.9; 1529 -1.5; 1636 -2.1; 1751 -3.1; 1873 -4.0; 2004 -4.4; 2145 -4.5; 2295 -4.2; 2455 -3.6; 2627 -2.2; 2811 -0.4; 3008 2.1; 3219 4.1; 3444 5.7; 3685 6.0; 3943 5.5; 4219 3.8; 4514 2.3; 4830 1.6; 5168 0.3; 5530 -2.1; 5917 -6.2; 6331 -8.4; 6775 -4.4; 7249 -1.1; 7756 0.2; 8299 0.0; 8880 -0.1; 9502 -0.7; 10167 -0.1; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.5dB` and instead set Global volume in the UI for both channels to **-65**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `PNY Midtown ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 12 Hz   | 1.34 | -10.0 dB |
| Peaking | 32 Hz   | 0.42 | -8.2 dB  |
| Peaking | 167 Hz  | 0.61 | -8.2 dB  |
| Peaking | 3755 Hz | 4.27 | 7.2 dB   |
| Peaking | 6248 Hz | 6.56 | -9.6 dB  |
| Peaking | 1101 Hz | 1.1  | 2.0 dB   |
| Peaking | 2165 Hz | 1.42 | -5.5 dB  |
| Peaking | 2982 Hz | 5.12 | 2.0 dB   |
| Peaking | 3312 Hz | 6.96 | 2.9 dB   |
| Peaking | 4645 Hz | 4.43 | 1.8 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/PNY%20Midtown/PNY%20Midtown.png)