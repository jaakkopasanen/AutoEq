# Techfusion Ecoofers

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.8dB
GraphicEQ: 10 -84; 20 -14.8; 22 -14.8; 23 -14.8; 25 -14.8; 26 -14.8; 28 -14.8; 30 -14.8; 32 -14.8; 35 -14.7; 37 -14.6; 40 -14.5; 42 -14.4; 45 -14.3; 49 -14.2; 52 -14.1; 56 -13.9; 59 -13.8; 64 -13.6; 68 -13.5; 73 -13.4; 78 -13.3; 83 -13.3; 89 -13.4; 95 -13.6; 102 -13.8; 109 -13.9; 117 -14.1; 125 -14.4; 134 -14.4; 143 -14.4; 153 -14.3; 164 -14.0; 175 -13.6; 188 -13.2; 201 -12.8; 215 -12.3; 230 -11.7; 246 -11.3; 263 -10.8; 282 -10.1; 301 -9.6; 323 -9.0; 345 -8.4; 369 -7.8; 395 -7.2; 423 -6.5; 452 -5.9; 484 -5.3; 518 -4.7; 554 -3.9; 593 -3.2; 635 -2.5; 679 -2.1; 726 -1.4; 777 -0.7; 832 -0.5; 890 -0.3; 952 -0.0; 1019 -0.0; 1090 0.1; 1167 0.1; 1248 0.1; 1336 -0.1; 1429 -0.4; 1529 -0.6; 1636 -0.9; 1751 -1.9; 1873 -2.8; 2004 -2.8; 2145 -2.7; 2295 -2.6; 2455 -2.5; 2627 -2.9; 2811 -3.0; 3008 -3.3; 3219 -1.9; 3444 0.3; 3685 1.2; 3943 1.0; 4219 -0.2; 4514 -1.2; 4830 -1.6; 5168 -1.8; 5530 -2.5; 5917 -4.1; 6331 -5.3; 6775 -4.3; 7249 -2.6; 7756 -0.7; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 -0.4; 11640 -0.4; 12455 0.0; 13327 0.0; 14260 0.0; 15258 -0.0; 16326 -1.4; 17469 -2.8; 18692 -1.7; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-1.8dB` and instead set Global volume in the UI for both channels to **-18**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Techfusion Ecoofers ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-2.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 20 Hz    | 0.15 | -14.4 dB |
| Peaking | 198 Hz   | 0.63 | -8.2 dB  |
| Peaking | 2435 Hz  | 2.43 | -3.0 dB  |
| Peaking | 6335 Hz  | 4.26 | -5.5 dB  |
| Peaking | 17694 Hz | 3.15 | -3.2 dB  |
| Peaking | 469 Hz   | 1.04 | -3.6 dB  |
| Peaking | 617 Hz   | 0.56 | 3.0 dB   |
| Peaking | 1874 Hz  | 5.34 | -2.1 dB  |
| Peaking | 3028 Hz  | 7.51 | -2.3 dB  |
| Peaking | 3683 Hz  | 6.69 | 2.4 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Techfusion%20Ecoofers/Techfusion%20Ecoofers.png)