# Grado HF-1 Serial 69

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 5.8; 37 5.5; 40 4.6; 42 4.0; 45 3.1; 49 2.1; 52 1.4; 56 0.6; 59 0.1; 64 -0.5; 68 -0.8; 73 -1.1; 78 -1.3; 83 -1.6; 89 -2.0; 95 -2.3; 102 -2.5; 109 -2.5; 117 -2.6; 125 -2.7; 134 -2.7; 143 -2.7; 153 -2.6; 164 -2.4; 175 -2.1; 188 -2.0; 201 -1.8; 215 -1.5; 230 -1.2; 246 -0.9; 263 -0.9; 282 -0.7; 301 -0.5; 323 -0.2; 345 -0.1; 369 -0.3; 395 -0.2; 423 -0.0; 452 0.1; 484 0.1; 518 0.1; 554 0.2; 593 0.4; 635 0.5; 679 0.5; 726 0.4; 777 0.5; 832 0.4; 890 0.2; 952 -0.1; 1019 -0.1; 1090 -0.3; 1167 -0.5; 1248 -0.9; 1336 -1.6; 1429 -2.6; 1529 -3.3; 1636 -3.8; 1751 -4.4; 1873 -4.8; 2004 -5.5; 2145 -6.0; 2295 -5.4; 2455 -5.9; 2627 -5.7; 2811 -4.7; 3008 -3.4; 3219 -2.0; 3444 -0.7; 3685 -0.7; 3943 -2.5; 4219 -3.6; 4514 -4.1; 4830 -2.7; 5168 -1.8; 5530 -0.7; 5917 0.9; 6331 0.8; 6775 -2.2; 7249 -4.2; 7756 -5.0; 8299 -7.3; 8880 -9.7; 9502 -8.6; 10167 -2.6; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado HF-1 Serial 69 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.0dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 27 Hz    | 0.87 | 7.0 dB   |
| Peaking | 105 Hz   | 0.78 | -3.5 dB  |
| Peaking | 2426 Hz  | 1.82 | -5.4 dB  |
| Peaking | 1769 Hz  | 2.87 | -2.4 dB  |
| Peaking | 8854 Hz  | 3.98 | -10.4 dB |
| Peaking | 747 Hz   | 1.11 | 0.9 dB   |
| Peaking | 3488 Hz  | 4.06 | 3.5 dB   |
| Peaking | 5148 Hz  | 1.14 | -4.3 dB  |
| Peaking | 5905 Hz  | 3.83 | 6.0 dB   |
| Peaking | 11112 Hz | 3.95 | 2.5 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20HF-1%20Serial%2069/Grado%20HF-1%20Serial%2069.png)