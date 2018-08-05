# Harman Kardon NI

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.7dB
GraphicEQ: 10 -84; 20 -8.2; 22 -8.2; 23 -8.2; 25 -8.2; 26 -8.2; 28 -8.1; 30 -8.0; 32 -8.0; 35 -7.8; 37 -7.7; 40 -7.5; 42 -7.4; 45 -7.2; 49 -7.0; 52 -6.8; 56 -6.6; 59 -6.4; 64 -6.2; 68 -6.0; 73 -5.7; 78 -5.6; 83 -5.6; 89 -5.6; 95 -5.7; 102 -5.9; 109 -6.1; 117 -6.2; 125 -6.5; 134 -6.6; 143 -6.6; 153 -6.4; 164 -6.2; 175 -5.9; 188 -5.5; 201 -5.2; 215 -4.8; 230 -4.4; 246 -4.1; 263 -3.7; 282 -3.2; 301 -2.9; 323 -2.5; 345 -2.1; 369 -1.8; 395 -1.5; 423 -1.1; 452 -0.8; 484 -0.6; 518 -0.4; 554 -0.1; 593 0.3; 635 0.5; 679 0.4; 726 0.4; 777 0.5; 832 0.5; 890 0.3; 952 0.2; 1019 -0.1; 1090 -0.4; 1167 -0.8; 1248 -1.2; 1336 -1.9; 1429 -2.6; 1529 -3.3; 1636 -4.0; 1751 -4.7; 1873 -5.3; 2004 -5.9; 2145 -6.8; 2295 -8.0; 2455 -9.1; 2627 -9.5; 2811 -8.4; 3008 -5.5; 3219 -3.0; 3444 -1.1; 3685 -0.6; 3943 -1.3; 4219 -3.6; 4514 -6.3; 4830 -9.5; 5168 -11.7; 5530 -8.1; 5917 -2.2; 6331 1.1; 6775 3.2; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 -0.6; 17469 -0.1; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.7dB` and instead set Global volume in the UI for both channels to **-37**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Harman Kardon NI ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 8 Hz    | 0.62 | -7.2 dB  |
| Peaking | 32 Hz   | 0.41 | -6.7 dB  |
| Peaking | 161 Hz  | 0.94 | -5.0 dB  |
| Peaking | 2413 Hz | 2.15 | -9.4 dB  |
| Peaking | 5089 Hz | 6.43 | -12.0 dB |
| Peaking | 772 Hz  | 1.63 | 1.3 dB   |
| Peaking | 1585 Hz | 4.21 | -1.6 dB  |
| Peaking | 3617 Hz | 4.4  | 4.5 dB   |
| Peaking | 4463 Hz | 1.3  | -2.4 dB  |
| Peaking | 6768 Hz | 4.95 | 5.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Harman%20Kardon%20NI/Harman%20Kardon%20NI.png)