# Koss ESP950 sample 2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 6.0; 37 6.0; 40 6.0; 42 6.0; 45 6.0; 49 6.0; 52 6.0; 56 6.0; 59 6.0; 64 6.0; 68 6.0; 73 6.0; 78 6.0; 83 6.0; 89 6.0; 95 5.5; 102 4.6; 109 3.8; 117 3.2; 125 2.9; 134 2.7; 143 2.6; 153 2.5; 164 2.3; 175 2.1; 188 2.0; 201 2.0; 215 2.0; 230 2.0; 246 2.0; 263 2.0; 282 2.1; 301 2.1; 323 2.1; 345 2.1; 369 2.0; 395 1.9; 423 1.8; 452 1.8; 484 1.5; 518 1.4; 554 1.3; 593 1.5; 635 1.3; 679 1.0; 726 1.0; 777 0.9; 832 0.6; 890 0.3; 952 0.1; 1019 -0.0; 1090 -0.1; 1167 -0.6; 1248 -1.1; 1336 -1.5; 1429 -1.8; 1529 -1.6; 1636 -1.2; 1751 -0.1; 1873 1.5; 2004 2.9; 2145 3.8; 2295 4.9; 2455 4.7; 2627 3.6; 2811 2.7; 3008 2.4; 3219 2.7; 3444 3.9; 3685 4.8; 3943 5.9; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 5.9; 5917 5.5; 6331 4.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.0; 8880 -1.9; 9502 -2.2; 10167 -0.4; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Koss ESP950 sample 2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 41 Hz   | 0.36 | 6.6 dB  |
| Peaking | 437 Hz  | 0.92 | 1.5 dB  |
| Peaking | 1495 Hz | 2.26 | -3.1 dB |
| Peaking | 2263 Hz | 2.77 | 4.6 dB  |
| Peaking | 4756 Hz | 1.67 | 6.7 dB  |
| Peaking | 3 Hz    | 1.84 | 0.3 dB  |
| Peaking | 88 Hz   | 5.99 | 1.3 dB  |
| Peaking | 6348 Hz | 5.75 | 2.0 dB  |
| Peaking | 9115 Hz | 3.81 | -3.2 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Koss%20ESP950%20sample%202/Koss%20ESP950%20sample%202.png)