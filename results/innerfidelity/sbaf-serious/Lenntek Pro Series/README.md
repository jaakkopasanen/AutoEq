# Lenntek Pro Series

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 5.9; 45 5.8; 49 5.7; 52 5.6; 56 5.3; 59 5.2; 64 4.9; 68 4.7; 73 4.4; 78 4.2; 83 3.8; 89 3.5; 95 3.2; 102 2.9; 109 2.8; 117 2.6; 125 2.3; 134 2.1; 143 1.9; 153 1.7; 164 1.6; 175 1.5; 188 1.4; 201 1.3; 215 1.2; 230 1.2; 246 1.1; 263 1.2; 282 1.2; 301 1.1; 323 1.2; 345 1.2; 369 1.3; 395 1.3; 423 1.5; 452 1.5; 484 1.4; 518 1.3; 554 1.6; 593 1.8; 635 1.8; 679 1.6; 726 1.5; 777 1.5; 832 1.2; 890 0.8; 952 0.4; 1019 -0.2; 1090 -0.7; 1167 -1.2; 1248 -1.8; 1336 -2.6; 1429 -3.6; 1529 -4.5; 1636 -5.3; 1751 -6.2; 1873 -6.7; 2004 -6.8; 2145 -6.2; 2295 -4.6; 2455 -2.0; 2627 0.5; 2811 2.5; 3008 4.3; 3219 4.8; 3444 4.7; 3685 3.7; 3943 1.3; 4219 -2.7; 4514 -3.3; 4830 0.6; 5168 5.2; 5530 6.0; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000002dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Lenntek Pro Series ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 32 Hz    | 0.38 | 6.3 dB   |
| Peaking | 1058 Hz  | 0.56 | 7.6 dB   |
| Peaking | 1980 Hz  | 0.58 | -14.0 dB |
| Peaking | 3066 Hz  | 2.28 | 12.8 dB  |
| Peaking | 5944 Hz  | 3.01 | 9.1 dB   |
| Peaking | 2038 Hz  | 7.81 | -0.6 dB  |
| Peaking | 3748 Hz  | 6.29 | 3.4 dB   |
| Peaking | 4405 Hz  | 5.37 | -5.0 dB  |
| Peaking | 5176 Hz  | 9.83 | 3.8 dB   |
| Peaking | 11576 Hz | 1.49 | 0.5 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Lenntek%20Pro%20Series/Lenntek%20Pro%20Series.png)