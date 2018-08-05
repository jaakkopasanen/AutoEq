# Zoukbox ZLX30

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -9.7; 22 -9.7; 23 -9.7; 25 -9.6; 26 -9.6; 28 -9.6; 30 -9.5; 32 -9.5; 35 -9.3; 37 -9.2; 40 -9.0; 42 -8.9; 45 -8.7; 49 -8.5; 52 -8.3; 56 -8.1; 59 -7.9; 64 -7.7; 68 -7.5; 73 -7.3; 78 -7.2; 83 -7.1; 89 -7.1; 95 -7.2; 102 -7.4; 109 -7.5; 117 -7.7; 125 -7.9; 134 -7.9; 143 -7.9; 153 -7.7; 164 -7.5; 175 -7.1; 188 -6.7; 201 -6.4; 215 -5.9; 230 -5.4; 246 -5.0; 263 -4.6; 282 -4.1; 301 -3.7; 323 -3.2; 345 -2.8; 369 -2.3; 395 -2.0; 423 -1.5; 452 -1.1; 484 -0.8; 518 -0.6; 554 -0.1; 593 0.3; 635 0.6; 679 0.6; 726 0.8; 777 1.0; 832 0.9; 890 0.7; 952 0.3; 1019 -0.1; 1090 -0.5; 1167 -0.8; 1248 -1.2; 1336 -2.0; 1429 -2.7; 1529 -3.5; 1636 -4.3; 1751 -5.0; 1873 -5.8; 2004 -6.4; 2145 -7.1; 2295 -7.6; 2455 -7.2; 2627 -6.0; 2811 -3.9; 3008 -1.6; 3219 -1.0; 3444 -1.9; 3685 -4.2; 3943 -7.2; 4219 -10.0; 4514 -9.3; 4830 -4.8; 5168 1.6; 5530 4.7; 5917 5.5; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.1; 10167 -2.4; 10879 -2.2; 11640 -0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 -1.5; 16326 -2.6; 17469 -0.4; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Zoukbox ZLX30 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 8 Hz     | 0.75 | -9.1 dB  |
| Peaking | 32 Hz    | 0.34 | -8.2 dB  |
| Peaking | 164 Hz   | 0.93 | -5.5 dB  |
| Peaking | 2169 Hz  | 2.28 | -7.9 dB  |
| Peaking | 4271 Hz  | 7.15 | -10.7 dB |
| Peaking | 747 Hz   | 2.56 | 1.9 dB   |
| Peaking | 4684 Hz  | 7.9  | -5.3 dB  |
| Peaking | 5901 Hz  | 3.21 | 7.4 dB   |
| Peaking | 16223 Hz | 4.96 | -3.1 dB  |
| Peaking | 10460 Hz | 6.94 | -3.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Zoukbox%20ZLX30/Zoukbox%20ZLX30.png)