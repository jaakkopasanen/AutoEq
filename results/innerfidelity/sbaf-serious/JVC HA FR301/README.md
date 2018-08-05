# JVC HA FR301

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -0.8dB
GraphicEQ: 10 -84; 20 -8.8; 22 -9.3; 23 -9.5; 25 -9.9; 26 -10.0; 28 -10.3; 30 -10.6; 32 -10.8; 35 -11.0; 37 -11.2; 40 -11.4; 42 -11.5; 45 -11.6; 49 -11.7; 52 -11.8; 56 -11.8; 59 -11.8; 64 -11.9; 68 -12.0; 73 -12.1; 78 -12.2; 83 -12.4; 89 -12.6; 95 -13.0; 102 -13.4; 109 -13.8; 117 -14.1; 125 -14.5; 134 -14.8; 143 -14.9; 153 -14.9; 164 -14.8; 175 -14.5; 188 -14.3; 201 -14.0; 215 -13.5; 230 -13.1; 246 -12.6; 263 -12.2; 282 -11.6; 301 -11.1; 323 -10.5; 345 -9.8; 369 -9.3; 395 -8.6; 423 -7.8; 452 -7.1; 484 -6.6; 518 -5.8; 554 -4.9; 593 -4.0; 635 -3.2; 679 -2.7; 726 -2.1; 777 -1.3; 832 -0.8; 890 -0.4; 952 -0.1; 1019 0.1; 1090 0.2; 1167 0.2; 1248 0.1; 1336 -0.3; 1429 -0.8; 1529 -1.3; 1636 -1.7; 1751 -2.0; 1873 -2.2; 2004 -2.4; 2145 -2.9; 2295 -3.2; 2455 -3.5; 2627 -4.3; 2811 -5.4; 3008 -6.1; 3219 -6.6; 3444 -6.8; 3685 -7.1; 3943 -7.9; 4219 -9.8; 4514 -11.5; 4830 -12.5; 5168 -11.2; 5530 -8.8; 5917 -6.1; 6331 -4.4; 6775 -3.2; 7249 -3.5; 7756 -4.5; 8299 -6.2; 8880 -7.2; 9502 -6.7; 10167 -4.2; 10879 -0.5; 11640 0.0; 12455 0.0; 13327 0.0; 14260 -2.7; 15258 -5.6; 16326 -4.3; 17469 -1.1; 18692 0.0; 20000 -0.5
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-0.8dB` and instead set Global volume in the UI for both channels to **-8**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JVC HA FR301 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 4 Hz     | 1.91 | -8.0 dB  |
| Peaking | 48 Hz    | 0.21 | -10.4 dB |
| Peaking | 207 Hz   | 0.65 | -8.4 dB  |
| Peaking | 4549 Hz  | 1.45 | -10.4 dB |
| Peaking | 12208 Hz | 0.35 | -2.0 dB  |
| Peaking | 1021 Hz  | 2.23 | 2.4 dB   |
| Peaking | 7017 Hz  | 2.22 | 6.1 dB   |
| Peaking | 9114 Hz  | 0.93 | -18.1 dB |
| Peaking | 11246 Hz | 0.72 | 15.6 dB  |
| Peaking | 15461 Hz | 2.46 | -7.5 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/JVC%20HA%20FR301/JVC%20HA%20FR301.png)