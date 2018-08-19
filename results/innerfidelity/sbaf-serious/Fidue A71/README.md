# Fidue A71

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 -1.5; 22 -1.9; 23 -2.1; 25 -2.5; 26 -2.6; 28 -2.9; 30 -3.1; 32 -3.3; 35 -3.6; 37 -3.7; 40 -3.9; 42 -4.0; 45 -4.2; 49 -4.5; 52 -4.6; 56 -4.9; 59 -5.1; 64 -5.3; 68 -5.5; 73 -5.7; 78 -6.0; 83 -6.2; 89 -6.4; 95 -6.7; 102 -6.8; 109 -6.8; 117 -6.9; 125 -7.0; 134 -7.1; 143 -7.1; 153 -7.1; 164 -7.0; 175 -6.9; 188 -6.7; 201 -6.6; 215 -6.3; 230 -6.1; 246 -5.8; 263 -5.6; 282 -5.2; 301 -4.8; 323 -4.5; 345 -4.1; 369 -3.7; 395 -3.5; 423 -3.0; 452 -1.9; 484 -1.6; 518 -1.3; 554 -0.9; 593 -0.3; 635 0.0; 679 0.1; 726 0.3; 777 0.7; 832 0.6; 890 0.5; 952 0.2; 1019 -0.1; 1090 -0.4; 1167 -0.8; 1248 -1.4; 1336 -2.2; 1429 -3.2; 1529 -4.1; 1636 -4.9; 1751 -5.2; 1873 -4.9; 2004 -4.0; 2145 -2.8; 2295 -1.6; 2455 -0.1; 2627 1.8; 2811 3.9; 3008 5.8; 3219 6.0; 3444 6.0; 3685 6.0; 3943 6.0; 4219 6.0; 4514 6.0; 4830 6.0; 5168 6.0; 5530 6.0; 5917 5.9; 6331 2.5; 6775 -1.3; 7249 -2.0; 7756 -1.2; 8299 -0.8; 8880 -1.1; 9502 -0.5; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.099999998715981dB` and instead set Global volume in the UI for both channels to **-60**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Fidue A71 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.3dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 89 Hz    | 0.38 | -5.3 dB  |
| Peaking | 222 Hz   | 0.7  | -3.4 dB  |
| Peaking | 1876 Hz  | 1.17 | -15.0 dB |
| Peaking | 3140 Hz  | 0.39 | 12.1 dB  |
| Peaking | 7998 Hz  | 1.32 | -7.3 dB  |
| Peaking | 4094 Hz  | 5.14 | -0.7 dB  |
| Peaking | 5936 Hz  | 4.54 | 3.8 dB   |
| Peaking | 6759 Hz  | 4.26 | -4.7 dB  |
| Peaking | 8127 Hz  | 1.99 | 1.8 dB   |
| Peaking | 13707 Hz | 0.89 | -1.0 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Fidue%20A71/Fidue%20A71.png)