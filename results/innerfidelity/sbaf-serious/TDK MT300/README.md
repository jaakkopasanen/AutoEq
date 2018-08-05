# TDK MT300

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.9dB
GraphicEQ: 10 -84; 20 -8.9; 22 -8.8; 23 -8.8; 25 -8.8; 26 -8.8; 28 -8.7; 30 -8.6; 32 -8.6; 35 -8.5; 37 -8.4; 40 -8.4; 42 -8.3; 45 -8.2; 49 -8.1; 52 -8.0; 56 -7.8; 59 -7.8; 64 -7.7; 68 -7.6; 73 -7.5; 78 -7.5; 83 -7.6; 89 -7.7; 95 -8.0; 102 -8.3; 109 -8.4; 117 -8.7; 125 -9.1; 134 -9.2; 143 -9.3; 153 -9.2; 164 -9.0; 175 -8.7; 188 -8.3; 201 -8.0; 215 -7.6; 230 -7.1; 246 -6.7; 263 -6.2; 282 -5.6; 301 -5.2; 323 -4.6; 345 -4.0; 369 -3.5; 395 -3.0; 423 -2.3; 452 -1.9; 484 -1.5; 518 -1.1; 554 -0.5; 593 -0.0; 635 0.2; 679 0.2; 726 0.4; 777 0.7; 832 0.5; 890 0.3; 952 0.2; 1019 -0.1; 1090 -0.3; 1167 -0.4; 1248 -0.4; 1336 -0.6; 1429 -0.6; 1529 -0.5; 1636 -0.0; 1751 0.8; 1873 1.6; 2004 2.5; 2145 3.3; 2295 3.9; 2455 4.6; 2627 4.9; 2811 5.0; 3008 4.9; 3219 4.3; 3444 3.6; 3685 2.2; 3943 0.4; 4219 -2.4; 4514 -5.3; 4830 -7.3; 5168 -4.7; 5530 -0.7; 5917 3.0; 6331 5.3; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.9dB` and instead set Global volume in the UI for both channels to **-59**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `TDK MT300 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 9 Hz    | 1.08 | -8.6 dB  |
| Peaking | 29 Hz   | 0.3  | -7.5 dB  |
| Peaking | 171 Hz  | 0.76 | -7.2 dB  |
| Peaking | 3911 Hz | 0.81 | 6.7 dB   |
| Peaking | 4685 Hz | 3.74 | -13.9 dB |
| Peaking | 704 Hz  | 2.15 | 1.4 dB   |
| Peaking | 1471 Hz | 1.86 | -2.0 dB  |
| Peaking | 2489 Hz | 2.26 | 2.0 dB   |
| Peaking | 6387 Hz | 4.68 | 6.8 dB   |
| Peaking | 6662 Hz | 1.02 | -2.7 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/TDK%20MT300/TDK%20MT300.png)