# V-Moda V-80 True Blood

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -4.9dB
GraphicEQ: 10 -84; 20 1.0; 22 0.6; 23 0.5; 25 0.2; 26 0.1; 28 -0.1; 30 -0.3; 32 -0.4; 35 -0.6; 37 -0.7; 40 -0.9; 42 -0.9; 45 -1.0; 49 -1.1; 52 -1.2; 56 -1.4; 59 -1.5; 64 -1.6; 68 -1.8; 73 -1.9; 78 -1.9; 83 -2.0; 89 -2.2; 95 -2.6; 102 -2.8; 109 -2.8; 117 -2.6; 125 -2.6; 134 -2.9; 143 -3.1; 153 -3.0; 164 -2.9; 175 -2.6; 188 -2.7; 201 -2.5; 215 -2.6; 230 -3.0; 246 -2.5; 263 -1.8; 282 -1.0; 301 -0.2; 323 0.4; 345 0.8; 369 1.2; 395 1.6; 423 2.1; 452 2.5; 484 2.9; 518 3.4; 554 3.9; 593 4.2; 635 4.1; 679 3.7; 726 3.3; 777 2.9; 832 2.1; 890 1.3; 952 0.6; 1019 -0.2; 1090 -0.9; 1167 -1.7; 1248 -2.2; 1336 -2.7; 1429 -2.9; 1529 -2.6; 1636 -2.2; 1751 -1.4; 1873 -0.5; 2004 0.6; 2145 1.3; 2295 1.7; 2455 2.3; 2627 2.3; 2811 1.9; 3008 1.6; 3219 0.4; 3444 0.1; 3685 1.3; 3943 2.8; 4219 3.6; 4514 3.4; 4830 2.6; 5168 4.0; 5530 4.7; 5917 3.4; 6331 2.9; 6775 3.1; 7249 1.3; 7756 0.3; 8299 0.0; 8880 0.0; 9502 0.0; 10167 0.0; 10879 0.0; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-4.883016518277472dB` and instead set Global volume in the UI for both channels to **-48**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `V-Moda V-80 True Blood ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-4.4dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -4.4dB.

| Type    | Fc      |     Q | Gain    |
|:--------|:--------|:------|:--------|
| Peaking | 192 Hz  |  0.45 | -4.0 dB |
| Peaking | 608 Hz  |  0.71 | 6.7 dB  |
| Peaking | 1372 Hz |  1.02 | -5.5 dB |
| Peaking | 2335 Hz |  2.12 | 3.5 dB  |
| Peaking | 5296 Hz |  1.93 | 4.3 dB  |
| Peaking | 18 Hz   |  2    | 1.2 dB  |
| Peaking | 329 Hz  |  7.88 | 0.6 dB  |
| Peaking | 3381 Hz | 13.81 | -1.4 dB |
| Peaking | 6723 Hz |  8.2  | 1.6 dB  |
| Peaking | 7984 Hz |  2.73 | -1.0 dB |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/V-Moda%20V-80%20True%20Blood/V-Moda%20V-80%20True%20Blood.png)