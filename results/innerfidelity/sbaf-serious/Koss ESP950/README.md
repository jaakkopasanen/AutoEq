# Koss ESP950

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 5.8; 95 5.1; 102 4.3; 109 3.6; 117 3.0; 125 2.8; 134 2.6; 143 2.5; 153 2.5; 164 2.3; 175 2.1; 188 2.0; 201 2.0; 215 2.1; 230 2.1; 246 2.1; 263 2.1; 282 2.1; 301 2.1; 323 2.1; 345 2.1; 369 2.1; 395 2.0; 423 2.0; 452 2.0; 484 1.8; 518 1.6; 554 1.6; 593 1.6; 635 1.5; 679 1.3; 726 1.2; 777 1.1; 832 0.8; 890 0.5; 952 0.3; 1019 0.0; 1090 0.0; 1167 -0.6; 1248 -1.0; 1336 -1.3; 1429 -1.6; 1529 -1.6; 1636 -1.3; 1751 -0.0; 1873 1.4; 2004 2.9; 2145 3.8; 2295 5.1; 2455 5.1; 2627 3.9; 2811 2.3; 3008 2.0; 3219 2.2; 3444 3.6; 3685 4.7; 3943 5.9; 4219 6.0; 4514 6.0; 4830 6.0; 5168 5.9; 5530 5.6; 5917 5.4; 6331 4.4; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 -1.4; 9502 -0.9; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss ESP950 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 41 Hz   | 0.37 | 6.5 dB  |
| Peaking | 455 Hz  | 0.86 | 1.6 dB  |
| Peaking | 1480 Hz | 2.31 | -2.8 dB |
| Peaking | 2294 Hz | 3.35 | 4.9 dB  |
| Peaking | 4764 Hz | 1.67 | 6.7 dB  |
| Peaking | 3 Hz    | 1.86 | 0.2 dB  |
| Peaking | 84 Hz   | 5.96 | 1.3 dB  |
| Peaking | 6706 Hz | 8.66 | 1.7 dB  |
| Peaking | 5952 Hz | 6.99 | 1.2 dB  |
| Peaking | 8732 Hz | 2.55 | -2.1 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20ESP950/Koss%20ESP950.png)