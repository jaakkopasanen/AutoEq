# T-Peos Spider

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.4dB
GraphicEQ: 10 -84; 20 -8.7; 22 -8.6; 23 -8.6; 25 -8.5; 26 -8.5; 28 -8.5; 30 -8.4; 32 -8.3; 35 -8.2; 37 -8.1; 40 -8.0; 42 -7.9; 45 -7.8; 49 -7.7; 52 -7.5; 56 -7.4; 59 -7.2; 64 -7.1; 68 -7.0; 73 -6.8; 78 -6.8; 83 -6.8; 89 -6.9; 95 -7.1; 102 -7.3; 109 -7.4; 117 -7.7; 125 -7.9; 134 -8.0; 143 -8.0; 153 -7.9; 164 -7.7; 175 -7.3; 188 -7.0; 201 -6.7; 215 -6.2; 230 -5.7; 246 -5.3; 263 -4.9; 282 -4.4; 301 -4.0; 323 -3.5; 345 -3.0; 369 -2.6; 395 -2.2; 423 -1.7; 452 -1.3; 484 -1.0; 518 -0.7; 554 -0.2; 593 0.3; 635 0.5; 679 0.6; 726 0.8; 777 0.9; 832 0.9; 890 0.6; 952 0.3; 1019 -0.0; 1090 -0.4; 1167 -0.8; 1248 -1.1; 1336 -1.7; 1429 -2.5; 1529 -3.2; 1636 -3.9; 1751 -4.4; 1873 -4.8; 2004 -4.9; 2145 -4.9; 2295 -4.3; 2455 -2.6; 2627 -0.8; 2811 1.1; 3008 3.3; 3219 4.8; 3444 5.8; 3685 5.4; 3943 4.0; 4219 1.2; 4514 -2.0; 4830 -5.2; 5168 -8.0; 5530 -6.6; 5917 -2.0; 6331 0.7; 6775 1.9; 7249 1.3; 7756 -0.3; 8299 -2.7; 8880 -4.3; 9502 -4.0; 10167 -2.2; 10879 -0.1; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.4dB` and instead set Global volume in the UI for both channels to **-64**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `T-Peos Spider ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-9.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 9 Hz    | 0.83 | -8.2 dB  |
| Peaking | 34 Hz   | 0.34 | -7.1 dB  |
| Peaking | 166 Hz  | 0.95 | -5.8 dB  |
| Peaking | 3446 Hz | 2.69 | 15.2 dB  |
| Peaking | 3382 Hz | 0.7  | -8.0 dB  |
| Peaking | 811 Hz  | 1.72 | 2.3 dB   |
| Peaking | 1917 Hz | 2.54 | -2.8 dB  |
| Peaking | 5290 Hz | 3.95 | -11.4 dB |
| Peaking | 6658 Hz | 1.04 | 8.3 dB   |
| Peaking | 8878 Hz | 2.64 | -7.9 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/T-Peos%20Spider/T-Peos%20Spider.png)