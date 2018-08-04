# Grado PS1000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.6dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 5.8; 37 5.5; 40 4.6; 42 3.9; 45 3.1; 49 2.0; 52 1.2; 56 0.3; 59 -0.4; 64 -1.3; 68 -1.9; 73 -2.7; 78 -3.2; 83 -3.7; 89 -4.2; 95 -4.6; 102 -4.8; 109 -4.8; 117 -4.9; 125 -4.7; 134 -4.6; 143 -4.3; 153 -4.1; 164 -3.7; 175 -3.3; 188 -2.9; 201 -2.6; 215 -2.1; 230 -1.7; 246 -1.4; 263 -1.1; 282 -0.6; 301 -0.4; 323 -0.5; 345 -0.3; 369 0.0; 395 -0.0; 423 -0.0; 452 0.1; 484 0.1; 518 0.1; 554 0.3; 593 0.4; 635 0.5; 679 0.4; 726 0.3; 777 0.5; 832 0.4; 890 0.1; 952 0.1; 1019 -0.1; 1090 -0.3; 1167 -0.7; 1248 -1.0; 1336 -1.6; 1429 -2.0; 1529 -2.2; 1636 -1.7; 1751 -2.2; 1873 -1.7; 2004 -1.3; 2145 -1.0; 2295 -1.4; 2455 -1.3; 2627 -1.7; 2811 -1.7; 3008 -2.0; 3219 -2.6; 3444 -1.4; 3685 -1.1; 3943 -4.3; 4219 -6.1; 4514 -7.1; 4830 -6.1; 5168 -7.2; 5530 -7.6; 5917 -9.6; 6331 -11.9; 6775 -11.0; 7249 -8.9; 7756 -6.8; 8299 -6.9; 8880 -9.1; 9502 -10.5; 10167 -8.8; 10879 -4.5; 11640 -0.6; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.6dB` and instead set Global volume in the UI for both channels to **-66**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado PS1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-7.5dB** and build filters manually with
these parameters. The first 5 filters can be used independently.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 29 Hz    |  0.8  | 7.2 dB   |
| Peaking | 105 Hz   |  0.88 | -6.0 dB  |
| Peaking | 1572 Hz  |  3    | -1.9 dB  |
| Peaking | 6249 Hz  |  1.52 | -10.7 dB |
| Peaking | 9612 Hz  |  4.94 | -8.2 dB  |
| Peaking | 596 Hz   |  1.16 | 0.8 dB   |
| Peaking | 4345 Hz  |  8.94 | -2.6 dB  |
| Peaking | 5567 Hz  | 10.64 | 1.8 dB   |
| Peaking | 12450 Hz |  4.19 | 2.1 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20PS1000/Grado%20PS1000.png)