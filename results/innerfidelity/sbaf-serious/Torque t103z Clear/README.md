# Torque t103z Clear

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.0dB
GraphicEQ: 10 -84; 20 -3.0; 22 -3.4; 23 -3.6; 25 -4.0; 26 -4.2; 28 -4.6; 30 -5.0; 32 -5.3; 35 -5.6; 37 -5.8; 40 -6.0; 42 -6.2; 45 -6.3; 49 -6.5; 52 -6.7; 56 -6.8; 59 -6.8; 64 -7.0; 68 -7.1; 73 -7.3; 78 -7.4; 83 -7.7; 89 -8.0; 95 -8.4; 102 -8.9; 109 -9.2; 117 -9.6; 125 -10.1; 134 -10.4; 143 -10.5; 153 -10.5; 164 -10.5; 175 -10.2; 188 -10.0; 201 -9.7; 215 -9.4; 230 -9.0; 246 -8.7; 263 -8.3; 282 -7.8; 301 -7.3; 323 -6.8; 345 -6.4; 369 -5.9; 395 -5.4; 423 -4.8; 452 -4.2; 484 -3.8; 518 -3.3; 554 -2.7; 593 -2.0; 635 -1.8; 679 -0.9; 726 -0.1; 777 -0.1; 832 0.1; 890 0.0; 952 0.1; 1019 0.0; 1090 0.0; 1167 0.0; 1248 -0.0; 1336 -0.3; 1429 -0.5; 1529 -0.7; 1636 -0.8; 1751 -0.8; 1873 -0.5; 2004 -0.3; 2145 -0.2; 2295 -0.1; 2455 -0.1; 2627 -0.8; 2811 -1.0; 3008 -0.5; 3219 0.4; 3444 1.1; 3685 1.0; 3943 -0.3; 4219 -3.1; 4514 -3.7; 4830 -2.5; 5168 -3.3; 5530 -0.0; 5917 3.7; 6331 5.4; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.0dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t103z Clear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc      |    Q | Gain    |
|:--------|:--------|:-----|:--------|
| Peaking | 2 Hz    | 2.01 | -1.8 dB |
| Peaking | 63 Hz   | 0.28 | -5.5 dB |
| Peaking | 193 Hz  | 0.67 | -6.9 dB |
| Peaking | 4911 Hz | 3.49 | -4.6 dB |
| Peaking | 6267 Hz | 4.8  | 6.9 dB  |
| Peaking | 13 Hz   | 1.34 | 1.0 dB  |
| Peaking | 429 Hz  | 1.89 | -0.9 dB |
| Peaking | 808 Hz  | 1.93 | 1.6 dB  |
| Peaking | 3519 Hz | 4.81 | 4.0 dB  |
| Peaking | 3677 Hz | 1.98 | -1.9 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t103z%20Clear/Torque%20t103z%20Clear.png)