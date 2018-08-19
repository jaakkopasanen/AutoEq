# Torque t096z Treble Boost Filter

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -3.3dB
GraphicEQ: 10 -84; 20 -1.2; 22 -1.7; 23 -1.9; 25 -2.3; 26 -2.4; 28 -2.7; 30 -2.9; 32 -3.1; 35 -3.2; 37 -3.3; 40 -3.5; 42 -3.6; 45 -3.8; 49 -4.0; 52 -4.2; 56 -4.4; 59 -4.5; 64 -4.8; 68 -5.0; 73 -5.3; 78 -5.7; 83 -5.8; 89 -6.0; 95 -6.2; 102 -6.5; 109 -6.6; 117 -6.7; 125 -6.7; 134 -6.9; 143 -7.0; 153 -6.9; 164 -7.0; 175 -6.8; 188 -6.7; 201 -6.6; 215 -6.4; 230 -6.1; 246 -5.9; 263 -5.7; 282 -5.3; 301 -5.0; 323 -4.6; 345 -4.2; 369 -3.8; 395 -3.4; 423 -2.8; 452 -2.3; 484 -2.1; 518 -1.7; 554 -1.2; 593 -0.6; 635 -0.2; 679 -0.1; 726 0.2; 777 0.5; 832 0.5; 890 0.4; 952 0.2; 1019 -0.0; 1090 -0.3; 1167 -0.5; 1248 -0.8; 1336 -1.3; 1429 -1.9; 1529 -2.6; 1636 -3.0; 1751 -3.4; 1873 -3.6; 2004 -3.8; 2145 -4.1; 2295 -4.7; 2455 -5.3; 2627 -6.0; 2811 -6.6; 3008 -6.2; 3219 -5.6; 3444 -4.3; 3685 -4.1; 3943 -5.0; 4219 -7.6; 4514 -10.4; 4830 -11.5; 5168 -8.5; 5530 -4.1; 5917 -0.2; 6331 1.9; 6775 3.1; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 -0.1; 10167 -3.0; 10879 -5.7; 11640 -5.2; 12455 -2.7; 13327 -0.8; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-3.2579105955486845dB` and instead set Global volume in the UI for both channels to **-32**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t096z Treble Boost Filter ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.1dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -0.1dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 88 Hz    | 0.45 | -5.2 dB  |
| Peaking | 216 Hz   | 0.92 | -3.9 dB  |
| Peaking | 2667 Hz  | 1.61 | -6.1 dB  |
| Peaking | 4704 Hz  | 5.39 | -11.4 dB |
| Peaking | 11402 Hz | 5.3  | -6.4 dB  |
| Peaking | 384 Hz   | 2.26 | -0.8 dB  |
| Peaking | 801 Hz   | 1.49 | 1.5 dB   |
| Peaking | 1631 Hz  | 3.63 | -1.5 dB  |
| Peaking | 5276 Hz  | 7.15 | -3.1 dB  |
| Peaking | 6605 Hz  | 3.9  | 4.6 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t096z%20Treble%20Boost%20Filter/Torque%20t096z%20Treble%20Boost%20Filter.png)