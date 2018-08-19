# Grado PS1000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 5.8; 37 5.4; 40 4.4; 42 3.8; 45 2.9; 49 1.8; 52 0.9; 56 -0.1; 59 -0.8; 64 -1.8; 68 -2.5; 73 -3.4; 78 -4.0; 83 -4.5; 89 -5.0; 95 -5.3; 102 -5.4; 109 -5.2; 117 -5.1; 125 -4.8; 134 -4.5; 143 -4.1; 153 -3.8; 164 -3.5; 175 -3.1; 188 -2.6; 201 -2.4; 215 -2.0; 230 -1.6; 246 -1.3; 263 -1.0; 282 -0.5; 301 -0.4; 323 -0.5; 345 -0.2; 369 0.0; 395 -0.0; 423 -0.0; 452 0.1; 484 0.1; 518 0.1; 554 0.3; 593 0.4; 635 0.5; 679 0.4; 726 0.3; 777 0.5; 832 0.4; 890 0.1; 952 0.1; 1019 -0.1; 1090 -0.3; 1167 -0.7; 1248 -1.0; 1336 -1.6; 1429 -2.0; 1529 -2.2; 1636 -1.7; 1751 -2.2; 1873 -1.7; 2004 -1.3; 2145 -1.0; 2295 -1.4; 2455 -1.3; 2627 -1.7; 2811 -1.7; 3008 -2.0; 3219 -2.6; 3444 -1.4; 3685 -1.1; 3943 -4.3; 4219 -6.1; 4514 -7.1; 4830 -6.1; 5168 -7.2; 5530 -7.6; 5917 -9.6; 6331 -11.9; 6775 -11.0; 7249 -8.9; 7756 -6.8; 8299 -6.9; 8880 -9.1; 9502 -10.5; 10167 -8.8; 10879 -4.5; 11640 -0.6; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.1000000000000005dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado PS1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 29 Hz    |  0.74 | 7.3 dB   |
| Peaking | 96 Hz    |  0.88 | -6.8 dB  |
| Peaking | 1572 Hz  |  2.99 | -1.9 dB  |
| Peaking | 6248 Hz  |  1.52 | -10.7 dB |
| Peaking | 9612 Hz  |  4.93 | -8.2 dB  |
| Peaking | 602 Hz   |  1.18 | 0.8 dB   |
| Peaking | 4346 Hz  |  9    | -2.6 dB  |
| Peaking | 5569 Hz  | 10.98 | 1.8 dB   |
| Peaking | 12460 Hz |  4.19 | 2.1 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20PS1000/Grado%20PS1000.png)