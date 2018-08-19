# Grado SR225i

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 6.0; 32 6.0; 35 5.9; 37 5.6; 40 4.9; 42 4.4; 45 3.7; 49 2.9; 52 2.3; 56 1.8; 59 1.4; 64 0.7; 68 0.2; 73 -0.3; 78 -0.8; 83 -1.2; 89 -1.5; 95 -1.8; 102 -2.0; 109 -2.0; 117 -2.0; 125 -2.1; 134 -2.1; 143 -2.0; 153 -2.0; 164 -1.9; 175 -1.6; 188 -1.5; 201 -1.4; 215 -1.2; 230 -0.9; 246 -0.8; 263 -0.6; 282 -0.4; 301 -0.4; 323 -0.5; 345 -0.2; 369 -0.1; 395 -0.3; 423 -0.1; 452 0.0; 484 -0.0; 518 0.0; 554 0.2; 593 0.4; 635 0.4; 679 0.4; 726 0.3; 777 0.5; 832 0.4; 890 0.2; 952 0.1; 1019 0.0; 1090 -0.1; 1167 -0.3; 1248 -0.7; 1336 -1.2; 1429 -2.1; 1529 -3.0; 1636 -3.8; 1751 -4.3; 1873 -6.5; 2004 -8.4; 2145 -8.6; 2295 -6.7; 2455 -5.4; 2627 -4.5; 2811 -3.5; 3008 -3.4; 3219 -2.3; 3444 -2.7; 3685 -3.5; 3943 -2.5; 4219 -0.8; 4514 -0.2; 4830 -0.7; 5168 -2.2; 5530 -1.8; 5917 -1.4; 6331 -2.5; 6775 -4.8; 7249 -6.0; 7756 -5.9; 8299 -6.8; 8880 -8.8; 9502 -9.1; 10167 -5.5; 10879 -0.5; 11640 0.0; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado SR225i ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.5dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.5dB.

| Type    | Fc       |     Q | Gain     |
|:--------|:---------|:------|:---------|
| Peaking | 28 Hz    |  0.67 | 6.7 dB   |
| Peaking | 105 Hz   |  0.83 | -3.2 dB  |
| Peaking | 2115 Hz  |  2.38 | -8.4 dB  |
| Peaking | 9326 Hz  |  1.82 | -12.4 dB |
| Peaking | 11081 Hz |  1.99 | 6.4 dB   |
| Peaking | 796 Hz   |  1.4  | 0.9 dB   |
| Peaking | 3788 Hz  |  4.38 | -2.9 dB  |
| Peaking | 4300 Hz  |  3.37 | 2.2 dB   |
| Peaking | 7049 Hz  | 12.56 | -2.1 dB  |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/innerfidelity/sbaf-serious/Grado%20SR225i/Grado%20SR225i.png)