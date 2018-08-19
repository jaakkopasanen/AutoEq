# Grado SR225i G Pads

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 5.9; 35 5.4; 37 4.9; 40 4.1; 42 3.6; 45 3.2; 49 2.7; 52 2.1; 56 1.1; 59 0.4; 64 -0.5; 68 -1.0; 73 -1.5; 78 -2.0; 83 -2.3; 89 -2.6; 95 -3.0; 102 -3.3; 109 -3.3; 117 -3.3; 125 -3.3; 134 -3.3; 143 -3.3; 153 -3.2; 164 -3.0; 175 -2.8; 188 -2.6; 201 -2.5; 215 -2.2; 230 -1.9; 246 -1.7; 263 -1.5; 282 -1.2; 301 -1.2; 323 -1.0; 345 -0.7; 369 -0.7; 395 -0.8; 423 -0.6; 452 -0.4; 484 -0.4; 518 -0.5; 554 -0.4; 593 -0.2; 635 -0.0; 679 -0.1; 726 -0.0; 777 0.2; 832 0.1; 890 -0.1; 952 -0.1; 1019 -0.1; 1090 -0.2; 1167 -0.6; 1248 -0.9; 1336 -1.1; 1429 -1.7; 1529 -1.7; 1636 -1.8; 1751 -2.2; 1873 -1.5; 2004 -1.8; 2145 -1.4; 2295 -1.5; 2455 -1.9; 2627 -2.2; 2811 -2.4; 3008 -3.2; 3219 -2.9; 3444 -3.9; 3685 -4.8; 3943 -4.4; 4219 -3.7; 4514 -3.1; 4830 -4.9; 5168 -7.6; 5530 -8.6; 5917 -10.0; 6331 -10.5; 6775 -9.4; 7249 -8.1; 7756 -7.6; 8299 -8.4; 8880 -10.0; 9502 -9.9; 10167 -7.1; 10879 -2.8; 11640 -0.1; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR225i G Pads ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.4dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 28 Hz    | 0.57 | 7.2 dB   |
| Peaking | 101 Hz   | 0.6  | -4.9 dB  |
| Peaking | 5940 Hz  | 3.83 | -1.7 dB  |
| Peaking | 6982 Hz  | 0.93 | -9.2 dB  |
| Peaking | 24000 Hz | 2.21 | -7.9 dB  |
| Peaking | 1626 Hz  | 3.61 | -1.3 dB  |
| Peaking | 4565 Hz  | 4.97 | 4.9 dB   |
| Peaking | 4604 Hz  | 1.43 | -3.5 dB  |
| Peaking | 9546 Hz  | 3.27 | -10.1 dB |
| Peaking | 9948 Hz  | 0.99 | 6.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20SR225i%20G%20Pads/Grado%20SR225i%20G%20Pads.png)