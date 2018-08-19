# RHA MA450i

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.1dB
GraphicEQ: 10 -84; 20 -11.8; 22 -11.8; 23 -11.7; 25 -11.7; 26 -11.6; 28 -11.6; 30 -11.5; 32 -11.4; 35 -11.3; 37 -11.2; 40 -11.1; 42 -11.0; 45 -10.9; 49 -10.8; 52 -10.7; 56 -10.6; 59 -10.6; 64 -10.5; 68 -10.5; 73 -10.4; 78 -10.3; 83 -10.3; 89 -10.2; 95 -10.2; 102 -10.1; 109 -9.9; 117 -9.7; 125 -9.4; 134 -9.3; 143 -9.1; 153 -8.9; 164 -8.5; 175 -8.1; 188 -7.9; 201 -7.5; 215 -7.2; 230 -6.7; 246 -6.3; 263 -6.0; 282 -5.4; 301 -5.1; 323 -4.6; 345 -4.0; 369 -3.8; 395 -3.3; 423 -2.7; 452 -2.3; 484 -2.2; 518 -1.7; 554 -1.3; 593 -0.8; 635 -0.4; 679 -0.4; 726 -0.1; 777 0.0; 832 0.3; 890 0.2; 952 -0.0; 1019 0.0; 1090 -0.3; 1167 -0.3; 1248 -0.5; 1336 -0.9; 1429 -1.2; 1529 -1.7; 1636 -1.8; 1751 -1.8; 1873 -1.7; 2004 -1.6; 2145 -1.4; 2295 -1.2; 2455 -1.0; 2627 -1.0; 2811 -1.1; 3008 -1.1; 3219 -1.3; 3444 -1.2; 3685 -1.8; 3943 -2.7; 4219 -5.0; 4514 -7.4; 4830 -10.3; 5168 -11.9; 5530 -7.9; 5917 -2.6; 6331 0.8; 6775 3.0; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -0.6; 15258 -2.1; 16326 -0.2; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.139962913245871dB` and instead set Global volume in the UI for both channels to **-31**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RHA MA450i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.8dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -2.8dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 22 Hz    | 0.18 | -11.4 dB |
| Peaking | 170 Hz   | 0.67 | -4.3 dB  |
| Peaking | 1769 Hz  | 3.14 | -1.7 dB  |
| Peaking | 5096 Hz  | 3.39 | -13.3 dB |
| Peaking | 6592 Hz  | 3.79 | 5.8 dB   |
| Peaking | 92 Hz    | 3.76 | -0.4 dB  |
| Peaking | 332 Hz   | 2.24 | -0.6 dB  |
| Peaking | 777 Hz   | 2.06 | 1.1 dB   |
| Peaking | 3614 Hz  | 4.43 | 0.4 dB   |
| Peaking | 14699 Hz | 5.14 | -1.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/RHA%20MA450i/RHA%20MA450i.png)