# T-Peos H-100

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.4dB
GraphicEQ: 10 -84; 20 -6.7; 22 -6.4; 23 -6.2; 25 -5.9; 26 -5.8; 28 -5.5; 30 -5.2; 32 -4.9; 35 -4.5; 37 -4.2; 40 -3.8; 42 -3.5; 45 -3.2; 49 -2.7; 52 -2.4; 56 -2.0; 59 -1.7; 64 -1.3; 68 -1.1; 73 -0.8; 78 -0.6; 83 -0.5; 89 -0.5; 95 -0.6; 102 -0.8; 109 -0.9; 117 -1.1; 125 -1.4; 134 -1.6; 143 -1.6; 153 -1.6; 164 -1.5; 175 -1.2; 188 -1.0; 201 -0.9; 215 -0.5; 230 -0.3; 246 -0.1; 263 0.1; 282 0.4; 301 0.6; 323 0.8; 345 1.0; 369 1.1; 395 1.3; 423 1.5; 452 1.6; 484 1.7; 518 1.7; 554 1.9; 593 2.0; 635 2.0; 679 1.9; 726 1.8; 777 1.8; 832 1.4; 890 1.0; 952 0.5; 1019 -0.1; 1090 -0.8; 1167 -1.3; 1248 -2.0; 1336 -2.9; 1429 -3.9; 1529 -4.7; 1636 -5.7; 1751 -6.7; 1873 -7.6; 2004 -8.4; 2145 -9.0; 2295 -9.0; 2455 -8.0; 2627 -7.1; 2811 -6.4; 3008 -5.7; 3219 -5.7; 3444 -3.1; 3685 0.8; 3943 3.4; 4219 3.5; 4514 2.5; 4830 2.5; 5168 3.9; 5530 5.2; 5917 5.9; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 -0.4; 8880 -3.7; 9502 -7.3; 10167 -9.5; 10879 -8.9; 11640 -6.0; 12455 -3.1; 13327 -1.1; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.4dB` and instead set Global volume in the UI for both channels to **-64**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `T-Peos H-100 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 0.59 | -6.6 dB  |
| Peaking | 2288 Hz  | 1.51 | -9.8 dB  |
| Peaking | 4024 Hz  | 6.31 | 5.1 dB   |
| Peaking | 5991 Hz  | 2.23 | 7.6 dB   |
| Peaking | 10355 Hz | 2.87 | -10.9 dB |
| Peaking | 160 Hz   | 2.06 | -1.6 dB  |
| Peaking | 664 Hz   | 0.79 | 2.7 dB   |
| Peaking | 1641 Hz  | 2.91 | -1.4 dB  |
| Peaking | 1308 Hz  | 2.03 | -0.8 dB  |
| Peaking | 14339 Hz | 4.48 | 1.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/T-Peos%20H-100/T-Peos%20H-100.png)