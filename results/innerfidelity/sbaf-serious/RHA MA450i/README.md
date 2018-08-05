# RHA MA450i

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.6dB
GraphicEQ: 10 -84; 20 -11.8; 22 -11.7; 23 -11.7; 25 -11.6; 26 -11.5; 28 -11.4; 30 -11.3; 32 -11.2; 35 -11.0; 37 -10.9; 40 -10.7; 42 -10.5; 45 -10.3; 49 -10.1; 52 -9.9; 56 -9.7; 59 -9.5; 64 -9.2; 68 -9.1; 73 -8.8; 78 -8.7; 83 -8.7; 89 -8.7; 95 -8.8; 102 -9.0; 109 -9.2; 117 -9.3; 125 -9.4; 134 -9.6; 143 -9.6; 153 -9.4; 164 -9.1; 175 -8.7; 188 -8.4; 201 -8.0; 215 -7.6; 230 -7.0; 246 -6.6; 263 -6.2; 282 -5.6; 301 -5.2; 323 -4.7; 345 -4.1; 369 -3.8; 395 -3.4; 423 -2.8; 452 -2.4; 484 -2.2; 518 -1.7; 554 -1.3; 593 -0.8; 635 -0.4; 679 -0.4; 726 -0.1; 777 0.0; 832 0.3; 890 0.2; 952 -0.0; 1019 0.0; 1090 -0.3; 1167 -0.3; 1248 -0.5; 1336 -0.9; 1429 -1.2; 1529 -1.7; 1636 -1.8; 1751 -1.8; 1873 -1.7; 2004 -1.6; 2145 -1.4; 2295 -1.2; 2455 -1.0; 2627 -1.0; 2811 -1.1; 3008 -1.1; 3219 -1.3; 3444 -1.2; 3685 -1.8; 3943 -2.7; 4219 -5.0; 4514 -7.4; 4830 -10.3; 5168 -11.9; 5530 -7.9; 5917 -2.6; 6331 0.8; 6775 3.0; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -0.6; 15258 -2.1; 16326 -0.2; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.6dB` and instead set Global volume in the UI for both channels to **-36**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `RHA MA450i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 10 Hz    | 1.02 | -11.5 dB |
| Peaking | 32 Hz    | 0.38 | -9.2 dB  |
| Peaking | 168 Hz   | 0.7  | -7.0 dB  |
| Peaking | 5115 Hz  | 3.14 | -13.5 dB |
| Peaking | 6552 Hz  | 3.49 | 6.3 dB   |
| Peaking | 360 Hz   | 1.86 | -0.6 dB  |
| Peaking | 818 Hz   | 1.2  | 1.2 dB   |
| Peaking | 1696 Hz  | 1.88 | -1.7 dB  |
| Peaking | 3624 Hz  | 5.61 | 0.9 dB   |
| Peaking | 32967 Hz | 7    | -2.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/RHA%20MA450i/RHA%20MA450i.png)