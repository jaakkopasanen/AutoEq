# JVC XX Elation HA FR100X

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.3dB
GraphicEQ: 10 -84; 20 2.4; 22 1.3; 23 0.8; 25 0.2; 26 -0.0; 28 -0.3; 30 -0.5; 32 -0.8; 35 -1.1; 37 -1.3; 40 -1.5; 42 -1.7; 45 -2.0; 49 -2.3; 52 -2.6; 56 -2.7; 59 -2.8; 64 -3.1; 68 -3.3; 73 -3.5; 78 -3.8; 83 -4.2; 89 -4.6; 95 -5.2; 102 -5.8; 109 -6.3; 117 -6.8; 125 -7.3; 134 -7.9; 143 -8.3; 153 -8.5; 164 -8.6; 175 -8.5; 188 -8.6; 201 -8.5; 215 -8.3; 230 -8.2; 246 -8.1; 263 -7.8; 282 -7.6; 301 -7.3; 323 -6.9; 345 -6.6; 369 -6.2; 395 -5.9; 423 -5.3; 452 -4.8; 484 -4.5; 518 -4.0; 554 -3.3; 593 -2.6; 635 -2.1; 679 -1.8; 726 -1.2; 777 -0.7; 832 -0.3; 890 -0.2; 952 0.0; 1019 0.2; 1090 0.7; 1167 0.9; 1248 1.1; 1336 1.0; 1429 1.1; 1529 1.0; 1636 1.0; 1751 0.9; 1873 0.7; 2004 0.1; 2145 -0.6; 2295 -1.0; 2455 -1.0; 2627 -1.2; 2811 -1.1; 3008 -0.3; 3219 0.4; 3444 0.9; 3685 0.3; 3943 -1.2; 4219 -3.8; 4514 -6.3; 4830 -7.3; 5168 -5.4; 5530 -1.6; 5917 2.1; 6331 4.4; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.3dB` and instead set Global volume in the UI for both channels to **-53**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `JVC XX Elation HA FR100X ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 20 Hz   | 2.81 | 2.6 dB  |
| Peaking | 162 Hz  | 0.67 | -8.1 dB |
| Peaking | 345 Hz  | 1.35 | -3.4 dB |
| Peaking | 4818 Hz | 4.65 | -8.6 dB |
| Peaking | 6406 Hz | 5.01 | 6.0 dB  |
| Peaking | 47 Hz   | 2.19 | -0.8 dB |
| Peaking | 525 Hz  | 3.53 | -1.0 dB |
| Peaking | 1677 Hz | 0.83 | 2.9 dB  |
| Peaking | 2613 Hz | 1.05 | -3.3 dB |
| Peaking | 3417 Hz | 3.87 | 3.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/JVC%20XX%20Elation%20HA%20FR100X/JVC%20XX%20Elation%20HA%20FR100X.png)