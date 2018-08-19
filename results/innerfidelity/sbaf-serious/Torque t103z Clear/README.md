# Torque t103z Clear

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.6dB
GraphicEQ: 10 -84; 20 -3.0; 22 -3.5; 23 -3.7; 25 -4.1; 26 -4.4; 28 -4.8; 30 -5.2; 32 -5.5; 35 -5.9; 37 -6.1; 40 -6.4; 42 -6.6; 45 -6.9; 49 -7.3; 52 -7.5; 56 -7.8; 59 -7.9; 64 -8.2; 68 -8.5; 73 -8.8; 78 -9.1; 83 -9.4; 89 -9.6; 95 -9.8; 102 -9.9; 109 -9.9; 117 -10.0; 125 -10.1; 134 -10.1; 143 -10.1; 153 -10.0; 164 -9.9; 175 -9.7; 188 -9.5; 201 -9.3; 215 -9.0; 230 -8.7; 246 -8.4; 263 -8.1; 282 -7.6; 301 -7.2; 323 -6.7; 345 -6.3; 369 -5.8; 395 -5.3; 423 -4.7; 452 -4.2; 484 -3.8; 518 -3.3; 554 -2.7; 593 -2.0; 635 -1.8; 679 -0.8; 726 -0.1; 777 -0.1; 832 0.1; 890 0.0; 952 0.1; 1019 0.0; 1090 0.0; 1167 0.0; 1248 -0.0; 1336 -0.3; 1429 -0.5; 1529 -0.7; 1636 -0.8; 1751 -0.8; 1873 -0.5; 2004 -0.3; 2145 -0.2; 2295 -0.1; 2455 -0.1; 2627 -0.8; 2811 -1.0; 3008 -0.5; 3219 0.4; 3444 1.1; 3685 1.0; 3943 -0.3; 4219 -3.1; 4514 -3.7; 4830 -2.5; 5168 -3.3; 5530 -0.0; 5917 3.7; 6331 5.4; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.556023056433222dB` and instead set Global volume in the UI for both channels to **-55**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Torque t103z Clear ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.9dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.9dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 66 Hz   |  0.4  | -7.0 dB |
| Peaking | 164 Hz  |  0.79 | -5.3 dB |
| Peaking | 324 Hz  |  1.35 | -3.1 dB |
| Peaking | 4915 Hz |  3.44 | -4.6 dB |
| Peaking | 6283 Hz |  4.79 | 6.9 dB  |
| Peaking | 544 Hz  |  1.87 | -1.6 dB |
| Peaking | 739 Hz  |  1.24 | 1.8 dB  |
| Peaking | 1670 Hz |  2.4  | -0.7 dB |
| Peaking | 3621 Hz |  6.28 | 2.0 dB  |
| Peaking | 4319 Hz | 13.44 | -2.5 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Torque%20t103z%20Clear/Torque%20t103z%20Clear.png)