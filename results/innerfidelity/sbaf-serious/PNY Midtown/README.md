# PNY Midtown

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -10.4; 22 -10.4; 23 -10.4; 25 -10.4; 26 -10.3; 28 -10.3; 30 -10.3; 32 -10.3; 35 -10.3; 37 -10.2; 40 -10.2; 42 -10.2; 45 -10.2; 49 -10.2; 52 -10.2; 56 -10.1; 59 -10.1; 64 -10.2; 68 -10.2; 73 -10.2; 78 -10.3; 83 -10.3; 89 -10.3; 95 -10.3; 102 -10.3; 109 -10.1; 117 -10.0; 125 -9.9; 134 -9.8; 143 -9.6; 153 -9.4; 164 -9.1; 175 -8.8; 188 -8.5; 201 -8.2; 215 -7.8; 230 -7.4; 246 -7.1; 263 -6.7; 282 -6.3; 301 -5.9; 323 -5.4; 345 -4.9; 369 -4.5; 395 -4.1; 423 -3.5; 452 -3.0; 484 -2.6; 518 -2.4; 554 -1.8; 593 -1.2; 635 -0.9; 679 -0.7; 726 -0.2; 777 0.2; 832 0.2; 890 0.1; 952 -0.2; 1019 0.2; 1090 0.5; 1167 0.4; 1248 0.1; 1336 -0.4; 1429 -0.9; 1529 -1.5; 1636 -2.1; 1751 -3.1; 1873 -4.0; 2004 -4.4; 2145 -4.5; 2295 -4.2; 2455 -3.6; 2627 -2.2; 2811 -0.4; 3008 2.1; 3219 4.1; 3444 5.7; 3685 6.0; 3943 5.5; 4219 3.8; 4514 2.3; 4830 1.6; 5168 0.3; 5530 -2.1; 5917 -6.2; 6331 -8.4; 6775 -4.4; 7249 -1.1; 7756 0.2; 8299 0.0; 8880 -0.1; 9502 -0.7; 10167 -0.1; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.098788956532994dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `PNY Midtown ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.2dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.3dB.

| Type    | Fc      |     Q | Gain     |
|:--------|:--------|:------|:---------|
| Peaking | 28 Hz   |  0.18 | -10.1 dB |
| Peaking | 180 Hz  |  0.66 | -4.5 dB  |
| Peaking | 2234 Hz |  2.26 | -6.1 dB  |
| Peaking | 3631 Hz |  2.14 | 7.4 dB   |
| Peaking | 6222 Hz |  5.77 | -9.9 dB  |
| Peaking | 193 Hz  |  1.33 | 1.2 dB   |
| Peaking | 595 Hz  |  0.35 | -2.1 dB  |
| Peaking | 847 Hz  |  0.67 | 3.2 dB   |
| Peaking | 1741 Hz |  4.74 | -1.2 dB  |
| Peaking | 7686 Hz | 10.74 | 1.3 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/PNY%20Midtown/PNY%20Midtown.png)