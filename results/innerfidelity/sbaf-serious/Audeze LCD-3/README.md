# Audeze LCD-3

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -5.5dB
GraphicEQ: 10 -84; 20 3.5; 22 3.5; 23 3.4; 25 3.1; 26 2.9; 28 2.4; 30 2.0; 32 1.7; 35 1.5; 37 1.5; 40 1.4; 42 1.4; 45 1.4; 49 1.1; 52 0.8; 56 0.6; 59 0.6; 64 0.5; 68 0.4; 73 0.2; 78 0.1; 83 -0.1; 89 -0.4; 95 -0.7; 102 -0.9; 109 -0.9; 117 -1.1; 125 -1.4; 134 -1.5; 143 -1.7; 153 -1.8; 164 -2.0; 175 -2.1; 188 -2.2; 201 -2.3; 215 -2.2; 230 -2.2; 246 -2.2; 263 -2.3; 282 -2.2; 301 -2.1; 323 -2.0; 345 -1.9; 369 -1.8; 395 -1.8; 423 -1.9; 452 -2.0; 484 -2.2; 518 -2.2; 554 -2.1; 593 -1.9; 635 -1.8; 679 -1.9; 726 -1.7; 777 -1.4; 832 -1.2; 890 -0.8; 952 -0.4; 1019 0.1; 1090 0.4; 1167 0.5; 1248 0.8; 1336 0.5; 1429 0.1; 1529 -0.2; 1636 -0.1; 1751 0.5; 1873 1.0; 2004 1.3; 2145 1.0; 2295 1.2; 2455 1.4; 2627 1.5; 2811 1.4; 3008 1.2; 3219 1.4; 3444 2.7; 3685 4.3; 3943 5.2; 4219 5.2; 4514 4.7; 4830 4.3; 5168 3.6; 5530 1.5; 5917 1.1; 6331 2.5; 6775 3.1; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 -0.2; 16326 -2.0; 17469 -4.5; 18692 -5.5; 20000 -3.7
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-5.47017458241406dB` and instead set Global volume in the UI for both channels to **-54**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Audeze LCD-3 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-5.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -5.1dB.

| Type    | Fc       |    Q | Gain    |
|:--------|:---------|:-----|:--------|
| Peaking | 11 Hz    | 0.33 | 4.1 dB  |
| Peaking | 271 Hz   | 0.46 | -2.4 dB |
| Peaking | 4269 Hz  | 1.62 | 5.1 dB  |
| Peaking | 15128 Hz | 1.83 | 2.2 dB  |
| Peaking | 18452 Hz | 1.06 | -6.0 dB |
| Peaking | 690 Hz   | 2.33 | -0.8 dB |
| Peaking | 1146 Hz  | 3.54 | 1.2 dB  |
| Peaking | 2150 Hz  | 2.85 | 0.8 dB  |
| Peaking | 3236 Hz  | 4.37 | -1.6 dB |
| Peaking | 3719 Hz  | 5.06 | 1.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Audeze%20LCD-3/Audeze%20LCD-3.png)