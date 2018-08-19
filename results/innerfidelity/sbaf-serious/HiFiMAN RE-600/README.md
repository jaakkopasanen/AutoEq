# HiFiMAN RE-600

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 4.1; 22 4.1; 23 4.1; 25 4.0; 26 4.0; 28 3.9; 30 3.8; 32 3.7; 35 3.6; 37 3.6; 40 3.5; 42 3.5; 45 3.3; 49 3.2; 52 3.0; 56 2.8; 59 2.6; 64 2.4; 68 2.2; 73 1.9; 78 1.6; 83 1.4; 89 1.1; 95 0.8; 102 0.6; 109 0.5; 117 0.4; 125 0.2; 134 -0.0; 143 -0.2; 153 -0.3; 164 -0.4; 175 -0.4; 188 -0.5; 201 -0.5; 215 -0.4; 230 -0.4; 246 -0.3; 263 -0.2; 282 -0.1; 301 0.0; 323 0.1; 345 0.3; 369 0.4; 395 0.6; 423 0.8; 452 1.0; 484 0.9; 518 1.1; 554 1.3; 593 1.5; 635 1.6; 679 1.5; 726 1.5; 777 1.5; 832 1.2; 890 0.8; 952 0.5; 1019 -0.1; 1090 -0.6; 1167 -1.2; 1248 -1.9; 1336 -2.8; 1429 -3.8; 1529 -4.7; 1636 -5.6; 1751 -6.2; 1873 -5.2; 2004 -4.6; 2145 -4.2; 2295 -2.1; 2455 0.8; 2627 3.4; 2811 5.6; 3008 6.0; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 5.7; 5530 5.1; 5917 5.3; 6331 5.5; 6775 3.9; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999999755221dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `HiFiMAN RE-600 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -7.0dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 24 Hz   | 0.96 | 3.9 dB   |
| Peaking | 52 Hz   | 1.53 | 2.1 dB   |
| Peaking | 728 Hz  | 1.37 | 2.2 dB   |
| Peaking | 1864 Hz | 1.38 | -10.8 dB |
| Peaking | 3313 Hz | 0.84 | 9.5 dB   |
| Peaking | 190 Hz  | 1.94 | -0.8 dB  |
| Peaking | 2848 Hz | 5.15 | 3.1 dB   |
| Peaking | 3052 Hz | 1.91 | -1.8 dB  |
| Peaking | 6367 Hz | 2.27 | 5.1 dB   |
| Peaking | 7513 Hz | 1.62 | -4.2 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/HiFiMAN%20RE-600/HiFiMAN%20RE-600.png)