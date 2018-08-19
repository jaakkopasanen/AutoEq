# Grado PS1000

### EqualizerAPO
In case of using EqualizerAPO without any GUI, replace `C:\Program Files\EqualizerAPO\config\config.txt`
with:
```
Preamp: -6.1dB
GraphicEQ: 10 -84; 20 6.0; 22 6.0; 23 6.0; 25 6.0; 26 6.0; 28 6.0; 30 5.9; 32 5.6; 35 4.8; 37 4.2; 40 3.2; 42 2.5; 45 1.7; 49 0.7; 52 -0.1; 56 -1.1; 59 -1.7; 64 -2.6; 68 -3.3; 73 -4.0; 78 -4.5; 83 -4.9; 89 -5.2; 95 -5.4; 102 -5.3; 109 -5.3; 117 -5.1; 125 -4.8; 134 -4.4; 143 -4.2; 153 -3.9; 164 -3.5; 175 -3.1; 188 -2.7; 201 -2.4; 215 -2.1; 230 -1.8; 246 -1.6; 263 -1.4; 282 -1.1; 301 -0.8; 323 -0.4; 345 0.1; 369 0.4; 395 0.0; 423 -0.0; 452 0.0; 484 0.1; 518 0.2; 554 0.4; 593 0.5; 635 0.5; 679 0.6; 726 0.5; 777 0.6; 832 0.5; 890 0.4; 952 0.2; 1019 -0.0; 1090 -0.3; 1167 -0.4; 1248 -0.7; 1336 -1.1; 1429 -1.7; 1529 -2.4; 1636 -2.6; 1751 -1.6; 1873 -1.2; 2004 -1.1; 2145 -1.1; 2295 -1.0; 2455 -1.0; 2627 -1.1; 2811 -1.1; 3008 -1.2; 3219 -1.0; 3444 0.1; 3685 -2.7; 3943 -8.1; 4219 -8.2; 4514 -6.2; 4830 -6.6; 5168 -7.2; 5530 -8.1; 5917 -8.8; 6331 -11.9; 6775 -11.7; 7249 -10.2; 7756 -9.3; 8299 -8.8; 8880 -8.5; 9502 -7.4; 10167 -5.2; 10879 -2.2; 11640 -0.1; 12455 0.0; 13327 0.0; 14260 0.0; 15258 0.0; 16326 0.0; 17469 0.0; 18692 0.0; 20000 0.0
```

### HeSuVi
In case of using HeSuVi, replace `C:\Program Files\EqualizerAPO\config\HeSuVi\eq.txt` and omit `Preamp:
-6.100000000000001dB` and instead set Global volume in the UI for both channels to **-61**

### Peace
In case of using Peace, click *Import* in Peace GUI and select `Grado PS1000 ParametricEQ.txt`.

### Parametric EQs
In case of using other parametric equalizer, apply preamp of **-6.6dB** and build filters manually
with these parameters. The first 5 filters can be used independently.
When using independent subset of filters, apply preamp of -6.6dB.

| Type    | Fc       |    Q | Gain     |
|:--------|:---------|:-----|:---------|
| Peaking | 27 Hz    | 0.84 | 7.2 dB   |
| Peaking | 95 Hz    | 0.82 | -6.5 dB  |
| Peaking | 1579 Hz  | 5.31 | -2.4 dB  |
| Peaking | 4119 Hz  | 6.83 | -5.6 dB  |
| Peaking | 6913 Hz  | 1.5  | -11.9 dB |
| Peaking | 654 Hz   | 1.09 | 1.0 dB   |
| Peaking | 2815 Hz  | 3.06 | 0.7 dB   |
| Peaking | 3488 Hz  | 9.01 | 3.4 dB   |
| Peaking | 5190 Hz  | 0.31 | -0.7 dB  |
| Peaking | 12428 Hz | 3.06 | 2.7 dB   |

![](https://raw.githubusercontent.com/jaakkopasanen/AutoEq/master/results/headphonecom/sbaf-serious/Grado%20PS1000/Grado%20PS1000.png)