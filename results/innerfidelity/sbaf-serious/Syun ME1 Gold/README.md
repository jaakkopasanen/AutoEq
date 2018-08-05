# Syun ME1 Gold

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.8dB
GraphicEQ: 10 -84; 20 6.2; 22 5.7; 23 5.5; 25 5.1; 26 4.8; 28 4.4; 30 3.9; 32 3.5; 35 3.0; 37 2.7; 40 2.4; 42 2.2; 45 2.0; 49 1.6; 52 1.5; 56 1.2; 59 1.0; 64 0.8; 68 0.5; 73 0.2; 78 -0.0; 83 -0.4; 89 -0.9; 95 -1.4; 102 -2.2; 109 -2.7; 117 -3.3; 125 -4.0; 134 -4.6; 143 -5.0; 153 -5.4; 164 -5.6; 175 -5.7; 188 -5.8; 201 -5.9; 215 -5.9; 230 -5.9; 246 -5.8; 263 -5.7; 282 -5.6; 301 -5.5; 323 -5.3; 345 -5.1; 369 -4.8; 395 -4.5; 423 -4.0; 452 -3.7; 484 -3.4; 518 -3.1; 554 -2.5; 593 -1.9; 635 -1.6; 679 -1.4; 726 -1.2; 777 -0.9; 832 -0.5; 890 0.0; 952 0.2; 1019 -0.0; 1090 -0.2; 1167 -0.4; 1248 -0.7; 1336 -1.0; 1429 -1.4; 1529 -1.8; 1636 -2.0; 1751 -2.1; 1873 -2.0; 2004 -1.8; 2145 -1.6; 2295 -1.2; 2455 -0.6; 2627 0.0; 2811 0.8; 3008 1.8; 3219 2.6; 3444 3.1; 3685 2.5; 3943 1.1; 4219 -1.7; 4514 -4.1; 4830 -5.5; 5168 -3.6; 5530 -0.7; 5917 2.9; 6331 4.7; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.8dB` and instead set Global volume in the UI for both channels to **-68**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Syun ME1 Gold ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 10 Hz   | 0.22 | 6.3 dB  |
| Peaking | 217 Hz  | 0.58 | -6.5 dB |
| Peaking | 3576 Hz | 3.58 | 5.4 dB  |
| Peaking | 4801 Hz | 2.38 | -7.1 dB |
| Peaking | 6204 Hz | 3.93 | 7.2 dB  |
| Peaking | 42 Hz   | 2.27 | -0.6 dB |
| Peaking | 81 Hz   | 3.62 | 0.7 dB  |
| Peaking | 958 Hz  | 2.43 | 1.5 dB  |
| Peaking | 1810 Hz | 1.64 | -2.0 dB |
| Peaking | 2992 Hz | 4.34 | 1.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Syun%20ME1%20Gold/Syun%20ME1%20Gold.png)