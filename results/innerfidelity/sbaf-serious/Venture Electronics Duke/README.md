# Venture Electronics Duke

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -1.8dB
GraphicEQ: 10 -84; 20 0.5; 22 0.3; 23 0.2; 25 -0.0; 26 -0.1; 28 -0.2; 30 -0.4; 32 -0.5; 35 -0.7; 37 -0.8; 40 -1.0; 42 -1.1; 45 -1.2; 49 -1.4; 52 -1.6; 56 -1.9; 59 -2.0; 64 -2.4; 68 -2.6; 73 -2.9; 78 -3.2; 83 -3.4; 89 -3.6; 95 -3.9; 102 -4.2; 109 -4.3; 117 -4.5; 125 -4.7; 134 -4.9; 143 -5.0; 153 -5.1; 164 -5.2; 175 -5.2; 188 -5.2; 201 -5.2; 215 -5.1; 230 -5.0; 246 -4.9; 263 -4.8; 282 -4.5; 301 -4.4; 323 -4.2; 345 -3.9; 369 -3.6; 395 -3.3; 423 -2.9; 452 -2.6; 484 -2.3; 518 -2.0; 554 -1.6; 593 -1.0; 635 -0.7; 679 -0.6; 726 -0.3; 777 0.1; 832 0.1; 890 0.2; 952 0.1; 1019 -0.0; 1090 -0.2; 1167 -0.3; 1248 -0.5; 1336 -0.8; 1429 -1.1; 1529 -1.4; 1636 -1.6; 1751 -1.6; 1873 -1.6; 2004 -0.6; 2145 -0.2; 2295 -0.6; 2455 -0.8; 2627 -2.1; 2811 -3.4; 3008 -2.7; 3219 -0.9; 3444 0.9; 3685 1.6; 3943 1.6; 4219 0.6; 4514 0.3; 4830 0.5; 5168 0.9; 5530 0.4; 5917 -0.4; 6331 -3.9; 6775 -7.4; 7249 -9.0; 7756 -8.2; 8299 -5.9; 8880 -2.7; 9502 -0.1; 10167 0.0; 10879 0.0; 11640 -1.2; 12455 -2.5; 13327 -1.2; 14260 0.0; 15258 0.0; 16326 0.0; 17469 -0.5; 18692 -0.6; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-1.849246087417042dB` and instead set Global volume in the UI for both channels to **-18**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Venture Electronics Duke ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-1.7dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -0.1dB.

| Type    | Fc      |    Q | Gain     |
|:--------|:--------|:-----|:---------|
| Peaking | 124 Hz  | 0.69 | -4.1 dB  |
| Peaking | 228 Hz  | 1.33 | -2.4 dB  |
| Peaking | 368 Hz  | 1.81 | -1.9 dB  |
| Peaking | 1746 Hz | 2.39 | -1.5 dB  |
| Peaking | 7410 Hz | 4.2  | -10.1 dB |
| Peaking | 2888 Hz | 4.53 | -4.4 dB  |
| Peaking | 3633 Hz | 5.29 | 1.3 dB   |
| Peaking | 5121 Hz | 0.67 | 2.4 dB   |
| Peaking | 9258 Hz | 1.02 | -4.1 dB  |
| Peaking | 9835 Hz | 3.08 | 4.4 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Venture%20Electronics%20Duke/Venture%20Electronics%20Duke.png)