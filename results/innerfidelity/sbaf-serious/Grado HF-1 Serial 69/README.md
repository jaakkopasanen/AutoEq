# Grado HF-1 Serial 69

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 5.8; 37 5.4; 40 4.5; 42 3.9; 45 2.9; 49 1.8; 52 1.1; 56 0.3; 59 -0.3; 64 -1.0; 68 -1.4; 73 -1.8; 78 -2.1; 83 -2.4; 89 -2.8; 95 -3.0; 102 -3.0; 109 -2.9; 117 -2.8; 125 -2.7; 134 -2.6; 143 -2.5; 153 -2.3; 164 -2.1; 175 -1.9; 188 -1.8; 201 -1.6; 215 -1.4; 230 -1.1; 246 -0.8; 263 -0.8; 282 -0.6; 301 -0.5; 323 -0.2; 345 -0.0; 369 -0.3; 395 -0.2; 423 0.0; 452 0.1; 484 0.1; 518 0.1; 554 0.2; 593 0.4; 635 0.5; 679 0.5; 726 0.4; 777 0.5; 832 0.4; 890 0.2; 952 -0.1; 1019 -0.1; 1090 -0.3; 1167 -0.5; 1248 -0.9; 1336 -1.6; 1429 -2.6; 1529 -3.3; 1636 -3.8; 1751 -4.4; 1873 -4.8; 2004 -5.5; 2145 -6.0; 2295 -5.4; 2455 -5.9; 2627 -5.7; 2811 -4.7; 3008 -3.4; 3219 -2.0; 3444 -0.7; 3685 -0.7; 3943 -2.5; 4219 -3.6; 4514 -4.1; 4830 -2.7; 5168 -1.8; 5530 -0.7; 5917 0.9; 6331 0.8; 6775 -2.2; 7249 -4.2; 7756 -5.0; 8299 -7.3; 8880 -9.7; 9502 -8.6; 10167 -2.6; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado HF-1 Serial 69 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 29 Hz    | 0.73 | 7.3 dB   |
| Peaking | 90 Hz    | 0.75 | -4.4 dB  |
| Peaking | 1775 Hz  | 2.81 | -2.5 dB  |
| Peaking | 2431 Hz  | 1.83 | -5.3 dB  |
| Peaking | 8853 Hz  | 3.97 | -10.4 dB |
| Peaking | 3585 Hz  | 4.72 | 2.9 dB   |
| Peaking | 4366 Hz  | 2.99 | -3.6 dB  |
| Peaking | 6231 Hz  | 4.56 | 3.9 dB   |
| Peaking | 7106 Hz  | 4.92 | -2.8 dB  |
| Peaking | 11040 Hz | 5.81 | 2.2 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20HF-1%20Serial%2069/Grado%20HF-1%20Serial%2069.png)