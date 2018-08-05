# Torque t096z Treble Boost Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.7dB
GraphicEQ: 10 -84; 20 -1.2; 22 -1.6; 23 -1.8; 25 -2.2; 26 -2.3; 28 -2.6; 30 -2.7; 32 -2.9; 35 -3.0; 37 -3.0; 40 -3.1; 42 -3.2; 45 -3.2; 49 -3.3; 52 -3.3; 56 -3.4; 59 -3.5; 64 -3.5; 68 -3.5; 73 -3.8; 78 -4.1; 83 -4.2; 89 -4.5; 95 -4.8; 102 -5.4; 109 -5.8; 117 -6.3; 125 -6.8; 134 -7.2; 143 -7.4; 153 -7.5; 164 -7.5; 175 -7.4; 188 -7.2; 201 -7.1; 215 -6.8; 230 -6.5; 246 -6.2; 263 -5.9; 282 -5.5; 301 -5.2; 323 -4.7; 345 -4.3; 369 -3.9; 395 -3.4; 423 -2.8; 452 -2.4; 484 -2.1; 518 -1.7; 554 -1.2; 593 -0.6; 635 -0.3; 679 -0.1; 726 0.2; 777 0.5; 832 0.5; 890 0.4; 952 0.2; 1019 -0.0; 1090 -0.3; 1167 -0.5; 1248 -0.8; 1336 -1.3; 1429 -1.9; 1529 -2.6; 1636 -3.0; 1751 -3.4; 1873 -3.6; 2004 -3.8; 2145 -4.1; 2295 -4.7; 2455 -5.3; 2627 -6.0; 2811 -6.6; 3008 -6.2; 3219 -5.6; 3444 -4.3; 3685 -4.1; 3943 -5.0; 4219 -7.6; 4514 -10.4; 4830 -11.5; 5168 -8.5; 5530 -4.1; 5917 -0.2; 6331 1.9; 6775 3.1; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.1; 10167 -3.0; 10879 -5.7; 11640 -5.2; 12455 -2.7; 13327 -0.8; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.7dB` and instead set Global volume in the UI for both channels to **-37**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t096z Treble Boost Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 46 Hz    | 0.31 | -2.3 dB  |
| Peaking | 183 Hz   | 0.77 | -6.7 dB  |
| Peaking | 2668 Hz  | 1.61 | -6.1 dB  |
| Peaking | 4719 Hz  | 5.41 | -11.4 dB |
| Peaking | 36793 Hz | 5.31 | -6.4 dB  |
| Peaking | 365 Hz   | 2.24 | -0.9 dB  |
| Peaking | 801 Hz   | 1.51 | 1.6 dB   |
| Peaking | 1627 Hz  | 3.6  | -1.5 dB  |
| Peaking | 5239 Hz  | 6.82 | -3.0 dB  |
| Peaking | 6561 Hz  | 3.81 | 4.6 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t096z%20Treble%20Boost%20Filter/Torque%20t096z%20Treble%20Boost%20Filter.png)