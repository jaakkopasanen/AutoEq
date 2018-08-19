# Thinksound Rain2

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -2.7dB
GraphicEQ: 10 -84; 20 -8.6; 22 -8.7; 23 -8.8; 25 -8.9; 26 -8.9; 28 -9.0; 30 -9.1; 32 -9.1; 35 -9.2; 37 -9.3; 40 -9.4; 42 -9.4; 45 -9.5; 49 -9.7; 52 -9.8; 56 -9.9; 59 -10.0; 64 -10.2; 68 -10.4; 73 -10.5; 78 -10.7; 83 -10.9; 89 -11.1; 95 -11.3; 102 -11.3; 109 -11.3; 117 -11.3; 125 -11.4; 134 -11.4; 143 -11.3; 153 -11.3; 164 -11.1; 175 -10.9; 188 -10.7; 201 -10.5; 215 -10.1; 230 -9.8; 246 -9.5; 263 -9.1; 282 -8.6; 301 -8.2; 323 -7.8; 345 -7.3; 369 -6.8; 395 -6.4; 423 -5.7; 452 -5.2; 484 -4.8; 518 -4.2; 554 -3.6; 593 -2.9; 635 -2.3; 679 -1.9; 726 -1.5; 777 -0.9; 832 -0.6; 890 -0.4; 952 -0.1; 1019 0.1; 1090 0.3; 1167 0.5; 1248 0.6; 1336 0.4; 1429 0.0; 1529 -0.6; 1636 -1.0; 1751 -1.2; 1873 -1.0; 2004 -0.6; 2145 -0.2; 2295 0.3; 2455 1.1; 2627 1.5; 2811 1.8; 3008 2.3; 3219 2.5; 3444 2.5; 3685 1.9; 3943 0.8; 4219 -1.3; 4514 -2.8; 4830 -4.0; 5168 -5.5; 5530 -8.7; 5917 -10.9; 6331 -8.3; 6775 -4.5; 7249 -1.6; 7756 0.1; 8299 0.0; 8880 0.0; 9502 -0.9; 10167 -2.4; 10879 -1.7; 11640 -0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 -0.2; 16326 -2.3; 17469 -1.8; 18692 -0.1; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-2.725402865079683dB` and instead set Global volume in the UI for both channels to **-27**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Thinksound Rain2 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-3.0dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -3.0dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 33 Hz    | 0.21 | -8.5 dB  |
| Peaking | 155 Hz   | 0.64 | -6.2 dB  |
| Peaking | 332 Hz   | 1.18 | -3.3 dB  |
| Peaking | 3256 Hz  | 2.75 | 3.5 dB   |
| Peaking | 5828 Hz  | 3.71 | -11.4 dB |
| Peaking | 1179 Hz  | 1.87 | 1.4 dB   |
| Peaking | 1724 Hz  | 3.57 | -1.5 dB  |
| Peaking | 7848 Hz  | 5.52 | 2.1 dB   |
| Peaking | 10230 Hz | 8.39 | -2.5 dB  |
| Peaking | 16870 Hz | 4.34 | -2.8 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Thinksound%20Rain2/Thinksound%20Rain2.png)